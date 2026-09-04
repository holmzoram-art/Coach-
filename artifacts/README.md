# artifacts/

Kildekode for de publiserte artifactene. Repoet er kilden — publisert versjon
skal alltid kunne bygges herfra.

| Fil | Artifact | Innhold |
|---|---|---|
| `kroppsloggen.html` | **Kroppsloggen** | Daglig vektlogg med trend, søvndata, ernæringsplan, kneflagg, læringslogg |
| *(ikke i repo)* | **Marathon** | Treningsplanen, økt for økt. Redigeres direkte i artifacten. |

## Kroppsloggen

URL: https://claude.ai/code/artifact/2ff64b78-d515-4fb8-bc2e-3cf7a0535438

Bruker `db`-capability til å lagre vektmålinger. Ett dokument per dato:

```
weights/ÅÅÅÅ-MM-DD  →  { d: "ÅÅÅÅ-MM-DD", kg: 119.0 }
```

Tallene kan leses tilbake med Artifact-verktøyets `read_db` og brukes i
analyser. `ernaering` bruker **ukesnitt**, ikke enkeltmålinger.

Seedet med de tre punktene Knut har oppgitt: 131 kg (feb), 119 kg (juli),
119 kg (4. sept). Resten legger han inn selv hver morgen.

## Arbeidsdeling mellom de to

- **Marathon** svarer på «hva gjør jeg i dag». Økter, soner, uker.
- **Kroppsloggen** er alt annet — det som avgjør om treningen virker, men som
  ikke er en økt.
