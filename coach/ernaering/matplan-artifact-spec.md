# Matplan-artifact — designspesifikasjon

Skrevet 07.09.2026 av `ux`. **Dette er planen, ikke bygget.** En byggeagent
skal kunne lage artifacten fra dette dokumentet uten å gjette.

Grunnlag: `coach/ernaering/matplan.md` (menyene), `coach/ernaering/vektplan.md`
(§ 0, 0.75, 0.76, 3, 4, 6, 9), `coach/ernaering/mage.md`, `coach/profil.md`.

**Knuts bestilling, ordrett:** «en liste over retter man kan velge og sette opp
en ukeplan, slik at jeg treffer mine macroer, og handleliste jeg kan huke av på
når jeg er i butikken.»

---

## 1. Premisser designet står på

1. **Menyer, ikke retter.** Matplanen ble skrevet om til seks valg per luke
   fordi Knut går lei. Artifacten må gjøre *å bytte* like billig som *å følge*.
   Alt som gjør et valg permanent eller vanskelig å endre bryter premisset.
2. **Ukedagene er ulike.** Man/tor kvalitet, tir styrke, ons/lør hvile,
   fre langtur, søn rolig. Karbonivået følger dagen. Dagtypen er derfor en
   førsteklasses egenskap, ikke en etikett.
3. **Lunsjen er ukjent.** Kantina 10:40–11:10 kan ikke planlegges som rett.
   Ett av fem måltider er alltid en antakelse. Designet må vise det som en
   antakelse, ikke skjule det.
4. **Fasene skifter 28.09.** Måltallene flyttes, menyene står. Målene må ligge
   ett sted, adressert av (fase × dagtype).
5. **Ingen veiing.** Grunnlaget er håndflate, neve, beger og fritekst.
   Artifacten skal ikke være mer presis enn kilden. Se § 8.
6. **Mobil i butikk er en hovedmodus**, ikke en tilpasning.
7. **Ingen skyldmekanikk.** Vektplan § 9.6 flagger matfokus som styrer livet.
   Ingen streaks, poeng, «du bommet i går» eller kompensasjonslogikk.

---

## 2. Informasjonsarkitektur

Én side, **tre faner** i bunnlinja (tommelrekkevidde):

| Fane | Svarer på | Brukes |
|---|---|---|
| **Uka** (standard) | «Hva spiser jeg, og treffer jeg?» | Daglig, hjemme |
| **Meny** | «Hva kan jeg velge mellom?» | Ved planlegging og når han er lei |
| **Handleliste** | «Hva skal i vogna?» | Lørdag, i butikk |

Ingen fjerde fane for makro. Makro er en **stripe** i Uka som kan foldes ut.
Fire faner gjør ingen av dem tydeligere.

### 2.1 Uka — ovenfra og ned
1. **I dag-kort** (øverst, alltid). Dato, dagtype med farge («Torsdag —
   kvalitetsøkt»), og dagens fem-seks luker som en liste. Neste luke etter
   klokkeslett er uthevet. Dette er det han ser når han åpner appen kl. 14:03
   og lurer på hva som var planen.
2. **Makrostripe for i dag** — tre felt, se § 5. Trykk = utvid til ukesbilde.
3. **Ukestripe** — 7 kolonner, man→søn, hver med dagtype-forkortelse og én
   statusprikk. Trykk en dag → dagvisning.
4. **Dagvisning** — alle luker for den dagen, hver med valgt rett eller
   tom-tilstand. Dette er der uka settes opp.
5. **Velg-ark** — bunnark som glir opp med de seks alternativene for luka.

### 2.2 Meny
Ren lesevisning av matplanens menyer: Frokost (6), Kl. 14 (6), Middagsrammer
(6), Kveld (6), pluss faste elementer (15:30 loff+banan, restitusjon etter økt)
og prinsippkortene: § 0 fem regler, § 0c fett-rammen, § 7 kantinaregelen.
Hvert kort viser mengde i husholdningsmål og merkelapper: `treningsdag`,
`hviledag-ok`, `fredag-ok`, `raskest`.
Hjerte-ikon = favoritt. Favoritter sorteres først i velg-arket. Det er hele
personaliseringen — ikke mer.

