# Research: frosne fiskeprodukter i norsk dagligvare

Faktagrunnlag. Ingen ernæringsvurdering eller anbefaling — det tas av ernæringsagenten.

Innsamlet: 2026-09-08.

---

## 0. Metode og begrensninger — les dette først

**Viktig teknisk begrensning:** direkte sidehenting (WebFetch) var blokkert av nettverkets egress-policy for **alle** relevante domener i denne sesjonen. Følgende ble forsøkt og avvist med `EGRESS_BLOCKED`:

oda.com, meny.no, coop.no, findus.no, lofoten.no, fiskemannen.no, kassal.app, produkter.matinfo.no, matvaretabellen.no, matoppskrift.no, mylog.no, ingrediens.no, leroyseafood.com, firstprice.no, spar.no, norges.online, ernær.no.

Alle tall under er derfor hentet via **søkemotor-uttrekk fra disse sidene**, ikke ved å lese næringsdeklarasjonen på siden selv. Konsekvens:

- Tallene er andrehånds. De stammer fra de oppgitte kildesidene, men er ikke verifisert mot selve produktsiden i denne sesjonen.
- Der to kilder spriker, er begge oppgitt.
- Der et felt (typisk **salt**) ikke kom med i uttrekket, står det `ikke funnet` — ikke et anslag.

**Kolonnen «Sikkerhet»** i tabellene:
- **V** = tallet ble gjengitt direkte fra en identifiserbar produkt-/deklarasjonskilde (høy tillit, men se forbeholdet over).
- **U** = usikkert: kilden var indirekte, aggregert, eller flere kilder spriker.
- **B** = beregnet av meg (utregning vises).

---

## 1. Naturell frossen filet

### 1a. Hvitfisk — næringsinnhold per 100 g (rå)

| Produkt | kcal | Fett | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|
| **Findus Torsk Naturell 400 g** | 75 | 0,7 g | 0 g | 17 g | 0,1 g | V | produkter.matinfo.no (Findus Norge, GTIN 07042110073034) |
| **Findus Torskefilet Gourmet / Ryggfileter 420 g** | 75 | 0,7 g | 0 g | 17 g | ikke funnet | V | kassal.app vare 4800 (GTIN 7310500113142) |
| **First Price Torskefilet Blokk u/skinn&ben 400 g MSC** | 81 | 1,0 g | 0 g | 18,1 g | ikke funnet | V | matoppskrift.no / kassal.app vare 4887 (GTIN 7035620017483) |
| **Coop Fra Havet Torskefilet Naturell 360 g** | 75 | 0,3 g | 0 g | 18,1 g | ikke funnet | V | kassal.app vare 25004 (GTIN 7025110145659) |
| **First Price Seifilet Blokk 400 g MSC** | 69 | 0,3 g | 0 g | 16,5 g | ikke funnet | V | matoppskrift.no / kassal.app vare 10124 |
| Sei, generisk naturell (referanse) | 69 | 0,3 g | 0 g | 16,5 g | 0,2 g | V | karlsfiskogskalldyr.no / matvaretabellen |
| Torsk, generisk naturell (referanse) | 75 | 0,2 g | 0 g | 16,1 g | 1,6 g (!) | U | karlsfiskogskalldyr.no — saltverdien 1,6 g virker å gjelde **lettsaltet** torsk, ikke naturell. Ikke bruk uten kontroll. |
| Hyse, generisk naturell (referanse) | 68 | 0,2 g | 0 g | 16,6 g | ikke funnet | U | fiskehandleren.no / karlsfiskogskalldyr.no |

**Lyr:** fant ingen frossen lyrfilet som standardvare i norsk kjede-dagligvare. Lyr selges i hovedsak fersk over disk / fra fiskebil. Ikke funnet.

### 1b. Fet fisk — næringsinnhold per 100 g (rå)

| Produkt | kcal | Fett | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|
| **Findus Laksefilet Naturell** | 230 | 17 g | 0 g | 20 g | ikke funnet | V | matoppskrift.no / mylog.no id 1264 |
| **Norsk Sjømat Laksefilet Naturell u/skinn 500 g** | 224 | 16 g | 0 g | 20 g | ikke funnet | V | oda.com prod. 27246 (via uttrekk) / kassal.app 29524 |
| **Lerøy Laksefilet Naturell (u/skinn og ben)** | 224 | 16 g | 0 g | 20 g | ikke funnet | V | leroyseafood.com |
| Coop laksefilet m/skinn | 200 | 13,5 g | 0 g | 20 g | ikke funnet | U | mylog.no |
| **Lerøy Ørret Naturell (frys, 2x125 g / 4x100 g)** | 161 | 10,2 g | 0 g | 17,2 g | ikke funnet | V | mylog.no id 25612 / leroyseafood.com |
| **First Price Ørretfilet** | ikke funnet | ikke funnet | – | ikke funnet | ikke funnet | – | produkter.matinfo.no (Unil AS, GTIN 27035620045343) — produktet eksisterer, deklarasjonen kom ikke ut |
| Makrell, varmrøkt (referanse) | ikke funnet | 24 g | – | 19 g | ikke funnet | V | matvaretabellen.no |
| Makrell, kaldrøkt (referanse) | ikke funnet | 18 g | – | 18 g | ikke funnet | V | matvaretabellen.no |

**Makrellfilet naturell frossen:** jeg fant **ingen** naturell frossen makrellfilet som standard kjedevare (Rema/Kiwi/Coop/Meny). Treffene var spesialforhandlere (Havøyet, Domstein, Jacobs). Makrell i norsk dagligvare er dominert av hermetikk (makrell i tomat) og røkt kjølevare. **Ikke funnet som frossenvare i kjedene.**

