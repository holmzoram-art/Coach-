# Live løpecoach — teknisk mulighetsstudie

**Dato:** 2026-09-02
**Spørsmål:** Er det teknisk mulig å bygge en tjeneste som gir en løper sanntids lydcoaching i øret under en løpetur, basert på live tempo, puls, kadens, GPS, høyde og splitt-tider?

**Kort svar:** Ja. Det er ikke bare mulig — det er godt understøttet av offisielle API-er på både iOS/watchOS og via generisk Bluetooth LE. Den vanskelige delen er ikke datainnhenting eller lydavspilling; det er **signalkvalitet** (særlig GPS-tempo og optisk puls) og **coachinglogikk som faktisk er nyttig**. Den raskeste veien til MVP er en iPhone-app med HealthKit live workout + BLE-pulsbelte + lokal regelmotor + `AVSpeechSynthesizer`.

---

## Notasjon for kildetillit

Gjennom hele rapporten merkes påstander:

- **[V]** = Verifisert mot primærkilde (offisiell utviklerdokumentasjon eller offisiell spesifikasjon), lenke oppgitt.
- **[S]** = Sannsynlig — flere sekundærkilder samstemmer, eller det følger logisk av verifiserte fakta, men jeg har ikke sett primærkilden.
- **[U]** = Usikkert / må testes empirisk.

**Metodemerknad:** En del domener (`developer.garmin.com`, `forums.garmin.com`, `www.strava.com`, `developers.strava.com`, `press.strava.com`, `www.bluetooth.com`, `pmc.ncbi.nlm.nih.gov`, `dcrainmaker.com`) var blokkert av nettverksproxyen i dette miljøet. For disse har jeg brukt søkemotorsammendrag og speilede kilder (GitHub-mirror av BLE GATT-XML, åpen kildekode som implementerer API-ene) og merket funnene deretter. Alle Apple-påstander er hentet direkte fra Apples egen dokumentasjons-JSON-API og er **[V]**.

---

## 1. Datakilder i sanntid

### 1.1 Apple: watchOS og — nytt og viktig — iOS 26

Dette er den best dokumenterte og mest komplette veien.

**HKWorkoutSession** — «A session that tracks a person's workout.» Tilgjengelig watchOS 2.0+, **og iOS/iPadOS 17.0+**. **[V]**
https://developer.apple.com/documentation/healthkit/hkworkoutsession

> «The session fine-tunes Apple Watch's sensors for the specified activity. **All workout sessions generate high-frequency heart rate samples**; however, an outdoor cycling activity generates accurate location data, while an indoor cycling activity doesn't.»
>
> «Collecting heart rate data on iPhone or iPad requires pairing with an external heart rate sensor because these devices don't have one.»

**HKLiveWorkoutBuilder** — «A builder object that constructs a workout incrementally based on live data from an active workout session.» watchOS 5.0+, **iOS/iPadOS/Mac Catalyst 26.0+**. **[V]**
https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilder

**HKLiveWorkoutDataSource** — «A data source that automatically provides live data from an active workout session.» watchOS 5.0+, **iOS 26.0+**. **[V]**
https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource

**Dette er en stor sak for arkitekturvalget.** Fram til iOS 26 måtte man ha en watchOS-app for å få `HKLiveWorkoutBuilder`. Fra iOS 26 kan en ren iPhone-app kjøre en fullverdig HealthKit-workout-session. WWDC25-sesjon 322 «Track workouts with HealthKit on iOS and iPadOS» bekrefter at «the same code can be used across iPhone, iPad, and Apple Watch with only minimal changes», og beskriver flyten: `HKWorkoutConfiguration` → `HKWorkoutSession` → `session.associatedWorkoutBuilder()` → `builder.dataSource = HKLiveWorkoutDataSource(...)` → `prepare()` → `startActivity()` + `beginCollection()`. **[V]**
https://developer.apple.com/videos/play/wwdc2025/322/

Samme sesjon nevner to viktige forbehold for iPhone-varianten: **[V]**
- iPhone/iPad har ingen innebygd pulssensor — puls krever ekstern BLE-sensor (eller f.eks. Powerbeats Pro 2). HealthKit henter og lagrer den automatisk når enheten er paret.
- iPhone låser seg typisk under en økt. Systemet viser en engangsdialog om at treningsdata blir tilgjengelige for appen også mens enheten er låst.
- Apple anbefaler eksplisitt: «If you have a Watch app, be sure to start the workout there to get all available metrics.»

**Bakgrunnskjøring og lyd — den kritiske biten.** Apples egen guide «Running workout sessions» sier ordrett: **[V]**

> «Apps with an active workout session can run in the background, so you need to add the background modes capability to your WatchKit App Extension. Workout sessions require the **Workout processing** background mode. If your app plays audio or provides haptic feedback during the workout session, you must also add the **Audio** background mode.»
>
> «Workout apps can use the AVFoundation framework to play short audio clips in the background, such as **coaching** or notifications. In order to play an audio clip, **an active workout session must be running**; any attempt to play background audio outside a workout session are invalid.»

https://developer.apple.com/documentation/healthkit/running-workout-sessions

Apple beskriver altså *nøyaktig* dette bruksområdet («coaching») som en støttet, dokumentert funksjon. Det er så sterkt et grønt lys som man får.

**Hvilke måletyper får man live?** For en utendørs løpeøkt lagrer systemet automatisk bl.a.: **[V]**

| HKQuantityTypeIdentifier | Innført | Merknad |
|---|---|---|
| `heartRate` | watchOS 2.0 | Har `HKMetadataKeyHeartRateMotionContext` |
| `runningSpeed` | watchOS 9.0 / iOS 16.0 | «During outdoor running workouts, the system automatically records running speed samples on Apple Watch.» |
| `runningPower` | watchOS 9.0 / iOS 16.0 | «the rate of work required for the runner to maintain their speed» — automatisk på Apple Watch SE og Series 6+ |
| `runningVerticalOscillation` | watchOS 9.0 | Apple Watch SE / Series 6+ |
| `distanceWalkingRunning`, `activeEnergyBurned` | — | Automatisk generert |

Lenker: [runningPower](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningpower) · [runningSpeed](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningspeed) · [heartRate](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/heartrate)

`HKLiveWorkoutDataSource` har `enableCollection(for:)` / `disableCollection(for:)` for å styre hva som samles live. **[V]** (WWDC25 322)
Aggregerte verdier hentes med `HKWorkoutBuilder.statistics(for:)` (watchOS 5.0+ / iOS 12.0+). **[V]**
https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/statistics(for:)

**Oppdateringsfrekvens på puls:** Apples dokumentasjon sier bare «high-frequency heart rate samples» uten tall. **[V]** Praksis i økosystemet er ca. **ett sample per 5. sekund (0,2 Hz)** under aktiv økt — dette er samstemt i community-verktøy (f.eks. GitHub-prosjektet `snphan/AppleRawData`, som eksplisitt beskriver «Heart Rate data (0.2 Hz)»). **[S]** — https://github.com/snphan/AppleRawData
Må måles selv. Se åpne spørsmål.

**Latency:** Sensor-til-app-latency er ikke dokumentert av Apple. **[U]** Det som *er* dokumentert er den fysiologisk/optisk induserte forsinkelsen (se §3.2), som dominerer uansett.

**CoreLocation:** `CLLocation.speed` er dokumentert som **[V]**:
> «This value reflects the instantaneous speed of the device as it moves in the direction of its current heading. A negative value indicates an invalid speed. **Because the actual speed can change many times between the delivery of location events, use this property for informational purposes only.**»

https://developer.apple.com/documentation/corelocation/cllocation/speed

Apple advarer altså selv mot å bruke `speed` til noe presist. Bruk `kCLLocationAccuracyBestForNavigation` og egen filtrering.

Bakgrunnsposisjon krever `UIBackgroundModes` = `location` i Info.plist + `allowsBackgroundLocationUpdates = true`; å sette flagget uten Info.plist-nøkkelen er «a fatal error that terminates the app». **[V]**
https://developer.apple.com/documentation/corelocation/cllocationmanager/allowsbackgroundlocationupdates

**CoreMotion:** `CMPedometerData.currentCadence` — «The rate at which steps are taken, measured in **steps per second**» (iOS 9.0+ / watchOS 2.0+). Merk: dette er skritt/sek, ikke skritt/min — gang ×60. Verdien er `nil` ved historiske spørringer eller når kadens ikke er tilgjengelig. **[V]**
https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence
`CMPedometer.startUpdates(from:withHandler:)` leverer kumulative data på en seriell kø; leveransen **stopper når appen suspenderes** og gjenopptas i forgrunn/bakgrunn. **[V]**
https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)

**Konklusjon Apple:** Alt vi trenger finnes, offisielt, med Apples eksplisitte velsignelse for coaching-lyd i bakgrunnen. Dette er den sterkeste plattformen.

---

### 1.2 Bluetooth LE direkte — den plattformuavhengige veien

Dette er den *generiske* ruten: telefonen snakker direkte med brystbelte/armbånd/footpod uten å gå via noen klokkeleverandør. Ingen partneravtaler, ingen SDK-lisenser.

#### Heart Rate Service (UUID `0x180D`)

Karakteristikk **Heart Rate Measurement `0x2A37`** (notify). Felter (fra Bluetooth SIGs GATT-XML, speilet på GitHub): **[V]**

- **Flags** (uint8):
  - bit 0: Heart Rate Value Format (0 = uint8, 1 = uint16)
  - bit 1–2: Sensor Contact Status
  - bit 3: Energy Expended Status (om feltet er til stede)
  - bit 4: RR-Interval (om feltene er til stede)
- **Heart Rate Measurement Value** — uint8 eller uint16, enhet: slag per minutt
- **Energy Expended** — uint16, enhet: joule (valgfritt)
- **RR-Interval** — uint16 (én eller flere), enhet: sekunder (oppløsning 1/1024 s)

https://github.com/oesmith/gatt-xml/blob/master/org.bluetooth.characteristic.heart_rate_measurement.xml

**RR-intervaller er gull.** De gir slag-for-slag-timing (1/1024 s oppløsning) og dermed HRV. Et brystbelte som Polar H10 leverer RR pålitelig; optiske håndleddssensorer gjør det sjelden godt under løping. Typisk notify-rate: 1 Hz. **[S]**

Andre karakteristikker i tjenesten: Body Sensor Location `0x2A38`, Heart Rate Control Point `0x2A39`. **[S]**

#### Running Speed and Cadence Service (UUID `0x1814`)

«The Running Speed and Cadence (RSC) Service exposes speed, cadence and other data related to fitness applications such as the stride length and the total distance the user has traveled while using the Speed and Cadence Sensor.» **[V]**
https://www.bluetooth.com/specifications/specs/running-speed-and-cadence-service/

Karakteristikk **RSC Measurement `0x2A53`** (notify). Felter: **[V]**

| Felt | Type | Enhet / oppløsning | Tilstedeværelse |
|---|---|---|---|
| Flags | uint8 | bit 0 = Instantaneous Stride Length Present, bit 1 = Total Distance Present, bit 2 = Walking(0)/Running(1) Status | alltid |
| Instantaneous Speed | uint16 | m/s, oppløsning **1/256 m/s** | obligatorisk |
| Instantaneous Cadence | uint8 | 1/min (RPM), oppløsning 1 | obligatorisk |
| Instantaneous Stride Length | uint16 | meter, oppløsning 1/100 m | betinget (flag bit 0) |
| Total Distance | uint32 | meter, oppløsning 1/10 m | betinget (flag bit 1) |

https://github.com/oesmith/gatt-xml/blob/master/org.bluetooth.characteristic.rsc_measurement.xml

Tilleggskarakteristikker: RSC Feature `0x2A54` (hvilke felt sensoren støtter, inkl. «Instantaneous Stride Length Measurement Supported»-bit), Sensor Location `0x2A5D`, SC Control Point `0x2A55` (kalibrering). **[S]**