### 2.3 Handleliste
Én liste for **den valgte handleuka**, gruppert på butikkavdeling. Se § 6.

---

## 3. Hovedflytene

### Flyt A — sette opp uka (lørdag formiddag, sofa, 5–8 min)
1. Åpner Uka → trykker **«Planlegg neste uke»** i ukestripa.
2. Ser sju dagkort. Hver dag har allerede: dagtype, klokkeslett, og kantina
   som låst prinsippkort. Ingen tomme skjemaer.
3. Trykker en tom luke, f.eks. «Torsdag 19:00 middag».
4. Bunnarket åpner med de seks middagsrammene. **Rammer som ikke passer dagen
   er ikke skjult — de er nedtonet med én linje grunn:** «Ramme 3 er merket
   hviledag — mye volum, lite karbo. Torsdag er karbodag.» Han kan velge den
   likevel. Vi rådgir, vi låser ikke.
5. Velger → arket lukkes → makrostripa og dagprikken oppdateres umiddelbart.
   Ingen «lagre»-knapp noe sted.
6. Gjentar. Snarveier som gjør dette raskt:
   - **«Kopier forrige uke»** — fyller alle luker fra sist. Hovedveien.
   - **«Gjenta hele uka»** på én rett (samme frokost man–fre).
   - **«Fyll resten med favoritter»** — merket som forslag, alt kan endres.
7. Når alle luker er fylt: en linje nederst — «Uka er satt opp. 34 varer på
   handlelista.» → knapp til Handleliste.

**Delvis utfylt er en gyldig tilstand.** Ingen blokkering, ingen prosentmåler
mot 100 %. Tomme luker vises som tomme, med unntak av kl. 14 (se § 5.3).

### Flyt B — sjekke at makroene treffer
Ikke en egen handling. Den skjer **inne i flyt A**, som umiddelbar respons:
stripa endrer seg mens han velger. Det er hele poenget — han skal se
konsekvensen av valget i valgøyeblikket, ikke etterpå i en rapport.

Egen inngang finnes likevel: trykk stripa → **ukesbilde**, sju rader
(én per dag) × tre kolonner (protein / karbo / fett). Én skjerm, ingen scroll.
Under den: én setning i klartekst om det som faktisk er galt, maks tre
setninger. Eksempel: «Torsdag ligger lavt på karbo. Det er en intervalldag —
bytt middag eller legg tilbake loff+banan kl. 15:30.»

### Flyt C — handle i butikken (lørdag, én hånd, handlekurv i den andre)
1. Åpner artifacten → trykker **Handleliste**. To trykk fra kald start.
   Lista er allerede den for uka han nettopp planla.
2. Ser: «0 av 34» øverst, så avdelingene i **gangrekkefølge** gjennom butikken.
3. Går gjennom Frukt & grønt. Trykker hvor som helst på raden «Bananer — 8 stk».
   Raden tones ned, får hake, glir ned til bunnen av sin avdeling. Telleren blir
   «1 av 34». **«Angre»** vises i 5 sekunder.
4. Når en avdeling er ferdig, kollapser den seg selv til én linje:
   «Frukt & grønt — 7 av 7 ✓». Han ser hvor han er.
5. Mangler noe → **«+ Legg til»** nederst, fritekst, havner i «Annet».
6. Ferdig: «34 av 34». Ingen feiring, ingen konfetti. Bare ferdig.

---

## 4. Datamodell

### 4.1 Hva som ligger hvor

| Innhold | Hvor | Hvorfor |
|---|---|---|
| Katalog (menyene, ingredienser, makroestimater) | **I sidekoden**, konstanter | Det *er* matplanen. Endres den, republiseres artifacten. |
| Måltall per fase × dagtype | **I sidekoden**, `MAAL[fase][dagtype]` | Se § 4.3 |
| Ukeplan (hans valg) | **`db`** | Må overleve at han planlegger på PC og handler på mobil |
| Handleliste + avhukinger | **`db`** | Samme — og han krysser av over 40 minutter i butikk |
| Favoritter | **`db`** | Skal ikke forsvinne når han bytter enhet |
| Aktiv fane, sist åpnet dag, kollapsede seksjoner | **`localStorage`** | Ren visningskomfort, per enhet |

