# Stående instrukser

**Les `coach/fakta.md` først.** Den inneholder alt som er avklart om Knut,
tidssone, treningstidspunkt og hvilke data som kommer automatisk. Spør du om
noe som står der, er det en feil og den føres i `coach/laering.md`.


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
- [2026-09-03] **Uka starter på mandag.** Søndagsøkta hører til slutten av
  uka, ikke starten. Første søndag (13.09) tilhører uke 2, ikke uke 3.
  Gjelder all planlegging og alle rapporter.
- [2026-09-04] **Fart sammenlignes aldri uten stigningsjustering.** Ethvert
  s/km-tall mellom to økter skal være GAP-justert eller fra samme rute, og
  hm/km skal oppgis for begge. Gjelder også kveldsspørsmål og ukestatus, ikke
  bare analyser. Full regel i `coach/fakta.md`, «Fart-sammenligninger».
- [2026-09-04] **Høydeprofil er utledbart — Knut skal aldri bes om den.**
  Å be ham anslå hm/km, eller å la et gyldighetskriterium hvile på anslaget
  hans, er en feil. «Velg en flat rute» er fortsatt en gyldig instruks før
  økta; gyldigheten avgjøres på måledataen etterpå.
- [2026-09-03] Langturen står på 16–18 km til langturandelen er under 40 %
  av ukesvolumet.

## Åpne punkter

- **HRmax ikke verifisert.** Høyeste målte i år: 187 (25. juli). Sonetabellen
  forutsetter ~207. Krever ekte makstest før sonene justeres.
- **Banedata mangler:** høydeprofil/GPX for 5 km-runden i Holmestrand,
  plassering av de 3 drikkestasjonene, hvor de siste 2,195 km legges.
- Maks tid i løpet er **6 timer** — reell begrensning.

## Flaggterskler — søvn og restitusjon

**Korrigert 07.09.26 av `belastning-restitusjon`.** Den forrige tabellen sto på
CSV-ens *Resting Heart Rate* (baseline 43,46 · SD 1,48 · spenn 41–47 på 28
netter). Tallene Knut ser daglig i appen er *avg overnight HR* — et snitt, ikke
et minimum, og systematisk **+4,4 bpm** høyere. Å lese den gamle tabellen på
skjermtallet ga falske flagg: gulvet hans er 46, så «to netter under 46» kunne
aldri innfris. Samme feil lå i HRV-raden, motsatt vei.

**Tabellen under gjelder metrikken vi faktisk får inn daglig: avg overnight HR
og nattlig HRV.**

| Signal | Terskel | Handling |
|---|---|---|
| Nattpuls, én natt | ≥ 51 | Rolig I1, maks 45 min |
| Nattpuls, to netter på rad | ≥ 49 | Ingen hard økt eller langtur på 48 t |
| Nattpuls | ≥ 7-dagerssnitt + 3 | Som én-natt-flagget. **Står permanent** — robust hvis metrikken byttes igjen |
| HRV, én natt | ≤ 67 | Ingen hard økt i dag |
| HRV | < 62 | Deload uka |
| Varighet | < 6t30 | Flytt dagens harde økt |
| Varighet | **< 7t to netter før langtur** | **Økta flyttes. Ingen unntak.** |
| Body Battery | < 45 / < 40 | Rolig / fri |
| Hudtemp ≥ +0,5° + nattpuls ≥ 49 | — | Infeksjonsmistanke, ingenting over I2 |
| Sleep Score | < 60 | Fri fra løping |

Testet mot uke 36 flagger tabellen **lørdag 05.09 (nattpuls 52, HRV 65)** og
ingenting annet. Det er riktig: lørdag var konfirmasjonsdagen.

**Forbehold:** n=7 for nattpulsmetrikken, ingen parede netter mot CSV-en.
Tersklene skal reberegnes på en 28-dagers eksport av den daglige metrikken.

**Ved sammenligning av pulstall: oppgi alltid hvilken metrikk tallet er fra.**
Et hvilepulstall uten metrikkangivelse er ubrukelig og skal avvises.

Bakgrunn: 18-kilometeren 27.08 fikk 7,2 % HR-drift og kadensfall 77,7 → 64,5.
Nettene før var 6t18 og 6t58 med periodetopp i puls og periodebunn i HRV.
Økta var ikke for lang — han var for dårlig uthvilt.

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

## Kneet — avklart inntil videre 07.09.26

Fysio 07.09: ingen strukturell skade, ingen restriksjoner, ingen øvelser,
ingen belastningsbegrensning. «Vev som sa ifra at det hadde blitt godt brukt.»
Beskjed: fortsett som før, ta kontakt igjen hvis det blir verre.