Merk også: makrellens fettinnhold varierer voldsomt med sesong — vårmakrell ca. 3 % fett, høstmakrell opptil 30 % (kilde: godfisk.no via uttrekk). Ett tall for «makrell» er derfor lite meningsfullt.

---

## 2. Panerte produkter

Dette er hovedspørsmålet, så tabellen er den mest komplette.

### 2a. Fiskepinner

| Produkt | Fiskeandel | kcal | Fett | Mettet | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|---|---|
| **Findus Fiskepinner Originalen 750 g (30 stk)** | 61 % stillehavslysing (Merluccius productus) | 208 | 9,6 g | <1 g | 18 g | 12 g | ikke funnet | V | matoppskrift.no / matinfo GTIN 07035110301818 |
| **Findus Fiskepinner MSC 750 g** (Oda-listing) | 61–65 % (kilden oppgir både Alaska pollock 65 % og torsk 61 % avhengig av batch/variant) | 230 | 9,3 g | – | 24 g | 12 g | 1,9 g | U | oda.com prod. 8906 — **salt 1,9 g avviker kraftig** fra alle andre kilder (0,7–0,96 g). Antatt feil i uttrekket. Ikke bruk. |
| **Findus Våre Beste Fiskepinner (100 % fiskefilet)** | 100 % filet (ikke farse) | 195 | 7,7 g | – | 18 g | 13 g | ikke funnet | V | mylog.no id 29174 / matoppskrift.no. Nøkkelhullsmerket. |
| **Findus Fiskepinner Glutenfri 360 g** | 65 % Alaska pollock | 204 | 9,1 g | – | 17 g | 13 g | ikke funnet | V | matinfo GTIN 07310500177878 / kassal.app 6704 |
| **First Price Fiskepinner 450 g MSC** | 65 % Alaska pollock | 190 | 8,9 g | 0,8 g | 14 g | 13 g | **0,7 g** | V | matoppskrift.no (GTIN 7035620057137) |
| Findus fiskepinner, Bramat-test 2020 (variant A) | 65 % Alaska pollock | – | – | – | – | 12 g | 0,7 g | V | bramat.no test fiskepinner 2020 |
| Findus fiskepinner, Bramat-test 2020 (variant B) | 65 % | – | – | – | – | 13 g | 0,96 g | V | bramat.no |
| Findus fiskepinner, Bramat-test 2020 (variant C) | 61 % | – | – | – | – | 12 g | 0,8 g | V | bramat.no |
| Coop fiskepinner, Bramat-test 2020 | 60 % torsk | – | – | – | – | 14,1 g | 0,55 g | V | bramat.no |
| **Prima Lavpris Fiskepinner 900 g / 450 g** | ikke funnet | – | – | – | – | – | – | – | oda.com prod. 4132 / 67340 — produktene eksisterer, deklarasjon ikke hentet |

Spennvidde fiskeandel i fiskepinner i test: **52–75 %** (klikk.no/nettavisen, test av 18 produkter). Bramats konklusjon: vinnerne hadde dobbelt så mye fisk som taperne.

### 2b. Panert filet / «crispy»-varianter

| Produkt | Fiskeandel | kcal | Fett | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|---|
| **Findus Steketorsk (nøkkelhullsmerket, rå panering)** | ikke funnet i % | 135 | **0,5 g** (én kilde oppgir 0 g) | 17,6 g | 14,3 g | **0,4 g** | U på fett (to kilder spriker 0 vs 0,5) | matvaretabellen.no «Torsk, panert, Findus Steketorsk» / ingrediens.no |
| **Findus Lettpanert Torsk** | **75 %** torsk | 185 | 9,0 g | – | **15,5 g** | 0,40 g | V | klikk.no test av panert fisk (3392926) — testens høyeste proteininnhold |
| **Findus Sprøbakte Fiskefileter 500 g** | 64 % Alaska pollock | 168 | 7,3 g | 13 g | 12 g | ikke funnet | V | matoppskrift.no / matinfo GTIN 07310500173702 |
| **Findus Fish & Crisp Originalen** | 52 % Alaska pollock | 216 | 11 g | 18 g | 11 g | ikke funnet | V | mylog.no id 29224 / matoppskrift.no |
| **Findus Fish & Crisp Gourmetfiléer** | 52 % | 226 | 14 g | 15 g | 11 g | ikke funnet | U (to varianter i kildene) | matoppskrift.no / matinfo GTIN 07035119999276 |
| **Findus Fisk i en Fei, torsk** | 61 % | 210 | 9,0 g | – | 13 g | 0,60 g | V | bramat.no test panert fisk |
| **Coop Sprø Torsk Fullkorn 320 g** | **70 %** torsk (Gadus morhua) | 180 | **5,3 g** | 18 g | **15,0 g** | ikke funnet | V | kassal.app vare 25934 (GTIN 7025110188625) |
| **Lerøy Torskefilet Pankopanert 350 g** | 70 % torsk / 30 % glutenfri pankopanering | 185 | 9,7 g | 11,6 g | 12,9 g | ikke funnet | V | kassal.app 11721 (GTIN 7033352352933) / tryggmat.app 14369 |
| **Lerøy Sprøpanert Torsk familiepakning 600 g** | 70 % torsk / 30 % panering | ikke funnet | ikke funnet | – | ikke funnet | ikke funnet | – | leroyseafood.com — ingrediensliste og ovnsinstruks hentet, næringstabell ikke |
| **Lerøy Sprøpanert Sei familiepakning 600 g** | 65 % norsk seifilet / 35 % panering | ikke funnet | ikke funnet | – | ikke funnet | ikke funnet | – | leroyseafood.com |
| **Norway Seafoods Sprø Torsk** | 70 % torsk | ikke funnet | ikke funnet | – | ikke funnet | ikke funnet | – | norwayseafoods.com |
| **Coop Pankopanert Torskefilet 320 g** | ikke funnet | – | – | – | – | – | – | tryggmat.app 8109 — produkt eksisterer, deklarasjon ikke hentet |
| **First Price Panert Seifilet** | ikke funnet | – | – | – | – | – | – | klikk.no test 3392797 — produkt eksisterer, tall ikke hentet |