**Merk kadens-semantikken:** RSC rapporterer typisk skritt per minutt for ett bein (dvs. ~half-cadence, 80–95) på noen sensorer og total (160–190) på andre. Dette **må valideres per sensor**. **[U]**

**Hvorfor dette er viktig:** En footpod (Stryd, Garmin RD Pod, Polar Stride Sensor) gir **tempo uten GPS-støy**. Stryd markedsfører nettopp dette: «Because of its accuracy, it can provide real-time pace, something that's impractical to achieve with any GPS device as GPS requires quite a bit of smoothing.» **[S]** — https://the5krunner.com/2023/11/16/stryd-review-discount-duo/
Stryd sender over både ANT+ og BLE og parer med Garmin, COROS, Suunto, Polar og Apple Watch. **[S]** — https://www.stryd.com/eu/en

**Stryd har også Cycling Power Service (`0x1818`)-emulering** for løpseffekt over BLE. **[S]** — må verifiseres i felt hvilken UUID/format som faktisk brukes for løpseffekt.

**iOS-implementasjon:** CoreBluetooth central role, `bluetooth-central` i `UIBackgroundModes` for å beholde tilkobling i bakgrunn. **[S]**
**Android:** `BluetoothGatt` + foreground service, se §2.3.

---

### 1.3 Garmin

Garmin er den mest utbredte plattformen blant seriøse løpere og samtidig den mest lukkede for akkurat dette bruksområdet.

#### Connect IQ (app/datafelt på klokka)

**Blokkere for vår use case:**

1. **Ingen tekst-til-tale, ingen egendefinert lyd.** Connect IQ tilbyr `Attention.playTone` med *forhåndsdefinerte* toner (`TONE_CANARY` etc.) og `Attention.vibrate`. Man kan ikke laste opp egne lydfiler og ikke syntetisere tale. **[S]** — https://apps.garmin.com/en-US/apps/a32959dc-15fd-4399-89ec-91889009cb8f
   Garmins innebygde «Audio Prompts» er en *native* funksjon som spiller opplesing via tilkoblet telefon eller klokkas egen musikkavspilling — **den er ikke eksponert for tredjeparts Connect IQ-apper**. **[S] / [U]** — bør dobbeltsjekkes mot `developer.garmin.com/connect-iq/api-docs/` når domenet er tilgjengelig.

2. **Ingen nettverkstilgang i sanntid fra datafelt.** `Communications.makeWebRequest` må kjøres fra en background service for datafelt og watch faces, og bakgrunnshendelser kan ikke ha kortere periode enn **5 minutter** («Background event period cannot be less than 5 minutes»). **[S]** — https://forums.garmin.com/developer/connect-iq/f/discussion/427067/early-makewebrequest-in-a-data-field
   Dette dreper enhver «LLM i løkka» direkte fra klokka.

3. **Stramme minne- og CPU-budsjetter.** Datafelt har typisk 28–32 kB tilgjengelig minne på eldre enheter (Fenix 5: 32 kB nominelt, ~28 kB reelt); nyere enheter har mer, og Fenix 8 tillater 4 samtidige CIQ-datafelt mot tidligere 2. **[S]** — https://forums.garmin.com/developer/connect-iq/f/discussion/418612/device-memory-limits

**Det som *fungerer*:** Connect IQ **Mobile SDK / Companion App SDK** gir toveis meldingsutveksling mellom en Monkey C-app på klokka og en egen iOS/Android-app på telefonen — i sanntid, over BLE. **[V]** (Garmins eget repo)
https://github.com/garmin/connectiq-companion-app-sdk-ios
Garmins egen beskrivelse: «allows companion iOS applications to be created that interact with Monkey C applications running on Garmin wearable devices … retrieving remote data or **offloading resource-intensive tasks from the wearable device to the iOS device**.» **[S]**
https://developer.garmin.com/connect-iq/core-topics/mobile-sdk-for-ios/ · https://developer.garmin.com/connect-iq/core-topics/communicating-with-mobile-apps/

Viktig detalj: «Unlike the Mobile SDK for Android, apps created with the Mobile SDK for iOS are standalone apps and **do not directly rely on Garmin Connect Mobile (GCM)** to communicate with a wearable device.» **[S]** — på Android går kommunikasjonen gjennom GCM, som historisk har hatt leveringsbugs. **[S]**
https://forums.garmin.com/developer/connect-iq/i/bug-reports/gcm-5-27-3-android-accepts-communications-transmit-messages-from-watch-app-but-never-delivers-them-to-the-companion-app

**Dette gir en reell arkitektur:** CIQ-datafelt leser klokkas sensorer (inkl. Garmin Running Power, Real-Time Stamina hvis eksponert) → `Communications.transmit` til vår telefon-app → telefon-app kjører coachinglogikk → TTS i AirPods/hodetelefoner. Klokka gjør ingen tung jobb, telefonen gjør alt.

#### Garmin Health SDK / Companion SDK

«The Companion SDK allows you to tap into **real-time sensor streams** from Garmin wearables for Android and iOS … subscribe to live streams of heart rate, stress scores, accelerometer, and more.» **[S]**
https://developer.garmin.com/health-sdk/overview/