**Status: avklart inntil videre — ikke lukket.** Det er ingen betingelse i
planleggingen lenger, og ingen agent skal bremse volum eller styrkelast på
grunn av kneet. Men symptomet er ikke borte, bare forklart, og det følges.

**«Verre» — konkrete kriterier. Ett av disse = si ifra samme dag:**
1. Oppstartsstivheten varer **over 60 sekunder** (dagens: 10–20 s).
2. Ubehag melder seg **før 15 km** i en langtur, eller i en økt under 10 km.
3. **Hevelse**, varme, eller at kneet ser annerledes ut enn det andre.
4. Smerte **i ro**, om natta, eller når du reiser deg fra stol.
5. Låsing, svikt, eller at du **endrer gangen** for å slippe unna.
6. Ubehag som **fortsatt er der dagen etter** en økt.

Punkt 3–5 er stopp umiddelbart, ikke «si ifra». De sto som røde flagg før
og står uendret — fysios klarering endrer dem ikke.

**Hypotesen står fortsatt.** `belastning-restitusjon` mener stivheten fra
15–16 km kommer av at knedominert styrke stoppet 28.12.2025 mens løpevolumet
ble bygget. «Ikke farlig» avkrefter ikke det — det sier bare at det ikke er en
skade. Knedominert styrke skal derfor **holdes ved like og progrederes**, ikke
fryses. Merk at legday 01.09 inneholdt belt squat 4×10 @100 kg og bulgarians
3×10 @20 kg — knedominert arbeid er altså gjenopptatt. Progresjonen skal
dokumenteres, ikke antas.

## Arbeidsdeling — hva Knut logger og hva agentene henter selv

Knut skal **aldri** bes om å notere noe som finnes i Strava. Det er dovent og
det blir ikke gjort. Alt under «hentes automatisk» er tilgjengelig via
Strava-MCP (`list_activities`, `get_activity_streams`, `get_activity_performance`).

**Hentes automatisk — ikke spør om det:**
distanse · tid · fart per km · GAP · snitt- og makspuls · pulskurve gjennom
økta · kadens · høydemeter · temperatur (ofte) · relative effort · splitter ·
og alt annet klokka registrerer.

**Fra Garmin-CSV (`coach/soevn/`), lastes opp ca. hver fjerde uke:**
søvnvarighet · sleep score · hvilepuls · HRV · Body Battery · hudtemperatur ·
leggetid og våknetid.

**Det Knut faktisk må gi oss — fordi det ikke finnes noe annet sted:**
1. **RPE 1–10.** Legges i Stravas eget «perceived exertion»-felt på økta.
   Da hentes den automatisk etterpå.
2. **Smerte:** sted, 0–10, og om det ble bedre eller verre underveis.
3. **Mage og næring** på langturer: én linje fritekst.
4. **Kontekst klokka ikke ser:** var det gruppeøkt eller solo, blåste det,
   var det glatt, sov du dårlig, var du stresset.

Punkt 4 er ofte det som avgjør om et avvik i dataen betyr noe eller ingenting.

## Arbeidsform — teamet skal svare, ikke hovedsamtalen

- [2026-09-04] Knut har bygget dette teamet for at **agentene** skal stille
  kartleggingsspørsmålene og gi svarene. Hovedsamtalen skal **ikke** svare
  faglig på hans vegne.

**Regel:** ethvert faglig spørsmål — trening, ernæring, belastning, pacing,
smerte, vekt — går til rett agent. Hovedsamtalen henter inn, formidler svaret
og fører ting til fil. Den er budbringer og redaktør, ikke coach.

Dette gjelder også små spørsmål. «Kan jeg ta en brødskive» er et
ernæringsspørsmål. At det er kort gjør det ikke til hovedsamtalens bord.

**Unntak, og bare disse:**
- Rene faktaoppslag i data som allerede ligger på bordet.
- Spørsmål om hvordan systemet fungerer — filer, agenter, planen som dokument.
- Hastesituasjoner der et svar må komme før en agent rekker å svare, og da
  skal det sies eksplisitt at det er hovedsamtalen som svarer.

**Kveldsspørsmålet er `hovedcoach` sitt.** Hovedsamtalen skal ikke finne på
spørsmål på egen hånd.

### Delegeringsregelen — etterprøvbar form [2026-09-05]

Regelen over ble brutt to ganger samme dag etter at den ble skrevet. Grunnen er
at hovedsamtalen delegerte **og** skrev sitt eget faglige svar i samme melding.
Knut leser hovedsamtalens versjon først; agentsvaret blir et etterslep.

**Regel 1 — én melding, én funksjon.** En melding fra hovedsamtalen som
delegerer skal inneholde nøyaktig tre ting og ingenting mer:
1. hva som er sendt videre,
2. til hvilken agent,
3. at svaret kommer.

