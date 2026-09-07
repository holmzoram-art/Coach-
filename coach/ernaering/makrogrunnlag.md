# Tallgrunnlag for matplan-artifacten

Skrevet 07.09.2026 av `ernaering`. Datagrunnlag for grensesnittet som skal
bygges. Menyene og prinsippene står i `coach/ernaering/matplan.md` — denne fila
inneholder bare tallene.

---

## 0. Les dette først — presisjonsgrensen, og hvor bestillingen bryter den

Alle tall i denne fila er **estimater med ±15–20 % usikkerhet på måltidsnivå**
og ±10 % på dagsnivå. De er utledet fra porsjoner i husholdningsmål, ikke fra
veiing. Det er godt nok til å styre etter — og ikke godt nok til å telle med.

**Det betyr fem konkrete designkrav. Brytes de, blir artifacten en
kaloriteller som later som den er nøyaktigere enn grunnlaget:**

1. **Ingen vekt, ingen strekkodeskanner, ingen «legg til egen matvare» i gram.**
   Brukeren velger retter fra faste menyer med faste porsjoner. Punktum.
   Dette er det viktigste punktet, og det er det som først kommer til å bli
   foreslått fjernet.
2. **Rund av: kalorier til nærmeste 25, makroer til nærmeste 5 g.** Aldri
   desimaler. «2287 kcal» er en løgn om presisjon. «2300» er et estimat.
3. **Ingen løpende dagssum som teller opp utover dagen.** Den gjør måltid nr. 4
   til en forhandling med et tall. Vis dagssummen når dagen er ferdig, og legg
   hovedvekten på **ukesummen**, som er det som faktisk styrer vekta.
4. **Ingen prosentring som fylles opp.** Den inviterer til å jakte 100 %, og
   100 % av et ±15 %-estimat er ikke en ting.
5. **Lunsjen logges ikke, den velges** — se § 5.

Bryter spesifikasjonen med noe av dette, si fra, så tar vi det.
Det ene tallet som **skal** være presist er karbo per time under løping. Det
teller seg selv, og det hører hjemme i `mage.md`, ikke her.

---

## 1. Makromål per dag og dagstype

### Forutsetninger — **REVIDERT 07.09.2026**

| | |
|---|---|
| Vekt | 119 kg · 195 cm · 38 år |
| Hvilestoffskifte | ~2 225 kcal |
| Forbruk uten trening | ~2 950 kcal/dag |
| **Løping** | **~105 kcal/km — korrigert ned fra 120** |
| Styrkeøkt | ~320 kcal |
| Vedlikeholdsbehov | ~2 950 kcal/dag + 105 per km + 320 på styrkedag |
| Underskuddsmål | 2 700 kcal/uke ≈ **0,35 kg/uke** |

**Hvorfor 105 og ikke 120.** Sjekket mot faktiske Strava-tall: 18,1 km ga
2 026 kcal, 16,4 km ga 1 819 kcal, 12,3 km ga 1 336 kcal. Det er
**110–112 kcal/km brutto**, og trekker vi fra hvileforbruket i samme tidsrom
lander netto på ~105. Den gamle forutsetningen overvurderte
langturdagen med rundt 250 kcal.

### 1.0 Grunnregel — målene er volumstyrte, ikke faste

Faste dagstall holder ikke når ukesvolumet svinger mellom 17 og 40 km.
**Målet for en dag = basis for dagstypen + 105 kcal per km faktisk løpt.**

| Dag | Basis, vedlikehold | Basis, underskudd | Tillegg |
|---|---|---|---|
| **Man** kvalitet | 2 950 | 2 750 | + 105 × km |
| **Tir** styrke | 3 270 | 2 875 | fast |
| **Ons** hvile | 2 950 | 2 250 | — |
| **Tor** intervaller | 2 950 | 2 750 | + 105 × km |
| **Fre** langtur | 2 950 | 2 950 | + 105 × km |
| **Lør** hvile | 2 950 | 2 250 | — |
| **Søn** rolig | 2 950 | 2 450 | + 105 × km |

**Tre regler til:**
1. **Blir en planlagt løpeøkt ikke gjennomført, blir dagen en hviledag.**
   Bruk hviledagsbasis (2 250 i underskudd), ikke kvalitetsdagsbasis.
2. **Fredag har tak på 4 500 kcal.** Overskytende legges på torsdag som
   karbolading. Ingen spiser 4 900 kcal på en fredag med langtur.
3. **Fredag får aldri underskuddsfradrag**, uansett hva vekta gjør.

### 1.1 Kontrollregning ved planlagt volum (37 km: man 8 · tor 8 · fre 16 · søn 5)

| Dag | kcal | Protein | Karbo | Fett |
|---|---|---|---|---|
| Man | 3 590 | 220 | 460 | 105 |
| Tir | 2 875 | 220 | 300 | 90 |
| Ons | 2 250 | 220 | 170 | **75** |
| Tor | 3 720 | 220 | 480 | 105 |
| Fre | 4 500 | 220 | 650 | 113 |
| Lør | 2 250 | 220 | 170 | **75** |
| Søn | 2 975 | 220 | 310 | 90 |
| **Uke** | **22 160** | 1 540 | 2 540 | 653 |