**Ikke bruk `localStorage` til ukeplan eller handleliste.** Det er nettopp
overgangen sofa→butikk, PC→mobil, som gjør hele greia nyttig. `db` er
kravet, ikke en oppgradering.

Byggeagent: last `artifact-capabilities`-skillen og deklarer
`capabilities: {db: {}}`. `claude.use("db")` kan returnere `null` — da rendres
siden i lesemodus fra katalogen, med et synlig banner «Lagring utilgjengelig —
valg blir ikke husket». Ingen stille datatap.

### 4.2 Dokumenter

```
uker/{2026-W37}
  fase            "vedlikehold" | "underskudd"
  handledag       "2026-09-12"          // se åpent spm. 6
  dager: {
    man: { dato, dagtype, valg: { frokost:"F3", kl14:"M2", pre:"fast",
                                  etterOkt:"fast", middag:"D5", kveld:"K1" },
           notat: "" },
    ... tir–søn
  }

handlelister/{2026-W37}
  generertAt
  varer: [ { id, navn, avdeling, mengde:"8 stk",
             kilder:["F3","D5"], kryssetAv:false, manuell:false } ]

preferanser
  favoritter: ["F3","M2","D4","K6"]
```

Ukesnøkkel er ISO-uke. Ukene er uavhengige dokumenter — ingen migrering,
ingen arv. Avhukinger ligger på handlelista for *den* uka og nullstilles
aldri, fordi neste uke er et nytt dokument.

`db` er sist-skriver-vinner uten transaksjoner. Det er greit her: én bruker,
én enhet om gangen. Skriv hele varelinja, ikke deltaer.

### 4.3 Fasehåndtering — kravet fra § 0.3
```
FASER = [ {fra:"2026-09-08", til:"2026-09-27", id:"vedlikehold"},
          {fra:"2026-09-28", til:"2026-11-08", id:"underskudd"}, ... ]
MAAL[fase][dagtype] = { protein_g, karbonivaa, fettmarkorer_maks }
```
Siden slår opp fase fra dato. **Når målene flyttes 28.09 endres kun tabellen** —
ingen skjerm, ingen flyt, ingen komponent skal vite hvilken fase det er.
Sju dager før faseskifte: en linje i I dag-kortet, «Underskuddet starter mandag
28.09. Karbo halveres ons/lør, granolaen ut.» Én gang, ikke som varsel.

---

## 5. Makroregnskapet

**Regelen: tre felt, tre farger, null desimaler.** Han skal lese det på to
sekunder, stående, uten å regne.

### 5.1 Per dag, ikke per uke — med ukesbilde som andrenivå
Karbo følger økta *den dagen*. Et ukessnitt som treffer mens torsdag ligger
lavt er verdiløst, fordi det er torsdag som er intervalldagen. Så: **dagen er
enheten.** Uka finnes som oversikt, ikke som fasit.

### 5.2 De tre feltene

| Felt | Vises som | Hvorfor sånn |
|---|---|---|
| **Protein** | Ett tall + stolpe: `185 / 220 g` | Det eneste tallet i planen som er et tall (vektplan § 4). Fortjener presisjon. |
| **Karbo** | Bånd i tre trinn: **Lav · Middels · Høy**, med dagens krav markert | Grunnlaget er never og øser. Et gramtall her ville vært oppdiktet. |
| **Fett** | Teller mot tak: `2 av 3` fettmarkører | Matplan § 0c teller allerede i markører — avokado, nøtter, olje, ost. Vi bruker hans egen valuta. |

Fargebruk: grønn/gul/rød, **alltid med ord eller ikon i tillegg** — han leser
dette i dårlig lys, og farge alene er ikke tilgjengelig.

### 5.3 Hvilket avvik som faktisk betyr noe
Rødt er dyrt. Reserver det:

| Tilstand | Status | Tekst |
|---|---|---|
| Protein > 40 g under mål | **Rød** | «Mangler et proteinmåltid» |
| Protein 20–40 g under | Gul | «Litt lavt på protein» |
| Protein innenfor 20 g, eller over | Grønn | ingen tekst |
| Karbo ett trinn **for lavt** på man/tor/fre | **Rød** | «Kvalitetsøkt på for lite karbo» |
| Karbo ett trinn **for høyt** på ons/lør | Gul | «Lavdagen er ikke lav» |
| Karbo for høyt på treningsdag | Grønn | ikke et problem |
| Fett over tak | Gul | «Fett over dagens ramme» |
| **Fredag: fettmarkør etter kl. 11** | **Rød**, egen linje | «Ikke fett etter 11 i dag — magen» |
| **Kl. 14-luka tom, hvilken som helst dag** | **Rød** | «14-måltidet kuttes aldri» |
| Måltid uten proteinkilde | Gul prikk på luka | «Kan du peke på proteinet?» |

Alt annet er grønt. Ingen advarsel for ±10 %.

### 5.4 Kantina — måltidet som ikke kan planlegges
Lunsjluka er **ikke** et velg-ark. Den er et kort som viser tallerkenregelen
(§ 7 i matplanen) med dagens karboporsjon uthevet: «I dag: full karboporsjon.»
I makroregnskapet teller den som et **antatt estimat** fra ernæringsagenten,
merket med en stiplet kant og teksten «anslag». Han skal se at én femtedel av
regnskapet er en antakelse — ikke tro at siden vet noe den ikke vet.

Én valgfri knapp: **«Lunsjen var tynn»** → dagens proteinestimat justeres ned,
og kl. 14-luka får teksten «kompenser her». Ett trykk, ingen skjema.
*Dette er det eneste stedet en egenrapportering finnes. Krever godkjenning,
se åpent spørsmål 3.*

### 5.5 Hva jeg trenger fra `ernaering` — og i hvilken form
Jeg henter ikke tallene selv. Design bygges mot at disse leveres, som
maskinlesbare tabeller (markdown-tabell holder):

**Tabell 1 — måltall per fase × dagtype.** Rader: vedlikehold og underskudd ×
{kvalitet, styrke, hvile, langtur, rolig}. Kolonner:
`protein_g` (heltall), `karbonivaa` (lav/middels/høy), `fettmarkorer_maks`
(heltall). Ingen kcal.

**Tabell 2 — estimat per menyalternativ.** Én rad per alternativ i alle fire
menyer (F1–F6, M1–M6, D1–D6, K1–K6) pluss de faste (loff+banan 15:30,
restitusjonsdrikk, langtur-loffmåltid fredag 13:30). Kolonner:
`protein_g` (avrundet til nærmeste 5), `karbobidrag` (0 / lav / middels / høy),
`fettmarkorer` (0–3). **Avrundede anslag er riktig presisjonsnivå. Ikke send
desimaler.**

**Tabell 3 — kantina-anslag** per dagtype: samme tre kolonner. Ett tall, ikke
et spenn — spennet gjør det uleselig og øker ikke sannheten.

**Tabell 4 — ingredienser per menyalternativ**, for handlelista. Kolonner:
`vare`, `mengde`, `enhet` i husholdningsmål (stk, beger, dl, neve, pose, brød,
boks — gram kun der varen faktisk selges i gram), `avdeling`.
For middagsrammene, som er rammer og ikke oppskrifter: oppgi **standardvarene
rammen krever** (D4 fisk-dag → «fet fisk, 1 porsjon» + «poteter, 4–5» +
«grønnsaker, 1 pose»), ikke en full oppskrift.

Uten tabell 1–3 er § 5 ikke byggbar. Uten tabell 4 er § 6 ikke byggbar.
Bygg de andre skjermene i mellomtiden; katalogen er en konstant som fylles inn.

---

## 6. Handlelista

### 6.1 Aggregering
Lista **genereres fra valgene**, aldri fra en statisk liste.

1. Samle ingredienslinjer fra alle valgte alternativer i uka (tabell 4).
2. Summer per `vare` **når enheten er lik**. Ulike enheter listes side om side
   på samme rad: «Grønnsaker — 4 poser frossen + fersk til 5 middager».
   Ikke konverter mellom neve og gram. Det er oppdiktet presisjon.
3. **Rund opp til det man faktisk kjøper.** 9 egg → «1 brett (12)». 4,5 beger
   skyr → «5 beger». Alltid opp, aldri ned.
4. Legg til gruppa **«Fast lager — sjekk om du har»** fra matplan § 9: olivenolje,
   knekkebrød, tunfisk, linser, te, seigmenn, proteinpulver. Denne genereres
   ikke fra uka — den er en påminnelse, og den ligger nederst.
