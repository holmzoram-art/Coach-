# Stående instrukser

Leses av `hovedcoach` før hvert kveldsspørsmål. Instrukser her overstyrer
agentenes egne regler.

## Spørsmålsinstrukser

_(Tom. Fylles ut når Knut gir feedback på spørsmålene — hver kommentar av typen
«ikke spør om X» eller «spør heller om Y» skal føres inn her med dato og hva
som utløste den.)_

## Rammer

- Mål: Holmestrand Maraton, lørdag 3. april 2027.
- Treningsplanen ligger i artifact «Marathon».
- Primærkilde for gjennomførte økter: Strava-MCP.

## Beslutninger

- [2026-09-03] **MP er et mål vi bygger, ikke en måling av dagsformen.** Planen
  skal alltid vise begge: målfart (7:05–7:15) og arbeidsfart nå (7:35–7:50).
  MP-økter kjøres på arbeidsfarten; målet er det vi sikter mot i april.
  (Knut: «Det som er viktig er vi bygger MP og ikke hva den er nå.»)
- [2026-09-03] Fjerde løpeøkt lagt inn: søndag, 4 km rolig fra 13. sept,
  progresjon 4 → 5 → 6 → 7 km. Puls 130–142. Droppes/kortes i deload-uker.
- [2026-09-03] Langturen står på 16–18 km til langturandelen er under 40 %
  av ukesvolumet.

## Åpne punkter

- **HRmax ikke verifisert.** Høyeste målte i år: 187 (25. juli). Sonetabellen
  forutsetter ~207. Krever ekte makstest før sonene justeres.
- **Banedata mangler:** høydeprofil/GPX for 5 km-runden i Holmestrand,
  plassering av de 3 drikkestasjonene, hvor de siste 2,195 km legges.
- Maks tid i løpet er **6 timer** — reell begrensning.

## Flaggterskler — søvn og restitusjon

Satt av `belastning-restitusjon` 03.09.26 på 28 dagers Garmin-data.
Baseline: hvilepuls 43,5 ± 1,5 · HRV 74,8 ± 1,6 · varighet 7t21 ± 58 min.

| Signal | Terskel | Handling |
|---|---|---|
| Hvilepuls | ≥ 46 én natt | Rolig I1, maks 45 min |
| Hvilepuls | ≥ 45 to netter | Ingen hard økt eller langtur på 48 t |
| HRV | ≤ 72 | Ingen hard økt i dag |
| HRV | ≤ 73 to netter | Deload uka |
| Varighet | < 6t30 | Flytt dagens harde økt |
| Varighet | **< 7t to netter før langtur** | **Økta flyttes. Ingen unntak.** |
| Body Battery | < 45 / < 40 | Rolig / fri |
| Hudtemp ≥ +0,5° + hvilepuls ≥ 45 | — | Infeksjonsmistanke, ingenting over I2 |
| Sleep Score | < 60 | Fri fra løping |

Bakgrunn: 18-kilometeren 27.08 fikk 7,2 % HR-drift og kadensfall 77,7 → 64,5.
Nettene før var 6t18 og 6t58, og morgenen hadde hvilepuls 45 (periodetopp) og
HRV 73 (periodebunn). Økta var ikke for lang — han var for dårlig uthvilt.

## Treningskontekst — viktig for tolkning av data

- [2026-09-03] **Langturer og lange løp kjøres i gruppe.** Farten er ikke
  Knuts egen — han må ofte holde igjen så alle henger med. Det betyr at
  fart, puls og EF fra langturer **ikke er rene målinger av formen hans**.
  `fysiolog` skal ikke lese trend ut av gruppeturer uten å si fra om dette.
- [2026-09-03] **Intervaller og tempoøkter kjøres solo.** Det er de rene
  dataene. Terskelutvikling og formkurve skal bygges på disse, ikke på
  langturene.
- [2026-09-03] Knut har selv bedt om **solo testøkter** for å kartlegge
  hvor han faktisk ligger. Det er riktig instinkt og skal inn i planen.

## Soner — revidert 03.09.26 (makspuls 190)

OLT-modellen. Erstatter den gamle tabellen, som forutsatte makspuls ~207.

| Sone | % av 190 | Puls | Bruk |
|---|---|---|---|
| I1 | 62–72 | 118–136 | Restitusjon |
| I2 | 72–82 | 137–156 | Rolig / langtur |
| I3 | 82–87 | 156–165 | Sub-terskel — her ligger tempoøktene |
| I4 | 87–92 | 166–175 | Terskel |
| I5 | 92–100 | 175–190 | VO2 |

Anaerob terskel: **puls 170 ± 3**, terskelfart 6:20–6:30/km flatt.
Forankret i 10 km 22.07 (64:40, snittpuls 166, siste km 178).

Intensiteten i tempoøktene er uendret — de het bare feil. Rettet er
VO2-øktene, der gulvet på puls 185 lå over det han når.

## Testprotokoll — solo

**Referanseøkt «8K Flat», hver 3.–4. uke.** 8,0 km på samme flate asfaltrunde,
solo, 15 min oppvarming logget separat, deretter **pulslås 145 ± 3**. Farten er
utfallet, ikke målet. Logges: GAP-fart, snittpuls, EF, kadens per km, Pa:HR,
temperatur, RPE. Ugyldig ved over 20 grader, under 48 t etter hardøkt, eller
mageuro. Koster én rolig økt, ikke en kvalitetsøkt.

**Testløp:** 10 km hardt uke 8 (slutten av okt) · halvmaraton uke 18 (midten av
jan) · 10 km eller HM uke 26 (slutten av feb).

**Solo langturer:** uke 10 (nov) og uke 22 (feb), 18–20 km i egen I2-fart.
Gruppelangturer beholdes for volum, men EF derfra føres i egen kolonne og
sammenlignes kun mot andre gruppelangturer.