Stemmer med underskuddsmålet på 22 100 kcal/uke. **Fettet på hviledager er
hevet fra 70 til 75 g** — se § 7.1.

### 1.2 Hva som faktisk gjelder nå — ACWR 0,51, volum 16,8 km

Siste uke (Strava): torsdag 4,5 km, fredag 12,3 km. Ingen mandagsøkt.

| Dag | Faktisk | kcal-mål nå | mot § 1.1 |
|---|---|---|---|
| Man | ingen økt | **2 250** | −1 340 |
| Tir | styrke | 2 875 | 0 |
| Ons | hvile | 2 250 | 0 |
| Tor | 4,5 km | **3 225** | −495 |
| Fre | 12,3 km | **4 240** | −260 |
| Lør | hvile | 2 250 | 0 |
| Søn | 4 km | **2 870** | −105 |
| **Uke** | 20,8 km | **19 960** | **−2 200** |

**Svar på spørsmålet: nei, tallene i den gamle § 1.2 gjelder ikke nå.**
De var 22 100 kcal/uke. Ved dagens volum er vedlikehold ~23 150 kcal/uke, og
riktig inntak for 0,35 kg/uke er **~19 960**, altså 2 200 kcal lavere per uke
enn den faste tabellen sa. Hadde han spist etter den gamle tabellen ville han
ligget nær vedlikehold og lurt på hvorfor vekta sto stille — nøyaktig samme
feil som juli.

**Dette er grunnen til at artifacten må regne per km, ikke slå opp i en
tabell.** Den skal hente distansen fra Strava og regne målet samme kveld.

---

## 2. Hardt krav mot retningsgivende

Dette avgjør hvordan avvik skal vises. Tre nivåer, tre visuelle uttrykk.

### Nivå 1 — GULV. Skal aldri brytes. Vises tydelig.

| Krav | Verdi | Hvorfor |
|---|---|---|
| **Protein** | **≥ 220 g, hver eneste dag** | Avgjør om vekttapet er fett eller muskel. Knut har akseptert noe tap av magert vev — nettopp derfor er dette gulvet skjerpet, ikke løsnet. Gjelder også hviledager. |
| **Fett** | **≥ 70 g, og ≥ 75 g på hviledager i underskudd** | Hormoner og fettløselige vitaminer. Ryker systematisk på ons/lør — se § 7.1. |
| **Karbo man/tor/fre** | **≥ 400 g (man/tor), ≥ 550 g (fre)** | Under dette er øktkvaliteten og magetreningen borte. Dette er de tre dagene karboen er et gulv og ikke et tak. |

Protein har **ingen øvre grense** og skal aldri flagges oppover.

### Nivå 2 — TAK. Skal ikke overskrides mye. Vises dempet.

| Krav | Verdi |
|---|---|
| **Karbo ons/lør (underskudd)** | ~170 g. Her er karbo et tak, ikke et gulv |
| **Fett alle dager** | ~150 g |

### Nivå 3 — RETNINGSGIVENDE. Vises som tall uten farge.

- **Kalorier per dag.** Dette er det minst presise tallet i hele systemet og
  skal ha den svakeste visuelle vekten. Aldri rødt på en enkeltdag.
- **Karbo på tir/ons/lør/søn.**
- **Alle måltidsnivåtall.**

### Visuelt uttrykk — konkret

| | Uttrykk |
|---|---|
| Brutt gulv (protein/fett/karbo hard dag) | Tydelig markering + én setning om hva som fikser det |
| Overskredet tak | Dempet grå note, ingen farge |
| Kalorier utenfor bånd | Grå tekst på **ukesnittet**, aldri på dagen |
| Alt innenfor | **Ingenting.** Ikke et grønt hak. Stillhet er tilbakemeldingen |

Den siste raden er ikke pynt. En skjerm som alltid sier noe, blir en skjerm
han slutter å lese.

---

## 3. Hvor stort avvik som faktisk betyr noe

**Grunnregel: én dag betyr ingenting. Uka betyr alt.**

### Kalorier

| Avvik fra dagsmål | Reaksjon |
|---|---|
| ± 10 % (± ca. 300 kcal) | **Støy. Vis ingenting.** Dette er innenfor målefeilen i grunnlaget |
| 10–20 % | Vis tallet grått. Ingen melding |
| > 20 % én dag | Fortsatt ingen melding. Enkeltdager svinger |
| **Ukesum > 5 % under mål, to uker på rad** | **Dette betyr noe.** Han spiser for lite — vanligste feilen i denne fasen |
| **Ukesum > 8 % over mål, to uker på rad** | Betyr noe. Underskuddet uteblir |

### Protein

| | Reaksjon |
|---|---|
| ≥ 220 g | Ingenting |
| 200–219 g | Dempet note: «litt under» |
| **< 200 g** | **Markeres.** Med forslag: «et beger kesam eller 2 egg fikser dette» |
| **< 180 g to dager på rad** | **Markeres tydelig.** Dette er det ene som skal bryte gjennom støyen |

### Karbo

