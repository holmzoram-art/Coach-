# Km-basert løpecoach — designspesifikasjon

Én melding per kilometer. Ingen kontinuerlig overvåking, ingen løpende
kommentar. Løperen hører 5 meldinger på en 5k, 10 på en 10k.

Dette dokumentet spesifiserer hva som utløser en melding, hva den
inneholder, og hvordan innholdet bestemmes. Det bygger på
`research/live-coach-feasibility.md`, men snevrer inn scope betydelig.

---

## 1. Hvorfor kilometersplitt er riktig oppløsning

Mulighetsstudien identifiserte signalkvalitet som den største tekniske
risikoen: GPS-øyeblikkstempo har 30–60 s/km støy, og Apple advarer selv
mot å bruke `CLLocation.speed` til annet enn informasjon.

**En kilometersplitt er en helt annen målestørrelse.** Den er et
gjennomsnitt over 4–7 minutter. Feilen i GPS-distanse over 1 km ligger
typisk på 1–2 %, som gir ±4–8 s/km på splitten. Det er omtrent en
tidels så mye støy som på øyeblikkstempo, og godt innenfor det som
trengs for å avgjøre om noen ligger foran eller bak skjema.

Samme effekt gjelder puls: et snitt over hele kilometeren er upåvirket
av den optiske sensorens 10–30 sekunders etterslep ved
intensitetsendringer.

Kort sagt: oppløsningen brukeren ba om er også den eneste oppløsningen
der dataene er til å stole på.

## 2. Hva dette fjerner fra prosjektet

| Fra mulighetsstudien | Status med km-basert design |
|---|---|
| Filtrering av GPS-tempo (EWMA/Kalman) | Faller bort — splitten er allerede et snitt |
| Artefaktdeteksjon på puls | Kraftig redusert — snitt over 4–7 min |
| Kalibrering av promptfrekvens | Avgjort: én per km |
| Latensbudsjett under 1,5 s | Faller bort — se §6 |
| Risiko for å mase / distrahere | Nesten borte — 10 meldinger på en time |

Det som står igjen som reell vanskelighet er ikke lenger teknisk. Det
er å ha noe verdt å si.

## 3. Utløsere

En melding spilles av ved:

- **Hver hele kilometer** (auto-lap på akkumulert distanse)
- **Start** — kort bekreftelse av planen, før første kilometer
- **Mål** — oppsummering

Og i tillegg, som eneste unntak fra km-regelen:

- **Nødbrems** — hvis pulsen ligger over makstaket i mer enn 60
  sammenhengende sekunder tidlig i løpet. Dette er den ene situasjonen
  der det er for sent å vente til neste kilometer. Maks én slik melding
  per løp.

Ingenting annet avbryter. Ingen halvkilometer, ingen segmentvarsler,
ingen «bra jobbet»-innskudd.

### Om lap-punktets drift

Auto-lap utløses på appens egen distansemåling, ikke på fysiske
kilometermarkeringer. Med 1,5 % GPS-avvik ligger appens km 10 rundt
150 m fra målstreken i et løp. For egentrening er dette irrelevant —
avviket er konsistent. I et arrangert løp bør brukeren vite det, ellers
oppleves det som en feil. Vises i etterkant, ikke under.

## 4. Meldingens form

Maks tre deler, i denne rekkefølgen. Under 8 sekunder tale totalt
(≈ 20 ord på norsk).

1. **Status** — hvor du står. Alltid med.
   > «Kilometer 4 på 6.05. Du ligger 22 sekunder foran skjema.»

2. **Handling** — én instruksjon. Alltid med.
   > «Slipp litt. Sikt på 6.20 herfra.»

3. **Begrunnelse** — kun når den endrer atferd. Ofte utelatt.
   > «Pulsen har klatret åtte slag på samme tempo.»

Regler for språket:

- Tall leses som tempo, ikke desimaler: «seks null fem», ikke «6,05».
- Aldri to instruksjoner i samme melding. Løperen husker én.
- Aldri ros uten informasjon. «Bra jobbet» alene er støy.
- Instruksjonen skal være noe som kan utføres i løpet av neste
  kilometer. «Hold igjen» er utførbart. «Bli sterkere» er ikke.

## 5. Data per splitt

Beregnes når kilometeren lukkes:

| Felt | Kilde | Bruk |
|---|---|---|
| `splitTime` | Akkumulert distanse + klokke | Status |
| `avgHR` | HealthKit / BLE `0x180D` | Driftdeteksjon |
| `avgPower` | BLE effektmåler | Innsatsstyring i kupert terreng |
| `avgCadence` | BLE `0x1814` / `CMPedometer` | Tretthetsindikator |
| `elevGain` | `CMAltimeter` (barometrisk) | Stigningsjustering |
| `cumulativeTime` | Klokke | Avvik mot skjema |

Alle felt er valgfrie utenom `splitTime` og `cumulativeTime`. Coachen
degraderer nedover: uten effektmåler brukes tempo, uten puls brukes
bare tempo. Den skal aldri tie fordi en sensor mangler.

## 6. Latensbudsjettet er nå enormt

