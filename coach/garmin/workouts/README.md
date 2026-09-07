# Garmin-øktfiler (.FIT)

Sju ferdige øktfiler med pulsalarm. Bygget med `fit-tool`, verifisert ved å
lese filene tilbake og dekode pulsverdiene.

## Import
**USB er eneste vei.** Koble klokka til PC, legg filene i `GARMIN/NewFiles/`
på enheten, koble fra. Øktene dukker opp under Trening → Økter.

Siden «Import Data» i Garmin Connect på nett tar **kun aktivitetsfiler**
(fullførte økter) og avviser øktmaler — det er ikke en feil i filene.

Filene har 14-byte header med header-CRC, gyldig fil-CRC og er lest tilbake
og dekodet. Verifiser med `python3 build_fit.py` og sjekken i git-historikken.

## Innhold

| Fil | Økt | Pulsmål | Alarmgrense i fila |
|---|---|---|---|
| 01_I1_restitusjon | I1 restitusjon | under 138 | 90–141 |
| 02_Sondag_rolig | Søndag rolig 4 km | under 142 | 90–145 |
| 03_Langtur_I2 | Langtur i gruppe | under 157 | 90–160 |
| 04_8K_Flat_referanse | «8K Flat» referanseøkt | 142–148 | 139–151 |
| 05_I3_tempo_kalibrering | I3 tempo / kalibrering | 157–166 | 154–169 |
| 06_I4_terskelintervaller | I4 terskel 4×6 min | under 176 | 90–179 |
| 07_Dagens_I2_40-50min | 40–50 min flatt I2 | 137–150 | 134–153 |

Alarmgrensa ligger **3 bpm utenfor** målsonen (fysiologens krav) så klokka
ikke maser på grensa. Tak-økter har gulv 90 slik at alarmen bare fyrer
oppover. Oppvarmingssteget har ingen pulsalarm — det dekker de første
10 minuttene (15 på terskeløkta).

## Fortsatt manuelt på klokka
Varsling som **vibrasjon, ikke lyd** — det er en enhetsinnstilling
(Innstillinger → Varsler/Lyd og vibrasjon), ikke noe som kan legges i fila.

## Bygging
`python3 build_fit.py` (kilde i scratchpad, kopi under `build_fit.py` her).
