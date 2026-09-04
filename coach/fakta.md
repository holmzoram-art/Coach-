# Faste fakta — les før du spør

Alt her er **avklart**. Spør du Knut om noe som står i denne fila, har du
kastet bort en tur. Feil som gjentas skal føres i `coach/laering.md`.

## Tid og sted

- Knut bor i **Norge (Tønsberg)**. Tidssone **Europe/Oslo** — CEST (UTC+2)
  om sommeren, CET (UTC+1) om vinteren.
- **Sjekk alltid klokka før du omtaler en økt:**
  `TZ=Europe/Oslo date`. Systemets tidsstempler er UTC og ligger 1–2 timer bak.
- **Han trener normalt fra ca. 16:30.** En økt planlagt «i dag» er som regel
  **ikke gjennomført** når han skriver på formiddagen. Aldri omtal dagens økt
  i fortid uten å ha sjekket Strava.
- Uka starter **mandag**. Søndagsøkta hører til slutten av uka.
- Arbeidsdag: lunsj i kantina ca. 10:40–11:10.

## Dette kommer automatisk — spør aldri om det

**Fra Strava** (`list_activities`, `get_activity_streams`, `get_activity_performance`):
- All løping: distanse, tid, fart per km, GAP, puls, pulskurve, kadens,
  høydemeter, splitter, relative effort, temperatur.
- **All styrketrening.** Han logger i Hevy, som synker til Strava med
  **fullstendig øvelsesliste, vekter, sett og reps i beskrivelsen.**
  Avvik fra styrkeplanen leses rett ut av dataen — be ham aldri skrive dem ned.
- **RPE** ligger i Stravas `perceived_exertion`-felt når det er satt.

**Fra Garmin-CSV** (`coach/soevn/`, lastes opp ca. hver fjerde uke):
søvnvarighet, sleep score, hvilepuls, HRV, Body Battery, hudtemperatur,
leggetid, våknetid.

## Fart-sammenligninger — skal alltid være stigningsjustert

**Høydeprofil er utledbart.** Høydemeter, hm/km, stigningsprofil, GAP, kadens,
puls og splitter hentes fra `get_activity_streams`. Vi kan alltid regne det ut.

**Regel:** ethvert fart- eller s/km-tall som sammenligner to økter skal enten
være **stigningsjustert (GAP)** eller **fra samme rute**. Rå snittfart mellom
to ulike ruter er ikke en måling — det er terrengforskjell blandet med form.

- Oppgi **hm/km for begge øktene** når du sammenligner. Ingen unntak.
- Er forskjellen i hm/km over ca. 3, kan rå fart ikke tolkes i det hele tatt.
- Dette gjelder også i kveldsspørsmål og ukestatus, ikke bare i analyser.
- Gjelder tilsvarende gåpauser: fart som blander løping og gange er ikke fart.

Bakgrunn: 03.09 hadde 11,0 hm/km mot 6,6 hm/km den 31.08. «22 s/km saktere
ved samme puls» ble tilskrevet stølhet. En ukjent andel var bakke.
Se `coach/laering.md`.

## Utledbart mot ikke utledbart — les før du ber om noe

| Utledbart (spør aldri) | Ikke utledbart (må spørres om) |
|---|---|
| Høydemeter, hm/km, stigningsprofil | Underlag: asfalt, grus, sti |
| GAP, splitter, fart per km | Vått løv, glatt, snø |
| Puls, pulskurve, kadens | Solo eller gruppe |
| Distanse, tid, relative effort | Hvordan det føltes, smerte |
| Styrkeøkter med vekter/sett/reps | Mage og næring på langtur |

**Temperatur er noen ganger med i Strava, ikke alltid.** Sjekk aktiviteten før
du enten spør om den eller fastslår at du har den.

**Skillet mellom instruks og rapportering:** «velg en flat rute» er en gyldig
instruks *før* økta — det er en beslutning Knut tar. Å be ham *rapportere*
profilen etterpå, eller å la et gyldighetskriterium hvile på hans anslag når
vi kan måle det, er feil. Gyldighet avgjøres på måledataen i etterkant.

## Dette må komme fra Knut

Bare dette, og det meste hentes gjennom **kveldsspørsmålet**, ikke som lekser:

1. **RPE** — spørres om i kveldsspørsmålet hvis den ikke er satt i Strava.
2. **Smerte** — sted, 0–10, bedre eller verre underveis.
3. **Mage og næring** på langturer.
4. **Kontekst klokka ikke ser** — solo eller gruppe, vær, føre, stress.

## Avklart om ham

- 38 år, 195 cm, 119 kg, makspuls 190.
- Tre års styrketrening. Løping startet i 2026.
- **Langturer kjøres i gruppe** — farten er ikke hans. Kvalitetsøkter er solo.
- Kantine på jobb med varmmat, salatbar og brød. Lager mat selv, god til det.
- Underskudd siden februar, 131 → 119 kg, platå siden juli.
- Fysioterapeut booket mandag 7. september (venstre kne).

## Oppløsning på Strava-strømmer

`get_activity_streams` tar en valgfri `resolution`. **Utelat den** — da får du
maksimal granularitet, ett punkt per sekund.

Hovedsamtalen hentet 04.09-økta med `resolution: 50`: 50 målepunkter for
6454 sekunder, ett per ~250 meter. Analysen som fulgte — andel gange,
kadensfordeling, fart på første og siste kilometer — var regnet på
stikkprøver og var derfor upålitelig.

**Regel:** analyse av strømmer gjøres av `fysiolog` eller
`belastning-restitusjon`, på full oppløsning, i deres egen kontekst.
Hovedsamtalen skal **ikke** hente strømmer og levere ferdigtygde tall videre
til agentene — da arver de en nedsampling de ikke vet om.

Hovedsamtalen kan hente `list_activities` (sammendrag) for å vite hva som er
gjennomført. Strømmer er agentenes bord.

## Kadens — Strava oppgir per bein

`avg_cadence` fra Strava er **per bein**. Skrittfrekvens = tallet × 2.

| Strava | Faktisk |
|---|---|
| 78 | 156 skritt/min |
| 70 | 140 skritt/min |

Knuts klokke viser skrittfrekvens. **Snakk alltid i skritt/min**, ikke i
Stravas råtall — ellers stemmer det ikke med det han ser.

## Gruppelangturer — gange er ofte planlagt

På gruppelangturer får de beskjed om å gå når det blir tungt, og dårlig sti
tvinger fram gange. **Gangpauser er derfor ikke automatisk et tretthetssignal.**
Spør før du tolker.