| | Reaksjon |
|---|---|
| Man/tor/fre, inntil 15 % under mål | Ingenting |
| **Man/tor/fre, > 20 % under** | Markeres — dette går ut over økta |
| Ons/lør, inntil 30 g over tak | Ingenting |
| Ons/lør, > 60 g over tak gjentatte ganger | Dempet note |
| Alle andre dager | Vis tallet, ingen vurdering |

### Fett

Flagges **kun** under 60 g eller over 160 g. Ellers vises tallet uten farge.
Fett er restposten og skal behandles som det.

### Det som ikke skal måles i det hele tatt
Enkeltmåltiders makrofordeling. Prosent karbo/protein/fett. «Score» på en dag.
Streaks. Ingen av dem har mening på dette datagrunnlaget.

---

## 4. Næringsinnhold per rett

Alle tall er per porsjon som beskrevet, avrundet. Rekkefølge: **kcal · P · K · F** (gram).

### 4.1 Frokost (§ 0b i matplanen)

| # | Rett | Porsjon | kcal | P | K | F |
|---|---|---|---|---|---|---|
| F1 | Eggerøre + grovbrød | 3 egg, skvett melk, 2 skiver, tynt smør | 450 | 30 | 35 | 22 |
| F2 | Stekt egg + grovbrød | 3 egg stekt, 2 skiver, tynt smør | 450 | 30 | 30 | 22 |
| F3 | Proteinyoghurt + havregryn + bær | 1 stort beger, 1 dl havregryn, 1 neve bær | 400 | 40 | 45 | 5 |
| F4 | Skyr/kesam + havregryn + bær + nøtter | 1 beger, 1 dl havregryn, bær, 1 ss nøtter | 475 | 45 | 40 | 12 |
| F5 | Havregrøt på melk + protein | 1 dl havregryn, 3 dl melk, 1 skje protein, bær | 400 | 35 | 45 | 8 |
| F6 | Grovbrød med proteinpålegg | 3 skiver + makrell i tomat / skinke / kaviar | 400 | 20 | 45 | 10 |

**Tillegg som kan hukes på:**

| Tillegg | Porsjon | kcal | P | K | F |
|---|---|---|---|---|---|
| Halv avokado | 1/2 stk | 120 | 2 | 2 | 11 |
| Ekstra skive grovbrød | 1 skive | 90 | 4 | 15 | 1 |
| Ekstra egg | 1 stk | 70 | 6 | 0 | 5 |
| Glass melk | 2 dl lett | 90 | 7 | 10 | 3 |

**Hviledagsversjon:** trekk fra én skive brød (−90 · −4 · −15 · −1) eller halver
havregrynene (−65 · −2 · −10 · −1).

**Merk F6:** eneste frokost under 25 g protein. Artifacten skal foreslå
«+ 1 egg» eller «+ glass melk» når den velges. Ikke blokkere den — foreslå.

### 4.2 Kl. 14-måltidet

| # | Rett | Porsjon | kcal | P | K | F |
|---|---|---|---|---|---|---|
| M1 | Kesam/cottage cheese + frukt | 4 dl beger + 1 frukt/neve bær | 330 | 45 | 30 | 2 |
| M2 | Proteinyoghurt + bær | 1 stort beger + 1 neve bær | 260 | 35 | 25 | 2 |
| M3 | 2 kokte egg + frukt | 2 egg + 1 frukt | 220 | 12 | 20 | 10 |
| M4 | YT proteinsjokolademelk + frukt | 0,5 l + 1 frukt | 410 | 30 | 70 | 2 |
| M5 | Knekkebrød + makrell/kylling + gulrot | 3 knekkebrød, 1/2 boks, 1 gulrot | 250 | 12 | 30 | 8 |
| M6 | Proteinbar + frukt | 1 bar + 1 frukt | 280 | 20 | 40 | 6 |

**Regler artifacten skal håndheve:**
- **M4 er kun tilgjengelig på treningsdager** (man, tir, tor, fre, søn). På
  hviledag er det 50 g rask karbo uten mottaker — grå den ut med begrunnelsen.
- M3 og M5 er under 15 g protein. Foreslå tillegg, ikke blokkér.

### 4.3 Middag

To porsjonsstørrelser per ramme: **karbodag** (man/tor/fre) og **hviledag**
(ons/lør). Tirsdag og søndag: bruk karbodag minus én neve karbo (−170 · −4 · −37 · 0).

| # | Ramme | | kcal | P | K | F |
|---|---|---|---|---|---|---|
| R1 | Panne/ovn: kylling/svin + poteter + rotgrønnsaker | Karbodag | 775 | 55 | 90 | 17 |
| | | Hviledag | 600 | 50 | 55 | 17 |
| R2 | Wok: biff/kylling/reker + grønnsaksblanding + ris | Karbodag | 875 | 55 | 90 | 28 |
| | | Hviledag | 675 | 55 | 65 | 27 |
| R3 | Gryte/suppe: kjøttdeig eller linser + mye grønt | Karbodag (m/brød el. poteter) | 960 | 70 | 100 | 26 |
| | | Hviledag | 700 | 60 | 55 | 25 |
| R4 | Fet fisk + poteter + grønnsaker | Karbodag | 850 | 50 | 90 | 28 |
| | | Hviledag | 675 | 50 | 55 | 28 |
| R5 | Pasta/ris med kjøttsaus + stor salat | Karbodag | 925 | 65 | 110 | 27 |
| | | *Ikke hviledagsvariant* | — | — | — | — |
| R6 | Taco/wraps: magert kjøttdeig, bønner, mye grønt | Karbodag | 800 | 60 | 80 | 22 |
| | | Hviledag (uten tortilla, som bolle) | 600 | 55 | 45 | 20 |

