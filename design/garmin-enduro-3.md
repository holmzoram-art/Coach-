# Arkitektur gitt Garmin Enduro 3

Brukerens klokke er en Garmin Enduro 3. Det avgjør arkitekturen, og
konklusjonen går på tvers av det man skulle tro: **klokka skal måle,
telefonen skal snakke.**

Konfidensmerking som i `research/live-coach-feasibility.md`:
`[V]` verifisert mot primærkilde, `[S]` sannsynlig, `[U]` må testes.

---

## 1. Blokkeren: Connect IQ har ingen talesyntese

Det nærliggende ønsket er en app som kjører på klokka alene og snakker
i hodetelefonene. Enduro 3 har 32 GB lagring og kobler Bluetooth-
hodetelefoner direkte, så maskinvaren er der. **Programvaren er det
ikke.**

Connect IQ eksponerer ingen text-to-speech-API. Garmins egne talte
lydvarsler genereres av Garmin Connect Mobile på telefonen og er
begrenset til forhåndsdefinerte varseltyper — rundetid, tempo, puls.
Tredjepartsapper kan ikke sende egen tekst inn i den kanalen. **[S]**
Utviklere på Garmins forum peker på forhåndsinnspilte lydfiler som
eneste omvei.

Det finnes en `Audio Content Provider`-API, men den er laget for
strømmetjenester — spillelister og spor, ikke korte innskutte
coachingfraser midt i en aktivitet. Om den kan misbrukes til formålet
er uavklart. **[U]**

Dermed: en ren klokkeløsning kan ikke si «du ligger 22 sekunder foran
skjema». Den kan vibrere og vise tall. Det er ikke produktet.

## 2. Hvorfor ikke Connect IQ med telefon-companion

Den åpenbare omveien er et CIQ-datafelt som sender splitten til en
companion-app på telefonen via `Communications.transmit`, og lar
telefonen snakke. Garmin har offisielle companion-SDK-er for både iOS
og Android. **[V]**

Vi bør likevel ikke gjøre dette, av tre grunner:

1. **Kjeden går gjennom Garmin Connect Mobile.** Meldingen fra klokka
   rutes gjennom Garmins egen app for å nå vår. Det er et ledd vi
   verken eier eller kan feilsøke.
2. **Leddet ryker i praksis.** Det foreligger en rapportert regresjon
   der `Communications.transmit` fra klokke til telefon aksepteres,
   men aldri leveres til companion-appen på Android — brudd rundt juni
   2026 uten endring på apputviklerens side. **[S]**
3. **Vi trenger den ikke.** Se neste punkt.

CIQ blir aktuelt igjen først hvis produktet en dag skal nå
Garmin-brukere som løper uten telefon. Da er det en egen fase, ikke en
forutsetning.

## 3. Anbefalt: klokka måler, telefonen snakker

```
Enduro 3                      iPhone/Android              Hodetelefoner
─────────                     ──────────────              ─────────────
Multi-band GPS  ─┐
Elevate v5 puls ─┼─ BLE ────► BLE-klient
Running Power   ─┘  0x180D    splittberegning
                    0x1814    regelmotor ──── TTS ──────► «6.14. Rett
                                                           på skjema.»
Tar opp økta som vanlig
og synker til Strava
```

Ingen Connect IQ-app. Ingen Garmin-SDK. Ingen avtale med Garmin. Vi
snakker standard Bluetooth-profiler som ingen eier: Heart Rate Service
`0x180D` og Running Speed and Cadence `0x1814`.

Fordelene er reelle:

- **Klokkas GPS er bedre enn telefonens.** Enduro 3 har multi-band
  GPS. Hvis den kringkaster fart og distanse over `0x1814`, arver vi
  målekvaliteten uten å gjøre noe.
- **Opptaket forblir uendret.** Økta havner i Garmin Connect og på
  Strava som før. Vi legger oss ved siden av, ikke i veien.
- **Ingen plattformrisiko.** Garmin kan ikke bryte noe vi ikke bruker.
- **Telefonen har talesyntese, batteri og nett.** Alt det klokka
  mangler.

Kostnaden er at telefonen må være med på turen. For en km-basert coach
i et 5k- eller 10k-løp er det ingen praktisk begrensning.

## 4. Det som må sjekkes på klokka først

Kringkasting av puls under aktivitet er dokumentert på nyere Garmin-
modeller og kan settes til å starte automatisk. **[S]** Om Enduro 3
også kringkaster fart og kadens som RSC er **[U]** og avgjør hvor mye
arbeid telefonen må gjøre selv.

Konkret, på klokka: `Innstillinger → Sensorer og tilbehør → Puls på
håndledd → Kringkast under aktivitet`. Og under løpsprofilen, se etter
et tilsvarende valg for løpsdata.

**Utfall A — også fart og kadens kringkastes.** Vi arver klokkas
multi-band-distanse. Splittene blir like nøyaktige som i Garmin
Connect, og telefonens GPS kan i prinsippet stå av.

**Utfall B — bare puls.** Telefonen må måle distanse selv med egen
GPS. Da får vi 1–2 % avvik på distansen, altså ±4–8 sek på splitten.
Som slått fast i `km-coach.md` er det fortsatt rikelig for
km-oppløsning — men appens kilometermarkering vil ligge litt forskjøvet
fra klokkas, og det må forklares brukeren i stedet for å oppleves som
en feil.

Utfall B er fullt brukbart. Utfall A er gratis oppside.

## 5. Konsekvens for MVP

Uke 1 i `km-coach.md` endres på ett punkt: ikke kjøp brystbelte ennå.
Mulighetsstudien anbefalte Polar H10 som første kjøp, men det gjaldt en
bruker uten pulsklokke. Enduro 3 kringkaster allerede puls, og
Elevate v5 er god nok når vi uansett midler over hele kilometeren.

Første oppgave blir dermed: koble telefonen til klokkas
pulskringkasting, og se hvilke BLE-tjenester som faktisk dukker opp i
scanningen. Det svarer på §4 på ti minutter, uten å skrive en linje
coachinglogikk.

Brystbelte kjøpes bare hvis feltest viser at håndleddspulsen svikter i
kulde eller ved høy intensitet.

## 6. Åpne spørsmål

1. Kringkaster Enduro 3 `0x1814` (fart og kadens), eller bare `0x180D`?
   **[U]** — avgjør utfall A vs. B over.
2. Kringkastes løpseffekt i det hele tatt? Garmin Running Power er
   ikke en standard BLE-profil, og er trolig utilgjengelig for
   telefonen. **[U]** Hvis ikke: effekt kan brukes i planlegging og
   etteranalyse via Strava, men ikke live.
3. Hvor mye batteri koster kringkasting over en 10k? Garmin oppgir at
   det reduserer batteritiden, uten tall. **[U]** Trolig uvesentlig på
   under en time.
4. Fungerer kringkasting samtidig med at klokka spiller musikk til
   hodetelefoner? Hvis brukeren hører musikk fra klokka, men coachen
   snakker fra telefonen, konkurrerer to kilder om samme ørepropper.
   Det er sannsynligvis den virkelige bruksbegrensningen — og taler for
   at musikken bør spilles fra telefonen. **[U]**