---

## 3. Panering — svar på de fire konkrete spørsmålene

### 3.1 Hvor mye av vekten er panering, og hvor mye fett tilfører den?

**Vektandel (verifisert fra ingredienslister):**
- Lerøy Sprøpanert Torsk: 70 % fisk / **30 % panering**
- Lerøy Sprøpanert Sei: 65 % fisk / **35 % panering**
- Findus fiskepinner: 61–65 % fisk → **35–39 % panering**
- Findus Fish & Crisp: 52 % fisk → **48 % panering**
- Findus Lettpanert Torsk: 75 % fisk → **25 % panering**

**Fettbidrag — regnestykke (B, beregnet):**

Naturell torsk/sei/Alaska pollock har 0,2–0,7 g fett per 100 g. I en fiskepinne med 65 % fisk bidrar fisken altså med ca. **0,1–0,5 g fett** per 100 g ferdig produkt. Produktet måler 8,9–9,6 g fett per 100 g.

→ **Ca. 8,5–9,5 g av fettet per 100 g kommer fra panering + forstekingsolje.** Det er >95 % av fettet i produktet.

Regnet per gram panering: 9 g fett fordelt på ~35 g panering = **ca. 25–27 g fett per 100 g panering**. (B — utregning basert på verifiserte fett- og andelstall over.)

For Fish & Crisp (52 % fisk, 11–14 g fett): ~11–14 g fett på ~48 g panering = ca. 23–29 g fett per 100 g panering. Samme størrelsesorden, men mer panering per porsjon.

### 3.2 Forstekt i olje vs. rå panering

**Ja, det er en reell og stor forskjell — og den er den viktigste variabelen i kategorien.**

- Bramat: *«De fleste typer panert fisk er forstekt i olje, så det er ikke nødvendig å steke fisken i ekstra fett.»* (bramat.no, test av panert fisk)
- Klikk/Nettavisen: *«Paneringen fungerer som en svamp og vil suge opp ekstra fett i stekepannen.»*
- Findus Foodservices har en egen produktkategori som heter bokstavelig **«panert fisk – forstekt»** (findusfoodservices.no), noe som bekrefter at forstekt/ikke-forstekt er et definert skille hos produsenten.

Målbart utslag i tallene:
- **Findus Steketorsk** (rå panering, stekes selv): **0,5 g fett** per 100 g, 14,3 g protein, 135 kcal.
- **Findus fiskepinner / Fish & Crisp** (forstekt): **9–14 g fett** per 100 g.

Det er en forskjell på ca. **1:20 i fett**. Steketorsk-tallet er imidlertid **U** — én kilde oppgir 0 g og én 0,5 g, og fiskeandelen er ikke funnet. Tallet gjelder også produktet **før** du tilsetter stekefett selv, som er hele poenget med et rå-panert produkt.

### 3.3 Finnes ovnsbakte varianter med vesentlig lavere fett?

Ja, men «vesentlig» er relativt:

| | Fett/100 g | Protein/100 g | Fiskeandel |
|---|---|---|---|
| Findus Steketorsk (rå panering) | 0,5 g | 14,3 g | ikke funnet |
| Coop Sprø Torsk Fullkorn 320 g | 5,3 g | 15,0 g | 70 % |
| Findus Sprøbakte Fiskefileter 500 g | 7,3 g | 12,0 g | 64 % |
| First Price Fiskepinner 450 g | 8,9 g | 13,0 g | 65 % |
| Findus Fiskepinner Originalen 750 g | 9,6 g | 12,0 g | 61 % |
| Lerøy Torskefilet Pankopanert 350 g | 9,7 g | 12,9 g | 70 % |
| Findus Fish & Crisp Originalen | 11 g | 11,0 g | 52 % |
| Findus Fish & Crisp Gourmet | 14 g | 11,0 g | 52 % |

Findus markedsfører Sprøbakte som *«kan ovnsbakes uten fett for best resultat»* (findus.no via uttrekk). Kiwis egen ernæringsartikkel anbefaler ovn framfor panne nettopp for å unngå at paneringen suger opp mer fett.

Merk: at et produkt *kan* ovnsbakes betyr ikke at det ikke allerede er forstekt. Ovnsbaking hindrer **ytterligere** fettopptak, den fjerner ikke fettet som allerede er der.

### 3.4 Hvor mye protein er egentlig igjen per 100 g?

Regnestykke (B):

100 g fiskepinne med 65 % fisk = 65 g fisk + 35 g panering.
65 g torsk/pollock à 17 g protein/100 g = **11,1 g protein fra fisken**.
Målt i produktet: 12–13 g protein.
→ ca. **1–2 g protein per 100 g kommer fra hvetemel i paneringen**, ikke fra fisk.

Samme regning for Fish & Crisp (52 % fisk): 52 g × 17 % = 8,8 g fra fisk, målt 11 g → ~2 g fra panering.

**Konsekvens for proteintetthet:** naturell torskefilet leverer 17–18 g protein per 100 g ved 75–81 kcal. Panert fiskepinne leverer 12–13 g protein ved 190–230 kcal. Per kalori er det ca. **3 ganger dårligere proteintetthet** (0,23 g protein/kcal mot 0,065 g/kcal). (B)

