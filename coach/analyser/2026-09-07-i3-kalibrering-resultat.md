# I3-kalibrering 07.09.2026 — resultat og gyldighetsvurdering

Aktivitet: `20075072380` «Afternoon Run», Tønsberg, start 16:23 lokal.
Strømmer hentet i **full oppløsning** (1 Hz, 3377 punkter). Ingen `resolution`-parameter brukt.
GAP-modell: Minetti et al. (2002) energikostnad, som håndterer både stigning og fall.
Gradient beregnet på glattet høyde (±8 s) over 20 m distansevindu.

## Kort konklusjon

Han traff **ikke** pulsvinduet. 28,7 % av tempoblokka lå i 156–165; 66,3 % lå over.
Økta ble en I4-terskeløkt, ikke en I3-kalibrering. Den er likevel **gyldig som
terskelpunkt** — ruta er den flateste vi har målt, og tallet står.

**20 min på GAP 5:54,0/km ved snittpuls 165,0, puls stigende 160 → 171.**

## Struktur (fra rundene)

| Runde | Innhold | Tid | Distanse | Snittpuls | Kadens |
|---|---|---|---|---|---|
| 1–2 | Oppvarming 2 km | 13:35 | 1997 m | 136 → 145 | 155–157 spm |
| 3 | Gåpause | 5:24 | 397 m | 104 | 86 spm |
| 4–7 | **Tempoblokk** | **20:02** | **3378 m** | **165,0** | **161 spm** |
| 8 | Gange | 10:51 | 1001 m | 127 | 97 spm |
| 9 | Nedjogg | 6:19 | 869 m | 148 | 154 spm |

Avvik fra protokollen: logget som **én** aktivitet med navn «Afternoon Run», ikke to
med testen døpt «I3-kalibrering 20 min». Ingen beskrivelse, ingen `perceived_exertion`.
Nedvarmingen ble 10,9 min gange + 870 m jogg, ikke 2 km jogg.

## 1. Ruteprofil — gyldighetskriteriet, målt

Tempoblokka:
- **hm/km: 4,65** (integrert stigning på glattet høydestrøm). Stravas rundesum gir 2,8 hm/km.
  Begge under protokollens krav på 5 hm/km.
- Høyde i blokka varierer mellom **55,8 og 58,5 m** — 2,7 m total relieff over 3,4 km.
- Lengste sammenhengende stigning over 2 %: **ingen over 50 m.** Kravet var «ingen over 200 m».
- **GAP-korreksjon: +1,8 s/km.** Rå 5:55,8/km → GAP 5:54,0/km.

Kriterium 6 er innfridd med god margin. Dette er det første virkelig flate
måledatapunktet i materialet, og GAP-korreksjonen er så liten at rå og justert
fart er praktisk talt samme tall.

Til sammenligning, samme metode: 04.09 langtur 15,3 hm/km, 27.08 9,9 hm/km,
03.09 11,0 hm/km, 31.08 6,6 hm/km.

## 2. Traff han pulsvinduet 156–165?

Nei. Av 1202 sekunder:

| | Sekunder | Andel |
|---|---|---|
| Under 156 | 60 | 5,0 % |
| **I vinduet 156–165** | **345** | **28,7 %** |
| Over 165 | 798 | 66,3 % |

- Nådde 156 etter 60 s, passerte 165 etter 112 s.
- Siste sekund på eller under 165 kom 941 s inn i blokka — resten lå over.
- Snittpuls 165,0, maks 175.

Pulsen **drev oppover gjennom hele blokka og stabiliserte seg aldri**:

| Minutt | Puls | GAP | Kadens |
|---|---|---|---|
| 0–2 | 148,4 | 5:30,3 | 158 spm |
| 2–4 | 164,2 | 5:55,8 | 162 spm |
| 4–6 | 165,9 | 5:41,7 | 161 spm |
| 6–8 | 164,0 | 6:02,6 | 161 spm |
| 8–10 | 166,0 | 5:52,0 | 161 spm |
| 10–12 | 166,5 | 5:54,2 | 161 spm |
| 12–14 | 167,9 | 5:56,3 | 160 spm |
| 14–16 | 168,3 | 6:05,9 | 159 spm |
| 16–18 | 167,8 | 6:09,7 | 161 spm |
| 18–20 | 171,2 | 5:51,7 | 162 spm |

