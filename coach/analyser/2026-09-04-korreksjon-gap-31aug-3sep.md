# Korreksjon: ujustert tempo-sammenligning 31.08 mot 03.09

Dato: 4. september 2026. Erstatter påstanden «stølheten kostet 22 s/km ved samme puls».

## Metode
Fullkurs-streams (`resolution` utelatt / 1000 punkter, ~2 s per punkt) for
19976884914, 20020851701, 20034661905. GAP per delstrekning med Minettis
energikostnadsligning
`Cr(i) = 155,4i^5 − 30,4i^4 − 43,3i^3 + 46,3i^2 + 19,5i + 3,6` (J/kg/m),
faktor `Cr(i)/Cr(0)`, gradient klippet til ±0,45. Segmenter under 0,6 m/s
forkastet. Puls tidsvektet.

Barometerstøy: rå høydestrøm gir 64 hm på 31.08 (Strava: 33) og 235 hm på
04.09 (Strava: 188). Derfor rapporteres GAP for glidende snitt over N
høydepunkter, N = 1, 3, 5, 9, 15. Konklusjonen er stabil over hele spennet.

## 31.08 (19976884914) mot 03.09 (20020851701)

| N (glatting) | rå-differanse | GAP-differanse | terreng forklarer |
|---|---|---|---|
| 1 (rå) | 21,9 s/km | 16,6 s/km | 5,2 s/km (24 %) |
| 3 | 21,9 | 18,1 | 3,7 (17 %) |
| 5 | 21,9 | 18,1 | 3,7 (17 %) |
| 9 | 21,9 | 17,8 | 4,1 (19 %) |
| 15 | 21,9 | 17,4 | 4,5 (20 %) |

**Terrenget forklarer 4–5 s/km av 22. Resten, 17–18 s/km, er ikke terreng.**

Ved N = 5: 31.08 rå 6:48/km, GAP 6:45/km, puls 146,0, EF_GAP 0,01689.
03.09 rå 7:10/km, GAP 7:04/km, puls 144,4, EF_GAP 0,01636. EF −3,1 %.

Pulsen var ikke lik: 146,0 mot 144,4 tidsvektet. 03.09 var altså 22 s/km
tregere på 1,6 slag lavere puls.

Høydemeter per km fra rå strøm: 12,7 mot 15,0 (glattet N=5: 10,1 mot 12,5).
Ikke «nesten dobbelt så mye» — Strava-tallene 6,6 og 11,0 er ulikt avrundet.

### Den viktigste forskjellen er drift, ikke tempo
- 31.08: 1. halvdel GAP 6:50/km @ 142, 2. halvdel 6:41/km @ 150. **Pa:HR 3,1 %**
- 03.09: 1. halvdel GAP 6:46/km @ 141, 2. halvdel 7:22/km @ 148. **Pa:HR 12,5 %**

03.09 startet raskere enn 31.08 og falt fra hverandre. Det er signaturen på
en dårlig dag, ikke på et kupert underlag.

### Begge øktene er for korte for EF
34 og 33 minutter bevegelsestid. Egen regel: minimum 40 minutter. Ingen av dem
skulle vært brukt som EF-punkt i det hele tatt.

## 04.09 (20034661905) — gjelder samme innvending?

Nei. Terrenget gjør bildet verre, ikke bedre.

| | rå | GAP (N=5) | puls | kadens |
|---|---|---|---|---|
| hele økta | 8:44/km | 8:32/km | 135,7 | 71,8 |
| kun løping (61 min, 8,24 km) | 7:25/km | 7:36/km | 139,3 | 78,1 |
| kun gange (46 min, 4,08 km) | 11:23/km | 9:53/km | 130,5 | 57,7 |

Gange: 43 % av tiden, 25 sammenhengende bolker over 30 s, lengste 306 s.
Kadens 69,9 er et blandingstall, ikke en fordeling. Løpekadensen var 78,1 spm
og falt **ikke**: 78,2 første halvdel, 78,0 andre.

Delstrekningene:
- Første km: 998 m, +12/−10 m (12 hm/km), 6:51/km, **GAP 6:43/km**, puls 143,
  og 36 s gange ligger allerede inne.
- Siste 1,2 km: 1221 m, +9/−19 m — **netto nedover**, 7 hm/km. 7:24/km,
  **GAP 7:40/km**, puls 144, 70 s gange.

Partiene var altså ikke kuperte. Slutten gikk nedover. Etter stigningsjustering
er fallet 57 s/km, ikke 35. Terreng redder ikke den observasjonen.

Pa:HR på løpepartiene alene: 6,8 % (hele økta: 5,3 %).

## Konsekvens for EF-tabellen i 2026-09-03-formvurdering-knut.md

Tabellen bruker `(distanse + 7,5 × høydemeter) / bevegelsestid`. Den modellen
legger bare til for stigning, gir ingen fradrag for fall, og bruker Stravas
avrundede hm. Testet mot Minetti:

| økt | GAP 7,5×hm | GAP Minetti | avvik |
|---|---|---|---|
| 31.08 (6,6 hm/km Strava) | 6:36/km | 6:45/km | 9 s/km |
| 03.09 (11,0) | 6:37/km | 7:04/km | 27 s/km |
| 04.09 (15,3) | 7:50/km | 8:32/km | 42 s/km |
| 27.08 (9,9) | 7:28/km | — | — |

Feilen vokser med hm/km. Med 7,5×hm ville 03.09 kommet ut som **raskere** enn
31.08 (6:37 mot 6:36 — i praksis likt) og med høyere EF. Modellen kan altså
snu fortegnet på en sammenligning.

**EF-kolonnen i tabellen er systematisk oppblåst på de kuperte øktene og må
regnes om med Minetti før noen trend leses ut av den.** Verdiene 14,32 → 16,50
→ 16,01 er ikke sammenlignbare før hm/km er kjent og korrigert per rad.
Konfidens på «+12 % juni → august»: **[for tidlig]** inntil omregning.

## Hva jeg tar med videre
- Retningen 31.08 → 03.09 er reell, men den er én dag og to for korte økter.
- Driftøkningen 3,1 % → 12,5 % på tre dager er det som fortjener oppmerksomhet.
- HRmax 187 bekreftet. Maksverdier i disse tre: 159, 154, 155. Alle øktene
  ligger i OLT I2 (135–153) eller lavere. Riktig sone.
