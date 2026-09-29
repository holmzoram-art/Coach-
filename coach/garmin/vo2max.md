# VO2max — Garmin

| Måned | VO2max |
|---|---|
| Mai 2026 | 38,8 |
| Juni 2026 | 41,2 |
| Juli 2026 | 42,4 |
| August 2026 | 43,3 |
| September 2026 | 43,2 |

**+4,5 poeng fra mai til august.** Flatt siste måned.

Rådata: `vo2max.csv`. Garmins VO2max er et estimat fra puls og fart, ikke en
laboratoriemåling — men den er konsistent målt på samme klokke og duger som
trendindikator.

## Nattverdier 05.09.2026 (første natt med Pulse Ox på)

| | Verdi | Garmins normalspenn | Baseline fra søvn-CSV (28 d) |
|---|---|---|---|
| Hvilepuls | **52** | 42–56 | 43,5 ± 1,5 |
| HRV | **64** | 62–89 | 74,8 ± 1,6 |
| Respirasjon | 13,6 | 12,4–14,5 | — |
| Hudtemp | −0,1° | −0,9 til +0,8 | — |
| Pulse Ox | 94–95 % | 90–100 % | — |
| Søvn | 9t30 | | snitt 7t21 |

**Uavklart:** hvilepuls 52 ligger 8,5 over baseline fra søvn-CSV-en, og HRV 64
ligger ~10 under. Begge krysser flaggtersklene i `coach/instrukser.md`. Men
Garmins eget normalspenn er videre, og det er ikke bekreftet at panelet viser
samme måling som CSV-kolonnene. Må avklares før det tolkes.


## Nattverdier 06.09.2026 (natt 2 med Pulse Ox)

| | 05.09 | **06.09** | Garmins spenn | Baseline søvn-CSV |
|---|---|---|---|---|
| Hvilepuls | 52 | **48** | 42–56 | 43,5 ± 1,5 |
| HRV | 64 | **76** | 62–89 | 74,8 ± 1,6 |
| Respirasjon | 13,6 | **13,4** | 12,4–14,5 | — |
| Hudtemp | −0,1° | **0°** | −0,9 til +0,8 | — |
| Pulse Ox | 94–95 % | **95 %** | 90–100 % | — |

**Avklart:** panelet heter «Health Status» og teksten sier «how your **sleep
metrics** compare to your typical ranges». Det er altså **søvnverdier**, ikke
døgntall. Garmins «typical range» er et bredere personlig spenn enn snitt ± SD
fra 28-dagers CSV-en.
