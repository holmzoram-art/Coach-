# coach/soevn/

Søvn- og restitusjonsdata eksportert fra Garmin Connect.

## Format

CSV per periode, navngitt `ÅÅÅÅ-MM-DD_ÅÅÅÅ-MM-DD-garmin-sleep.csv`.
Kolonner: dato, Sleep Score, hvilepuls, Body Battery, Pulse Ox, respirasjon,
hudtemperaturavvik, HRV Status, kvalitet, varighet, søvnbehov, leggetid,
våknetid, Sleep Alignment.

Dette er **eksportert rådata**, ikke avlest fra graf. Tallene er eksakte.

## Slik hentes den

Garmin Connect → Sleep → 4 Weeks → menyen oppe til høyre → eksporter CSV.
Legg fila her. Ca. hver fjerde uke holder.

## Hvem bruker den

`belastning-restitusjon` er hovedbruker (hvilepuls, varighet, HRV, alignment).
`fysiolog` bruker hvilepuls og HRV til å forklare pulsavvik i økter.