Porsjonsdefinisjon i husholdningsmål: **protein = håndflate + halv**
(ca. en tydelig porsjon kjøtt/fisk), **grønnsaker = dobbel porsjon, minst to
never**, **karbo karbodag = 1,5–2 never**, **karbo hviledag = under én neve**.

### 4.4 Kl. 21-måltidet

| # | Rett | Porsjon | kcal | P | K | F |
|---|---|---|---|---|---|---|
| K1 | Skyr/kesam + bær | 1 beger + neve bær | 250 | 35 | 20 | 2 |
| K1+ | Samme + granola | + 1 dl oppmålt granola | 430 | 40 | 45 | 6 |
| K2 | Cottage cheese + bær/ananas | 4 dl beger + 1 neve frukt | 380 | 50 | 25 | 8 |
| K3 | Proteinyoghurt + nøtter | 1 beger + 1 ss nøtter | 325 | 40 | 20 | 10 |
| K4 | 2 kokte egg + grønnsaksstaver | 2 egg + gulrot/agurk | 170 | 15 | 5 | 10 |
| K5 | Kvarg / proteinpudding | 1 beger | 200 | 25 | 10 | 3 |
| K6 | Varm kakao på skummet melk + liten skyr | 4 dl + 150 g | 235 | 30 | 25 | 2 |

**K1+ er kun tilgjengelig på treningsdager**, og bare til 28.09. Fra
underskuddsfasen grås granolatillegget ut på alle dager.

### 4.5 Rundt økta — faste poster

| Post | Porsjon | kcal | P | K | F | Når |
|---|---|---|---|---|---|---|
| Før økt: banan | 1 stk | 105 | 1 | 25 | 0 | Alle øktdager |
| Før økt: 2 skiver loff + syltetøy | 2 skiver | 250 | 6 | 50 | 2 | Man/tor/fre |
| Fredag 13:30: 3 skiver loff + syltetøy | 3 skiver | 375 | 9 | 75 | 3 | Kun fredag |
| Etter økt: YT Protein restitusjonsdrikk | 1 flaske | 350 | 30 | 50 | 3 | Løpedager |
| Etter økt: sjokolademelk | 5 dl | 330 | 17 | 50 | 8 | Alternativ |
| Etter styrke: melk | 5 dl lett | 225 | 17 | 24 | 8 | Tirsdag |
| Under langtur: seigmenn | Per 25 g | 90 | 0 | 22 | 0 | **Se `mage.md`** |

**Under langtur er `mage.md` overordnet.** Artifacten skal lenke dit og
**ikke** foreslå mengder selv. Der er tallet g karbo per time, og det er det
eneste stedet vi regner presist.

---

## 5. Kantinelunsjen — min vurdering

**Den skal være et forhåndsvalg han trykker på, ikke en post han fyller inn.**

Begrunnelse: han vet ikke innholdet i kantinemat, og han skal ikke måtte vite
det. Å be ham anslå innholdet i en kantinelunsj er akkurat den falske
presisjonen vi prøver å unngå — anslaget hans blir dårligere enn mitt estimat,
og han kommer til å slutte å logge etter to uker. Samtidig er lunsjen faktisk
**forutsigbar**, fordi tallerkenregelen bestemmer sammensetningen selv når
retten varierer.

Fire forhåndsvalg. Ett trykk, ingen inntasting:

| Valg | Beskrivelse | kcal | P | K | F | Standard på |
|---|---|---|---|---|---|---|
| **Full karbo** | Halv salat · kvart protein · **full** karboporsjon | 850 | 50 | 95 | 25 | Man, tor, fre |
| **Normal** | Halv salat · kvart protein · normal karbo | 700 | 50 | 65 | 22 | Tir, søn |
| **Halv karbo** | Halv salat · kvart protein · **halv** karbo | 550 | 50 | 35 | 20 | Ons, lør |
| **Brødmåltid** | 3 skiver med proteinpålegg + salat | 500 | 30 | 55 | 15 | Nødvalg |

**Riktig valg er forhåndsutfylt per ukedag.** Han trenger bare gjøre noe hvis
han avvek. Det er forskjellen på en app han bruker i sju måneder og en han
bruker i to uker.

Ett justeringstrykk ved siden av: **«mye saus/dressing/panert»** → legg til
+150 kcal og +15 g fett. Det er den stille kalorien i enhver kantine, og den
er den eneste variasjonen som er verdt å fange opp.

---

## 6. Handlelistegrunnlag

