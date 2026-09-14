# Treningsplanen

**Kilde: artifacten «Marathon»** — https://claude.ai/code/artifact/6086486b-ac75-4f4b-9dae-66f0f792d4d4
Denne fila er en kopi av plandataen i artifacten, lagt i repoet fordi agentene
ikke kan lese artifacter. **Endres planen i artifacten, skal denne oppdateres.**

Hentet 10.09.2026.

> **Regel for alle agenter:** før du spør Knut hva som sto på planen, eller
> antar at en økt ble valgt der og da — **les denne fila**. Han følger planen.
> Avvik han gjør, sier han fra om selv.

Mål: **Holmestrand Maraton, lørdag 3. april 2027.**

---

## Ukestruktur

Fem dager fra uke 3: **fire løpeøkter og én styrke.**

| Dag | Rolle |
|---|---|
| **Mandag** | Kvalitet — tempo eller sub-terskelintervaller |
| **Tirsdag** | Styrke |
| **Onsdag** | Hvile |
| **Torsdag** | Kort kvalitet — bakkesprint eller drag. Under en time |
| **Fredag** | Langtur |
| **Lørdag** | Hvile |
| **Søndag** | Kort og rolig. Vokser 4 → 5 → 6 → 7 km gjennom høsten |

Søndagsøkta er restitusjon mellom fredagens langtur og mandagens kvalitet.
**Puls over 145 på søndagen betyr ned i fart.** Blir den en fjerde
kvalitetsøkt, er den verre enn ingen økt.

Ukesvolum ~34–45 km i byggeuker. Fra januar mot 55–60 km.

---

## Soner — revidert 14.09.26 av `fysiolog`. AVVENTER GODKJENNING FRA `hovedcoach`

> **Pace er GAP** (stigningsjustert), ikke rå klokkefart.
> På Knuts flate ruter er forskjellen **under 2 s/km** — GAP-korreksjonen har målt
> +0,6 til +1,8 s/km på tempoøktene og +1,8 s/km på «Brygga 16». Der viser altså
> klokka praktisk talt riktig.
> **I kupert terreng skal han styre etter puls og ignorere fartstallet.**
> Målt eksempel: siste 530 m av nedjoggen 14.09 hadde 21,7 hm/km og en
> GAP-korreksjon på **+51 s/km**. Der er klokkefarten ubrukelig.

| Sone | Puls | Pace (GAP) | Brukes til | Forankring |
|---|---|---|---|---|
| **I1 Restitusjon** (62–72 %) | 118–136 | *ikke fastsatt* — styr på puls | Nedjogg, dager som skal koste null | `[for tidlig]` |
| **I2 Rolig / langtur** (72–82 %) | 137–**155** | **6:30–8:00** | Langtur og alt rolig volum. Langtur: 7:20–8:00. Kortere rolige økter: 6:30–7:20 | `[foreløpig]` |
| **MP — mål** | ~145–155 | **7:05–7:15** | Maratonfart. **Uendret — settes etter halvmaraton i januar** | `hovedcoach` |
| **MP — arbeidsfart nå** | ~140–150 | **7:35–7:50** | Fart å bygge langturene rundt | `[foreløpig]` |
| **I3 Sub-terskel** (82–87 %) | 156–165 | **6:00–6:15** | Mandagens tempoøkter. Hovedjobben i basefasen | `[foreløpig]` |
| **I4 Terskel** (87–92 %) | 166–175 | **5:45–6:05** | Korte terskeldrag. Tallet er avledet, ikke målt direkte | `[for tidlig]` |
| **I5 VO2** (92–100 %) | 175–190 | *ikke fastsatt* | 5 × 1000 m fra 02.11. Styr på puls til vi har målt | `[for tidlig]` |