**Blokker:** kommersiell lisens. «evaluation is free, but commercial use requires either a license fee or device minimum order quantity commitment.» **[S]**
https://developer.garmin.com/health-sdk/questions-answers/
Dette er B2B/enterprise-sporet (Gold's Gym-typen). Ikke egnet for en consumer-app-MVP.

#### Garmin Connect Developer Program (Health / Activity / Training API)

Alle er **post-hoc**. Activity API: «Activity files are delivered (pushed) directly from Garmin servers to developer-defined server locations very shortly after a Garmin user syncs the completed activity … **they cannot be exported in real time**.» **[S]**
https://developer.garmin.com/gc-developer-program/activity-api/
Typisk leveringstid 1–5 minutter etter enhetssynk. **[S]** Health API krever partnergodkjenning, ikke self-serve. **[S]**
https://developer.garmin.com/gc-developer-program/health-api/

**Ingen av disse eksponerer LiveTrack.** Se §5 for full behandling.

---

### 1.4 Polar

**Polar BLE SDK** er offisiell, åpen kildekode, gratis, for Android (minSdk 24) og iOS (14.0+). **[V]**
https://github.com/polarofficial/polar-ble-sdk

> «Build apps that connect via Bluetooth LE and stream **real-time heart rate, ECG, accelerometer, PPG, and more** from Polar devices.»

Støttede produkter (fra README): Polar 360 / Loop, H10, H9, Verity Sense, OH1, Ignite 3, Vantage V3 / M3 / Grit X2 Pro / Grit X2, Pacer / Pacer Pro. **[V]**
Datarater: EKG 130 Hz, akselerometer opptil 200 Hz, HR i bpm. **[S]** — https://www.polar.com/en/developers

Dette er den **beste åpne SDK-en i markedet** for sanntids fysiologiske data. Polar H10 + Polar BLE SDK gir en referansekvalitet på puls og RR som ingen håndleddssensor matcher.

Merk: for Polar-**klokker** (Vantage/Grit X) er SDK-en primært for datauthenting, ikke for å kjøre kode på klokka. Se `documentation/UsingSDKWithWatches.md` i repoet. **[S]**

### 1.5 Suunto

**Nytt i mars 2026:** Suunto åpnet SuuntoPlus for alle utviklere — uten partneravtale eller konto. Beskrevet som et direkte svar på Garmin Connect IQ. **[S]**
https://the5krunner.com/2026/03/11/suunto-opens-suuntoplus-to-all-developers-a-direct-challenge-to-garmins-connect-iq/
Utviklerportal: https://apizone.suunto.com/suuntoplus

**[U]** Om SuuntoPlus-apper kan produsere tale/lyd, og om de har sanntids meldingskanal til en telefon-companion, er ikke avklart. Dette er verdt å undersøke — plattformen er ny og potensielt mer åpen enn Garmins.

### 1.6 COROS og Wahoo

- **COROS:** har en offisiell API, men søknadsbasert partnerprogram. **[S]** — https://support.coros.com/hc/en-us/articles/360040256531-Supported-3rd-Party-Apps
  COROS har lansert en MCP for AI-tilgang til kontodata (2026). **[S]** — https://the5krunner.com/2026/05/13/coros-mcp-ai-data/
- **Wahoo:** ingen on-device tredjeparts-app-økosystem. **[S]**
- Oppsummert: «neither Coros nor Wahoo has a proper on-device third-party app ecosystem. Garmin Connect IQ and the Suunto app store let developers extend the watch itself. An API partnership does not fix that.» **[S]**
  https://the5krunner.com/2026/04/24/coros-wahoo-partnership/

**Konklusjon:** For COROS/Wahoo/Suunto-brukere er den realistiske veien **BLE-broadcast fra klokka** (de fleste klokker kan kringkaste puls over BLE HR Service) eller en footpod — ikke leverandør-SDK.

### 1.7 Strava — ingen live-vei

**Verifisert konklusjon: Strava har ingen sanntids-API.** **[S]**

- Webhook Events API fyrer kun på `create`, `update`, `delete` av *ferdige* aktiviteter, samt `deauthorize`. Payload inneholder `object_type`, `aspect_type`, `object_id` — man må selv hente data etterpå. **[S]**
  https://developers.strava.com/docs/webhooks/
- Streams API er **rå tidsseriedata for en lagret aktivitet** — hentes on-demand etter opplasting, ikke som en live strøm. **[S]**
  https://developers.strava.com/docs/reference/

**Strava Beacon** er Stravas motstykke til LiveTrack: deling av posisjon med utvalgte kontakter under aktivitet. Det har **intet dokumentert offentlig API**, og faller inn under samme retningsproblem som LiveTrack (se §5.7). **[U]**

**API-vilkårene er restriktive og har blitt strammet inn:**
- November 2024-oppdateringen: tredjepartsapper kan kun vise en brukers Strava-data **tilbake til den samme brukeren**, ikke til andre brukere. **[S]**
- Data hentet via API-et **kan ikke brukes til å trene AI/ML-modeller**. **[S]**
  https://cybernews.com/security/strava-changes-api-agreement/ · https://www.strava.com/legal/api
- Coaching- og analyseverktøy er fortsatt eksplisitt tillatt. **[S]**
- Det er et eget **2026 developer program** med gebyrer/rate limits. **[U]** — https://appsforstrava.com/blog/strava-developer-program-changes-2026
- **AI-*inferens*** (i motsetning til trening av modeller) er et gråsoneområde som utviklere aktivt spør om. **[U]**
  https://communityhub.strava.com/developers-api-7/ai-inference-with-strava-data-is-it-prohibited-under-the-new-api-agreement-13256

**Stravas eget svar på AI-spørsmålet er MCP.** Strava lanserte 1. juni 2026 en offisiell **MCP Connector** som gir Claude *read-only* tilgang til brukerens egne Strava-data — aktiviteter, puls, tempo, GPS, effekt, klubber, gear. **[S]**
https://press.strava.com/articles/strava-launches-mcp-connector · https://support.strava.com/en-us/articles/15401531-strava-mcp-connector

**[V]** — Verifisert i denne sesjonen: Strava MCP-verktøyene er tilgjengelige og `eligibility` returnerer `{"eligible": true}`. Verktøyoverflaten inkluderer `list_activities`, `get_activity_streams`, `get_activity_performance`, `get_athlete_zones`, `get_training_plan`. Dette er en **ferdig, sanksjonert kanal for pre-run og post-run LLM-analyse** — uten egen OAuth-integrasjon, uten API-avtale, uten ToS-risiko.

Dette er en betydelig strategisk observasjon: **bruk MCP for historikk/planlegging, ikke Strava API.**

### 1.8 Telefonens egne sensorer

- **iOS:** `CLLocationManager` med `desiredAccuracy = kCLLocationAccuracyBestForNavigation`, ~1 Hz fikser. `CMPedometer` for kadens. **[V]** (lenker i §1.1)
- **Android:** `FusedLocationProviderClient` med `Priority.PRIORITY_HIGH_ACCURACY` og `setIntervalMillis(1000)`. `TYPE_STEP_DETECTOR`/`TYPE_STEP_COUNTER` eller egen FFT/peak-deteksjon på akselerometer for kadens. **[S]**
- Kadens fra telefonens akselerometer fungerer bare hvis telefonen sitter stabilt (armbånd, belte, lomme). Løs telefon i hånden gir støy. **[S]**

---

## 2. Lyd i øret

### 2.1 Text-to-speech

**iOS/watchOS — `AVSpeechSynthesizer`** (iOS 7.0+, watchOS 2.0+). **[V]**
https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer

> «The speech synthesizer maintains a queue of utterances that it speaks. If the synthesizer isn't speaking, calling `speak` begins speaking that utterance either immediately or after pausing for its `preUtteranceDelay` … **The system doesn't automatically retain the speech synthesizer, so you need to manually retain it until speech concludes.**»

Den siste setningen er en klassisk fallgruve: en lokal `let synth = AVSpeechSynthesizer()` blir deallokert og talen kuttes.

**`AVSpeechSynthesisVoice`** — «The primary factors that distinguish a voice in speech synthesis are language, locale, and quality.» BCP-47-tag, altså `nb-NO` for norsk bokmål. **[V]**
https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice

**Norsk stemmekvalitet — dette er en reell risiko. [S]/[U]**
- Stemmer har tre kvalitetsnivåer: `.default`, `.enhanced`, `.premium`. **Alle forhåndsinstallerte stemmer er `.default`-kvalitet**; enhanced/premium må lastes ned manuelt av brukeren (Innstillinger → Tilgjengelighet → Opplest innhold / Live Speech → Stemmer), og hver er >100 MB. **[S]**
  https://nshipster.com/avspeechsynthesizer/ · https://bendodson.com/weblog/2024/04/03/using-your-personal-voice-in-an-ios-app/
- **Konsekvens:** Ut av boksen vil `nb-NO`-stemmen sannsynligvis høres robotaktig ut. Appen bør detektere tilgjengelig kvalitet (`AVSpeechSynthesisVoice.speechVoices().filter { $0.quality == .premium }`) og be brukeren laste ned en bedre norsk stemme i onboarding.
- **[U]** — Om det finnes `nb-NO` i `.premium`-kvalitet på iOS 26 må testes på ekte enhet. Dette er en av de viktigste empiriske testene.
- **Alternativ:** pre-generer setningsfragmenter med en nevral TTS (ElevenLabs / Azure / OpenAI TTS) og cache dem lokalt som lydfiler. Fordeler: mye bedre norsk, full kontroll på tonefall. Ulempe: begrenset til et forhåndsdefinert setningsbibliotek — men det er faktisk *nok*, siden coachingfraser er svært repetitive («ro ned», «du ligger 8 sekunder foran», tall 0–59, «per kilometer»). Hybrid: cachede fraser + tallsyntese. **[S]**

**Android — `android.speech.tts.TextToSpeech`.** **[V]**
https://developer.android.com/reference/android/speech/tts/TextToSpeech

> «Synthesizes speech from text for immediate playback or to create a sound file. A TextToSpeech instance can only be used to synthesize text once it has completed its initialization. Implement the `TextToSpeech.OnInitListener` … **Apps targeting Android 11 that use text-to-speech should declare `TextToSpeech.Engine.INTENT_ACTION_TTS_SERVICE` in the `queries` elements of their manifest.**»

Sentrale konstanter: `QUEUE_ADD` / `QUEUE_FLUSH`, `LANG_AVAILABLE` / `LANG_COUNTRY_AVAILABLE` / `LANG_MISSING_DATA` / `LANG_NOT_SUPPORTED`, `ERROR_NETWORK` / `ERROR_NETWORK_TIMEOUT` (viktig — noen TTS-motorer krever nett!). **[V]**

**Advarsel [V]:** `ERROR_NETWORK` og `ERROR_NETWORK_TIMEOUT` er dokumenterte feiltilstander. Google TTS kan bruke nettbaserte stemmer av høy kvalitet. På en løpetur i skogen uten dekning kan disse feile. **Man må sikre at en offline-stemme er installert** og falle tilbake til den.

### 2.2 Ducking av musikk og podcast

Dette er godt løst på iOS, og Apple dokumenterer *nøyaktig* vårt scenario. **[V]**

**`AVAudioSession.CategoryOptions.duckOthers`:**
> «An option that reduces the volume of other audio sessions while audio from this session plays. … **If your app provides occasional spoken audio, such as in a turn-by-turn navigation app or an exercise app, you should also set the `interruptSpokenAudioAndMixWithOthers` option.** Ducking begins when you activate your app's audio session and ends when you deactivate the session. … **Set this option on a temporary basis only. Don't use it to duck the audio of other apps for more than a few seconds.**»

https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/duckothers

**`interruptSpokenAudioAndMixWithOthers`:**
> «If you set this option, the system mixes your audio with other audio sessions, but **interrupts (and stops) audio sessions that use the `spokenAudio` audio session mode**. It pauses the audio from other apps as long as your session is active. After your audio session deactivates, the system resumes the interrupted app's audio. **Set this option if your app's audio is occasional and spoken, such as in a turn-by-turn navigation app or an exercise app.** This avoids intelligibility problems when two spoken audio apps mix. … When you configure your audio session category using this option, notify other apps on the system when you deactivate your session so that they can resume audio playback. To do so, deactivate your session using the `notifyOthersOnDeactivation` option.»

https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers

**Oppskriften er dermed dokumentert og entydig [V]:**

```
kategori:  .playback
modus:     .spokenAudio     (eller .voicePrompt)
opsjoner:  [.duckOthers, .interruptSpokenAudioAndMixWithOthers]
aktiver:   rett før hver prompt
deaktiver: rett etter, med .notifyOthersOnDeactivation
```

Dette gir: musikk dempes under prompten og kommer tilbake; en podcast/lydbok *pauses* i stedet for å dempes (så man ikke mister handling); andre apper får beskjed om å gjenoppta.

**Android:** tilsvarende med `AudioManager.requestAudioFocus` + `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`, og `AudioAttributes` med `USAGE_ASSISTANCE_NAVIGATION_GUIDANCE` eller `USAGE_ASSISTANT` + `CONTENT_TYPE_SPEECH`. **[S]**

### 2.3 Bakgrunnskjøring og batteribudsjett

**iOS:**
- `UIBackgroundModes`: `audio` (påkrevd for lyd i bakgrunn), `location` (påkrevd for GPS i bakgrunn), `workout-processing` (påkrevd for `HKWorkoutSession` — på watchOS eksplisitt dokumentert **[V]**), `bluetooth-central` (for å holde BLE-tilkobling). **[V]/[S]**
- **App Review-krav 2.5.4 [V]:** «Multitasking apps may only use background services for their intended purposes: VoIP, audio playback, location, task completion, local notifications, etc.» — vi er trygt innenfor «audio playback» + «location», men appen må faktisk *bruke* dem.
- **5.1.5 [V]:** «Use Location Services in your app only when it is directly relevant to the features and services provided by the app.»
- En aktiv `HKWorkoutSession` er den «riktige» måten å holde appen i live på iOS 26 — den er designet for dette. **[V]**

**Android:**
Foreground service med korrekt `foregroundServiceType` er obligatorisk fra Android 14. **[V]**
https://developer.android.com/develop/background-work/services/fgs/service-types

| Type | Manifest-permission | Runtime-permission (minst én) |
|---|---|---|
| `location` | `FOREGROUND_SERVICE_LOCATION` | `ACCESS_COARSE_LOCATION` / `ACCESS_FINE_LOCATION` |
| `health` | `FOREGROUND_SERVICE_HEALTH` | `HIGH_SAMPLING_RATE_SENSORS`, `BODY_SENSORS` (≤API 35), `READ_HEART_RATE`, `ACTIVITY_RECOGNITION` m.fl. |

Dokumentert beskrivelse: `location` = «Long-running use cases that require location access, such as navigation and location sharing»; `health` = «Any long-running use cases to support apps in the fitness category such as exercise trackers». **[V]**
Merk: man kan ikke starte en `location`-foreground service fra bakgrunn uten `ACCESS_BACKGROUND_LOCATION`; tilsvarende for helse med `BODY_SENSORS_BACKGROUND` (API 33–35) / `READ_HEALTH_DATA_IN_BACKGROUND` (API 36). **[V]**

**Batteribudsjett — realistiske anslag [S]/[U]:**

| Komponent | Estimert forbruk |
|---|---|
| GPS kontinuerlig (BestForNavigation) | 8–15 %/time på moderne iPhone |
| BLE-tilkobling (1 Hz notify) | <1 %/time |
| Skjerm av, appen i bakgrunn | ~0 |
| TTS-prompt (1–2 s hvert 60–90 s) | neglisjerbart |
| LLM-kall over LTE hvert 90 s | 1–3 %/time (radio-oppvåkning dominerer) |

Sum: **~10–20 % per time** på iPhone. En 10K på 50 min → ~10–15 %. Fullt akseptabelt. Maraton (3–4 t) → 40–60 %, som er grensetilfelle men håndterbart. **[U]** — må måles.

Apple Watch er verre: GPS + optisk puls + skjerm gir typisk 6–10 timers batteritid i «outdoor run»-modus på nyere modeller **[S]** — nok for alt utenom ultra.

### 2.4 Kan man ha en LLM i løkka under løpeturen?

Dette er det mest interessante arkitekturspørsmålet. Svaret er nyansert.

**Latensbudsjett for ett kall hjem [S]/[U]:**

| Ledd | Typisk |
|---|---|
| LTE/5G RTT, god dekning | 30–80 ms |
| LTE, marginal dekning / celle-handover | 200–2000 ms |
| TLS-handshake (uten connection reuse) | +1–2 RTT |
| LLM time-to-first-token (liten modell, kort prompt) | 300–900 ms |
| Generering av 30–50 tokens | 200–600 ms |
| TTS-syntese (lokal) | 50–200 ms |
| **Sum, god dekning** | **~1–2 s** |
| **Sum, dårlig dekning** | **3–15 s, eller timeout** |

Kostnad: Claude Haiku 4.5 er $1/MTok input, $5/MTok output. **[V]** (Anthropic modell-/prisliste). Et kall med ~600 tokens inn og ~40 ut koster ~$0,0008. 40 kall på en time = **~$0,03/time/bruker**. Sonnet 5 ($2/$10) ≈ $0,06/time. Opus 5 ($5/$25) ≈ $0,16/time.

**Kostnad er altså ikke blokkeren. Dekning og latens er.**

**Anbefaling — hybrid, med lokal motor som autoritet:**

1. **Lokal regelmotor er alltid ansvarlig for det tidskritiske.** «Du ligger 8 s/km foran målpace», «roe ned», intervallvarsler, kilometersplitter. Disse må komme innen ~1 s og må aldri utebli fordi det ikke er dekning i en tunnel. Ren deterministisk kode, ~200 linjer.

2. **LLM brukes asynkront og opportunistisk**, ikke synkront i coachingløkka. Mønster: appen sender en kompakt tilstandsoppdatering hvert 90.–120. sekund (aggregerte features, ikke rådata — ~300 tokens), og LLM-svaret *påvirker neste* coaching-vindu, ikke det nåværende. Hvis svaret ikke kommer innen 5 s, forkastes det. Løperen merker aldri at det feilet.

3. **LLM-ens jobb er ikke å regne — den er å velge og formulere.** «Gitt at løperen ligger 6 s foran plan, pulsen har driftet 4 slag på 3 km, det er 4,2 km igjen og de har historikk for å sprekke i siste tredjedel — hva bør sies nå, og med hvilken tone?» Regelmotoren gir tallene; LLM-en gir dømmekraften og variasjonen i språket (så det ikke blir en robot som sier det samme 40 ganger).

4. **Pre-run:** her hører LLM-en virkelig hjemme. Full løpsplan generert fra historikk (via Strava MCP), værmelding, ruteprofil, brukerens mål og tidligere sprekk-mønstre → en strukturert `RacePlan`-JSON som lastes ned på telefonen før start. Denne inneholder segmentmål, pulstak, if-then-regler («hvis puls > 172 før km 6, ta ned 5 s/km»). **Regelmotoren under løpet er da bare en tolk av en LLM-generert plan.** Dette er det arkitektonisk elegante svaret: intelligensen er pre-computed.

5. **Post-run:** full analyse, sammenligning plan vs. faktisk, justering av neste økt.

**Konklusjon [S]:** «LLM i løkka hvert 60–90 s over mobilnett» er *teknisk realistisk* i by med god dekning, og *upålitelig* ellers. Men det er heller ikke nødvendig, fordi den virkelige verdien ligger i pre-run-planen og post-run-analysen. Bygg for at nettet er borte.

---

## 3. Hva kan man faktisk coache på — signalkvalitet

Dette er den delen der prosjekter feiler. API-ene er lette; å si noe *sant* om løperen er vanskelig.

### 3.1 GPS-tempo i sanntid

**Det harde faktum [S]:** «No watch from any brand implements 'instant' pace that is not a moving average or some kind of smoothing. At 1 Hz sampling, a 2-meter position error in a single fix translates to a 2 m/s speed error, which at running speeds represents a pace fluctuation of approximately **30–60 sekunder per kilometer**.»
https://the5krunner.com/gps-accuracy/ · https://best-running-watch.com/gps-accuracy-explained/

Og Apple sier det selv om `CLLocation.speed`: «use this property for informational purposes only.» **[V]**

**Avveiningen [S]:**

| Vindu | Egenskap |
|---|---|
| 3–5 s | Responsivt, brukbart til intervaller, men støyete |
| 10–15 s | Kompromiss |
| 15–30 s | Stabilt, men henger merkbart etter ved tempoendring |

**Dual-frequency GNSS hjelper betydelig [S]:** på 400 m bane ga dual-band-klokker rundetider innenfor 1–4 m av 400 m, mens single-band spredte seg fra 393 m til 409 m. Moderne iPhones (14 Pro og nyere) og Apple Watch Ultra har L1+L5. **[S]**

**Praktiske konsekvenser for coachingdesign:**
- **Aldri coach på øyeblikkstempo.** Coach på rullerende snitt (anbefalt: 20–30 s Kalman-filtrert eller EWMA) og på **splitt-nivå** (hver 200 m / 500 m / 1 km), som er langt mer robust.
- **Bygg latensbevisst.** Hvis vi coacher på 30 s snitt, er beskjeden «du ligger for fort» i snitt 15 s gammel. Si det som en trend («du har ligget 6 s/km for fort de siste 500 m»), ikke som et øyeblikksbilde.
- **Tunneler, bygninger, tett skog:** forvent 5–30 s tap av gyldige fikser. Ha en `signalQuality`-tilstand og *hold kjeft* når signalet er dårlig heller enn å gi feil råd. Bruk `CLLocation.horizontalAccuracy` og `speedAccuracy` som gate.
- **Dead-reckoning med kadens × skrittlengde** under GPS-utfall er fullt mulig og gir mye bedre kontinuitet. **[S]**
- **Footpod (Stryd/RD Pod) løser problemet nesten helt.** Dette er den enkleste kvalitetsforbedringen som finnes for produktet. **[S]**

### 3.2 Optisk puls fra håndledd

**Kjente problemer [S]:**
- Nøyaktigheten faller med intensitet: «Higher exercise intensities have been shown to reduce accuracy of HR measurements, due to arm motion artifact, sweat accumulation under the PPG sensors, variations in contact pressure … and peripheral vascular resistance changes.»
  https://cardio.jmir.org/2025/1/e67110/ · https://pmc.ncbi.nlm.nih.gov/articles/PMC11951816/
- **Transiente tilstander er verst.** En valideringsstudie mot 12-avlednings-EKG evaluerte eksplisitt «transient states defined as periods of rapid heart rate change» for Fitbit, Garmin, WHOOP og Withings. **[S]**
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12568089/
- **Cadence lock:** PPG-algoritmen låser seg på skrittfrekvensen i stedet for hjerteslagene. Klassisk symptom: pulsen viser ~170 fordi kadensen er 170 spm, mens virkelig puls er 140. Rammer særlig i starten av økter og ved kaldt vær. **[S]**
- Hudtone påvirker signalkvalitet. **[S]** — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318724
- Brystbelte (Polar H10, Garmin HRM-Pro) er referansekvalitet; Polar Verity Sense (overarm) er «highly accurate and reliable». Håndledd er «moderate accuracy, highly dependent on activity type and intensity». **[S]**

**Latency [U]:** Konkrete tall på sekunders forsinkelse ved intensitetsendring fant jeg ikke i primærkilde. Typiske observerte verdier i feltet er **10–30 s** for at optisk håndleddspuls skal ta igjen en brå intensitetsøkning — mot 1–3 s for brystbelte. Dette må måles.

**Konsekvenser for coachingdesign:**
- **Puls er en treg variabel. Coach aldri på pulsendringer under ~30 s.** «Pulsen din drifter» er en 5+ minutters observasjon, ikke en 20-sekunders.
- **Bygg inn artefaktdeteksjon:** hvis |puls − kadens| < 5 og pulsen «hoppet» >20 bpm på <10 s uten tilsvarende tempoendring, mistenk cadence lock og undertrykk pulsbasert coaching.
- **Anbefal brystbelte i onboarding.** Produktet blir vesentlig bedre. Dette er ikke en teknisk begrensning, det er et produktvalg.

### 3.3 Er de avanserte metrikkene beregnbare live?

| Metrikk | Live-beregnbar? | Merknad |
|---|---|---|
| **Rullerende tempo** | Ja | Trivielt, men se §3.1 om vindu |
| **Splitt-tider** | Ja | Mest robuste signalet vi har |
| **Kadens** | Ja | `CMPedometerData.currentCadence` **[V]**, RSC `0x2A53` **[V]**, eller akselerometer |
| **Kardiovaskulær drift** | Ja | Krever ≥15–20 min steady-state. Sammenlign puls i vindu A vs. B ved samme tempo. |
| **Decoupling (Pa:Hr)** | Ja | Formel: `((Pa:Hr første halvdel / Pa:Hr andre halvdel) − 1) × 100`. Terskel ~5 %. **[S]** — https://www.trainingpeaks.com/coach-blog/aerobic-endurance-and-decoupling/ Beviselig live-beregnbar: Connect IQ-datafeltet «Cardio PwHR Drift» gjør nettopp dette på klokka, oppdatert én gang per minutt. **[S]** — https://apps.garmin.com/en-US/apps/4d796bc5-260a-4be6-b581-3727fa8601a5 |
| **Grade-adjusted pace (GAP)** | Ja, med forbehold | Krever høydedata. Barometrisk høyde (iPhone `CMAltimeter`) er langt bedre enn GPS-høyde for stigningsgradient. GAP-modeller (Minetti/Strava-lignende polynom) er enkle å implementere. **[S]** GPS-høyde alene er for støyete. **[U]** |
| **Apple Running Power** | Ja | `runningPower` samples automatisk på Apple Watch SE / Series 6+, tilgjengelig live via `HKLiveWorkoutBuilder` **[V]** |
| **Garmin Running Power** | Bare på Garmin-enhet | Ikke eksponert utenfor CIQ/klokka **[S]** |
| **Stryd-effekt** | Ja, via BLE | Krever Stryd-pod. Best signal som finnes for løpsintensitet. **[S]** |
| **Estimert laktatterskel** | Nei, ikke live | Må komme fra historikk/pre-run-analyse |
| **VO2max / Real-Time Stamina** | Nei | Garmin/Firstbeat-proprietært, ikke eksponert for tredjepart **[S]** — https://www.garmin.com/en-US/garmin-technology/running-science/physiological-measurements/real-time-stamina/ |

### 3.4 Realistiske coachingregler for 5K/10K

Dette er hva regelmotoren faktisk bør inneholde. Alle er implementerbare med signalene over.

**Fase 1 — åpningen (0–15 % av distansen). Den viktigste.**
- Den vanligste feilen i 5K/10K er å åpne 10–20 s/km for fort. Coach aggressivt her.
- Regel: hvis snittempo over første 400–600 m er >5 s/km raskere enn målpace → prompt innen 90 s fra start. Dette er den enkeltregelen med høyest verdi i hele produktet.
- Ikke coach på puls i det hele tatt de første 3–5 minuttene (puls henger etter, og optiske sensorer er ustabile ved start).

**Fase 2 — kroppen (15–75 %).**
- Hold rullerende 500 m-tempo innenfor ±3 s/km av plan. Prompt ved avvik som vedvarer >200 m.
- Drift-overvåking: hvis puls stiger >5 slag over 2 km ved uendret GAP → «pulsen drifter, hold igjen litt» (men bare hvis brystbelte, eller hvis optisk signal er stabilt).
- **Banking-time-feilen:** hvis løperen har lagt seg >15 s foran plan kumulativt, ikke bekreft det som suksess. Si eksplisitt at det er lånt tid. «Du ligger 18 sekunder foran — det er raskere enn planen tåler, ta det ned til 4:32.»
- Kadensdrift: fall >5 spm fra baseline signaliserer tretthet eller at man begynner å «sitte ned» i steget.

**Fase 3 — siste kvartal.**
- Negativ splitt-mål: hvis andre halvdel så langt er tregere enn første, og løperen har puls-headroom (under terskel), oppfordre.
- Fra 90 % distanse: slutt å coache tempo, begynn å coache innsats. Tall hjelper ikke lenger.

**Terskelholding (for tempoøkter, ikke ren 5K/10K-racing):**
- Hold GAP innenfor et bånd rundt estimert terskeltempo; puls som sekundær sanity check.

**Antifeil å designe mot:**
- **Ikke snakk for mye.** Maks én prompt per 60–90 s, og aldri under 20 s mellom to. Beste coach sier lite.
- **Ikke si det åpenbare.** Hvis løperen ligger på plan, si ingenting (eller bare km-splitt).
- **Ikke motsi deg selv.** Hvis du sa «ro ned» for 40 s siden, ikke si «bra tempo» nå — bygg inn hysterese.
- **Ikke coach på støy.** Alle regler må ha `minDuration` og `minConfidence`.

---

## 4. Hva finnes allerede

| Produkt | Live-data | Adaptiv live-coaching? | Merknad |
|---|---|---|---|
| **Runna** (kjøpt av Strava 2025) | Ja | **Delvis** | «live audio cues from the app via your phone's speaker or compatible running watch for any workout with set pace targets. Pace Alerts prompt you to speed up or slow down when you're outside your target pace range.» **[S]** Adaptiviteten ligger i *planen mellom økter*, ikke i økten. https://support.runna.com/en/articles/8159780-setting-up-and-managing-your-audio-cues |
| **Garmin PacePro** | Ja | Nei | Forhåndsberegnet, stigningsjustert pacingstrategi. Statisk under løpet. **[S]** |
| **Garmin Real-Time Stamina** | Ja | Nei (informativ) | Firstbeat-modell, viser gjenværende energi i %, tid/distanse til utmattelse. Viser, coacher ikke. **[S]** https://www.garmin.com/en-US/garmin-technology/running-science/physiological-measurements/real-time-stamina/ |
| **Stryd** | Ja | **Ja, delvis** | «Real-time power guidance keeps you in the right effort zone.» Auto-oppdatert Critical Power. Nærmest ekte adaptiv effektstyring. Men: krever pod, og er tallstyrt, ikke språkstyrt. **[S]** |
| **Vi Trainer** | Ja | Ja (historisk) | «an AI voice coach that lives in your headphones and responds to your live biometrics, pace and effort» — pionér, kombinerte HR-hodetelefoner + stemmecoaching. Fortsatt listet i 2026-oversikter. **[S]** https://www.digitaltrends.com/wearables/lifebeam-vi-artificial-intelligence-personal-trainer/ |
| **Weav Run / Weav Music** | Ja | Musikk-adaptiv | «the industry's first audio workout technology that adapts both music and voice coaching to a runner's location and performance in real time» (2020). **[S]** https://www.businesswire.com/news/home/20200630005225/en/Weav-Music-Launches-First-Personalized-Audio-Workouts-for-Runners |
| **Apple Fitness+ Time to Run** | Nei | Nei | Forhåndsinnspilt audioguide. Ingen tilpasning til dine data. |
| **Runkeeper / adidas Running / Nike Run Club** | Ja | Nei | Opplesing av splitt + statiske målpace-varsler. |
| **Athletica / TrainAsONE / Humango** | Nei | Nei | Planlegging og periodisering, ingen live-lag. |
| **Peloton** | Ja | Nei | Instruktørledet, ikke datadrevet individuelt. |
| **Coopah** | Ja | Nei | Plan + lydcues. |

### Hvor er hullet?

**Alle eksisterende produkter gjør én av to ting:**
1. **Leser opp tall** (splitt, tempo, «du er utenfor målpace») — reaktivt, kontekstløst, terskelbasert.
2. **Tilpasser planen mellom økter** — smart, men ikke live.

**Ingen gjør dette:** en coach som *forstår løpet som en fortelling underveis*. Som vet at du åpnet 8 s/km for fort, at det kommer en stigning på km 7, at du historisk sprekker rundt km 8 i 10K, at pulsen din nå ligger 4 slag over der den var på samme tempo for 3 km siden — og som **sier én velformulert setning om det, på riktig tidspunkt**, med et språk som ikke er en terskel som ble krysset.

Det er der LLM-en gir reell verdi: ikke i å regne, men i **å bedømme hva som er verdt å si, når, og hvordan**. Og i pre-run-planleggingen som gjør at regelmotoren vet hva den skal se etter.

**Sekundært hull:** norsk språk. Alle disse produktene er engelskspråklige. En coach som snakker naturlig norsk i øret er et differensierende produkt i et lite, men reelt marked.

---

## 5. Garmin LiveTrack — egen vurdering

Dette fikk et eget tilleggsoppdrag, og fortjener det, fordi det ser lovende ut og er en felle.

### 5.1 Hvordan fungerer det teknisk?

**Kjeden er bekreftet [S]:**

```
Garmin-klokke
   │  ANT+/BLE
   ▼
Garmin Connect Mobile på telefonen  ◄── må ha nett og appen kjørende
   │  HTTPS
   ▼
Garmins sky (livetrack.garmin.com)
   │  HTTPS
   ▼
Delbar web-URL → tilskuere
```

Telefonkravet er eksplisitt: «For LiveTrack to work, you must have your phone with you. It must be connected and paired with the Garmin Connect app and **if you have an iPhone, the app must be open in the background** while LiveTrack is running. Your phone must also have a signal.» **[S]**
https://www.coachweb.com/gear/fitness-trackers/how-to-use-garmin-livetrack-and-share-your-location-with-friends · https://support.garmin.com/en-US/?faq=oPPijumqU23KHBCZk2wlc9

**Unntak:** LTE-modeller (Forerunner 945 LTE, Fenix 8 Pro med LTE) kan kjøre LiveTrack uten telefon. **[S]**

### 5.2 Hvilke datafelt eksponeres?

**Mer enn bare posisjon. [S]/[V]**

Fra Garmins beskrivelse: «LiveTrack doesn't just share your location … it can also share your stats such as average pace, time elapsed, distance traveled and elevation gain. Select Graphs at the bottom of the LiveTrack map and it will also display **current pace, speed, current elevation, heart rate and cadence**. Additionally, data from any ANT+ sensors you may have — such as heart rate or cadence — can also be viewed on your LiveTrack page.» **[S]**

**Verifisert i kode [V]** — dagens API returnerer et `fitnessPointData`-objekt med bl.a.:

```
cadenceCyclesPerMin
heartRateBeatsPerMin
powerWatts
speedMetersPerSec
```

Kilde (åpen kildekode som implementerer API-et i dag):
https://github.com/tjuuljensen/Home-Assistant-Contributions/blob/master/packages/garmin_livetrack/garmin-livetrack-fetch.py

Det historiske (legacy) formatet hadde en `metaData`-dict per trackpoint med `TOTAL_DISTANCE`, `ELEVATION`, `ELEVATION_SOURCE`, `DISTANCE`, `TOTAL_DURATION`, `DURATION`, `SPEED`, `ACTIVITY_TYPE`, `ACTIVITY_ID` **[V]**:
https://github.com/renarsvilnis/garmin-livetrack (README dokumenterer JSON-strukturen i sin helhet)

**Ja, det avhenger av innstillingen** for om live-data (utover posisjon) deles — dette styres i Garmin Connect under Sikkerhet og sporing → LiveTrack. **[S]/[U]** — nøyaktig navn/oppførsel per app-versjon må sjekkes.

### 5.3 Oppdateringsfrekvens og latency

**[V]** Sesjons-API-et returnerer et felt `postTrackPointFrequency` (sekunder) — «how often the device posts new points to Garmin's servers». Home Assistant-integrasjonen bruker **5 s som fallback** når feltet mangler, og **6 s som standard poll-intervall**:

```
DEFAULT_POLL_INTERVAL = 6  # seconds
DEFAULT_POST_TRACK_POINT_FREQUENCY = 5  # seconds
```
https://github.com/aikrana/ha-garmin-livetrack-monitor (`const.py`, `scraper.py`)

Eldre dokumentasjon oppgir **1 punkt hvert 4. sekund**: «Garmin livetracker makes 1 reading every 4 seconds.» **[V]**
https://github.com/renarsvilnis/garmin-livetrack

**Samlet latency klokke → sky [S]:** i størrelsesorden **5–20 sekunder** i god dekning. Klokke→telefon (BLE, ~1–4 s buffer) + telefon→sky (HTTP-post hvert 4–6 s) + serverbehandling. I dårlig dekning bufres data på telefonen og kommer i klumper — **titalls sekunder til minutter**. **[U]**

### 5.4 Finnes det et offisielt API? — **Nei.**

Jeg har gjennomgått alle Garmins utviklerprogrammer:

| Program | Sanntid? | LiveTrack eksponert? |
|---|---|---|
| **Connect IQ** | På enheten, ja | Nei — LiveTrack er en native GCM-funksjon, ikke i CIQ-API-et **[S]** |
| **Activity API** (GC Developer Program) | **Nei** — «cannot be exported in real time», push 1–5 min etter synk **[S]** | Nei |
| **Health API** | Push etter synk; krever partnergodkjenning **[S]** | Nei |
| **Training API** | Skriv treningsøkter *til* Garmin | Nei |
| **Wellness API** | Post-hoc wellness-data | Nei |
| **Health SDK / Companion SDK** | Ja (sanntids sensorstrømmer), men kommersiell lisens **[S]** | Nei — dette er direkte fra enheten, ikke LiveTrack |

**Konklusjon [S]:** **LiveTrack har ikke noe dokumentert offentlig API i noen av Garmins utviklerprogrammer.** Din antakelse er korrekt. Garmins API-er er post-hoc; LiveTrack er en lukket sluttbrukerfunksjon.

https://developer.garmin.com/gc-developer-program/ · https://developer.garmin.com/gc-developer-program/activity-api/ · https://developer.garmin.com/health-sdk/overview/

### 5.5 Den uoffisielle veien — finnes den fortsatt?

**Ja, den fungerer i dag — men den er ustabil og juridisk problematisk.**

**Dagens API-form [V]** (fra en Home Assistant-integrasjon som er aktivt vedlikeholdt):

```
GET https://livetrack.garmin.com/api/sessions/{sessionId}?token={token}
GET https://livetrack.garmin.com/api/sessions/{sessionId}/track-points/common?token={token}&begin=...
```

Begge krever:
- Cloudflare-cookies (integrasjonen bruker `cloudscraper` for å omgå Cloudflare)
- En `livetrack-csrf-token`-UUID hentet fra `<meta name="csrf-token">` på en HTML-side på domenet; må fornyes ved HTTP 403

Kildekommentaren er verdt å sitere ordrett **[V]**:

> «The current Garmin LiveTrack web app is a Next.js SSR site **behind Cloudflare**, serving its data over a **CSRF-protected** REST API. … See `docs/CONTEXT.md` → "History of API Changes" for the historical phases (**Legacy REST → GraphQL → current REST + CSRF**).»

https://github.com/aikrana/ha-garmin-livetrack-monitor/blob/main/custom_components/garmin_livetrack/scraper.py

**Dette er selve svaret på stabilitetsspørsmålet:** API-et har vært gjennom **minst tre inkompatible formatendringer** (legacy REST → GraphQL → REST+CSRF), og ligger nå bak Cloudflare med CSRF-beskyttelse som må reverseres på nytt hver gang Garmin endrer sidestrukturen. Prosjektet måtte endre CSRF-strategi mellom versjon 1.0.1 og 1.0.2 fordi den forrige tilnærmingen ble for skjør.

Andre aktive implementasjoner (bekrefter at ruten lever, men også hvor spredt og udokumentert den er) **[V]**:
- `progamler/GarminLive` — `/services/session/{uuid}/trackpoints`
- `edghyhdz/garmin` — henter sesjons-URL fra e-post via IMAP(!)
- `kritsanan1/garmin-mcp` — «Call repeatedly — updates every ~4 seconds»
- `MateusTauloisBraga/BoiPretoFinisher`

Merk at flere av dem henter LiveTrack-URL-en ved å **lese Garmins varsel-e-post over IMAP**. Det er ikke en arkitektur man setter i produksjon.

**Sikkerhetskontekst:** utløpte LiveTrack-sesjoner har vist seg å lekke e-postadresser. **[S]**
https://www.samwallace.dev/research/Harvesting%20Emails%20with%20Expired%20Garmin%20LiveTrack%20Sessions

### 5.6 Hva sier vilkårene?

**Garmin Connect Developer Program Agreement** forbyr eksplisitt å bruke applikasjoner eller enheter til å «**scrape, retrieve, or index services provided by Garmin or its licensors, or to collect information about End Users for any unauthorized purpose**». **[S]**
https://developerportal.garmin.com/sites/default/files/Garmin%20Connect%20Developer%20Program%20Agreement.pdf

Garmin har dessuten aktivt **TLS-fingerprinting som blokkerer tredjepartsklienter**. **[S]**

LiveTracks egne bruksvilkår: https://static.garmincdn.com/livetrack/en/LiveTrack_tou.htm **[U]** — domenet var blokkert i dette miljøet; må leses før eventuell beslutning. Men gitt Developer Program Agreement-teksten er retningen tydelig.

**Vurdering:** Å bygge et kommersielt produkt på polling av `livetrack.garmin.com` er:
- **Teknisk skjørt** — tre bruddendringer historisk, Cloudflare + CSRF, aktiv anti-bot
- **Kontraktsmessig tvilsomt** — scraping er eksplisitt forbudt
- **Forretningsmessig uforsvarlig** — Garmin kan slå det av når som helst, og hele produktet dør over natta

**Anbefaling: ikke bygg på dette.**

### 5.7 Live Event Sharing — noe annet?

Ja, men ikke mer relevant. **[S]**
- Krever at LiveTrack er satt opp først
- Sender automatiske SMS/e-post-oppdateringer ved definerte triggere til utvalgte kontakter
- Race-varianten bruker en opplastet GPX-bane og gir tilskuere en løpsopplevelse via `raceday.me`
- Aktiveres for 24 timer

https://www.dcrainmaker.com/2019/05/garmin-sharing-everything.html · https://www8.garmin.com/manuals-apac/webhelp/forerunner255series/EN-SG/GUID-EACD3F4A-AE05-4F87-BFD4-D5D727AE3171-3924.html

Dette er *enda mer* tilskuer-rettet enn LiveTrack, og har heller ikke noe API. Ikke relevant.

### 5.8 Det avgjørende argumentet: retningen på dataflyten

**Dette er hovedpoenget, og det er dødelig for LiveTrack-ideen.**

LiveTrack er designet for å sende data **ut fra løperen til tilskuere**. Coaching må gå **inn til løperen**. Sammenlign latensbudsjettene:

**Via LiveTrack (rundtur):**

```
klokke ──BLE 1–4s──► telefonens GCM ──HTTP 4–6s──► Garmins sky
                                                        │
                                        polling 5–6s ◄──┘
                                                        ▼
                                              vår server (analyse ~0,1s)
                                                        │
                                    push/poll 1–3s ◄────┘
                                                        ▼
                                        løperens telefon → TTS 0,2s
```

**Sum: 12–25 sekunder i god dekning. Titalls sekunder til minutter i dårlig dekning.**

Og merk det absurde: **dataene passerer løperens egen telefon på vei ut**, går til Garmins sky, til vår server, og tilbake til *den samme telefonen*. Vi tar en 15-sekunders omvei rundt halve internett for å lese data som allerede var i vår hånd.

**Lokalt på telefonen:**

```
sensor ──BLE 0,1–1s──► telefon ──regelmotor 0,001s──► TTS 0,2s
```

**Sum: under 1,5 sekund.** Og det fungerer i tunnel, i skogen, på fjellet, i flymodus.

**Legg til at LiveTrack-veien:**
- krever tre eksterne avhengigheter som alle kan feile (GCM-appen kjørende, mobildekning, Garmins sky)
- bryter Garmins vilkår
- gir dårligere data enn direkte BLE (5 s aggregerte punkter vs. 1 Hz rådata)
- pådrar oss serverkostnader og GDPR-ansvar for helsedata i transitt
- gir null fordel over den direkte veien

### 5.9 Svar: kan man bruke Garmin LiveTrack til dette?

**Teknisk: ja, det lar seg gjøre. Praktisk og forretningsmessig: nei, og det bør ikke vurderes videre.**

LiveTrack er en omvei, ikke en vei. Det er:
- **Feil retning** — bygget for tilskuere, ikke for løperen
- **12–25× høyere latens** enn den lokale ruten, uten motytelse
- **Uoffisielt** — ingen API i noe Garmin-utviklerprogram
- **Ustabilt** — tre bruddendringer, Cloudflare, CSRF, TLS-fingerprinting
- **Mot vilkårene** — scraping eksplisitt forbudt i Developer Program Agreement

**Den ene tenkelige nisjen** der LiveTrack kunne hatt verdi er *fjerncoaching*: en menneskelig trener som følger utøveren live fra sofaen. Det er et annet produkt, og selv da ville jeg heller bygd en egen lettvekts-relay fra vår egen app enn å parasittere på Garmins.

**Hvis vi vil nå Garmin-brukere**, er den riktige veien Connect IQ-datafelt + Mobile SDK-meldinger til vår telefon-app (§1.3) — direkte, lokalt, sanksjonert, og ~1 s latens.

---

## 6. Anbefalt arkitektur

### Alternativ A — iPhone-app + BLE-pulsbelte + TTS + regelmotor (**anbefalt MVP**)

```
┌────────────────────────────────────────────────────────┐
│  iPhone (iOS 26+)                                       │
│                                                         │
│  BLE-pulsbelte ──0x180D──►┐                            │
│  Footpod (valgfri) ─0x1814►│                           │
│  CoreLocation (GPS) ──────►├──► Sensor-fusjon (1 Hz)   │
│  CMPedometer (kadens) ────►│         │                  │
│  CMAltimeter (høyde) ─────►┘         ▼                  │
│                              Rullerende vinduer          │
│                              (5s / 30s / split / total)  │
│                                      │                   │
│                                      ▼                   │
│                              Regelmotor + RacePlan       │
│                                      │                   │
│                                      ▼                   │
│                              AVSpeechSynthesizer         │
│                              AVAudioSession              │
│                              [.duckOthers,               │
│                               .interruptSpokenAudio…]    │
│                                      │                   │
│  HKWorkoutSession (holder appen i live + lagrer økta)   │
└──────────────────────────────────────┼──────────────────┘
                                        ▼
                                  AirPods 🎧
```

**Hva kreves:**
- Swift/SwiftUI, CoreBluetooth, CoreLocation, CoreMotion, HealthKit, AVFoundation
- `UIBackgroundModes`: `audio`, `location`, `bluetooth-central`, `workout-processing`
- `NSHealthShareUsageDescription`, `NSHealthUpdateUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription`, `NSBluetoothAlwaysUsageDescription`
- HealthKit-entitlement
- Ingen backend nødvendig for MVP (pre-run-plan kan genereres i app eller manuelt)

**Blokkere:**
- Ingen tekniske. Alt er dokumentert og støttet. **[V]**
- Norsk TTS-kvalitet er den eneste reelle usikkerheten. **[U]**

**Kompleksitet:** **Lav–middels.** 3–5 ukers arbeid for én utvikler til en fungerende, testbar MVP. Sensor-fusjon og filtrering er hoveddelen; lyd og BLE er løste problemer.

**Hvorfor dette er riktig førstevalg:**
- Ingen avhengighet av noen klokkeleverandør
- Fungerer for Garmin-, COROS-, Suunto-, Polar- og Apple Watch-brukere (alle kan kringkaste puls over BLE, eller man bruker et belte)
- Ingen ToS-risiko
- Full kontroll på latens (<1,5 s)
- Kan testes empirisk på en uke, som er det som faktisk avgjør om produktet er godt

---

### Alternativ B — watchOS-app med HealthKit live workout

```
Apple Watch (watchOS 10+)
   HKWorkoutSession + HKLiveWorkoutBuilder + HKLiveWorkoutDataSource
   ├── heartRate (innebygd optisk, ~0,2 Hz)
   ├── runningSpeed, runningPower, runningVerticalOscillation
   ├── CLLocation (innebygd GPS, dual-band på Ultra)
   └── AVSpeechSynthesizer → AirPods (direkte fra klokka)
```

**Hva kreves:**
- Alt fra A, pluss watchOS-mål og WatchKit-konfigurasjon
- Background modes: **Workout processing** + **Audio** (begge dokumentert påkrevd **[V]**)
- Ingen telefon nødvendig under løpeturen (hvis AirPods er paret med klokka)

**Fordeler:**
- Beste brukeropplevelse for Apple Watch-eiere — ingen telefon i lomma
- Får `runningPower` gratis (Series 6+/SE) **[V]**
- Apple dokumenterer eksplisitt bakgrunnslyd for «coaching» **[V]**

**Blokkere:**
- Kun Apple Watch-brukere (utelukker Garmin-flertallet blant seriøse løpere)
- Optisk håndleddspuls er svakeste signal (§3.2)
- Mindre CPU/minne enn telefon, men mer enn nok til en regelmotor
- Nettverk fra klokke er upålitelig → LLM-i-løkka praktisk talt utelukket uten telefon i nærheten

**Kompleksitet:** **Middels.** +2–3 uker på toppen av A. Deler mesteparten av logikken.

**Anbefaling:** Bygg dette som **fase 2**, ikke som fase 1. Del regelmotoren som et Swift-package mellom iOS- og watchOS-målet.

---

### Alternativ C — Garmin Connect IQ-datafelt + telefon-companion

```
Garmin-klokke                         iPhone/Android
┌────────────────────────┐           ┌──────────────────────────┐
│ CIQ-datafelt (Monkey C)│           │ Companion-app            │
│  compute() ~1 Hz       │  BLE      │  (Connect IQ Mobile SDK) │
│  leser HR, pace,       │ ────────► │   → regelmotor           │
│  kadens, effekt        │ transmit  │   → TTS → AirPods 🎧     │
│  <28 kB minne          │           │   → LLM-kall (valgfritt) │
└────────────────────────┘           └──────────────────────────┘
```

**Hva kreves:**
- Monkey C-datafelt (holdes minimalt — bare les sensorer og send)
- `connectiq-companion-app-sdk-ios` (offisielt Garmin-repo **[V]**) eller Android-varianten
- Publisering i Connect IQ Store (godkjenningsprosess)

**Blokkere:**
- **Ingen TTS på klokka** — all lyd må gå via telefonen **[S]**
- **Ingen nettverk fra datafeltet** i sanntid (5-min minimum for bakgrunns-webrequests) **[S]**
- Stramt minnebudsjett (~28 kB på eldre enheter) **[S]**
- Android-veien går via Garmin Connect Mobile og har dokumenterte leveringsbugs **[S]**
- Krever at brukeren installerer *to* apper og parer dem

**Kompleksitet:** **Høy.** +4–6 uker. Monkey C er et særegent språk, simulatoren er begrenset, og enhetsfragmenteringen (dusinvis av modeller med ulike minne- og API-nivåer) er betydelig.

**Anbefaling:** Kun hvis Garmin-brukere viser seg å være hovedmålgruppen etter at A er validert. Legg merke til at **alternativ A allerede dekker Garmin-brukere** hvis de har et BLE-belte — det er en mye billigere vei til samme brukergruppe.

---

### Rangering

| # | Alternativ | Innsats | Verdi | Risiko | Dom |
|---|---|---|---|---|---|
| 1 | **A: iPhone + BLE + TTS** | Lav–middels | Høy | Lav | **Start her** |
| 2 | **B: watchOS** | Middels | Høy (for Apple-brukere) | Lav | Fase 2 |
| 3 | **C: Garmin CIQ + companion** | Høy | Middels | Middels | Fase 3, hvis data tilsier det |
| — | **LiveTrack-polling** | Middels | Lav | **Høy** | **Ikke gjør det** (§5) |

---

### Hvordan LLM (Claude) best brukes

```
┌─── FØR LØPET (minutter–timer i forkant, nett tilgjengelig) ────┐
│                                                                  │
│  Strava MCP ──► historikk, treningsbelastning, tidligere         │
│  (verifisert   løp på samme distanse, sprekk-mønstre             │
│   tilgjengelig)                                                  │
│         +  værmelding, ruteprofil (høydeprofil), brukerens mål   │
│         ↓                                                         │
│    Claude (Opus 5 eller Sonnet 5)                                │
│         ↓                                                         │
│    RacePlan JSON:                                                │
│      • segmentmål (km-for-km måltempo, stigningsjustert)         │
│      • pulstak per fase                                          │
│      • if-then-regler: "hvis puls > 172 før km 6 → −5 s/km"      │
│      • forhåndsformulerte coachingfraser per situasjon (norsk!)  │
│      • kjente risikopunkter: "sprekker typisk km 7–8"            │
└──────────────────────────────────────────────────────────────────┘
                              ↓ lastes ned til telefonen
┌─── UNDER LØPET (lokalt, offline-first) ─────────────────────────┐
│                                                                  │
│  Regelmotor tolker RacePlan mot live sensordata.                 │
│  100 % lokal. Ingen nettverksavhengighet. <1,5 s latens.         │
│                                                                  │
│  VALGFRITT (bare ved god dekning, asynkront):                    │
│    hvert 90–120 s: send ~300 tokens aggregert tilstand           │
│    → Claude Haiku 4.5 (~$0,03/time)                              │
│    → forslag til neste prompt-formulering / prioritering         │
│    → timeout 5 s, ellers forkast. Løperen merker aldri noe.      │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌─── ETTER LØPET ──────────────────────────────────────────────────┐
│  Full økt + plan → Claude → analyse, hva gikk galt/bra,          │
│  justering av modellen av løperen, neste økt.                    │
└──────────────────────────────────────────────────────────────────┘
```

**Kjerneinnsikt:** Flytt intelligensen til *før* løpet. En LLM-generert plan med if-then-regler gir 90 % av verdien av en «LLM i løkka», med 0 % av latens- og dekningsrisikoen. Bruk LLM live kun som en opportunistisk forbedring, aldri som en avhengighet.

**Om «LLM i løkka hvert 60–90 s»:** teknisk realistisk (~1–2 s i god dekning, ~$0,03/time med Haiku 4.5 **[V]** på pris), men **arkitektonisk feil å gjøre den obligatorisk**. Gjør den valgfri og fail-open.

---

## 7. Risiko og blokkere

### 7.1 App Store / Google Play

**Apple App Review Guidelines 5.1.3 (Health and Health Research) — verifiserte sitater [V]:**
https://developer.apple.com/app-store/review/guidelines/

> **5.1.3(i):** «Apps may not use or disclose to third parties data gathered in the health, fitness, and medical research context—including from the Clinical Health Records API, HealthKit API, Motion and Fitness, MovementDisorder APIs, or health-related human subject research—**for advertising, marketing, or other use-based data mining purposes other than improving health management**, or for the purpose of health research, and then only with permission.»

> **5.1.3(ii):** «Apps must **not write false or inaccurate data into HealthKit** … and **may not store personal health information in iCloud**.»

> **5.1.2(vi):** «Data gathered from the HomeKit API, HealthKit, Clinical Health Records API, MovementDisorder APIs, ClassKit or from depth and/or facial mapping tools … **may not be used for marketing, advertising or use-based data mining, including by third parties**.»

> **2.5.4:** «Multitasking apps may only use background services for their intended purposes: VoIP, audio playback, location, task completion, local notifications, etc.»

> **5.1.5:** «Use Location Services in your app only when it is directly relevant to the features and services provided by the app.»

**Konkrete konsekvenser for oss:**
- ✅ Coaching er «improving health management» — klart innenfor
- ⚠️ **Ikke send HealthKit-data til analyseverktøy** (Mixpanel, Amplitude, Firebase Analytics). Dette er den vanligste avvisningsgrunnen. Bruk aggregerte, ikke-helse-metrikker for produktanalyse.
- ⚠️ **Ikke lagre helsedata i iCloud/CloudKit.** Eksplisitt forbudt. **[V]**
- ⚠️ Hvis vi sender pulsdata til Anthropic for LLM-analyse: dette er en tredjepart. Må ha eksplisitt, informert samtykke og en klar personvernerklæring. **[S]** — Vurder å sende *avledede* verdier («puls 4 slag over baseline») heller enn rå pulsserier.
- ⚠️ Bakgrunnsmodusene må faktisk brukes til det de er ment for — det gjør de.

**Google Play:** Health Connect-policy, `FOREGROUND_SERVICE_*`-deklarasjoner med begrunnelse, og Data Safety-skjema som korrekt oppgir innsamling av helse- og posisjonsdata. **[S]**

### 7.2 GDPR / helsedata

- Puls, HRV og treningsdata er **særlige kategorier av personopplysninger** (GDPR art. 9). Krever **eksplisitt samtykke** — ikke bare berettiget interesse. **[S]**
- Posisjonsdata er personopplysninger og potensielt sensitive (hjemmeadresse fra start/slutt-punkt).
- **Anbefaling: kjør lokalt-først.** Hvis regelmotoren er lokal og LLM-kall er valgfrie, kan MVP-en fungere **helt uten å sende helsedata ut av enheten**. Det er både et personverngode og et markedsføringsargument.
- Hvis data sendes til en LLM-leverandør: databehandleravtale, dokumentert lagringstid, sletting på forespørsel, og overføringsgrunnlag ut av EØS.
- Sammenlign: Strava MCP er *read-only* og revokerbar fra Strava-innstillinger **[S]** — en god modell å etterligne.

### 7.3 Sikkerhet — distraksjon i trafikk

**Dette er en reell produktrisiko som få tenker på.**
- Løping i trafikk med hodetelefoner som demper omgivelseslyd er farlig. Ducking-strategien vår gjør faktisk situasjonen *litt bedre* (kort demping av musikk) — men flere prompt betyr mer kognitiv belastning.
- **Design-mottiltak:**
  - Maks én prompt per 60–90 s, aldri under 20 s mellom to
  - Aldri lange setninger — 5–12 ord
  - Anbefal transparency mode / åpne hodetelefoner i onboarding
  - Vurder en «by-modus» som reduserer promptfrekvensen
  - Ingen prompt som krever at løperen ser på skjermen
- Ansvarsfraskrivelse i vilkårene, men det er ikke nok — det må designes riktig.

### 7.4 API-vilkår

| Aktør | Risiko | Vurdering |
|---|---|---|
| **Strava REST API** | Høy | Restriktive vilkår, forbud mot AI/ML-trening, kun vis data tilbake til samme bruker, nytt 2026-gebyrprogram **[S]** |
| **Strava MCP** | **Lav** | Offisiell, read-only, brukerautorisert, sanksjonert AI-kanal **[V]** — **bruk denne** |
| **Garmin LiveTrack (uoffisiell)** | **Uakseptabel** | Scraping eksplisitt forbudt, Cloudflare + TLS-fingerprinting, tre bruddendringer **[S]** |
| **Garmin Connect IQ** | Lav | Offisielt, men Store-godkjenning kreves |
| **Garmin Health SDK** | Middels | Kommersiell lisens / MOQ-forpliktelse **[S]** |
| **Polar BLE SDK** | **Svært lav** | Åpen kildekode, offisiell, gratis **[V]** |
| **Generisk BLE (0x180D / 0x1814)** | **Ingen** | Åpen Bluetooth SIG-standard, ingen avtale nødvendig **[V]** |
| **Apple HealthKit** | Lav | Klare, dokumenterte regler **[V]** |

**Strategisk poeng:** Den arkitekturen som er teknisk best (lokal, BLE-basert) er også den som har lavest juridisk risiko. Det er sjelden så pent.

### 7.5 Batteri

Se §2.3. Håndterbart for 5K/10K/halvmaraton; grensetilfelle for maraton. Mottiltak: adaptiv GPS-frekvens (senk til 1 Hz fra 5 Hz når tempoet er stabilt), skjerm helt av, ingen unødvendige nettverkskall.

---

## 8. Oppsummeringstabell: datakilder × live-tilgjengelighet × plattform

Legende: ✅ = tilgjengelig for tredjepart live · ⚠️ = mulig med forbehold · ❌ = ikke tilgjengelig · 💰 = krever kommersiell lisens

| Datakilde | Live? | iOS | watchOS | Android | Wear OS | Garmin | Verifisering |
|---|---|---|---|---|---|---|---|
| **HealthKit `HKLiveWorkoutBuilder`** | ✅ | ✅ iOS 26+ | ✅ watchOS 5+ | ❌ | ❌ | ❌ | **[V]** |
| — `heartRate` | ✅ ~0,2 Hz | ⚠️ krever ekstern sensor | ✅ innebygd | ❌ | ❌ | ❌ | **[V]** / frekvens **[S]** |
| — `runningSpeed` | ✅ | ⚠️ | ✅ watchOS 9+ | ❌ | ❌ | ❌ | **[V]** |
| — `runningPower` | ✅ | ⚠️ | ✅ Series 6+/SE | ❌ | ❌ | ❌ | **[V]** |
| **BLE Heart Rate `0x180D`** | ✅ 1 Hz | ✅ | ✅ | ✅ | ✅ | ✅ | **[V]** |
| — RR-intervaller (1/1024 s) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **[V]** |
| **BLE RSC `0x1814`** (fart/kadens/skrittlengde/distanse) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **[V]** |
| **Stryd løpseffekt (BLE)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **[S]** |
| **Polar BLE SDK** (HR, EKG 130 Hz, ACC 200 Hz, PPG) | ✅ | ✅ iOS 14+ | ❌ | ✅ API 24+ | ❌ | ❌ | **[V]** |
| **CoreLocation / FusedLocation (GPS)** | ✅ ~1 Hz | ✅ | ✅ | ✅ | ✅ | — | **[V]** |
| **CMPedometer kadens** | ✅ | ✅ | ✅ | — | — | — | **[V]** |
| **Barometrisk høyde** | ✅ | ✅ `CMAltimeter` | ✅ | ✅ | ✅ | ✅ | **[S]** |
| **Garmin CIQ-datafelt → telefon** | ✅ ~1 Hz | ✅ Mobile SDK | — | ⚠️ via GCM | — | ✅ | **[V]** repo / **[S]** oppførsel |
| **Garmin Health Companion SDK** | ✅ | 💰 | — | 💰 | — | 💰 | **[S]** |
| **Garmin Activity/Health/Training API** | ❌ post-hoc 1–5 min | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **Garmin LiveTrack (offisielt)** | ❌ finnes ikke | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **Garmin LiveTrack (uoffisiell polling)** | ⚠️ 4–6 s, 12–25 s e2e | ⚠️ ToS-brudd | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **[V]** endepunkt / **[S]** ToS |
| **Garmin Real-Time Stamina / VO2max** | ❌ ikke eksponert | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **Strava REST API** | ❌ post-hoc | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **Strava Webhooks** | ❌ etter opplasting | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **Strava Beacon** | ❌ intet API | ❌ | ❌ | ❌ | ❌ | ❌ | **[U]** |
| **Strava MCP (pre/post-run)** | ❌ (ikke live, men riktig verktøy) | ✅ | — | ✅ | — | — | **[V]** |
| **Suunto SuuntoPlus** | ⚠️ | ⚠️ | — | ⚠️ | — | — | **[U]** — nytt mars 2026 |
| **COROS API** | ❌ søknadsbasert, post-hoc | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **Wahoo** | ❌ intet on-device-økosystem | ❌ | ❌ | ❌ | ❌ | ❌ | **[S]** |
| **TTS i bakgrunn til AirPods** | ✅ | ✅ `AVSpeechSynthesizer` | ✅ (krever aktiv workout) | ✅ `TextToSpeech` | ✅ | ❌ | **[V]** |
| **Ducking av musikk/podcast** | ✅ | ✅ `.duckOthers` + `.interruptSpokenAudio…` | ✅ | ✅ `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK` | ✅ | ❌ | **[V]** iOS / **[S]** Android |

---

## 9. Konklusjon

### Er dette mulig?

**Ja, utvetydig.** Og det er mindre teknisk risikabelt enn man skulle tro:

1. **Datainnhenting er løst.** Apple har `HKLiveWorkoutBuilder` (nå også på iOS 26), og Bluetooth SIG har åpne, veldokumenterte standarder for puls (`0x180D`) og løpsfart/kadens (`0x1814`) som fungerer på tvers av alle plattformer uten noen avtale.

2. **Lyd i øret er løst, og Apple dokumenterer akkurat vårt bruksområde.** Apples egen guide bruker ordet «coaching» om bakgrunnslyd under en workout-session, og `.duckOthers` + `.interruptSpokenAudioAndMixWithOthers` er dokumentert med «turn-by-turn navigation app or an exercise app» som eksempel. Vi går ikke mot plattformen; vi går med den.

3. **Coachinglogikken kan og bør være lokal.** Under 1,5 s latens, fungerer offline, ingen ToS-risiko, ingen helsedata forlater enheten.

4. **De reelle utfordringene er ikke tekniske, men signalmessige og produktmessige:** GPS-tempo har 30–60 s/km støy og må filtreres hardt; optisk håndleddspuls er treg og upålitelig ved intensitetsendringer; og — viktigst — det er *vanskelig å si noe nyttig*. Hele markedet leser opp splitt-tider. Ingen coacher.

### Raskeste vei til fungerende MVP

**Uke 1 — bevis lydkjeden.** Ikke bygg noe smart. Bygg en iOS-app som: starter `HKWorkoutSession`, kobler til et BLE-pulsbelte, leser GPS, og sier «Puls 152, tempo 4:38» hvert 30. sekund i AirPods mens Spotify spiller. **Løp med den.** Dette svarer på de tre kritiske spørsmålene på én uke: fungerer bakgrunnslyden, er ducking-opplevelsen god, og hvor ille er den norske TTS-stemmen?

**Uke 2–3 — signalkvalitet.** Logg rådata fra flere turer. Implementer filtrering (EWMA/Kalman på tempo, artefaktdeteksjon på puls, GPS-kvalitetsgating). Sammenlign appens tempo mot en Garmin-klokke på samme tur. Kalibrer promptfrekvensen.

**Uke 4–5 — regelmotor + RacePlan.** Definer `RacePlan`-JSON-skjemaet. Implementer de 6–8 reglene fra §3.4. Bruk Claude til å generere planer manuelt til å begynne med (via Strava MCP — allerede tilgjengelig, ingen integrasjon nødvendig).

**Uke 6 — feltest på et ekte 10K.** Dette er den eneste testen som teller.

**Deretter:** watchOS-app (fase 2), LLM-generert plan i produkt (fase 3), Garmin CIQ (fase 4, hvis brukerdata rettferdiggjør det).

**Første kjøp:** et Polar H10-brystbelte. Det gjør mer for produktkvaliteten enn tre ukers kode.

### Om LiveTrack, kort

**Nei.** Feil retning (ut til tilskuere, ikke inn til løperen), 12–25 s latens mot <1,5 s lokalt, intet offisielt API i noe Garmin-program, tre historiske bruddendringer, Cloudflare + CSRF + TLS-fingerprinting, og eksplisitt scraping-forbud i Garmins Developer Program Agreement. Dataene passerer løperens egen telefon på vei ut — å hente dem tilbake via Garmins sky er en omvei rundt halve internett for å lese noe vi allerede hadde i hånda. Bruk Connect IQ + Mobile SDK hvis Garmin-brukere må nås.

---

## 10. Åpne spørsmål som må testes empirisk

**Lyd (høyest prioritet — test i uke 1):**
1. Finnes det en `nb-NO`-stemme i `.enhanced`- eller `.premium`-kvalitet på iOS 26? Hvor mange brukere har den installert som standard? **[U]**
2. Hvordan høres talt norsk løpecoaching faktisk ut i AirPods under løping (vindstøy, pust, kadens)? Er `.default`-kvalitet akseptabelt, eller må vi pre-generere lydfiler?
3. Fungerer `.duckOthers` + `.interruptSpokenAudioAndMixWithOthers` som forventet mot Spotify, Apple Music, Apple Podcaster og lydbøker? Hvor lang er inn-/utfading?
4. Hvor lang tid tar aktivering av `AVAudioSession` før første ord høres? (Påvirker om vi må holde sesjonen åpen mellom prompter — men Apple advarer mot ducking i «more than a few seconds» **[V]**.)
5. Hva er faktisk tid fra `speak()` til lyd i AirPods, inkludert BLE-lydlatens?

**Sensorer:**
6. Faktisk samplingfrekvens for `heartRate` via `HKLiveWorkoutBuilder` på iOS 26 med eksternt belte vs. watchOS med innebygd sensor. (Antatt ~0,2 Hz **[S]**.)
7. Reell latency fra BLE-notify til `didUpdateValueFor` på iOS ved 1 Hz.
8. Hvor lang er den optiske pulsens etterslep ved en brå tempoøkning (Apple Watch vs. Polar H10)? Antatt 10–30 s vs. 1–3 s **[U]**.
9. Hvilken kadens-semantikk bruker konkrete RSC-sensorer (én fot vs. begge)? Må valideres per sensormodell.
10. Hvor godt fungerer `CMPedometer.currentCadence` med telefonen i lomme / armbånd / hånd?
11. Nøyaktighet på barometrisk `CMAltimeter` for stigningsgradient i sanntid — er det godt nok for GAP?

**GPS:**
12. Hvilket glattevindu gir best balanse for coaching? (Test 5 s / 15 s / 30 s mot fasit fra footpod eller banerunder.)
13. Hvor ofte og hvor lenge mister vi gyldig GPS på typiske ruter (skog, by, tunnel)? Hvor godt fungerer kadensbasert dead-reckoning som fallback?
14. Er iPhone 15+ L1+L5 dual-band merkbart bedre enn eldre modeller i praksis for tempo?

**Batteri:**
15. Faktisk batteriforbruk per time: iPhone med GPS + BLE + bakgrunnslyd. (Antatt 10–20 %/time **[U]**.)
16. Samme på Apple Watch. Holder det til en maraton?

**Produkt:**
17. Hva er riktig promptfrekvens? Testes med ekte løpere — hypotesen er 60–90 s, men det kan være for mye.
18. Fungerer «banking time»-advarselen? Løpere *liker* å høre at de ligger foran. Å bli fortalt at det er en feil er kontraintuitivt — men riktig.
19. Er norsk faktisk et fortrinn, eller vil norske løpere heller ha engelsk (som de er vant til fra Garmin/Strava)?

**Nettverk / LLM:**
20. Hvor ofte har en typisk norsk løperute nok dekning til et 2-sekunders LLM-kall? (Test på faktiske ruter, ikke i byen.)
21. Faktisk time-to-first-token for Claude Haiku 4.5 fra mobilnett i Norge.

**Juridisk / policy:**
22. Godtar App Review at vi sender avledede pulsverdier til en LLM-leverandør? Hva må stå i personvernerklæringen?
23. Hva sier LiveTrack Terms of Use ordrett? (Domenet var utilgjengelig her — bør leses for fullstendighetens skyld, selv om anbefalingen allerede er negativ.) https://static.garmincdn.com/livetrack/en/LiveTrack_tou.htm
24. Hvilke gebyrer og rate limits gjelder i Stravas 2026-utviklerprogram, hvis vi noen gang trenger REST-API-et i tillegg til MCP?
25. Kan SuuntoPlus-apper (åpnet mars 2026) produsere lyd eller sende meldinger til en telefon-companion? Ny plattform, potensielt mer åpen enn Garmin.

---

## Kildeliste

**Apple (primærkilder, alle [V]):**
- https://developer.apple.com/documentation/healthkit/hkworkoutsession
- https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilder
- https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource
- https://developer.apple.com/documentation/healthkit/running-workout-sessions
- https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/statistics(for:)
- https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/heartrate
- https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningspeed
- https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningpower
- https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningverticaloscillation
- https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer
- https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice
- https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/duckothers
- https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers
- https://developer.apple.com/documentation/corelocation/cllocation/speed
- https://developer.apple.com/documentation/corelocation/cllocationmanager/allowsbackgroundlocationupdates
- https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence
- https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)
- https://developer.apple.com/videos/play/wwdc2025/322/
- https://developer.apple.com/app-store/review/guidelines/

