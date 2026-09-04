# Læring — feil, gjentakelser og rettelser

Føres av `kvalitetskontroll`. Nyeste øverst.

---

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