Per rett: råvarer i **innkjøpsenheter**, ikke porsjoner. Artifacten summerer
opp fra ukas valg og runder opp til hele pakker.

### 6.1 Frokost

| Rett | Råvarer (innkjøpsenhet · porsjoner per enhet) |
|---|---|
| F1 / F2 | Egg, brett à 12 stk · **4 porsjoner** · Grovbrød, 1 brød · 8 porsjoner · Smør, 1 pk · 20+ · Melk, 1 l · mange |
| F3 | Proteinyoghurt naturell, 1 beger · **1** · Havregryn, 1 kg pose · 25 · Frosne bær, 1 pose 500 g · 6 |
| F4 | Kesam/skyr, 1 beger · **1** · Havregryn · Frosne bær · Nøtter, 1 liten pose 200 g · 12 |
| F5 | Havregryn · Melk, 1 l · 3 · Proteinpulver, 1 boks · 25+ · Frosne bær |
| F6 | Grovbrød, 1 brød · 5 · **Ett av:** makrell i tomat 1 boks · 2 / kokt skinke 1 pk · 3 / kaviar 1 tube · 5 / kalkun 1 pk · 3 |
| Tillegg avokado | Avokado, 1 stk · **2 porsjoner** (halv om gangen) |

### 6.2 Kl. 14

| Rett | Råvarer |
|---|---|
| M1 | Kesam eller cottage cheese, 1 beger · **1** · Frukt, 1 stk · 1 |
| M2 | Proteinyoghurt, 1 beger · **1** · Frosne bær |
| M3 | Egg, brett · **6 porsjoner** · Frukt |
| M4 | YT proteinsjokolademelk, 1 flaske · **1** · Frukt |
| M5 | Grovt knekkebrød, 1 pk · 8 · Makrell i tomat 1 boks · 2 **eller** kyllingfilet i skiver 1 pk · 3 · Gulrot, 1 pose · 10 |
| M6 | Proteinbar, 1 stk · **1** · Frukt |

### 6.3 Middag

| Ramme | Råvarer |
|---|---|
| R1 | Kyllingfilet 500 g · **2 porsjoner** *eller* svinefilet 500 g · 2 *eller* kjøttkaker 1 pk · 2 · Poteter, 3 kg · 7 · Rotgrønnsaker, 1 pose · 3 · Olje, 1 fl · mange |
| R2 | Biffstrimler 400 g · **2** *eller* kylling 500 g · 2 *eller* reker 1 pk · 2 · Frossen wokblanding, 1 pose 750 g · 2 · Ris, 1 kg pose · 8 · Soyasaus, 1 fl · mange |
| R3 | Kjøttdeig 5 % 400 g · **2** *eller* linser/kikerter 2 bokser · 2 · Frossen grønnsaksblanding, 1 pose · 2 · Hakkede tomater, 1 boks · 1 · Løk, 1 nett · 6 |
| R4 | Laks 400 g · **2** *eller* ørret 400 g · 2 *eller* makrellfilet 1 pk · 2 · Poteter · Grønnsaker, fersk el. frossen |
| R5 | Kjøttdeig 400 g · **2** *eller* tunfisk 2 bokser · 2 · Fullkornspasta, 1 pk 500 g · 4 · Hakkede tomater, 1 boks · 1 · Salat, 1 pose · 3 |
| R6 | Kjøttdeig 400 g · **2** · Fullkornstortilla, 1 pk · 2 · Bønner, 1 boks · 2 · Lettrømme, 1 beger · 3 · Paprika/salat/mais |

### 6.4 Kl. 21

| Rett | Råvarer |
|---|---|
| K1 | Skyr eller kesam, 1 beger · **1** · Frosne bær |
| K1+ | + Granola, **liten pose 350 g · 8 porsjoner.** Aldri storpakke |
| K2 | Cottage cheese, 1 beger · **1** · Bær eller ananas 1 boks · 3 |
| K3 | Proteinyoghurt, 1 beger · **1** · Nøtter, liten pose |
| K4 | Egg, brett · **6** · Gulrot/agurk |
| K5 | Kvarg/proteinpudding, 1 beger · **1** |
| K6 | Skummet melk, 1 l · 2 · Kakaopulver, 1 boks · mange · Skyr, 1 beger · 2 |

### 6.5 Faste poster (uavhengig av valg)

Legges alltid på lista: bananer 7–8 stk · loff 1 brød (frys halve) · syltetøy
1 glass · YT Protein restitusjonsdrikk 4–5 stk · kaffe · te · seigmenn til
langtur.

### 6.6 Innkjøpsregler artifacten skal følge

1. **Rund alltid opp til hel pakke**, og vis restporsjonene («2 igjen»).
2. **Nøtter og granola kjøpes i små pakker. Aldri storpakke — også når det er
   billigere.** Dette er en bevisst regel: det som er hjemme, blir spist.
3. **Egg alltid minst 2 brett** hvis F1, F2, M3 eller K4 er valgt mer enn to
   ganger i uka.
4. **Ferskvare med kort holdbarhet flagges** — leverpostei har allerede blitt
   muggen én gang. Vis datoadvarsel på pålegg, kesam og fersk fisk.