Mellom to meldinger går det 4–7 minutter. Det betyr at et LLM-kall
midt i løpet ikke lenger er risikabelt — det var den viktigste
innvendingen i mulighetsstudien, og den gjelder ikke her.

Mønsteret:

1. Splitten lukkes. Lokal regelmotor beregner umiddelbart en gyldig
   melding og holder den klar.
2. Samtidig sendes hele løpshistorikken så langt til modellen.
3. Kommer svar innen 3 sekunder, sies det. Ellers sies regelmotorens
   melding.
4. Uansett utfall er neste beslutningspunkt 4–7 minutter unna.

Løperen merker aldri forskjell på om kallet gikk gjennom. Dekning i
skogen slutter å være en blokker, fordi fallbacken alltid er der. Ti
kall per løpetur koster øre.

**Hva modellen tilfører over regelmotoren:** regler ser på én splitt av
gangen. Modellen ser fortellingen — at dette er tredje kilometer på rad
der pulsen stiger uten at tempoet gjør det, at åpningen var for hard i
forhold til hvordan de tre siste turene så ut, at det gjenstår en
motbakke på km 8 som planen forutsetter at du har noe igjen til.

## 7. Beslutningslogikk

Regelmotoren evalueres i prioritert rekkefølge. Første treff vinner —
det sendes aldri to instruksjoner.

1. **Puls over tak** → «Du ligger over taket. Slipp tempoet nå.»
2. **For rask åpning** (km 1–3 mer enn 15 s/km foran plan) →
   «Det er for kjapt så tidlig. Legg deg på `målpace`.»
3. **Kardiovaskulær drift** (puls +8 slag over tre km på uendret
   tempo) → «Pulsen klatrer på samme tempo. Ta av fem sekunder.»
4. **Bak skjema, har margin** (puls under tak) → «Du kan ta litt igjen.
   Prøv `målpace minus 5` neste kilometer.»
5. **Bak skjema, ingen margin** → planen revideres nedover, og det sies
   rett ut: «Vi justerer målet til `ny tid`. Hold det du har.»
6. **På skjema** → «Du ligger rett på. Fortsett akkurat sånn.»

Punkt 5 er det som skiller en coach fra en stoppeklokke. En plan som
ikke lar seg justere underveis er ikke en plan, den er en dom.

## 8. Eksempel: 10 km, mål 1.02.00

Målpace 6.12/km. Pulstak 172 til og med km 7, deretter åpent.

| Km | Splitt | Puls | Melding |
|---|---|---|---|
| Start | — | — | «Mål 1.02. Første tre kilometer på 6.20, det skal føles for lett.» |
| 1 | 5.58 | 148 | «5.58 er 22 sekunder for kjapt. Roe ned til 6.20.» |
| 2 | 6.18 | 154 | «6.18. Bedre. Hold den.» |
| 3 | 6.21 | 158 | «6.21, du ligger 23 sekunder foran. Nå kan du gå ned på 6.12.» |
| 4 | 6.14 | 163 | «6.14. Rett på skjema.» |
| 5 | 6.10 | 168 | «Halvveis på 31.01. Pulsen er høy for å være her. Hold 6.15.» |
| 6 | 6.16 | 169 | «6.16. Bra kontroll.» |
| 7 | 6.20 | 171 | «Du taper litt. Fire kilometer igjen — nå kan du bruke av reservene.» |
| 8 | 6.14 | 176 | «6.14, sterkt. Ligg der.» |
| 9 | 6.11 | 180 | «Én kilometer igjen, du ligger an til 1.02.10. Alt du har nå.» |
| 10 | 5.52 | 186 | «1.01.54. Under målet.» |

Legg merke til at km 2, 4, 6 og 8 nesten ikke sier noe. Det er
meningen. En coach som har en mening om hver eneste kilometer, blir
ignorert innen km 5.

## 9. Konsekvens for MVP

Mulighetsstudiens uke 1 — bevis lydkjeden — står uendret, men blir
enklere: si splitten høyt hver kilometer mens musikken spiller. Ingen
filtrering, ingen sensorfusjon.

Uke 2 blir regelmotoren i §7, som er under hundre linjer kode og
testbar mot lagrede aktiviteter uten å løpe en meter.

Uke 3 er feltest. LLM-laget i §6 kan legges til når som helst etterpå
uten å røre resten, fordi fallbacken er selve regelmotoren.

## 10. Åpne spørsmål

1. Skal km-splitten leses opp *før* eller *etter* instruksjonen?
   Hypotesen er før — løperen venter på tallet og hører ikke etter før
   det er sagt.
2. Er nødbremsen i §3 verdt kompleksiteten, eller holder det å vente
   til neste kilometer også der?
3. Hvordan varsles en revidert målsetting (§7 punkt 5) uten at det
   oppleves som at appen gir opp på dine vegne?
4. Bør stigningsjustert tempo brukes i statusmeldingen, eller bare i
   beslutningen? Å høre «6.40, men det var motbakke» er ærligere, men
   lengre.
5. Hva sies på km 1 hvis GPS-en ennå ikke har låst seg skikkelig?
