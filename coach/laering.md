# Læring — feil, gjentakelser og rettelser

Føres av `kvalitetskontroll`. Nyeste øverst.

---

## [2026-09-04] Fart sammenlignet uten justering for stigning

**Kategori:** gal antagelse
**Hvem:** hovedsamtalen, `hovedcoach` (ukestatus og kveldsspørsmål), `fysiolog`
**Hva skjedde:** Påstanden «stølheten kostet 22 s/km ved samme puls» ble gjentatt
flere steder og lå til grunn for hele bestillingen til `belastning-restitusjon`.
Høydedataen viser at 03.09 hadde 11,0 hm/km mot 6,6 hm/km den 31.08 — nesten
dobbelt så mye stigning per kilometer. En ukjent andel av de 22 sekundene er
terreng, ikke stølhet.
**Rotårsak:** Sammenligningen ble gjort på rå fart. Høydeprofilen lå tilgjengelig
i `get_activity_streams` hele tiden, men ingen hentet den. `fysiolog.md` sa
«sammenlign like økter», men hadde ingen regel som gjorde det umulig å publisere
et s/km-tall uten hm/km ved siden av.
**Rettet:** `coach/fakta.md` — ny seksjon «Fart-sammenligninger» slår fast at
ethvert fart- eller s/km-tall mellom to økter skal være stigningsjustert (GAP)
eller på samme rute, og at hm/km skal oppgis for begge øktene.
`.claude/agents/fysiolog.md` — GAP-avsnittet gjort til en absolutt regel med
hm/km-tabell som krav. `coach/logg/2026-09-04.md` — hm/km ført inn i
sammenligningstabellen, og 22 s/km-påstanden markert som ikke stigningsjustert.

**Tallene, for ordens skyld:**

| Økt | km | hm | hm/km | Fart | Puls |
|---|---|---|---|---|---|
| 31.08 rolig | 5,01 | 33 | 6,6 | 6:47/km | 146 |
| 03.09 | 4,55 | 50 | 11,0 | 7:09/km | 146 |
| 04.09 langtur | 12,32 | 188 | 15,3 | 8:40/km | 137 |
| 27.08 langtur | 18,14 | 179 | 9,9 | 7:54/km | 148 |

## [2026-09-04] Ba Knut logge høydeprofil som ligger i datastrømmen

**Kategori:** data vi hadde
**Hvem:** `fysiolog`
**Hva skjedde:** I `coach/analyser/2026-09-07-i3-kalibrering-protokoll.md` ble
Knut bedt om å skrive «temperatur, underlag, rute» i Strava-beskrivelsen, og
kriteriet «rute under 5 hm/km» ble satt opp som noe han skal vurdere selv.
Høydeprofil og hm/km hentes som datastrøm og regnes ut i etterkant.
**Rotårsak:** Protokollen blandet sammen *instruks før økta* og *rapportering
etter økta*. «Velg en flat rute» er en gyldig instruks — det er en beslutning
han tar. Å la gyldigheten av testen hvile på hans anslag av hm/km er ikke.
**Rettet:** Protokollen skiller nå de to. Loggekravet er redusert til det som
ikke kan utledes: underlag, solo/gruppe, følelse, smerte, RPE, søvn.
`coach/fakta.md` presiserer skillet mellom utledbart og ikke utledbart.

Merk: dette skal ikke overkorrigeres. Underlag (asfalt/grus/sti), vått løv,
solo eller gruppe og hvordan det føltes er **ikke** i dataen og skal fortsatt
spørres om. Temperatur er noen ganger med i Strava — sjekk før du fastslår noe.

## [2026-09-04] Dagens økt omtalt i fortid før den var gjennomført

**Kategori:** gal antagelse
**Hvem:** `hovedcoach` og hovedsamtalen
**Hva skjedde:** Begge skrev at Knut «løp 12 km i dag». Klokka var 08:38 norsk
tid, og han trener normalt fra 16:30 — økta lå flere timer fram i tid.
**Rotårsak:** Systemets tidsstempler er UTC, og ingen sjekket faktisk lokaltid
eller Strava før de omtalte økta. Knut hadde oppgitt treningstidspunktet flere
ganger uten at det var skrevet ned noe sted.
**Rettet:** `coach/fakta.md` opprettet med tidssone, treningstidspunkt og krav
om å sjekke `TZ=Europe/Oslo date` og Strava før dagens økt omtales.

## [2026-09-04] Ba Knut notere styrkeavvik som allerede lå i Strava

**Kategori:** data vi hadde
**Hvem:** `hovedcoach`
**Hva skjedde:** Ba ham skrive ned avvik fra styrkeplanen samme dag. Han logger
i Hevy, som synker til Strava med fullstendig øvelsesliste, vekter, sett og
reps. Avviket 01.09 (bulgarians 20 kg mot planlagte 10) ble faktisk funnet i
nettopp den dataen.
**Rotårsak:** `coach/instrukser.md` nevnte at løpsdata kommer fra Strava, men
sa ikke at styrkeøktene gjør det samme.
**Rettet:** `coach/fakta.md` slår fast at all styrketrening kommer inn med
full detalj. Fjernet som krav til Knut.

## [2026-09-04] Ba Knut logge RPE selv i stedet for å spørre om den

**Kategori:** gjentatt spørsmål
**Hvem:** `fysiolog`, `belastning-restitusjon`, `hovedcoach`
**Hva skjedde:** Tre agenter ba i tur og orden om at han skulle føre RPE på
hver økt. Knut påpekte at dette er nettopp det kveldsspørsmålet er til for.
**Rotårsak:** Agentene behandlet RPE som en lekse framfor som noe
`hovedcoach` henter inn i dialogen.
**Rettet:** `coach/fakta.md` fastslår at RPE hentes gjennom kveldsspørsmålet
når den ikke er satt i Stravas eget felt. Ingen agent skal be om den som
selvstendig oppgave.

## [2026-09-04] Hovedsamtalen svarte faglig i stedet for å delegere

**Kategori:** gal antagelse
**Hvem:** hovedsamtalen
**Hva skjedde:** Svarte selv på ernæringsspørsmål gjennom en lang samtale om
frokost, metthet og måltidsstruktur, framfor å sende dem til `ernaering`.
**Rotårsak:** Behandlet korte spørsmål som for små til å delegere. Det var
ikke hovedsamtalens vurdering å gjøre.
**Rettet:** `coach/instrukser.md` — faglige spørsmål går til agentene, også de
korte. Hovedsamtalen er budbringer og redaktør.

## [2026-09-04] Vektplanen bygget uten å kjenne tidslinja

**Kategori:** gal antagelse
**Hvem:** hovedsamtalen
**Hva skjedde:** `ernaering` fikk i oppdrag å lage vektplan uten å vite at
Knut hadde vært i sammenhengende underskudd siden februar, eller at han endret
kosthold i juni. Planen måtte skrives om da tidslinja kom fram.
**Rotårsak:** Ingen hadde spurt hvor lenge underskuddet hadde pågått før
planen ble bestilt.
**Rettet:** `coach/ernaering/kartlegging.md` opprettet med full tidslinje.
Merk: at `ernaering` endret plan da premisset ble riktig er **ikke** en feil —
det er riktig oppførsel. Feilen lå i bestillingen.