**Forbudt i samme melding som en delegering:** anbefalinger, vurderinger,
mulige årsaker, symptomtolkning, tidsvurderinger («seks uker er lenge»),
forslag om tiltak, forbehold om hva agenten trolig vil si, og «i mellomtiden»
/ «mens du venter»-avsnitt. Har du skrevet en delegering, er meldingen ferdig.

**Regel 2 — ingen påplussing etter et agentsvar.** Når et agentsvar er
formidlet, er hovedsamtalens rolle over. «Én ting til», «for øvrig», «verdt å
nevne» og lignende tillegg med faglig innhold er forbudt. Har hovedsamtalen et
poeng agenten ikke dekket, sendes det til agenten — ikke til Knut.

**Regel 3 — hastesituasjoner må navngis.** Skal hovedsamtalen svare faglig,
skal meldingen begynne med: «Dette er hovedsamtalen som svarer, ikke en agent,
fordi …». Uten den setningen er faglig innhold fra hovedsamtalen et brudd.

**Etterprøving:** enhver melding fra hovedsamtalen som både nevner en agent og
inneholder en faglig påstand er et brudd — uansett om påstanden er riktig.
Riktighet er ikke et forsvar. `kvalitetskontroll` fører det i
`coach/laering.md`.

## Kvalitetskontroll

`kvalitetskontroll` fanger opp feil, gjentatte spørsmål og gale antagelser, og
skriver rettelsene inn i `coach/fakta.md`, `coach/instrukser.md` eller direkte
i agentfilene. Historikken ligger i `coach/laering.md`.

Kjøres når Knut påpeker noe, og i gjennomgangen før hver fredagsrapport.

## Lengde på svar — hardt krav

Knut, 04.09: «Du skriver fryktelig lange avhandlinger som burde vært 1/10 av
teksten. Det er så mye greier at det gir null mening for meg.»

**Regler for alt som går til Knut, fra agentene og fra hovedsamtalen:**

1. **Konklusjonen først, i én setning.** Så eventuelt hvorfor.
2. **Maks tre punkter.** Har du fem funn, velg de tre som endrer noe.
3. **Bare tall som endrer en beslutning.** Pa:HR, glattingsspenn,
   barometerstøy, metodevalg — det hører hjemme i filene under `coach/`,
   ikke i svaret. Han skal kunne handle på svaret, ikke etterprøve det.
4. **Ingen mellomregninger.** «Terrenget forklarer 4–5 av de 22 s/km» holder.
   Ikke vis hvordan.
5. **Ingen oppsummering til slutt.** Han har nettopp lest det.
6. **Er noe langt fordi det er viktig, si det på én linje og legg resten i fil.**

Et svar på ti linjer som han leser slår et svar på femti han hopper over.

## Spør før du tolker — hardt krav

Knut, 04.09: «Når du finner sånne ting så spør du heller hvorfor enn å anta
hvorfor. Da trenger jeg ikke 100 siders avhandling, men spørsmålene alene
først, og så kan du skrive avhandlingen når man er ferdig, i korte konsise trekk.»

**Rekkefølgen er:**

1. **Finner du et avvik i dataen — spør først.** Ett til tre korte spørsmål,
   ingenting annet. Ikke analyse, ikke hypoteser, ikke forbehold.
2. **Vent på svaret.**
3. **Så konkluder**, kort, etter lengdekravet over.

Grunnen er at han vet ting dataen ikke viser, og at en analyse bygget på feil
antagelse er verre enn ingen analyse — den ser like overbevisende ut.

**Eksempler på antagelser som var feil fordi ingen spurte:**

| Data | Vi antok | Faktisk |
|---|---|---|
| Kadens faller til 47–61 i 43 % av tida | Beina sviktet | Fikk beskjed om å gå. Dårlig sti. |
| Kadens 70 | Lav skrittfrekvens | Strava måler per bein. 140 skritt/min. |
| Tempofall 22 s/km | Stølhet | Delvis terreng, og økta var uansett for kort til å telle |
| Kadensfall på 18-kilometeren | Tretthet | Han ble dårlig i magen og måtte på do |
| Langturer som formmåling | Hans egen fart | Gruppeøkter. Farten er ikke hans. |

Fem ganger på to dager. **Mønsteret er at dataen ser entydig ut og ikke er det.**

## FIT-øktfiler: droppet
Knut har prøvd .FIT-øktfiler til klokka og forkastet løsningen — import via USB
er for tungvint. **Ikke foreslå FIT-filer, øktimport eller strukturerte økter på
klokka igjen.** Han følger pulssonen ved å se på klokka underveis. Skal en økt
formidles, gjør det som tekst: oppvarming, hoveddel med pulsspenn, nedvarming.
Filene under `coach/garmin/workouts/` blir liggende, men er ikke i bruk.
