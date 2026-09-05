# Søvn- og belastningsanalyse — Garmin rådata 7. aug–3. sept 2026
Kilde: `coach/soevn/2026-08-07_2026-09-03-garmin-sleep.csv` (28 netter, eksport) + Strava 1.8–3.9.
Erstatter skjermbildeavlesningen (snitt 81 / uteligger 48) — den var omtrentlig.

## 1. Baseline (n=28)
| Mål | Snitt | SD | Median | Min–maks |
|---|---|---|---|---|
| Hvilepuls | 43,5 | 1,5 | 43 | 41–47 |
| HRV Status | 74,8 | 1,6 | 75 | 72–78 |
| Varighet | 7t 21 | 58 min | 7t 21 | 4t10–9t14 |
| Sleep Score | 84,9 | 9,5 | 85 | 50–100 |
| Body Battery | 55,6 | 7,6 | 54 | 35–75 |
| Respirasjon | 13,52 | 0,36 | — | 12,91–14,20 |

Uten 15.08 (gjennomvåket natt): snittvarighet 7t 28.
**19 av 28 netter under Garmins eget søvnbehov.** Snittunderskudd 25 min/natt.
8 netter under 7t, 5 under 6t30. Verstinger: 18.08 (−90), 02.09 (−87), 14.08 (−80),
25.08 og 26.08 (−72 hver).
27 av 28 netter «Aligned» (2 «Behind»). Døgnrytmen er ikke problemet — **lengden er det.**
HRV er påfallende stabil (SD 1,6). Det gjør små utslag meningsfulle: 72–73 er reelt lavt for ham.

## 2. Kryssjekk mot trening
Radens dato = morgenen man våkner, dvs. natten *inn mot* den datoen.

**Navy Race 8.–9. august.** Hvilepuls 47 begge netter — men den var 47 allerede natten
*før* løpet (7→8. aug), sammen med hudtemp +0,6° og respirasjon 13,99. Natten etter:
47, +0,6°, respirasjon 14,20 (høyest i hele perioden). Begge netter «Behind»/skjev.
Tolkning: dette er ikke bare løpsbelastning — det startet før startskuddet. Reise, varme,
nervøsitet eller begynnende infeksjon. Restituert på to netter: 10.08 8t50, RHR 43, BB 66.
Ingen ettervirkning å se etter 11. august.

**16,4 km sti 20.08 (RE 125).** Natten etter: RHR 45 (periodetopp), HRV 74. Normalisert
til 44/42 innen to netter. Normal og akseptabel respons.

**18 km 27.08 (RE 172, periodens hardeste økt).** Natten *etter*: RHR 44, hudtemp −0,1°,
HRV 73. Altså **lav akutt kostnad**. Det interessante ligger foran økta:
- 25.08: 6t18 (−72 mot behov)
- 26.08: 6t58 (−72 mot behov)
- 27.08 morgen: RHR 45 (periodetopp), HRV 73 (periodebunn), hudtemp +0,5°

Han gikk inn i periodens hardeste økt på to netter under 7 timer og med hvilepuls og HRV
på hver sin ytterkant. Formvurderingen viser at den økta fikk 7,2 % HR-drift (høyest av
tre langturer) og kadensfall 77,7 → 64,5 spm. Det er samme historie fortalt to ganger.
**Ikke at 18 km var for langt — at han var for dårlig uthvilt da han løp den.**

## 3. Endrer dette vurderingen? Ja — på to punkter.

**a) ACWR 1,08 står ikke lenger.** Med relative effort, vindu t.o.m. 3. sept:
- Akutt (28.08–03.09): 5 + 39 + 7 = **51** (+ én legday 01.09)
- Kronisk (07.08–03.09): 799 RE / 4 = **199,8/uke**
- **ACWR = 51 / 199,8 = 0,26**

På distanse: 9,9 km akutt mot 26,2 km/uke kronisk = 0,38. Uansett mål: **langt under 0,8.**
Aug 29, 30 og 2., 3. sept er helt tomme. Siste ordentlige løpeøkt var 5 km + strides 31.08.
Dette er ikke en planlagt nedtrapping som er beskrevet noe sted — det er et hull.

**b) Langturandelen er verre enn antatt, ikke bedre.**
| Uke | Løpsvolum | Langtur | Andel |
|---|---|---|---|
| 10.–16.08 | 28,6 km | 14,5 | **51 %** |
| 17.–23.08 | 27,5 km | 16,4 | **60 %** |
| 24.–30.08 | 27,9 km | 18,1 | **65 %** |