### Endringer mot forrige tabell
- **I3: 6:30–6:50 → 6:00–6:15.** Den gamle var **30–45 s/km for treg.**
  Målt to ganger på flate arbeidsblokker: 07.09 GAP 5:54,0 ved median puls 166
  (4,65 hm/km, korr +1,8 s/km) og 14.09 GAP 6:04,2 ved median puls 164
  (2,80 hm/km, korr +0,8 s/km). **Dette er den viktigste rettelsen.**
- **I2: 6:45–7:45 → 6:30–8:00.** Utvidet i begge ender, se under.
- **I4: 6:20–6:30 → 5:45–6:05.** Avledet av 01.08-parkrunens andre halvdel
  (puls 170,1 → GAP 5:46,2) og halen på tempoøktene (puls 169 → GAP 6:03).
  **Ingen dedikert I4-økt er kjørt.** Første blir 08.10.
- **I2-taket 156 → 155.** Fjerner overlappet mot I3, som begynner på 156.
- **I1 og I5 står uten tall.** Vi har ikke grunnlag, og et tall som ser sikkert
  ut er verre enn ingen.

### Hvorfor I2-båndet ble utvidet, ikke flyttet
To målinger ved puls ~145 ga GAP 7:34 og 6:45 — 49 s/km fra hverandre.
Forklaringen er **pulsetterslep**, ikke form: 6:45-punktet var
oppvarmingsrunde 2 den 07.09, der pulsen steg gjennom hele runden
(første tredjedel snitt 138,5 → siste tredjedel 146,6). Snittet på 145 er en
stigende kurve, ikke en likevekt, og runden er derfor **ikke et gyldig
I2-punkt**. Det samme gjelder alle korte oppvarmingsrunder.

> **Rettelse:** påstanden i `2026-09-07`- og `2026-09-10`-analysene om at
> «I1/I2-pacene er for konservative» bygget på nettopp slike oppvarmingsrunder.
> Den var ikke holdbar og er trukket.

De gyldige I2-punktene er økter med stabil puls over tid:

| Økt | Varighet | Puls | hm/km | GAP | Korr |
|---|---|---|---|---|---|
| «Brygga 16» 11.09 | 121,7 min | 145,6 | 6,80 | **7:34,4** | +1,8 s/km |
| Søndag 13.09, km 2–4 | 19,7 min | 153,3 | 12,90 | **6:26,8** | +7,3 s/km |

Derfor spenner båndet fra 6:30 (øvre I2, uthvilt) til 8:00 (nedre I2, sent i langtur).

### Terskelen
Anaerob terskel anslått til **puls 168–171**, terskelfart **6:10–6:25/km GAP**.
Hviler fortsatt på optisk pulsmåling — **brystbelte på én terskeløkt ville
avgjort det.** `[foreløpig]`

Tempoøktene ligger i **I3**, ikke I4 — det er riktig sted å bygge
maratonmotoren nå.

### Forbehold som gjelder hele tabellen
Knut løper **uten brystbelte** så vidt vi vet. Absolutt puls bærer **±3–5 slag**.
Pulsgrensene er likevel beholdt, fordi de er forankret i HRmax 190 som også er
målt optisk — feilen går delvis mot seg selv. Pacetallene er derimot GPS-målte
og upåvirket.

---

## Basefasen — uke 1–15

### Uke 1 · Reset, DELOAD · styrke B
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 31.08 | Man | deload | 5 km + 6 strides — gjennomført, snittpuls 146, pace 6:47 |
| 01.09 | Tir | styrke | Styrke B, leg-day |
| 03.09 | Tor | deload | 12 km rolig |
| 04.09 | Fre | deload | 4 km eller gåtur |

### Uke 2 · Bygg 1 — Terskel intro · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 07.09 | Man | kvalitet | **Tempo 20 min.** 2 km opp + 20 min puls 156–165 + 2 km ned. Kalibrering av terskel |
| 08.09 | Tir | styrke | Styrke A, no-legs |
| 10.09 | Tor | kvalitet | **6 km + 8 bakkesprint.** 4 km rolig + 8 × 15 sek bratt bakke i full fart, gå rolig ned, 2 km ned |
| 11.09 | Fre | langtur | **16 km.** Strengt I2. Beina er trøtte fra i går — med vilje |
| 13.09 | Søn | rolig | **4 km.** Puls 130–142. Skal føles for lett |