5. Behold matplanens innkjøpsregler som **låste linjer** der de finnes:
   granola = 1 liten pose (aldri kilospose), nøtter = små poser, egg = 2 brett.
   Disse er ikke beregnet, de er bestemt. Vis dem med et lite «regel»-merke.

### 6.2 Gruppering
Fast rekkefølge, valgt som gangrute gjennom en norsk dagligvarebutikk:

**Frukt & grønt → Brød & bakeri → Meieri → Kjøtt & fisk → Frys →
Tørrvarer & kolonial → Annet**

Ikke konfigurerbar. En innstilling han må stelle med er en innstilling han
ikke bruker.

### 6.3 Avhuking
- **Hele raden er trykkflaten.** Minst 56 px høy. Ingen liten avkrysningsboks.
- Avhuket: hake, nedtonet, gjennomstrøket navn, **glir til bunnen av sin
  avdeling** — den forsvinner ikke, for han kan trenge å se den igjen.
- **«Angre» i 5 sekunder** etter hvert trykk. Feiltrykk skjer med hanske på.
- Teller øverst, klebrig ved scroll: «12 av 34».
- Ferdig avdeling kollapser til én linje.
- Trykk og hold på en rad → «Hvorfor står denne her?» → viser hvilke retter
  varen kommer fra. Dette er svaret på «trenger jeg egentlig 5 beger kesam».

### 6.4 Neste uke
Ny uke = **nytt dokument, blank liste, ingen avhukinger arvet.** Vi bærer ikke
over «du kjøpte dette forrige uke», fordi vi ikke vet hva som ble spist opp,
og en feil antakelse her betyr tom kjøleskap på en onsdag.

Det eneste som følger med: **manuelt lagte varer merket «fast»** (f.eks. «kaffe»)
kommer tilbake hver uke. Én bryter på varen, ikke en egen skjerm.

Endrer han uka etter at handlelista er laget: lista oppdateres, og nye varer
markeres med en prikk i 24 timer, «ny siden du sist så på lista». Allerede
avhukede varer beholder haken.

---

## 7. Mobil i butikk — kravene

Dette er ikke responsive design. Det er en egen bruksmodus med egne krav.

- **Én hånd.** Alt han må trykke ligger i nederste to tredjedeler. Fanelinja i
  bunn. Ingen handling i toppen av skjermen.
- **Dårlig lys og glans.** Brødtekst minst 17 px, mengder 20 px halvfet.
  Kontrast minst 7:1 på tekst mot bakgrunn. Ingen grå tekst på hvitt for noe
  som skal leses. Følg temaet (lys/mørk) — butikker er lyse, kjølerommet ikke.
- **Halv oppmerksomhet.** Ingen modaler i handlemodus. Ingen dialog som må
  besvares. Trykk → resultat, alltid reversibelt.
- **Ingen posisjonstap.** Avhuking flytter aldri det han ser på; lista skal
  ikke hoppe. Klebrige avdelingsoverskrifter så han alltid vet hvor han er.
- **Tåler dårlig nett.** Rendre fra det som ligger lokalt i minnet, skriv til
  `db` i bakgrunnen. Aldri en spinner mellom trykk og hake.
- **Ingen scroll-jakt.** Kollapsede ferdige avdelinger holder lista kort.
  34 varer skal aldri bli 34 skjermhøyder.
- Ingen bilder. Ingen ikoner per vare. Tekst er raskere å lese enn en
  gulrotillustrasjon.

---

## 8. Hva vi IKKE skal bygge

Eksplisitt avvist. Byggeagenten skal ikke legge til noe av dette, uansett hvor
lett det er:

1. **Ingen kaloritelling per gram.** Ingen vekt, ingen «g»-felt for annet enn
   protein, ingen matvaredatabase, ingen strekkodeskanner. Grunnlaget er
   håndflate og neve. Å legge på desimaler *oppfinner* presisjon som ikke
   finnes, og gir Knut et tall han vil stole på og som er feil.
2. **Ingen kcal.** Ikke per rett, ikke per dag, ikke som «ca.». Vektplanen
   opererer aldri med kalorimål; det gjør ikke artifacten heller.
