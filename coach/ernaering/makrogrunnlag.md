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

### Forutsetninger (så de kan justeres når de endrer seg)

| | |
|---|---|
| Vekt | 119 kg · 195 cm · 38 år |
| Hvilestoffskifte | ~2 225 kcal |
| Forbruk uten trening | ~2 950 kcal/dag (hvilestoffskifte × 1,35, justert ned for sju måneders adaptasjon) |
| Løping | ~1 kcal per kg per km ≈ 120 kcal/km |
| Styrkeøkt | ~320 kcal |
| Planlagt ukesvolum | 34–40 km |
| Vedlikeholdsbehov | **~24 800 kcal/uke** |
| Underskuddsmål | 2 700 kcal/uke ≈ **0,35 kg/uke** |

**Volumavhengighet — viktig akkurat nå.** Ukesvolumet er 16,8 km, ikke 34–40.
Tallene under forutsetter planlagt volum. Regelen artifacten skal bruke:
**faller ukesvolumet mer enn 30 % under plan, trekk 120 kcal per manglende km
fra kvalitets- og langturdagene** — ikke fra hviledagene, som allerede er lave.

### 1.1 Vedlikeholdsfasen — 08.–28.09.2026

| Dag | Type | kcal | Protein | Karbo | Fett |
|---|---|---|---|---|---|
| **Man** | Kvalitet | 3 900 | 220 g | 480 g | 120 g |
| **Tir** | Styrke | 3 300 | 220 g | 380 g | 100 g |
| **Ons** | Hvile | 2 900 | 220 g | 280 g | 100 g |
| **Tor** | Intervaller | 3 900 | 220 g | 480 g | 120 g |
| **Fre** | Langtur | 4 500 | 220 g | 650 g | 113 g |
| **Lør** | Hvile | 2 900 | 220 g | 280 g | 100 g |
| **Søn** | Rolig | 3 400 | 220 g | 380 g | 110 g |
| **Uke** | | **24 800** | 1 540 g | 2 930 g | 763 g |

### 1.2 Underskuddsfasen — fra 28.09.2026

| Dag | Type | kcal | Protein | Karbo | Fett | Endring |
|---|---|---|---|---|---|---|
| **Man** | Kvalitet | 3 700 | 220 g | 470 g | 105 g | −200 |
| **Tir** | Styrke | 2 900 | 220 g | 300 g | 90 g | −400 |
| **Ons** | Hvile | 2 200 | 220 g | 170 g | 70 g | **−700** |
| **Tor** | Intervaller | 3 700 | 220 g | 470 g | 105 g | −200 |
| **Fre** | Langtur | **4 500** | 220 g | 650 g | 113 g | **0** |
| **Lør** | Hvile | 2 200 | 220 g | 170 g | 70 g | **−700** |
| **Søn** | Rolig | 2 900 | 220 g | 300 g | 90 g | −500 |
| **Uke** | | **22 100** | 1 540 g | 2 530 g | 643 g | **−2 700** |

**Merk at fredag er identisk i begge faser.** Det er ikke en glipp. Langturen
er ukas viktigste økt og den eneste magetreningen vi har. Artifacten skal
**aldri** foreslå å kutte på fredag, uansett hvor mye vekta har stått stille.

---

## 2. Hardt krav mot retningsgivende

Dette avgjør hvordan avvik skal vises. Tre nivåer, tre visuelle uttrykk.

### Nivå 1 — GULV. Skal aldri brytes. Vises tydelig.

| Krav | Verdi | Hvorfor |
|---|---|---|
| **Protein** | **≥ 220 g, hver eneste dag** | Avgjør om vekttapet er fett eller muskel. Knut har akseptert noe tap av magert vev — nettopp derfor er dette gulvet skjerpet, ikke løsnet. Gjelder også hviledager. |
| **Fett** | **≥ 70 g** | Hormoner og fettløselige vitaminer. Brytes typisk på underskuddshviledager — se § 7. |
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

## 7. Kjente problemer artifacten må håndtere

Regnet gjennom på faktiske dagskombinasjoner. Tre reelle funn:

1. **Fettgulvet ryker på hviledager i underskuddsfasen.** En typisk
   ons/lør-kombinasjon (F3 + halv karbo-lunsj + M2 + R3 hviledag + K2) lander
   på ca. 60 g fett mot gulvet på 70. **Fiks:** artifacten skal foreslå
   halv avokado til frokost eller 1 ss nøtter til kl. 14 på hviledager. Ikke
   som advarsel — som forslag ved planlegging.

2. **Karboen på fredag underleveres nesten alltid.** Målet er 650 g, og en
   full fredag med alle måltider lander typisk på 550–600. Det er den ene
   dagen karbogapet skal vises **før** dagen, ikke etter — som et forslag om
   ekstra brød eller en ekstra porsjon karbo til middag.

3. **Proteinet treffer lett — for lett.** De fleste kombinasjoner lander på
   230–270 g, altså godt over gulvet på 220. Det er bra og skal ikke
   «korrigeres» ned. Men det betyr at proteinvarselet nesten aldri utløses —
   og da må det bety noe når det først gjør det. Ikke svekk terskelen for å
   få det til å vises oftere.

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