### Uke 3 · Bygg 2 — Tempo bygger · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 14.09 | Man | kvalitet | Tempo 22 min, puls 156–165 |
| 15.09 | Tir | styrke | Styrke A |
| 17.09 | Tor | kvalitet | 6 km + 10 bakkesprint |
| 18.09 | Fre | langtur | 16 km, ren I2 |
| 20.09 | Søn | rolig | 4 km |

### Uke 4 · Bygg 3 — Tempo utvidet · styrke A · TOPPUKE
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 21.09 | Man | kvalitet | Tempo 25 min, puls 156–165 |
| 22.09 | Tir | styrke | Styrke A, lettere |
| 24.09 | Tor | kvalitet | 6 km + 10 bakkesprint |
| 25.09 | Fre | langtur | 18 km. Test næring og væske |
| 27.09 | Søn | rolig | 4 km — siste uke på 4 |

### Uke 5 · DELOAD · styrke B
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 28.09 | Man | deload | 5 km + 6 strides |
| 29.09 | Tir | styrke | Styrke B, leg-day |
| 01.10 | Tor | deload | 5 km rolig |
| 02.10 | Fre | deload | 12 km rolig |
| 04.10 | Søn | deload | 3 km, eller dropp |

### Uke 6 · Bygg 4 — Intervaller inn · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 05.10 | Man | kvalitet | 2 × 12 min sub-terskel, 3 min jogg mellom |
| 06.10 | Tir | styrke | Styrke A |
| 08.10 | Tor | kvalitet | 4 × 2 min @ I4 (166–175), 2 min jogg |
| 09.10 | Fre | langtur | 16 km |
| 11.10 | Søn | rolig | 5 km |

### Uke 7 · Bygg 5 — Dobbel terskel · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 12.10 | Man | kvalitet | 2 × 15 min sub-terskel — 30 min totalt |
| 13.10 | Tir | styrke | Styrke A |
| 15.10 | Tor | kvalitet | 6 × 1 min hardt (puls 170–178), 2 min jogg |
| 16.10 | Fre | langtur | 18 km |
| 18.10 | Søn | rolig | 5 km |

### Uke 8 · Bygg 6 — Toppuke · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 19.10 | Man | kvalitet | 3 × 10 min sub-terskel, 2 min jogg |
| 20.10 | Tir | styrke | Styrke A, lettere |
| 22.10 | Tor | kvalitet | 8 × 1 min hardt |
| 23.10 | Fre | langtur | **20 km — høstens lengste.** Drifter pulsen over 155 sent: gå litt |
| 25.10 | Søn | rolig | 5 km |

### Uke 9 · DELOAD + sjekkpunkt · styrke B
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 26.10 | Man | deload | 6 km + 6 strides |
| 27.10 | Tir | styrke | **Styrke B, LETT** — ~60 % vekt, 2 × 8, dropp Bulgarians |
| 29.10 | Tor | deload | 5 km rolig |
| 30.10 | Fre | deload | **14 km · SJEKKPUNKT.** Lett = grønt lys. Tung = gjenta uke 8 |
| 01.11 | Søn | deload | 3 km, eller dropp |

### Uke 10 · Bygg 7 — VO2 intro · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 02.11 | Man | kvalitet | **5 × 1000 m** (puls 172–183), 2 min jogg. Første ekte VO2-økt |
| 03.11 | Tir | styrke | Styrke A |
| 05.11 | Tor | kvalitet | 4 × 2 min @ I4 |
| 06.11 | Fre | langtur | 18 km. Mørketid — hodelykt |
| 08.11 | Søn | rolig | 6 km |