### 3.5 Er noen panerte produkter «bedre» enn andre?

Faktagrunnlaget, uten vurdering:

- Fiskeandel i kategorien spenner fra **52 % til 100 %** blant produkter faktisk i norsk dagligvare.
- Protein/100 g spenner fra **11 g til 15,5 g**.
- Fett/100 g spenner fra **0,5 g til 14 g**.
- Salt/100 g der det er funnet: **0,4–0,96 g**.
- De tre produktene med samtidig høyest fiskeandel og høyest protein i datasettet: Findus Lettpanert Torsk (75 %, 15,5 g protein, 9 g fett), Coop Sprø Torsk Fullkorn (70 %, 15 g protein, 5,3 g fett), Findus Våre Beste Fiskepinner (100 % filet, 13 g protein, 7,7 g fett).
- Bramat/Kiwi bruker **50–60 % fiskeandel som «bra»**-terskel for kategorien.

---

## 4. Fiskekaker, fiskeboller, fiskegrateng

### 4a. Fiskekaker

| Produkt | Fiskeandel | kcal | Fett | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|---|
| **Lofoten Hjemmelagde Fiskekaker 450 g** | **60 %** hysefilet | 146 | 7,6 g | 7,9 g | 11 g | **1,4 g** | V | lofoten.no / matvaretabellen.no |
| Lofoten fiskekaker (annen variant) | 60 % | – | – | – | 10,9 g | 1,30 g | V | ingrediens.no |
| **Lofoten Hjertekaker / Familiens Fiskekaker** | ikke funnet | 143 | – | – | 9,5 g | 1,2 g | V | lofoten.no |
| **Fiskemannen Fiskekaker 80 % 500 g** | **80 %** (torsk 60 % / hyse 40 % av fiskeandelen) | 134 | 7,2 g | 3,2 g | **14,2 g** | ikke funnet | V | fiskemannen.no (GTIN 7035620049101) / kassal.app 43692 |
| **Fiskemannen Fiskekaker 65 % 500 g** | **65 %** | – | – | – | 11,4 g (nedre ende av Fiskemannens spenn) | ikke funnet | U | fiskemannen.no (GTIN 7035620048074) |
| **Godehav Fiskekaker** | ikke funnet | 110 | 3,6 g | – | 12,3 g | **1,6 g** | V | ingrediens.no |
| Bramat 2024, best i test | 75 % | – | – | – | 17 g | 1,0 g | V | bramat.no fiskekaker 2024 |
| Bramat 2024, nr. 2 | 70 % | – | – | – | 14 g | 1,1 g | V | bramat.no |

Bramat 2024 om kategorien: fiskeandel spenner fra **50 % til over 90 %**. Mange produkter ligger fortsatt på **1,4–1,5 g salt per 100 g**. Produkter med lite fisk har mer karbohydrat og mindre protein.

### 4b. Fiskeboller (frosne / ikke-hermetiske)

| Produkt | Fiskeandel | kcal | Fett | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|---|
| **Lofoten Hjemmelagde Fiskeboller 350 g** | **65 %** fersk hysefilet | 69 | 0,7 g | 3,9 g | **11,4 g** | ikke funnet | V | matoppskrift.no / kassal.app 18552 |
| **Fiskemannen Fiskeboller (frossen)** | 60 % (torsk/hyse/sei) | – | – | – | – | ikke funnet | U | fiskemannen.no |
| Fiskemannen Fiskeboller i Kraft 500 g | 51 % hvitfisk | – | – | – | – | ikke funnet | U | fiskemannen.no (GTIN 7035620017667) |
| **Findus Fiskeboller** | 43 % | – | – | – | – | ikke funnet | U | klikk.no test av fiskeboller |
| Bolga Fryseri Fiskeboller (frossen) | 50 % renskåret fisk | 90 | 2 g | 8 g | 10 g | **2 g** | V | bolgafryseri.no |
| Fiskeboller kjølevare, generisk | – | – | 0,9 g | 5,5 g | 9,5 g | 1,4 g | V | ingrediens.no |

Merk: mesteparten av fiskebollemarkedet i Norge er hermetikk/kjølevare, ikke frys. Frosne fiskeboller finnes (Lofoten, Fiskemannen, Findus storhusholdning 25 g), men er en smalere hylle.

### 4c. Fiskegrateng

| Produkt | Fiskeandel | kcal | Fett | Mettet | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|---|---|
| **Findus Familiens Fiskegrateng 1 kg** | **24 %** Alaska pollock (+ 14 % makaroni) | 140 | 6 g | 0,6 g | 11 g | **9 g** | 0,3 g | V | matoppskrift.no / kassal.app 13534 (GTIN 7310500098968) |
| **Findus Kystens Fiskegrateng 390 g** | **19 %** Alaska pollock | 135 | 5,8 g | – | 14 g | **6,8 g** | ikke funnet | V | kassal.app 6088 (GTIN 7310500142746) |
| Findus (variant i Bramat 2024) | 30 % | – | – | – | – | 8,7 g | 0,79 g | V | bramat.no fiskegrateng 2024 |
| Lofotprodukt AS torskegrateng (best i test 2024) | **50 %** torsk | – | – | – | – | 12 g | 0,7 g | V | bramat.no fiskegrateng 2024 |
| Lofotprodukt AS (variant 2) | 36 % | – | – | – | – | 13 g | 0,9 g | V | bramat.no |
| **Coop Xtra Fiskegrateng** | ikke funnet | – | – | – | – | – | – | – | matoppskrift.no — produkt eksisterer, deklarasjon ikke hentet |

Bramat 2024 om kategorien: fiskeandel spenner fra **19 % til ca. 50 %**. Nesten ingen grønnsaker i produktene.

