# Steg 1 — finn ut hva klokka sender ut

**Tid: ca. 15 minutter. Ingen programmering.**

Før vi bygger noe som helst må vi vite én ting: *hva sender Enduro 3
faktisk ut over Bluetooth mens du løper?* Alt annet i prosjektet henger
på svaret.

Du trenger ikke kunne noe fra før. Dette er å installere en gratis app,
trykke på et par ting, og lese av en liste.

---

## Hva vi leter etter

Bluetooth-enheter beskriver seg selv med nummererte «tjenester».
Vi er ute etter to:

| Nummer | Navn | Hva det gir oss |
|---|---|---|
| `0x180D` | Heart Rate | Puls |
| `0x1814` | Running Speed and Cadence | Fart, kadens, distanse |

**Hvis begge er der:** telefonen kan bruke klokkas mål på distanse og
fart. Klokka di har multi-band GPS, som er bedre enn telefonens, og vi
arver den gratis.

**Hvis bare `0x180D` er der:** vi får puls fra klokka, og telefonen må
måle distansen selv. Det fungerer også — splittene blir bare noen
sekunder unna klokkas. Ikke et problem, men greit å vite på forhånd.

Begge utfall er brukbare. Vi trenger bare å vite hvilket vi har.

---

## A. Slå på kringkasting på klokka

Garmin kaller dette å «kringkaste» eller «broadcast» pulsen. Det betyr
at klokka sender pulsen ut på Bluetooth samtidig som den tar opp økta,
slik at andre enheter kan lese den.

Det ligger ett av to steder. Prøv den enkleste først:

**Under en aktivitet:** start en løpsaktivitet på klokka, hold inne
`MENU`-knappen, og se etter et valg som heter noe i retning av
*Kringkast puls* / *Broadcast Heart Rate*.

**I innstillingene, permanent:** hold inne `MENU` fra klokkeskiven, og
gå deretter:

```
Innstillinger  →  Sensorer og tilbehør  →  Puls på håndledd
               →  Kringkast under aktivitet   (slå PÅ)
```

Ordlyden kan avvike litt — Garmin flytter på menyer mellom
programvareversjoner. Leter du etter ordet «kringkast» eller
«broadcast» finner du det.

Når det er på, viser klokka vanligvis et lite kringkastingsikon.

> **Merk:** dette bruker litt ekstra batteri. På en løpetur under en
> time er det uvesentlig.

## B. Installer en Bluetooth-skanner på telefonen

Last ned **nRF Connect for Mobile** fra Google Play. Den er gratis, laget
av Nordic Semiconductor, og er standardverktøyet for å se hva
Bluetooth-enheter faktisk tilbyr. Den endrer ingenting — den bare leser.

Appen vil be om tillatelse til posisjon og Bluetooth. Begge er
nødvendige: Android krever posisjonstillatelse for å skanne etter
Bluetooth-enheter i det hele tatt, av personvernhensyn. Den bruker ikke
posisjonen din til noe her.

## C. Koble til og les av

1. Start en løpsaktivitet på klokka, med kringkasting på. **Ikke bare
   la klokka ligge i ro** — noen funksjoner slås først på når en
   aktivitet faktisk går.
2. Åpne nRF Connect. Du er på `SCANNER`-fanen. Trykk `SCAN`.
3. Finn klokka i lista. Den heter noe med `Enduro` eller `Garmin`, ofte
   med noen tall etter.
4. Trykk `CONNECT` ved siden av den.
5. Nå kommer det opp en liste over tjenester. Se etter linjer som
   heter `Heart Rate` og `Running Speed and Cadence`.

**Dette er svaret vi trenger.** Ta et skjermbilde av lista.

### Vil du se tallene live

Trykk på `Heart Rate` for å utvide den. Under kommer det en linje som
heter `Heart Rate Measurement`. Ved siden av den er det et lite ikon
med tre piler i en sirkel — trykk på det for å abonnere på verdiene.

Da skal pulsen din begynne å ticke inn i sanntid, oppdatert hvert
sekund. Gjør du det samme på `Running Speed and Cadence`, ser du fart
og kadens.

Ser du tall som beveger seg her, er hele datakjeden bevist. Resten av
prosjektet er bare programvare.

---

## Om pulsbeltet ditt

Du har et Garmin-belte fra generasjonen før den nyeste. Det er verdt å
finne ut nøyaktig hvilket, for det er én reell forskjell:

- **HRM-Run og HRM-Tri** sender kun på ANT+, ikke Bluetooth. En
  Android-telefon kan normalt ikke lese dem direkte.
- **HRM-Dual, HRM-Pro og HRM-Pro Plus** sender på begge.

Modellnavnet står vanligvis trykt på selve pulsmåleren, den lille
plastboksen som klikkes på stroppen.

**Men det spiller mindre rolle enn det høres ut som.** I arkitekturen
vår kobles beltet til klokka som før, og klokka kringkaster videre til
telefonen. Kjeden blir:

```
belte  ──ANT+──►  Enduro 3  ──Bluetooth──►  telefon  ──►  ørepropper
```

Klokka fungerer altså som bro. Beltet trenger ikke å snakke Bluetooth
i det hele tatt.

Fordelen med beltet er nøyaktigheten: brystbelte reagerer på 1–3
sekunder ved tempoendring, mens optisk puls på håndleddet bruker 10–30.
Siden vi midler over hele kilometeren betyr det mindre for oss enn for
en app som coacher sekund for sekund — men gratis presisjon er gratis
presisjon. Bruk beltet når du har det på.

---

## Hva du rapporterer tilbake

1. Fant du kringkastingsvalget på klokka? Hvor lå det?
2. Hvilke tjenester dukket opp i nRF Connect? (Skjermbilde holder.)
3. Kom det tall når du abonnerte på `Heart Rate Measurement`?
4. Hvilken modell står det på pulsbeltet?

Med det på plass vet vi nøyaktig hva appen har å jobbe med, og kan
begynne å skrive den.