Tre uker på rad med stigende langtur (14,5 → 16,4 → 18,1; +1,9 og +1,7 km) uten
nedtrappingsuke, mens ukesvolumet står stille på ~28 km. Hele progresjonen er lagt i
én økt. Det er det klassiske mønsteret før beinhinne- og akillesplager.
Beslutningen i `instrukser.md` om å fryse langturen på 16–18 km til andelen er under
40 % er riktig — den må bare faktisk følges, og de manglende kilometerne må inn i
ukas *andre* økter.

**Status: GULT.** Ikke rødt — hvilepuls, HRV og hudtemperatur er rolige akkurat nå
(43/75/−0,2 siste natt), og han er godt uthvilt. Men gult av motsatt grunn enn sist:
belastningen har falt for brått, og strukturen i uka er skjev.

**Tiltak:**
1. Ikke gjenoppta med langtur. Neste uke: 3 løpeøkter på 5–7 km, samlet 18–20 km, ingen over 8 km.
2. Uken etter: legg til 4. økt (søndag 4 km rolig, jf. instrukser) og løft langturen til
   maks 12 km. Da er andelen ~40 % — første gang under 50 % siden 9. august.
3. Bygg ukesvolumet mot 35 km før langturen får gå over 14 km igjen. Ikke motsatt rekkefølge.
4. Sengetid er en treningsvariabel: siste økt før langtur skal ligge minst 48 t unna,
   og de to nettene før skal begge over 7 t.

## 4. Flaggterskler til `hovedcoach`
Baselinen er smal. Bruk disse, ikke skjønn.

| Signal | Terskel | Handling |
|---|---|---|
| Hvilepuls | **≥ 46** én natt | Dagens økt til rolig I1, maks 45 min. Meld til `belastning-restitusjon`. |
| Hvilepuls | **≥ 45 to netter på rad** | Ingen hard økt / langtur de neste 48 t. Flytt, ikke kutt. |
| HRV Status | **≤ 72** én natt | Ikke hard økt samme dag. Rolig eller fri. |
| HRV Status | **≤ 73 to netter på rad** | Deload resten av uka: halver intervallvolum, langtur maks 60 % av planlagt. |
| Varighet | **< 6t 30** én natt | Planlagt hard økt flyttes én dag. Rolig økt går som normalt. |
| Varighet | **< 7t to netter på rad før hard økt/langtur** | Økta flyttes. Ingen unntak — dette er nøyaktig 25.–27. august. |
| Body Battery ved oppvåkning | **< 45** | Rolig dag. Under 40: fri. |
| Hudtemp | **≥ +0,5°** sammen med RHR ≥ 45 | Mistenk infeksjon eller varmestress. Ingen økt over I2 før begge er tilbake. |
| Respirasjon | **≥ 14,0** | Alene: bare notér. Sammen med RHR ≥ 45: som infeksjonsflagget over. |
| Sleep Score | **< 60** | Fri fra løping. |
| Alignment | «Not Aligned» | Kun kontekst, ikke eget flagg (n=1 i 28 netter). |

Kombinasjonsregelen som veier tyngst: **to netter under 7 t + hvilepuls ≥ 45 + HRV ≤ 73
samtidig = ingen langtur, uansett hva planen sier.** Den kombinasjonen inntraff én gang
i perioden, 27. august, og økta ble dyrere enn nødvendig.

Grensene revideres ved neste CSV-eksport (ca. 1. oktober). Baseline vil trolig flytte seg
nedover når volumet bygges opp igjen — 43,5 er ikke en fast verdi.

## 5. Hva mangler
**RPE og smerte. Det er alt.** Søvn, hvilepuls, HRV, hudtemperatur og treningsdata er nå
komplette. Uten RPE kan jeg ikke skille «tung dag» fra «for hard økt», og uten smertelogg
oppdager jeg beinhinne- eller akillesplager først når de er synlige i kadens og gange —
altså for sent. Logg-mappa `coach/logg/` er tom. `hovedcoach` bør spørre om begge to
hver kveld, kort: RPE 1–10 for dagens økt, og smerte ja/nei + hvor.

En ting til, som ikke haster: kroppsvekt mangler i profilen. Den påvirker hvor strengt
volumøkningsgrensene skal settes.