Farten var 10–15 s/km for høy for vinduet. Skal han sitte i 156–165 i 20 min,
er inngangsfarten omtrent **6:10/km GAP på flatt**, ikke 5:50.

### Sonetolkning — vær presis om modell
OLT-soner (HRmax 190, `2026-09-03-sonetabell-hrmax190.md`): I3 = 156–165, I4 = 166–175.
Snittpuls 165,0 ligger **på grensen I3/I4**, og siste halvdel (168,5 i snitt) ligger
klart i **I4**. I Strava-profilens egen modell (`MaxHeartRate`, sone 3 = 155–169)
ville hele blokka framstått som «sone 3». Det er to ulike modeller — økta var i
praksis en I4-terskeløkt etter OLT.

## 3. Pa:HR-decoupling gjennom temposteget

To tall, fordi valget av startpunkt betyr mye på en så kort blokk:

| Beregning | 1. halvdel | 2. halvdel | Pa:HR |
|---|---|---|---|
| Hele blokka (inkl. pulsopptrekk fra 106) | EF 0,01776 (puls 161,7 / GAP 5:48,2) | EF 0,01650 (puls 168,4 / GAP 6:00,0) | **7,1 %** |
| Uten de første 2 min (opptrekk fjernet) | EF 0,01715 (puls 165,3 / GAP 5:52,8) | EF 0,01644 (puls 168,5 / GAP 6:01,1) | **4,2 %** |

Det reelle tallet er **4,2 %**. De 7,1 % er en artefakt av at han startet blokka
på puls 106 rett etter 5,4 min gåpause, slik at første halvdel får kunstig lav snittpuls.

**Men tallet skal ikke scores mot 5/10 %-tersklene.** Pa:HR-grensene i instruksen
gjelder aerobe økter over 60 min. 4,2 % drift på **18 minutter** ved terskel er noe
helt annet enn 4,2 % på en to-timers langtur — det er mye drift på kort tid.
Drivkraften er entydig: puls +3,3 slag samtidig som farten falt 8,3 s/km GAP.

Tolkning: han lå **på eller like over MLSS**. En puls som klatrer monotont i 20 min
uten å finne et platå er signaturen på en intensitet over det som kan holdes.

## 4. Kadens

**Helt flat gjennom hele tempoblokka: 161 spm i første halvdel, 161 spm i andre.**
(Strava rapporterer 80,3 per bein.) Ingen fall mot slutten, ingen tegn til
muskulær tretthet. Steglengden krympet — 2,7 % lavere fart ved uendret kadens.

Dette er et positivt funn: **begrensningen var sirkulatorisk, ikke mekanisk.**
Beina holdt. Det er motoren som satte taket.

Ingen gåpauser i blokka: 2 sekunder uten bevegelse, 6 sekunder med kadens under 70.
Farten er ekte løping hele veien — i motsetning til 04.09, som var et snitt av løping og gange.

## 5. Sammenligning mot terskelankeret 01.08

Eneste sammenligning i materialet som er faglig forsvarlig: begge er flate,
begge er 20+ min sammenhengende arbeid nær terskel, begge er behandlet med
samme GAP-modell på full oppløsning.

| | 07.09 tempoblokk | 01.08 parkrun 5 km |
|---|---|---|
| Varighet | 20:02 | 30:01 |
| Distanse | 3378 m | 5131 m |
| **hm/km** | **4,65** | **8,56** |
| Rå fart | 5:55,8/km | 5:51,0/km |
| **GAP** | **5:54,0/km** | **5:49,1/km** |
| **GAP-korreksjon** | **+1,8 s/km** | **+1,9 s/km** |
| Snittpuls | 165,0 | 164,5 |
| Makspuls | 175 | 184 |
| Kadens | 161 spm | 160 spm |
| EF | 0,01712 | 0,01741 |

**Differanse: +5,0 s/km GAP (+4,8 s/km rå) ved praktisk talt identisk snittpuls.**
GAP-korreksjonene ligger 0,1 s/km fra hverandre — godt innenfor 5 s/km-grensen,
så rå- og GAP-differansen forteller det samme.