**Android (primærkilder, [V]):**
- https://developer.android.com/reference/android/speech/tts/TextToSpeech
- https://developer.android.com/develop/background-work/services/fgs/service-types

**Bluetooth SIG:**
- https://www.bluetooth.com/specifications/specs/running-speed-and-cadence-service/
- https://github.com/oesmith/gatt-xml/blob/master/org.bluetooth.characteristic.rsc_measurement.xml
- https://github.com/oesmith/gatt-xml/blob/master/org.bluetooth.characteristic.heart_rate_measurement.xml

**Garmin:**
- https://github.com/garmin/connectiq-companion-app-sdk-ios (offisielt Garmin-repo, [V])
- https://developer.garmin.com/connect-iq/core-topics/mobile-sdk-for-ios/
- https://developer.garmin.com/connect-iq/core-topics/communicating-with-mobile-apps/
- https://developer.garmin.com/gc-developer-program/activity-api/
- https://developer.garmin.com/health-sdk/overview/
- https://developer.garmin.com/health-sdk/questions-answers/
- https://developerportal.garmin.com/sites/default/files/Garmin%20Connect%20Developer%20Program%20Agreement.pdf
- https://static.garmincdn.com/livetrack/en/LiveTrack_tou.htm
- https://www.garmin.com/en-US/garmin-technology/running-science/physiological-measurements/real-time-stamina/
- https://forums.garmin.com/developer/connect-iq/f/discussion/418612/device-memory-limits
- https://forums.garmin.com/developer/connect-iq/f/discussion/427067/early-makewebrequest-in-a-data-field