5. Grupper lista **etter butikkavdeling**, ikke etter rett. Han står i butikken,
   ikke på kjøkkenet.

---

## 7. Gjennomgang 07.09.2026 — leverer planen?

Regnet gjennom på faktiske menykombinasjoner. **Kort svar: to av de tre
problemene fra forrige versjon står fortsatt åpne, og det har kommet ett nytt.**

### 7.1 Fettgulvet på hviledager — FORTSATT ÅPENT, nå fikset med regel

Typisk underskuddshviledag: F3 + halv karbo-lunsj + M2 + R3 hviledag + K2
→ **60 g fett** mot gulvet på 70. Menyene løser det ikke av seg selv, fordi
alle de magre valgene er de som ellers er mest praktiske.

**Fiks (hardt, ikke forslag): på ons og lør skal minst ett av disse med —
halv avokado, 1 ss nøtter, eller K3 som kveldsmåltid.** Det gir +11 g fett og
lander på 71–78. Fettmålet på hviledag er samtidig hevet til **75 g**, og
karbotaket justert til 170 g slik at kaloriene går opp.
Artifacten skal legge dette inn automatisk når en hviledag settes opp, og
markere hvis det fjernes.

### 7.2 Fredagskarboen — FORTSATT ÅPENT, og verre enn antatt

Full fredag med alle måltider (F3 + full lunsj + loff 13:30 + banan +
seigmenn underveis + YT etter + R5 + K1+) summerer til:

| | Sum | Mål (12,3 km) | Avvik |
|---|---|---|---|
| kcal | 3 705 | 4 240 | **−535** |
| Karbo | 511 g | 592 g | **−81 g (−14 %)** |
| Protein | 235 g | 220 g | ✓ |
| Fett | 69 g | 110 g | **under gulvet** |

Fredagen underleverer på alle tre. **To faste poster inn:**
1. **Kl. 09:30: banan + 2 skiver grovbrød med syltetøy** (+340 kcal, +65 g
   karbo). Fredag er den eneste dagen med et femte måltid.
2. **Fettet legges i fredagsmiddagen, ikke i frokosten** — +1 ss olje og ost
   i middagen (+15 g fett). Fett før langtur er fortsatt forbudt.

Med disse: kcal 4 045, karbo 576 g, fett 84 g. Fortsatt litt under, men
innenfor 15 %-terskelen og realistisk å spise.

### 7.3 Proteinvarselet — LØST, men motsatt av antatt

Forrige versjon sa at varselet nesten aldri utløses. Det var feil.
**Det finnes en fullt lovlig kombinasjon som lander på 157 g protein:**
F6 (brødmåltid, 20 g) + halv karbo-lunsj (50) + M5 (12) + R3 hviledag (60) +
K4 (15). Det er 63 g under gulvet, og alle fem valgene er tilgjengelige i
katalogen.

**Fiks: artifacten skal summere protein ved planlegging, ikke ved logging.**
Faller en planlagt dag under 200 g, skal den si fra *mens han velger* — ikke
dagen etter. De tre lavproteinrettene (F6, M3, M5, K4) skal ha et lite merke.

### 7.4 Nytt funn: energiforbruket var overvurdert med ~10 %

Se § 1. Dette er det som betyr mest av alt i denne gjennomgangen.
Ved dagens volum lå de gamle måltallene 2 200 kcal/uke for høyt — han ville
spist på vedlikehold og trodd han var i underskudd.

### 7.5 Konklusjon

Menyene leverer protein, variasjon og karbo på kvalitetsdager. De svikter på
tre punkter, alle nå adressert: **fett på hviledager, karbo og fett på
fredag, og volumjustering av kaloriene.** Det fjerde — tidsbruk på kjøkkenet
— er behandlet i `matplan.md` § 11.

---

## 8. Hva som skal skje når vekta ikke følger tallene

Artifacten skal **ikke** justere målene selv. Regelen er:

- Ukesnitt faller > 0,5 kg/uke i to uker → **spis mer**, ikke mindre.
  Artifacten viser meldingen, `ernaering` justerer tallene.
- Ukesnitt står stille i tre uker med planen fulgt → **da** justerer vi.
  Ikke før.
- Ingen automatisk nedjustering av kalorier. Ingen adaptive algoritmer.
  Tallene i § 1 endres av `ernaering` og skrives inn her, med dato.

**Og: fra 15. januar 2027 slås underskuddsfasen av.** Det er ikke
forhandlingsbart og bør ligge som en hard dato i systemet.

---

## 9. Katalogendringer 07.09.2026 — for bygging

Alle endringer fra mealprep-omleggingen. Samme kolonner som § 4 og § 6.
**Kcal · P · K · F i gram.**

### 9.1 FJERNET

| # | Rett | Grunn |
|---|---|---|
| **F5** | Havregrøt kokt på melk + protein | 6 min og en kjele kl. 07. Erstattet av F5n |

### 9.2 LAGT TIL — frokost