Forbehold som gjør at dette **ikke** skal leses som formtap:
- 01.08 var et maksimalt 5 km-løp med sluttspurt til puls 184. 07.09 var en
  kontrollert 20 min som toppet på 175. Ikke samme innsatsprofil.
- 01.08 startet uthvilt om morgenen. 07.09 kom etter 2 km oppvarming i 6:41–6:55/km
  og en gåpause, på slutten av en dag med fysiotime.
- Fem uker mellom dem, og bare to sammenlignbare punkter.

Konklusjonen er derfor: **terskelen er uendret siden begynnelsen av august.**
5 s/km på to punkter med ulik innsatsprofil er ikke en retning.

## 6. Hva sier dette om terskelen?

Anslaget i `2026-09-03-sonetabell-hrmax190.md` var anaerob terskel puls 170 ± 3,
terskelfart 6:20–6:30/km. Dagens økt **bekrefter det og strammer det inn**:

- Ved GAP 5:54/km klatret pulsen monotont fra 160 til 171 på 20 min. Den farten
  ligger altså **over** MLSS.
- Terskelfart (60 min holdbar) anslås til **6:10–6:25/km GAP på flatt**, ved puls **168–171**.
- I3-vinduet 156–165 svarer til ca. **6:05–6:20/km GAP på flatt**. Dette er første
  gang I3-paceraden hviler på måling og ikke på interpolasjon — men kun ett punkt.

Bonusfunn fra oppvarmingen: runde 2 gikk på **GAP 6:45,3/km ved snittpuls 145,0**
(8,7 hm/km, GAP-korreksjon −3,9 s/km). Sonetabellen setter I2 (137–156) til
7:10–8:10/km. Han lå 25+ s/km raskere enn tabellens midtsjikt. Det støtter
forbeholdet som ble ført inn 04.09: **I1- og I2-pacene er for konservative.**
Merk at pulsen steg gjennom runden (136 → 152), så snittet underdriver — behandle
funnet som [foreløpig], ikke som en tabellrevisjon.

## 7. Hva betyr det for maratonmålet?

Mål 7:05–7:15/km. Nåværende arbeidstempo 7:35–7:50/km.

Med terskel på 6:10–6:25/km ligger maratonmålet **40–65 s/km saktere enn terskel**.
Det er nøyaktig der maratontempo skal ligge for en utøver på hans nivå.

**Aerob kapasitet er ikke det som begrenser 7:05–7:15/km. Målet er forsvart av
dagens måling.** Han har farten. Gapet mellom 7:35–7:50 og 7:05–7:15 er ikke et
terskelproblem.

Det som begrenser er **holdbarhet**: 4,2 % decoupling på 18 minutter, og en puls
som ikke fant platå. Det som skal bygges er evnen til å holde en lav intensitet
lenge — volum i I1/I2 — ikke raskere terskel. Terskelen er allerede god nok til
målet; den må bare bli billigere å bære.

## 8. Er dette en gyldig formmåling?

**Som terskelpunkt: ja.**
- Ruta er flat og målt: 4,65 hm/km, GAP-korreksjon +1,8 s/km.
- 20 min sammenhengende løping, ingen gåpauser, stabil kadens.
- Pulsstrømmen er sammenhengende og uten dropouts.

**Som EF-punkt: nei.** EF-regelen krever I1–I2 og over 40 min. Dette var I3/I4 i
20 min. Det endrer ikke EF-trenden, som fortsatt står på for tynt grunnlag.

**Som I3-kalibrering: nei.** Formålet var å feste farten ved puls 156–165. Han lå
i vinduet i 28,7 % av tiden. Vi har fått et I4-punkt i stedet — verdifullt, men
ikke det som ble bestilt. **I3-kalibreringen bør gjentas**, med instruks om å
starte på 6:10/km og la pulsen komme opp til vinduet, ikke starte på følelse.

**To ting er ikke i dataen og må spørres om:**
- **Solo eller gruppe?** Kriterium 9. Ingen beskrivelse på aktiviteten.
- **Underlag og temperatur.** `temp`-strømmen mangler i Strava for denne økta,
  så kriterium 4 (under 20 grader) og 5 (tørt, asfalt/grus) kan ikke verifiseres.