---

## 5. Ferdigretter med fisk

Tynt datagrunnlag — dette var den kategorien jeg fikk minst ut av.

| Produkt | Fiskeandel | kcal | Fett | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|
| **Findus Fisk i en Fei, torsk** | 61 % | 210 | 9,0 g | 13 g | 0,60 g | V | bramat.no |
| Findus Fisk i en Fei, torsk med middelhavssmør | ikke funnet | – | – | – | – | – | matoppskrift.no — eksisterer, tall ikke hentet |

**Ikke funnet:** en systematisk oversikt over frosne fiskeferdigretter (fiskegryter, fiskepanner, laks med tilbehør) i norsk kjede-dagligvare med deklarasjoner. Kategorien er liten sammenlignet med kjøtt-ferdigretter.

---

## 6. Røkt / gravet frossen fisk

| Produkt | kcal | Fett | Karbo | Protein | Salt | Sikkerhet | Kilde |
|---|---|---|---|---|---|---|---|
| Laks, røkt (generisk) | 225 | – | – | **23,2 g** | **3,1 g** | V | matvaretabellen.no / ingrediens.no |
| Laks, røkt (annen kilde) | 225 | – | – | 20 g | 1,0 g | U — spriker kraftig på salt | mylog.no id 231 |
| Laks, filet, gravet | 179 | 9 g | 2 g | **21 g** | ikke funnet | V | matvaretabellen.no / ingrediens.no |
| Makrell, varmrøkt | – | 24 g | – | 19 g | ikke funnet | V | matvaretabellen.no |
| Makrell, kaldrøkt | – | 18 g | – | 18 g | ikke funnet | V | matvaretabellen.no |

**Viktig forbehold:** dette er generiske matvaretabell-verdier for røkt/gravet laks, **ikke** for et navngitt frossent dagligvareprodukt. Røkt og gravet laks i norsk dagligvare selges i all hovedsak som **kjølevare**, ikke frossen. Jeg fant ingen navngitt frossen røkt/gravet-SKU i Rema/Kiwi/Coop/Meny-sortimentet. Spriket på salt (1,0 vs 3,1 g) er uavklart.

---

## 7. Pris og pris per gram protein

**Store forbehold på pris:**
- Rema 1000, Kiwi og Coop Extra **publiserer ikke priser på nett** (bekreftet av gjerrigknark.com/nettavisen-uttrekk). Prisene under er derfor i hovedsak fra **Meny, Joker og Spar**, som er dyrere kjeder enn Rema/Kiwi. Faktisk pris hos Knuts butikker er sannsynligvis lavere.
- Datering på prisene er usikker (uttrekk uten tidsstempel). Behandle som **U** gjennomgående.
- Kr/g protein er **B** (beregnet): (kr/kg) ÷ (g protein per 100 g × 10).

### Naturell filet

| Produkt | Pakke | Pris | Kr/kg | Protein/100 g | **Kr per g protein** | Kilde pris |
|---|---|---|---|---|---|---|
| First Price Seifilet Blokk 400 g | 400 g | 39,90 | 99,75 | 16,5 g | **0,60** | meny.no |
| Torskefilet i blokk (Kiwi, tilbud) | 400 g | 36,90 | 92,25 | ~18 g | **0,51** | allematpriser.no (tilbudspris, ikke ordinær) |
| Findus Torsk Naturell 400 g | 400 g | 67,90 | 169,75 | 17 g | **1,00** | norges.online |
| First Price Torskefilet Blokk 400 g | 400 g | 69,90 | 174,75 | 18,1 g | **0,97** | kassal.app |
| Norsk Sjømat Laksefilet u/skinn 500 g | 500 g | 120,00 | 240,00 | 20 g | **1,20** | oda.com-uttrekk |
| Findus Torskefilet Gourmet 420 g | 420 g | 185–199 | 440–474 | 17 g | **2,59–2,79** | spar.no / joker.no / meny.no |

### Bearbeidet

| Produkt | Pakke | Pris | Kr/kg | Protein/100 g | **Kr per g protein** | Kilde pris |
|---|---|---|---|---|---|---|
| First Price Fiskepinner 450 g | 450 g | 19,90 | 44,22 | 13 g | **0,34** | meny.no |
| Findus Fiskepinner 750 g | 750 g | 95,00 | 126,67 | 12 g | **1,06** | meny.no |
| Findus Fiskepinner 450 g | 450 g | 58,90 | 130,89 | 12 g | **1,09** | meny.no (godpris.no: spenn 53,60–61,90) |
| Findus Fiskepinner Glutenfri 360 g | 360 g | 65,90 | 183,06 | 13 g | **1,41** | meny.no / spar.no |
| Findus Sprøbakte Fiskefileter 500 g | 500 g | 86,90 | 173,80 | 12 g | **1,45** | joker.no |
| Fiskemannen Fiskekaker 80 % 500 g | 500 g | 57,90 | 115,80 | 14,2 g | **0,82** | meny.no |
| Vesterålens Fiskeboller i kraft 800 g | 800 g | 48,90 | 61,13 | ikke funnet | – | meny.no |

**Observasjon (faktum, ikke råd):** billigste kr/g protein i datasettet er First Price fiskepinner (0,34) og seifilet i blokk (0,60). Dyreste er Findus Gourmet torskefilet (2,6–2,8). Fiskepinnene er billige per gram protein, men leverer proteinet med 190–230 kcal per 100 g mot seifiletens 69.

---

## 8. Praktisk tilberedning — fra frossen, uten tining