| # | Rett | Porsjon | kcal | P | K | F | Tid | Prep |
|---|---|---|---|---|---|---|---|---|
| **F5n** | Overnight oats | 1 glass: 1 dl havregryn, 250 g skyr, 1 dl melk, bær, 1 ts chiafrø | 375 | 35 | 40 | 6 | **0 min** | Søndag, 5 stk |
| **F7** | Egg-muffins + grovbrød | 3 muffins + 1 skive | 380 | 30 | 20 | 21 | **2 min** | Søndag, 12 stk |
| **F8** | Proteinsmoothie | 100 g frosne bær, 250 g skyr, 2 dl melk, 0,5 dl havregryn | 350 | 35 | 35 | 5 | **2 min** | Nei |

### 9.3 LAGT TIL — kl. 14 og faste poster

| # | Rett | Porsjon | kcal | P | K | F | Tid |
|---|---|---|---|---|---|---|---|
| **M7** | Skyr-boks (samme prep som F5n) | 1 liten boks: skyr, bær, havregryn | 250 | 25 | 28 | 3 | 0 min |
| **P-fre** | **Fredag kl. 09:30:** banan + 2 skiver grovbrød m/syltetøy | — | 340 | 9 | 65 | 2 | 2 min |

**P-fre er obligatorisk på fredager.** Se § 7.2. Skal ikke kunne velges bort.

### 9.4 ENDRET — status og tidsmerking, tall uendret

| # | Rett | Endring |
|---|---|---|
| **F1** Eggerøre | **5 min + panne.** Merkes «helg». Ikke standardvalg på ukedag |
| **F2** Stekt egg | Merkes 3 min. Beholdt som ukedagsvalg |
| **F3** Proteinyoghurt | **Nytt standardvalg på treningsdag.** 1 min |
| **F4** Skyr + havregryn + nøtter | **Nytt standardvalg på hviledag** — dekker fettgulvet. 1 min |
| **F6** Grovbrød m/pålegg | Lavproteinmerke (20 g) |
| **M3** 2 kokte egg | Eggene kokes søndag. Lavproteinmerke |
| **M5** Knekkebrød + makrell | Lavproteinmerke |
| **K4** 2 kokte egg + grønnsaker | Eggene kokes søndag. Lavproteinmerke |
| **R1** Panne/ovn | **Krever prepede poteter.** 15 min med prep, 50 uten |
| **R2** Wok | Krever prepet ris. 15 min |
| **R3** Gryte/suppe | **Er selv en prep-rett.** 4 porsjoner søndag, 8 min å varme |
| **R4** Fet fisk | Krever prepede poteter + frossen fisk tint dagen før. 18 min |
| **R5** Pasta m/kjøttsaus | **Krever prepet saus.** 12 min med, 40 uten |
| **R6** Taco | Krever prepet kjøttdeig. 12 min |
| **R3–R6 fredag** | +1 ss olje og ost: **+150 kcal, +15 g fett.** Se § 7.2 |
| **K1+** granola | Uendret. Fortsatt kun treningsdag, kun til 28.09 |

### 9.5 Nye felter artifacten trenger per rett

| Felt | Verdier |
|---|---|
| `tid_min` | Minutter aktiv tid. Vises alltid |
| `krever_prep` | Hvilken prep-komponent retten avhenger av |
| `prep_dag` | søndag / onsdag / ingen |
| `holdbarhet_dager` | Fra § 11.5 i matplanen |
| `lavprotein` | true på F6, M3, M5, K4 |
| `kun_treningsdag` | true på M4, K1+ |
| `obligatorisk` | true på P-fre |

**Ukedagsfilter:** artifacten skal kunne skjule alt over 20 minutter aktiv tid
på man–fre. Det er hele Knuts bestilling i ett filter.

### 9.6 Handleliste — nye og endrede poster

| Rett | Råvarer (innkjøpsenhet · porsjoner) |
|---|---|
| **F5n** | Havregryn 1 kg · 25 · Skyr 1 kg-beger · 4 · Melk 1 l · mange · Frosne bær 500 g · 6 · **Chiafrø, 1 liten pose · 30** |
| **F7** | Egg, brett à 12 · **4 porsjoner** (12 muffins) · Revet ost 1 pk · 3 · Paprika 1 stk · 2 · Spinat 1 pose · 3 |
| **F8** | Frosne bær · Skyr · Melk · Havregryn |
| **M7** | Samme som F5n |
| **P-fre** | Grovbrød 1 brød · Syltetøy · Bananer |
| **Prep generelt** | Poteter **3 kg** (fast, hver uke) · Ris 1 kg · Frossen wokblanding 750 g · 2 · Hakkede tomater 2 bokser · Løk 1 nett |
| **Fisk** | **Kjøpes frossen.** Laks/torsk 400 g frossen · 2 |

**Utstyr — engangskjøp, må på lista første uke:**
8–10 tette matbokser · 5 glass med lokk (overnight oats) · 1 muffinsform.

### 9.7 Handleregler — tillegg

7. **Grupper etter prep-økt i tillegg til butikkavdeling.** Vis hvilke varer
   som brukes på søndag, så han vet hva som må være hjemme før prepen.
8. **Fisk foreslås alltid frossen.** Fersk fisk holder 1–2 dager og passer
   ikke i et ukesystem.