- Hva fysio sa, siden økta lå etter timen.

RPE kommer på kveldsspørsmålet og skal ikke spørres om her.

## Leveranse

1. **Retning:** For tidlig å si noe om retning. Ett terskelpunkt mot ett fra 01.08
   gir +5,0 s/km GAP ved samme puls (165,0 mot 164,5) — innenfor det ulik
   innsatsprofil alene kan forklare. Terskelen står stille, den faller ikke.
2. **Grunnlaget:** To økter, 01.08 og 07.09, fem uker fra hverandre. Begge flate
   (8,56 og 4,65 hm/km), begge GAP-behandlet på full oppløsning.
3. **Konfidens:** **[for tidlig]** for retning. **[foreløpig]** for nivåanslaget
   terskel 6:10–6:25/km ved puls 168–171.
4. **Flagg:**
   - **Ikke et avvik.** Pulsen på 165–171 ved 5:54/km er som forventet for
     intensiteten. Ingenting i dagsformtallene (nattpuls 46, HRV 77, hudtemp −0,2)
     motsies av økta.
   - **Utførelsesavvik:** vinduet 156–165 ble truffet 28,7 % av tiden. Øktas
     bestilte formål ble ikke oppfylt.
   - **Til oppfølging:** I1/I2-pacene i sonetabellen ser for konservative ut
     (GAP 6:45/km ved puls 145 i oppvarmingen). Bør festes på en flat 40+ min I2-økt.

---

# TILLEGG 07.09 — korreksjon etter innspill fra Knut

Knut kjente seg ikke igjen i punkt 2. Han oppga samtidig en opplysning jeg ikke
hadde da jeg regnet: **han hadde ikke med seg brystbeltet.** Pulsen er optisk
målt på håndleddet. Begge deler er sjekket mot dataen under.

## A. Han har rett. Overskriften min var misvisende

«66,3 % over 165» er aritmetisk riktig og retorisk feil. Fordelingen:

| Puls | Sekunder | Andel |
|---|---|---|
| ≤155 | 60 | 5,0 % |
| **156–165 (i vinduet)** | **345** | **28,7 %** |
| 166–167 | 316 | 26,3 % |
| 168–169 | 341 | 28,3 % |
| 170–171 | 77 | 6,4 % |
| 172–173 | 33 | 2,7 % |
| 174–175 | 31 | 2,6 % |

- **Median puls i blokka: 166.** Ett slag over vinduet.
- **59,9 % lå på eller under 167. 83,8 % lå på eller under 168.**
- Bare **5,7 %** lå over 170, og **2,6 %** nådde 174–175.

Og det avgjørende: **all puls over 170 lå i én eneste sammenhengende periode på
69 sekunder, som startet 18,9 minutter inn i blokka.** Altså helt på slutten.

Minutt 0–15: snitt 163,7, median 166, maks 170.
Siste 5 min: snitt 169,1, median 168, maks 175.

**Knuts beskrivelse — «156 til 165–167-ish, og 175 helt på slutten» — er en
presis gjengivelse av det som faktisk skjedde.** Min var det ikke.

## B. Hvorfor klokka og jeg viste ulikt

Klokka viser et glattet øyeblikkstall; jeg regnet på hvert sekund.
Med 10 s glatting (omtrent det klokka viser) blir bildet nesten identisk med hans:
toppen framstår som 174, og bare 21,3 % av tiden ligger over 168.

I tillegg: han fulgte tallet i sanntid og husker der han **korrigerte**.
Snittet mitt teller også sekundene mellom korrigeringene.

Merk også at pulsen lå på 156–165 ved snittgradient **−0,14 %** og på 170+ ved
**+0,23 %**, maks +2,33 %. Bakkeeffekten han beskriver finnes i dataen, men
er liten — ruta er for flat til at bakkene forklarer stort.

## C. Brystbelte manglet — hva dataen viser

Sjekket eksplisitt for de kjente optiske feilmodusene:

| Test | Funn | Vurdering |
|---|---|---|
| **Kadenslåsing** | \|puls − spm\| i snitt 7,2 slag; bare 21,9 % innenfor 3 slag; korrelasjon puls~kadens **r = +0,37** | **Utelukket.** Ved kadenslåsing ville pulsen klistret seg til 161. Den gjør den ikke. |
| **Dropouts / nullverdier** | Ingen nuller, ingen hull i 3377 punkter | Ingen |
| **Plutselige hopp** | Maks endring 5 slag/s i blokka, 6 slag/s i hele økta; null endringer ≥8 | Ingen hoppartefakter |
| **Fysiologisk respons** | Opptrekk 106 → 155 på 60 s ved start, jevn nedgang 172 → 155 på 30 s etter blokka | Ser ekte ut |
| **Trappetrinn / kvantisering** | 26 sekvenser ≥10 s med identisk verdi, lengste 39 s (på 168, 12,3 min inn) | **Mildt tegn på optisk glatting.** Ikke diskvalifiserende, men det er der. |

**Konklusjon: dataen viser ingen grov optisk feil.** Kurveformen er troverdig.

Men — og dette er poenget — optisk måling kan ligge **systematisk noen slag feil**
uten å etterlate et eneste synlig artefakt i strømmen. Det kan jeg ikke utelukke
fra dataen. Absoluttnivået bærer derfor en usikkerhet på anslagsvis **±3–5 slag**
som jeg ikke kan måle bort.

## D. Hva som står, og hva som nå er usikkert

**Står uendret — måles av GPS og høydestrøm, ikke av pulsmåleren:**
- 20 min, 3378 m, **GAP 5:54,0/km**, rå 5:55,8/km.
- **4,65 hm/km**, **GAP-korreksjon +1,8 s/km**.
- Kadens 161 spm, helt flat gjennom begge halvdeler.
- Fartsfallet på 8,3 s/km GAP fra første til andre halvdel.
- Sammenligningen mot 01.08 på **fart**: +5,0 s/km GAP.

**Står, men av en annen grunn enn jeg først skrev:**
Konklusjonen «på eller like over MLSS» hvilte på at pulsen klatret monotont.
Den hviler nå like mye på at **farten falt 8,3 s/km ved uendret kadens** — et
GPS-målt forhold som er helt uavhengig av pulsbeltet. Konklusjonen overlever
selv om pulstallene skulle være noen slag feil.

**Blir mer usikkert:**
- **Terskelanslaget «puls 168–171»** hviler direkte på absolutt puls fra optisk
  måler. Nedgrader til **[foreløpig, usikker absoluttverdi]**.
- **Snittpuls 165,0** og dermed sammenligningen «samme puls som 01.08» — 01.08 er
  fra en annen dag og muligens en annen målemetode. Differansen på +5,0 s/km GAP
  skal leses med det forbeholdet.
- **Fartsanslaget 6:10–6:25/km for terskel står bedre enn pulsanslaget**, fordi
  det er forankret i GPS.

## E. Krav framover — brystbelte

Foreslås lagt inn som **kriterium 12** i gyldighetsprotokollen:

> **12. Brystbelte på alle kalibrerings- og terskeløkter.** Optisk håndleddsmåling
> godtas for I1/I2-økter, men ikke som grunnlag for å feste en sonegrense eller et
> terskelanslag. Mangler brystbelte, er økta gyldig som treningsøkt og som
> **fart**-punkt, men pulstallene skal merkes med usikkerhet og ikke brukes til
> å revidere sonetabellen.

Begrunnelse: hele poenget med en kalibreringsøkt er å knytte en fart til en puls.
Er pulsen usikker, er koblingen usikker — selv når farten er perfekt målt.

## F. Revidert leveranse

1. **Retning:** Uendret — for tidlig å si. Terskelen står stille.
2. **Utførelse — revidert:** Han lå **nærmere målet enn jeg først formidlet**.
   Median 166, ett slag over vinduet; 84 % av tiden på eller under 168; all puls
   over 170 lå i de siste 69 sekundene. Dette er en akseptabelt utført økt med et
   for hardt sluttdrag, ikke en bommet økt.
3. **Konfidens:** fart/GAP **[foreløpig]**. Absolutt puls og terskelanslag
   **[for tidlig]** inntil en økt med brystbelte foreligger.
4. **Flagg:** Brystbelte manglet. Ingen grov målefeil påvist, men absoluttnivået
   kan ikke verifiseres. Kadenslåsing eksplisitt utelukket (r = +0,37).
