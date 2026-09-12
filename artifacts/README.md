# Artifacts

HTML-sidene her er **frittstående**. De trenger ingen server og ingen konto:
last ned fila og åpne den i en nettleser, så virker den.

| Fil | Hva |
|---|---|
| `matplan.html` | Ukesmat — dagens måltider, uka, handleliste, søndagsprep |
| `kroppsloggen.html` | Daglig vektregistrering |

## Hvordan lagringen virker

Sidene lagrer avhukinger og valg to steder, avhengig av hvor de kjøres:

- **Åpnet via claude.ai:** delt lagring. Setter du opp noe på PC, ser du det på
  mobilen. Dette er det som gjør handlelista nyttig i butikken.
- **Åpnet som fil, uten claude.ai:** nettleserens eget lager, altså per enhet.
  Alt virker, men ingenting følger med til en annen telefon eller maskin.

Siden sier selv hvilken modus den er i, øverst.

## Hvis Claude-tilgangen tar slutt

Du mister ingenting som betyr noe. **Selve planen ligger i markdown-filene**
under `coach/` — `ernaering/planen.md`, `treningsplan.md` og resten. De kan
leses hvor som helst, i all framtid, uavhengig av alt.

For å bruke appen videre:

1. Last ned `artifacts/matplan.html` fra dette repoet.
2. Åpne den i nettleseren. På mobil: lagre til hjemskjermen, så oppfører den
   seg som en app.
3. Avhukinger lagres lokalt på den enheten.

Vil du ha den på nett med synk mellom enheter uten Claude, er det to veier:
GitHub Pages fra et **privat** repo krever betalt GitHub-plan, mens
Cloudflare Pages og Netlify hoster private repoer gratis. Begge gir fortsatt
bare lokal lagring — ekte synk krever en database.

**Ikke gjør repoet offentlig** for å få gratis hosting. Det inneholder vekt,
hvilepuls, HRV og notater om legetimer.