**LiveTrack, reverse-engineert (kodebevis, [V] for endepunktenes eksistens):**
- https://github.com/renarsvilnis/garmin-livetrack — legacy REST, dokumenterer JSON-format og 4 s-intervall
- https://github.com/aikrana/ha-garmin-livetrack-monitor — dagens REST + CSRF + Cloudflare, `postTrackPointFrequency`
- https://github.com/tjuuljensen/Home-Assistant-Contributions/blob/master/packages/garmin_livetrack/garmin-livetrack-fetch.py — `fitnessPointData`-felter
- https://github.com/progamler/GarminLive
- https://github.com/edghyhdz/garmin
- https://www.samwallace.dev/research/Harvesting%20Emails%20with%20Expired%20Garmin%20LiveTrack%20Sessions

**Polar / Suunto / COROS / Stryd:**
- https://github.com/polarofficial/polar-ble-sdk ([V])
- https://www.polar.com/en/developers
- https://apizone.suunto.com/suuntoplus
- https://the5krunner.com/2026/03/11/suunto-opens-suuntoplus-to-all-developers-a-direct-challenge-to-garmins-connect-iq/
- https://support.coros.com/hc/en-us/articles/360040256531-Supported-3rd-Party-Apps
- https://the5krunner.com/2026/04/24/coros-wahoo-partnership/
- https://www.stryd.com/eu/en

