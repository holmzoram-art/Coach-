# Hvor er det flatt? — kartlegging av Knuts egne ruter

Spørsmål fra Knut 10.09: «hvor skal jeg løpe her i området som er så flat?»
Svaret er hentet fra hans egen Strava-historikk, ikke fra kart.

Metode: alle løp 01.04–10.09.2026 rangert på Stravas høydemeter, deretter er de
fem beste kandidatene hentet med **altitude + location i full oppløsning** og
regnet om med min egen metode (glattet høyde ±8 s, integrert stigning).
Min metode gir gjennomgående **høyere** hm/km enn Stravas eget tall — tallene
under er mine, og skal sammenlignes med mine.

## Rangering — målt, ikke antatt

| Rute | Dato | Distanse | **hm/km** | Høydespenn | Geometri |
|---|---|---|---|---|---|
| **400 m bane, Færder** | 07.06 | 7,69 km | **0,11** | 5,6 m | 19 runder à 400 m |
| **~740 m runde, Tønsberg** | 14.08 | 7,27 km | **4,31** | 9,3 m | miks av 400 m og 740 m runder |
| Tempoøktas midtparti | 07.09 | 3,38 km | **4,65** | 2,7 m | rett strekk |
| **~750 m runde, Tønsberg** | 01.06 | 7,53 km | **5,00** | 7,9 m | 8 runder à 752 m |
| Parkrun-traseen | 01.08 | 5,13 km | **8,56** | — | — |
| Tempoøkta i sin helhet | 07.09 | 7,65 km | **7,93** | 11,6 m | ut 1047 m nordover og tilbake |
| Oppvarming dammene | 10.09 | 3,97 km | **7,97** | — | — |
| Langtur 18 km | 27.08 | 18,14 km | **11,24** | 77,2 m | ekte rundtur, 3,1 km fra start |
| Retur dammene | 10.09 | 2,12 km | **12,72** | — | — |
| Langtur 12 km | 04.09 | 12,32 km | **15,3** | — | — |

## Hva dataene faktisk viser

**Han har flate ruter. Men alle er runder, ikke strekninger.**

- **400 m bane ved Færder** (start 59,21667 / 10,45161). Rundelengdene måler
  391, 400, 383, 401, 400, 399, 400, 400, 401, 399, 403, 399, 411, 401, 399,
  401, 400, 400 m. Det er en oppmerket 400-metersbane. **0,11 hm/km** — så flatt
  det går an å komme. Han løp 19 runder der 07.06.
- **Tønsberg, Greveskogen-området** (start 59,2836 / 10,4110 og 59,28048 / 10,41226,
  350 m fra hverandre). Her finnes **to** løyper: en 400-metersbane og en runde på
  **~750–790 m**. Rundelengdene 01.06: 756, 757, 757, 749, 750, 750, 748, 752 m —
  helt konsistent. Dette er samme runde som Strava-segmentet
  **«TFIK Terskelrunde 790meter»**, som dukket opp i mandagens økt.
- **Alt som er en ekte tur ut i terrenget er kupert.** 18-kilometeren 27.08 strekker
  seg 3,1 km fra start og har 11,24 hm/km. 12-kilometeren 04.09 har 15,3.

**Konklusjonen er entydig: det finnes ingen flat 16 km-strekning i materialet hans.
Vil han løpe 16 km under 5 hm/km, må det bli runder.**

## Svaret på det viktigste spørsmålet: er 5 hm/km absolutt?

**Nei — ikke for en EF-serie.**

De 5 hm/km ble satt for **kalibreringstesten** 07.09, der tallet skulle stå alene
og GAP-korreksjonen måtte være neglisjerbar. Det var riktig der.

For en **EF-trend** er kravet et annet. EF måler *endring* over tid. Da gjelder:

1. **Samme rute hver gang.** Løper han samme løype, blir enhver feil i GAP-modellen
   en **konstant** som faller ut av differansen mellom målingene.
2. **Ingen gåpauser.** Blandes løping og gange, er snittfarten ikke fart.
3. **Sammenlignbare forhold** — årstid, føre, tid på døgnet.

**En rute på 8 hm/km løpt likt hver tredje uke gir en bedre EF-serie enn en helt
flat rute løpt én gang.** Konsistens slår flathet.

Grensen går der GAP-modellen begynner å bli upålitelig og der pacingen blir
ujevn av terrenget — erfaringsmessig over 10–12 hm/km. Under det er en fast rute
fullt brukbar.

## Anbefaling — én fast EF-rute

**«Terskelrunda», ~790 m, Greveskogen/Tønsberg.**
Start 59,2836 / 10,4110. 4,3–5,0 hm/km målt over to separate økter.

Hvorfor akkurat den:
- **Den er flat nok** til at GAP-korreksjonen blir liten, i praksis samme nivå som
  mandagens tempoøkt (+1,8 s/km ved 4,65 hm/km).
- **Han har allerede to økter på den** — 01.06 og 14.08. Serien starter ikke på null.
- **Den skalerer med planen.** Langturene går 16 → 16 → 18 → 20 → 22 km utover
  høsten. Samme runde, flere runder. Ingen ny rute å kalibrere hver gang.
- **Den har en Strava-segmentmatch**, så jeg kan kjenne den igjen automatisk i
  framtidige økter uten å spørre.

16 km = **ca. 20 runder**.

**Alternativ for maksimal presisjon:** 400 m-banen ved Færder, 0,11 hm/km.
16 km = 40 runder. Måleteknisk perfekt, mentalt tungt. Brukes hvis vi en gang
trenger et helt rent referansepunkt.

## Hvis 20 runder er uaktuelt

Da gjelder dette, og det er en fullgod løsning: **velg én ekte rute, gi den et navn,
og bruk den på hver eneste langtur.** Selv 27.08-runden på 11,24 hm/km fungerer som
EF-serie hvis den er den samme hver gang. Da måler jeg utviklingen hans, ikke
terrenget — forutsatt at han sier fra når han bytter.

Det som **ikke** fungerer er å løpe en ny rute hver gang. Da måler jeg
ruteforskjeller, og EF-serien blir støy. Det er nøyaktig feilen fra 03.09.

## Til fredagens økt

Førstevalg: **Terskelrunda, ~20 runder, 16 km.**
Brystbelte. Solo. Sammenhengende løping. Puls 140–150.

Dette blir seriens **nullpunkt**. Alt som kommer senere måles mot det.