3. **Ingen etterlogging av hva han faktisk spiste.** Dette er en *plan*, ikke
   en dagbok. Unntaket er den ene «lunsjen var tynn»-knappen, § 5.4 — og den
   krever godkjenning.
4. **Ingen vektregistrering, ingen vektgraf.** Det bor i veieprotokollen
   (vektplan § 7) og i ukesrapporten. Vekt inn i matappen kobler mat til tall
   på badevekta daglig, som er nøyaktig det § 7 forbyr.
5. **Ingen streaks, poeng, prosent gjennomført, eller «du bommet»-historikk.**
   Vektplan § 9.6. En app som scorer spising er en app som lager skyld.
6. **Ingen oppskrifter med fremgangsmåte.** Han lager mat bedre enn oss
   (profil.md). Rammer og mengder, ikke steg.
7. **Ingen låsing.** Ingen valg skal være umulig. Vi tonet ned, vi sperret ikke.
8. **Ingen automatisk uke som standard.** «Kopier forrige uke» ja, «generer
   optimal uke» nei. Han velger — det var hele grunnen til at menyene ble laget.
9. **Ingen varsler eller push.** Fem klokkeslett i døgnet som piper er en app
   han sletter.
10. **Ingen langtursernæring under økt.** Det bor i `mage.md`, endres per test,
    og skal ikke kopieres inn her. Fredagskortet viser **gjeldende testtekst
    som sitat med kildehenvisning**, skrivebeskyttet.
11. **Ingen pris, budsjett eller butikkjede-integrasjon.**
12. **Ingen deling, innlogging eller flere brukere.**

---

## 9. Åpne spørsmål

| # | Spørsmål | Hvem svarer | Blokkerer |
|---|---|---|---|
| 1 | Makrotabell 1–3 i formen § 5.5 beskriver. Er `fettmarkorer` en modell ernæring vil stå for, eller foretrekkes noe annet? | `ernaering` | § 5 |
| 2 | Ingredienstabell 4, inkl. standardvarer per middagsramme | `ernaering` | § 6 |
| 3 | Skal «Lunsjen var tynn» finnes? Det er ett skritt mot egenrapportering, og profil.md advarer mot matfokus. Min anbefaling: ja, men bare denne ene, og aldri med historikk. | `ernaering` + `hovedcoach` | § 5.4 |
| 4 | Faseskifte 28.09 — automatisk på dato, eller manuell bryter Knut slår på? Anbefaling: automatisk, med varsling sju dager før. | `ernaering` | § 4.3 |
| 5 | Planlegger han uka på mobil eller PC? Avgjør hvor mye desktop-layout er verdt. | Knut | layout-innsats |
| 6 | **Handleuka.** Matplanen sier «én lørdagshandel». Handler han lørdag for uka som starter mandag etter? Da må Handleliste-fanen som standard vise *neste* uke fra torsdag og ut helga, ikke inneværende. Feil standard her koster ham en tur til butikken. | Knut | § 3 flyt C |
| 7 | Skal lista anta at ingenting finnes hjemme, eller skal han kunne krysse «har hjemme» så varen faller ut? Anbefaling: anta at alt må kjøpes, med «Fast lager»-gruppa som eneste sjekkliste. Enklere, og feiler på riktig side. | Knut | § 6.1 |
| 8 | Hvem oppdaterer fredagskortets sitat fra `mage.md` når testen endres? Anbefaling: `ernaering` republiserer artifacten. | `ernaering` | § 8 pkt. 10 |
| 9 | Hva skjer når matplanens menyer utvides (matplan § 9b lover det)? Katalogen ligger i sidekoden, så det betyr republisering. Er det greit, eller skal katalogen ligge i `db` så ernæringsagenten kan skrive til den? Anbefaling: sidekoden nå, `db` hvis det skjer oftere enn månedlig. | `ernaering` | nei |

---

## 10. Byggerekkefølge

1. Katalog + Meny-fanen. Byggbar i dag, uten tabellene.
2. Uka: dagvisning, velg-ark, `db`-lagring. Byggbar i dag.
3. Handleliste — venter på tabell 4.
4. Makrostripe og ukesbilde — venter på tabell 1–3.

Punkt 1 og 2 alene er allerede to av Knuts tre funksjoner.