| Kategori | Fra frossen? | Metode og tid | Sikkerhet | Kilde |
|---|---|---|---|---|
| **Panert fisk (fiskepinner, panert filet)** | **Ja, alltid** — skal ikke tines | Ovn, direkte fra fryser | V | Findus/Lerøy/Norway Seafoods bruksanvisninger |
| Lerøy Sprøpanert Torsk 600 g | Ja | Varmluft **220 °C, 22–25 min**, bakepapir, midt i ovnen | V | leroyseafood.com |
| Findus Sprøbakte Fiskefileter | Ja | Ovn, uten fett («best resultat») — tid ikke funnet | V (metode) / ikke funnet (tid) | findus.no |
| Fiskepinner, generelt | Ja | Ovn eller panne fra frossen; ovn anbefalt for å unngå fettopptak | V | kiwi.no ernæringsartikkel, bramat.no |
| **Naturell hvitfiskfilet, ovn** | **Ja** — «du kan steke frosne torskefileter rett i ovnen» | **180–200 °C, 10–20 min** avhengig av tykkelse | V | findus.no «Hvordan tilberede torsk og annen frossen fisk» |
| **Naturell hvitfiskfilet, koking** | Ja | Legg frossen filet i kokende vann. **9–10 min** halvtint; 5–7 min tint | V | findus.no |
| **Naturell hvitfiskfilet, stekepanne** | **Nei — frarådes** | Kilden anbefaler opptinte fileter i panne | V | findus.no / meny.no tilberedningsguide |
| Fiskekaker (frosne) | Ja, stekes fra frossen | Tid ikke funnet | U | – |
| Fiskegrateng | Ja, fra frossen | Ovn; tid varierer 45–60 min for 1 kg-pakning (**anslag, ikke verifisert**) | **Anslag** | ikke funnet i kilde |
| Laksefilet naturell frossen | ikke funnet | – | – | ikke funnet |

**Relevant for 18-minuttersvinduet:** ovnsbaking av naturell hvitfisk på 180–200 °C i 10–20 min er den eneste naturell-metoden som er verifisert å fungere fra frossen. Panert fisk i ovn ligger på 20–25 min hos Lerøy, altså **over** 18 minutter for det produktet. Halvtint fisk avgir vann og krever ekstra tid (findus.no).

---

## 9. Hva jeg ikke fant

Eksplisitt liste:

1. **Enghav som merke.** Jeg fant ingen bekreftelse på at «Enghav» er et aktivt merke i norsk dagligvare i dag. Ingen produktsider, ingen deklarasjoner. Enten er merket utgått, regionalt, eller navnet er feil. **Bør kontrolleres i butikk.**
2. **Eldorado frosne fiskeprodukter.** Ingen treff på Eldorado laksefilet/torskefilet frossen. Eldorado ser ut til å ikke føre frossen fisk.
3. **Naturell frossen makrellfilet** i kjede-dagligvare. Finnes hos spesialforhandlere, ikke funnet som kjedevare.
4. **Frossen lyrfilet** i dagligvare. Ikke funnet.
5. **Navngitte frosne røkt/gravet-produkter.** Kategorien ser ut til å være kjølevare i Norge. Tallene i seksjon 6 er generiske matvaretabell-verdier.
6. **Saltinnhold** for et stort antall produkter — se `ikke funnet` i tabellene. Særlig: alle naturelle laksefileter, Findus Sprøbakte, Fish & Crisp, Lerøy pankopanert, Fiskemannen fiskekaker 80 %, Lofoten fiskeboller.
7. **Priser hos Rema 1000 og Kiwi.** Kjedene publiserer ikke priser på nett. Alle priser i seksjon 7 er fra Meny/Joker/Spar og er systematisk høyere enn Rema/Kiwi.
8. **Prima Lavpris fiskepinner** (900 g / 450 g) — produktene finnes, deklarasjon ikke hentet.
9. **Coop Xtra Fiskegrateng, Coop Pankopanert Torskefilet 320 g, First Price Ørretfilet, First Price Panert Seifilet** — produktene er bekreftet å eksistere, men næringsdeklarasjonene ble ikke hentet ut.
10. **Fiskeandel i Findus Steketorsk** — produktet er nøkkelhullsmerket og har svært lavt fettinnhold, men fiskeprosenten er ikke funnet.
11. **Ovnstider for fiskegrateng og fiskekaker fra frossen** — ikke funnet i kilde.
12. **Tilberedning av naturell laksefilet fra frossen** — ikke funnet.

---

## 10. Kjente datakonflikter (må avklares før tallene brukes)

| Konflikt | Verdi A | Verdi B | Kommentar |
|---|---|---|---|
| Findus Fiskepinner, salt | 1,9 g/100 g (oda-uttrekk) | 0,7–0,96 g/100 g (bramat, First Price-deklarasjon) | A er trolig uttrekksfeil. Bruk 0,7–1,0. |
| Findus Steketorsk, fett | 0 g (matvaretabellen) | 0,5 g (ingrediens.no) | Begge svært lave. Bruk 0,5 som konservativt. |
| Findus Fish & Crisp | 216 kcal / 11 g fett / 18 g karbo | 226 kcal / 14 g fett / 15 g karbo | Trolig Originalen vs. Gourmetfiléer. |
| Røkt laks, salt | 3,1 g/100 g | 1,0 g/100 g | Uavklart. Stor praktisk forskjell. |
| «Torsk naturell», salt | 0,1 g (Findus deklarasjon) | 1,6 g (karlsfiskogskalldyr generisk) | 1,6 g gjelder nesten sikkert lettsaltet torsk. Bruk 0,1 g for naturell. |
| Findus fiskepinner, fiskeandel | 61 % (stillehavslysing) | 65 % (Alaska pollock) | Findus bruker ulike arter i ulike varianter/batcher. Begge er reelle. |

---

## Kildeliste