9. **Vis holdbarhet på prepede retter som nedtelling** — «gryte: 2 dager
   igjen, frys i kveld». Det er onsdagsregelen i § 11.5, automatisert.

---

## 10. Katalogendringer 07.09.2026 (nr. 2) — jobb-måltidene

**Bakgrunn:** Knut jobber 08–16. Både kl. 14 og 15:30 spises på jobb.
Kantina koster ekstra utenom lunsjen, og matboks hjemmefra hver dag er
utelukket. Løsningen er en **skuff med romtemperaturvarer** (hovedløsning) og
**én ukentlig kjøleskapspåfylling** (kl. 14). Full begrunnelse i
`matplan.md` § 12.

### 10.1 FJERNET

| # | Rett | Grunn |
|---|---|---|
| **P-15:30-gammel** | «1 banan + 2 skiver loff med syltetøy» som standard | Forutsatte at han var hjemme. Beholdes kun som hjemme-variant |

### 10.2 LAGT TIL — kl. 15:30, skuff (romtemperatur)

| # | Rett | Porsjon | kcal | P | K | F | Lagring |
|---|---|---|---|---|---|---|---|
| **J1** | **Corny Big + rosiner** — standardvalget | 1 bar (50 g) + 1 neve Sun-Maid (~40 g) | 320 | 4 | 60 | 6 | Skuff |
| **J2** | **Corny Big alene** — minimumsvarianten | 1 bar (50 g) | 200 | 3 | 30 | 6 | Skuff |
| **J3** | **Riskaker + rosiner** — fettfattigst, ved urolig mage | 4 riskaker + 1 neve rosiner | 240 | 4 | 55 | 2 | Skuff |
| **J4** | **Banan + Corny Big** — når han har banan med | 1 banan + 1 bar | 305 | 4 | 55 | 6 | Delvis |
| **J5** | **Fredag 13:30** — juice + bar + riskaker | 1 Sunniva 0,33 l + 1 Corny Big + 3 riskaker | 440 | 7 | 82 | 7 | Skuff |

### 10.3 LAGT TIL — kl. 14, skuffereserve

| # | Rett | Porsjon | kcal | P | K | F | Lagring |
|---|---|---|---|---|---|---|---|
| **M8** | **Barebells proteinbar** — reserve når kjøleskapet er tomt | 1 bar (55 g) | 200 | 20 | 17 | 7 | Skuff |

M8 erstatter den generiske M6 «proteinbar + frukt» med et konkret produkt som
tåler skuff. M6 kan beholdes eller slås sammen.

### 10.4 ENDRET

| # | Endring |
|---|---|
| **M1, M2, M4** | Merkes **`krever_kjoleskap`**. Inngår i mandagens påfylling, ikke daglig medbringing |
| **P-fre (09:30)** | Endret fra «banan + 2 skiver grovbrød m/syltetøy» til **J1 fra skuffen** (320 · 4 · 60 · 6). Samme rolle, ingen medbringing |
| **Fredag 15:15** | Endret fra «1 banan» til **1 neve rosiner** (120 · 1 · 30 · 0) |
| **Alle 15:30-poster** | Nytt minimumskrav: **≥ 40 g karbo, < 10 g fett, lavt fiber** |

### 10.5 Nye felter

| Felt | Verdier |
|---|---|
| `lagring` | `skuff` / `kjoleskap_jobb` / `hjemme` |
| `krever_medbringing` | true/false. **Alt med true skal merkes visuelt** |
| `holdbarhet_skuff_uker` | Se `matplan.md` § 12.5 |

**Designregel:** artifacten skal alltid **foreslå skuffvarianten først** på
man–fre. Hjemme-variantene (banan, loff) vises som sekundærvalg. En plan som
krever daglig handling hjemmefra er en plan som ryker.

### 10.6 Handleliste — nye poster

**Månedskjøp, én gang hver fjerde uke:**

| Vare | Innkjøpsenhet | Antall | Rekker |
|---|---|---|---|
| **Corny Big musli-bar** | 6-pk | **3** | 4 uker (18 barer) |
| **Sun-Maid rosiner** | Pose 500 g | **1** | 4–5 uker |
| **Sunda/Kavli riskaker** | Liten pk | **2** | 3–4 uker |
| **Sunniva juice 0,33 l** | 4-pk | **1** | 4 fredager |
| **Barebells proteinbar** | Boks | **1** | Nødreserve |
| **Tett plastboks** | 1 stk | **1** | Engangskjøp |

**Ukentlig, mandag morgen — «mandagsposen» til kjøleskapet på jobb:**

| Vare | Antall |
|---|---|
| Tine Skyr eller Q Kesam, beger | **5** |
| Litago sjokolademelk 0,33 l | **4** |

**Handleregler — tillegg:**

10. **Skuffvarer er et månedskjøp, ikke et ukeskjøp.** Egen liste, egen
    påminnelse hver fjerde uke.
11. **Mandagsposen er én påminnelse i uka**, søndag kveld. Ikke fem.
12. **Ingenting med sjokoladetrekk, nøtter eller melk i skuffen.**
    Smelter, harskner eller blir dårlig.