### Uke 11 · Bygg 8 — Terskelvolum · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 09.11 | Man | kvalitet | 3 × 10 min sub-terskel |
| 10.11 | Tir | styrke | Styrke A |
| 12.11 | Tor | kvalitet | 8 × 1 min hardt |
| 13.11 | Fre | langtur | 20 km |
| 15.11 | Søn | rolig | 6 km |

### Uke 12 · Bygg 9 — Toppuke · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 16.11 | Man | kvalitet | **Tempo 30 min** sammenhengende — lengste drag i basefasen |
| 17.11 | Tir | styrke | Styrke A, lettere |
| 19.11 | Tor | kvalitet | 5 × 400 m raskt, 90 sek jogg |
| 20.11 | Fre | langtur | **20 km progressiv** — start I1, siste 3 km øvre I2 |
| 22.11 | Søn | rolig | 6 km |

### Uke 13 · DELOAD · styrke B
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 23.11 | Man | deload | 6 km + 6 strides |
| 24.11 | Tir | styrke | Styrke B, leg-day |
| 26.11 | Tor | deload | 5 km rolig |
| 27.11 | Fre | deload | 14 km rolig |
| 29.11 | Søn | deload | 3 km, eller dropp |

### Uke 14 · Base 10 — Vedlikehold · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 30.11 | Man | kvalitet | 2 × 15 min sub-terskel |
| 01.12 | Tir | styrke | Styrke A |
| 03.12 | Tor | kvalitet | 6 × 1 min hardt |
| 04.12 | Fre | langtur | 20 km. Brodder klare |
| 06.12 | Søn | rolig | 7 km |

### Uke 15 · Base avsluttes · styrke A
| Dato | Dag | Type | Økt |
|---|---|---|---|
| 07.12 | Man | kvalitet | Tempo 30 min — siste kvalitetsøkt i basefasen |
| 08.12 | Tir | styrke | Styrke A |
| 10.12 | Tor | kvalitet | 4 × 2 min @ I4 |
| 11.12 | Fre | langtur | **22 km — basefasen ferdig** |
| 13.12 | Søn | rolig | 7 km |

---

## Etter nyttår — rammer, ikke økt for økt

| Blokk | Når | Innhold | Langtur |
|---|---|---|---|
| **1 — Langturen vokser** | 14.12–24.01 · uke 16–21 | Terskel vedlikeholdes med én økt i uka. Økt 2 blir lengre og roligere. Første MP-arbeid mot slutten | 22 → 26 km · deload uke 17 og 20 |
| **2 — Maratonspesifikk** | 25.01–07.03 · uke 22–28 | Tyngste blokka. **MP-avslutninger** på langturene, siste 5–10 km i maratonfart på slitne bein. Næring øves på hver langtur | 28 → 34 km · topp 06.03 · deload uke 24 og 28 |
| **3 — Nedtrapping** | 08.03–03.04 · uke 29–31 | Volum ned ~40 %, intensiteten beholdes. Siste lange tur 20.03 | 28 → 18 km |

---

## Styrkeøktene

**A — no-legs**
Bench Press 4×5 @ 75 kg · Seated Cable Row 4×6 @ 90 kg · Lat Pulldown 3×8 @ 55 kg ·
Single-leg RDL 3×8 @ 20 kg · Standing Calf Raise 3×12 · Cable Crunch 3×10 @ 80 kg ·
Band Walks 3×12 per retning

**B — leg-day**
Belt Squat 4×10 @ 100 kg (maskinmaks) · Romanian Deadlift 3×8, 3 sek ned ·
Bulgarian Split Squat 3×10 @ 10 kg · Seated Calf Raise 3×15 @ 40 kg ·
Seated Chest Fly 3×12 @ 40 kg · Lying Leg Raise 3×20 · Clamshells + Side Plank 3×10 per side

> Merk: hovedcoach har 07.09 bestemt at **knedominert styrke skal progrederes,
> ikke bare vedlikeholdes** — se `coach/instrukser.md`. Vektene over er
> utgangspunktet, ikke taket.