- [Oda – Findus Fiskepinner MSC 750 g](https://oda.com/no/products/8906-findus-fiskepinner-msc/)
- [Oda – Findus Fiskepinner 450 g](https://oda.com/no/products/28088-findus-fiskepinner/)
- [Oda – Findus Fiskepinner Glutenfri 360 g](https://oda.com/no/products/19294-findus-fiskepinner-glutenfri/)
- [Oda – Norsk Sjømat Laksefilet Naturell u/skinn 500 g](https://oda.com/no/products/27246-norsk-sjomat-laksefilet-naturell-uten-skinn/)
- [Matinfo – Findus Torsk Naturell (GTIN 07042110073034)](https://produkter.matinfo.no/Findus-Norge-AS/Torsk-naturell/07042110073034)
- [Matinfo – Findus Fiskepinner Originalen 750 g](https://produkter.matinfo.no/Findus-Norge-AS/Fiskepinner-originalen-750g-30stk/07035110301818)
- [Matinfo – Findus Fiskepinner Glutenfri](https://produkter.matinfo.no/Findus-Norge-AS/Fiskepinner-glutenfri/07310500177878)
- [Matinfo – Findus Sprøbakte Fiskefileter](https://produkter.matinfo.no/Findus-Norge-AS/Spr%C3%B8bakte-fiskefileter/07310500173702)
- [Matinfo – Findus Fish & Crisp Gourmet](https://produkter.matinfo.no/Findus-Norge-AS/Fish-og-crisp-gourmet/07035119999276)
- [Matinfo – Fiskemannen Fiskekaker 80 % torsk & hyse](https://produkter.matinfo.no/Unil-AS/Fiskekaker-80pr-torskoghyse/07035620049101)
- [Matinfo – First Price Ørretfilet](https://produkter.matinfo.no/Unil-AS/%C3%98rretfilet/27035620045343)
- [Kassalapp – Findus Torskefilet Gourmet 420 g](https://kassal.app/vare/4800-torskefilet-gourmet-420g-findus-7310500113142)
- [Kassalapp – First Price Torskefilet Blokk 400 g](https://kassal.app/vare/4887-torskefilet-blokk-uskinnben-400g-msc-first-price-7035620017483)
- [Kassalapp – Coop Fra Havet Torskefilet Naturell 360 g](https://kassal.app/vare/25004-coop-fra-havet-torskefilet-naturell-360g-7025110145659)
- [Kassalapp – Coop Sprø Torsk Fullkorn 320 g](https://kassal.app/vare/25934-coop-spro-torsk-fullkorn-320g-7025110188625)
- [Kassalapp – Lerøy Torskefilet Pankopanert 350 g](https://kassal.app/vare/11721-torskefilet-pankopanert-350g-leroy-7033352352933)
- [Kassalapp – Findus Fiskegrateng Familiens 1 kg](https://kassal.app/vare/13534-fiskegrateng-familiens-1kg-findus-7310500098968)
- [Kassalapp – Findus Fiskegrateng Kystens 390 g](https://kassal.app/vare/6088-fiskegrateng-kystens-390g-findus-7310500142746)
- [Kassalapp – Lofoten Fiskeboller Hjemmelagde 350 g](https://kassal.app/vare/18552-fiskeboller-hjemmelagde-350g-lofoten-7023530141053)
- [Kassalapp – Fiskemannen Fiskekaker 80 % 500 g](https://kassal.app/vare/43692-fiskekaker-80-500g-fiskemannen-7035620049101)
- [Findus – Fiskepinner](https://www.findus.no/var-mat/fisk/fiskepinner/fiskepinner)
- [Findus – Våre beste fiskepinner](https://www.findus.no/var-mat/fisk/fiskepinner/vare-beste-fiskepinner)
- [Findus – Sprøbakte Crispies](https://www.findus.no/var-mat/fisk/panert-fisk/sprobakte-crispies)
- [Findus – Fish & Crisp](https://www.findus.no/var-mat/fisk/panert-fisk/fish-crisp)
- [Findus – Steketorsk / nøkkelhullsmerket panert fisk](https://www.findus.no/var-mat/fisk/panert-fisk/steketorsk)
- [Findus – Hvordan tilberede torsk og annen frossen fisk](https://www.findus.no/oppskrifter/tips-og-triks/hvordan-tilberede-torsk-og-annen-frossen-fisk)
- [Findus Foodservices – panert fisk, forstekt](https://www.findusfoodservices.no/produkter/fisk/panert-fisk-forstekt/sprobakt-fisk-med-rug-og-havre-125gr,-1x7kg-msc)
- [Lofoten – Hjemmelagde Fiskekaker](https://lofoten.no/produkt/hjemmelagde-fiskekaker-av-fersk-norsk-hysefilet)
- [Lofoten – Hjertekaker](https://lofoten.no/produkt/familiens-fiskekaker)
- [Fiskemannen – Fiskekaker 80 % 500 g](https://fiskemannen.no/varer/fiskekaker-7035620049101)
- [Fiskemannen – Fiskekaker 65 % 500 g](https://fiskemannen.no/varer/fiskekaker-7035620048074)
- [Fiskemannen – Er fiskekaker sunt?](https://fiskemannen.no/artikkel/er-fiskekaker-sunt/)
- [Lerøy – Sprøpanert torsk familiepakning 600 g](https://www.leroyseafood.com/no/smakfull-sjomat/produkter/frys---spropanert-torsk/)
- [Lerøy – Sprøpanert sei familiepakning 600 g](https://www.leroyseafood.com/no/smakfull-sjomat/produkter/frys---spropanert-sei/)
- [Lerøy – Torskefilet i blokk 400 g](https://www.leroyseafood.com/no/smakfull-sjomat/produkter/torsk-i-blokk/)
- [Lerøy – Ørretfilet naturell 2x125 g](https://www.leroyseafood.com/no/smakfull-sjomat/produkter/orretfilet-naturell/)
- [Lerøy – Laksefilet naturell 2x125 g](https://www.leroyseafood.com/no/smakfull-sjomat/produkter/laksefilet-naturell/)
- [Norway Seafoods – Sprø torsk](https://www.norwayseafoods.com/no/produkter/spro-torsk/)
- [Matvaretabellen – Torsk, panert, Findus Steketorsk](https://www.matvaretabellen.no/torsk-panert-findus-steketorsk/)
- [Matvaretabellen – Fiskekaker, Lofoten](https://www.matvaretabellen.no/fiskekaker-lofoten/)
- [Matvaretabellen – Laks, røkt](https://www.matvaretabellen.no/laks-rokt/)
- [Matvaretabellen – Laks, filet, gravet](https://www.matvaretabellen.no/laks-filet-gravet/)
- [Matvaretabellen – Makrell, varmrøkt](https://www.matvaretabellen.no/makrell-varmrokt/)
- [Bramat – tester panert fisk](https://www.bramat.no/kosthold/tester/1502-bramat-tester-panert-fisk)
- [Bramat – tester fiskepinner 2020](https://bramat.no/forsiden/tester/3356-bramat-tester-fiskepinner-2020?start=1)
- [Bramat – tester fiskekaker 2024](https://bramat.no/kosthold/tester/3910-bramat-tester-fiskekaker-2024?start=1)
- [Bramat – tester fiskegrateng 2024](https://bramat.no/kosthold/tester/3890-bramat-tester-fiskegrateng-2024?start=1)
- [KIWI – Er panert fisk usunt?](https://kiwi.no/fisk/er-panert-fisk-usunt)
- [KIWI – Er fiskepinner sunt? Ernæringsfysiologen svarer](https://kiwi.no/tema/middag/fisk-til-middag/lurer-du-pa-om-fiskepinner-er-sunt-ernaringsfysiologen-gir-deg-svaret)
- [Klikk/Nettavisen – Test av panert fisk: hvilken inneholder mest fisk?](https://www.nettavisen.no/klikk/test-av-panert-fisk/hvilken-inneholder-mest-fisk/s/12-95-3603371)
- [Klikk – Findus lettpanert torsk](https://www.klikk.no/foreldre/tester/test-av-panert-fisk-3392926)
- [Dagbladet – Stor test: dobbelt så mye fisk i vinnerne som i taperne](https://www.dagbladet.no/tema/stor-test-dobbelt-sa-mye-fisk-i-vinnerne-som-i-taperne/60741225)
- [MENY – Findus Fiskepinner 450 g](https://meny.no/varer/middag/fiskeretter/fiskepinner/fiskepinner-7035110121607)
- [MENY – Findus Fiskepinner 750 g](https://meny.no/varer/middag/fiskeretter/fiskepinner/fiskepinner-7035110400894)
- [MENY – First Price Fiskepinner 450 g](https://meny.no/varer/middag/fiskeretter/fiskepinner/fiskepinner-7035620057137)
- [MENY – First Price Seifilet Blokk 400 g](https://meny.no/varer/fisk-skalldyr/fisk/sei/seifilet-7035620068669)
- [MENY – Fiskemannen Fiskekaker 80 % 500 g](https://meny.no/varer/middag/fiskeretter/fiskekaker/fiskekaker-7035620049101)
- [MENY – Slik koker, steker og ovnsbaker du fisk](https://meny.no/tilbereding/koke-steke-ovnsbake-fisk)
- [Joker – Findus Sprøbakte Fiskefileter 500 g](https://joker.no/nettbutikk/varer/middag/fiskeretter/panert-fisk/fiskefileter-7310500173702)
- [Norges Online – Findus Torsk Naturell 400 g](https://norges.online/produkt/findus-torsk-naturell-400-g)
- [Ingrediens.no – Fiskekaker, Godehav](https://www.ingrediens.no/ingredienser/fiskekaker-godehav/)
- [Ingrediens.no – Fiskekaker, Lofoten](https://www.ingrediens.no/ingredienser/fiskekaker-lofoten/)
- [Ingrediens.no – Fiskeboller, kjølevare](https://www.ingrediens.no/ingredienser/fiskeboller-kjolevare/)
- [MyLog – Våre Beste Fiskepinner 100 % Fiskefilet](https://www.mylog.no/matvaretabell/29174)
- [MyLog – Fish & Crisp Originalen](https://www.mylog.no/matvaretabell/29224)
- [MyLog – Findus Laksefilét Naturell](https://www.mylog.no/matvaretabell/1264)
- [MyLog – Ørret Naturell](https://www.mylog.no/matvaretabell/25612)
- [Matoppskrift – First Price fiskepinner (utvidet)](https://www.matoppskrift.no/ingrediens-utvidet/first-price-fiskepinner)
- [Matoppskrift – Findus familiens fiskegrateng (utvidet)](https://www.matoppskrift.no/ingrediens-utvidet/findus-familiens-fiskegrateng)
- [Matoppskrift – Lofoten Hjemmelagde Fiskeboller](https://www.matoppskrift.no/ingrediens/lofoten-hjemmelagde-fiskeboller)
- [Bolga Fryseri – Fiskeboller](https://www.bolgafryseri.no/products/fiskeboller)
- [Allematpriser – Torskefilet i blokk, Kiwi-tilbud](https://allematpriser.no/tilbud/shopgun:product:b3efBQeu)
- [Godpris – Findus Fiskepinner 450 g prissammenligning](https://godpris.no/produkt/4354)