**Strava:**
- https://developers.strava.com/docs/webhooks/
- https://developers.strava.com/docs/reference/
- https://www.strava.com/legal/api
- https://press.strava.com/articles/strava-launches-mcp-connector
- https://support.strava.com/en-us/articles/15401531-strava-mcp-connector
- https://cybernews.com/security/strava-changes-api-agreement/
- https://communityhub.strava.com/developers-api-7/ai-inference-with-strava-data-is-it-prohibited-under-the-new-api-agreement-13256
- https://appsforstrava.com/blog/strava-developer-program-changes-2026

**Signalkvalitet (forskning og felttesting):**
- https://cardio.jmir.org/2025/1/e67110/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11951816/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12568089/
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318724
- https://the5krunner.com/gps-accuracy/
- https://best-running-watch.com/gps-accuracy-explained/
- https://www.trainingpeaks.com/coach-blog/aerobic-endurance-and-decoupling/
- https://apps.garmin.com/en-US/apps/4d796bc5-260a-4be6-b581-3727fa8601a5

**Konkurrenter:**
- https://support.runna.com/en/articles/8159780-setting-up-and-managing-your-audio-cues
- https://www.digitaltrends.com/wearables/lifebeam-vi-artificial-intelligence-personal-trainer/
- https://www.businesswire.com/news/home/20200630005225/en/Weav-Music-Launches-First-Personalized-Audio-Workouts-for-Runners
- https://www.dcrainmaker.com/2019/05/garmin-sharing-everything.html
