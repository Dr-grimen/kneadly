# Meta-annonser — Kneadly Mini

Laga 8. september 2026. Landingsside: `https://dr-grimen.github.io/kneadly/`
Tilbod: **$79.99** · 2 stk $139.99 (spar $20) · gratis frakt · 30 dagar pengane tilbake.

---

## Filene

| Fil | Format | Bruk |
|---|---|---|
| `ad-A-feed-1080x1350.jpg` | 4:5 | Feed, «YOUR THUMBS GAVE UP» |
| `ad-A-story-1080x1920.jpg` | 9:16 | Reels / Stories, same hook |
| `ad-B-feed…` / `-story…` | | «SIX SPEEDS. FOUR HEADS. ONE HAND.» |
| `ad-C-feed…` / `-story…` | | «SMALL ENOUGH FOR A GYM BAG.» |
| `ad-video-story-1080x1920.mp4` | 9:16, 13,7 s | Reels / Stories |
| `ad-video-feed-1080x1350.mp4` | 4:5, 13,7 s | Feed |

Alle videoar er H.264 / yuv420p / 30 fps — nøyaktig det Meta ber om. Under 1 MB,
så opplasting går på sekundet. Ingen lyd: Meta spelar av lydlaust som standard,
og all bodskap ligg som tekst i biletet.

**Kjeldebilete:** berre `raa/g-6`, `g-7` og `g-8`. Dei viser 6 GEAR-modellen du
faktisk sender. `g-1`, `g-2`, `g-4`, `g-5` og `g-9` viser eit **større apparat med
hard koffert** — bruk dei aldri. Same gjeld leverandøren sin eigen video
(`ads/produktvideo.mp4`): han pakkar ut ein koffert kunden din ikkje får.

---

## Annonsetekstar

Bruk éin tekst per annonse, ikkje bland. Overskrift maks 40 teikn, beskriving 30.

### A — «tommelen gav opp»

> **Primærtekst**
> Your thumbs give up long before the knot does.
>
> The Kneadly Mini doesn't. Six speeds, four heads, and enough punch on the top
> setting to sort out a shoulder that's been tight all week. It's the size of your
> hand, charges over USB-C, and lives in a gym bag instead of a cupboard.
>
> $79.99, shipped free. Thirty days to change your mind — and you keep it.

> **Overskrift:** Six speeds. Four heads. One hand.
> **Beskriving:** Free shipping · 30-day money back

### B — spesifikasjonar

> **Primærtekst**
> Most mini massage guns are a toy. This one has six speeds, a display that shows
> the level and the charge, and four heads — ball for big muscles, bullet for one
> stubborn knot, fork for either side of the spine, flat for everything else.
>
> Charges with the same cable as your phone. Fits in a glovebox.
>
> $79.99 with free worldwide shipping.

> **Overskrift:** The mini massage gun that isn't a toy
> **Beskriving:** $79.99 · free shipping

### C — storleik

> **Primærtekst**
> Small enough for a gym bag. Six speeds, four heads, USB-C.
>
> Two minutes on a tight calf and it lets go. No appointment, no table, no
> massage therapist's diary to work around.
>
> $79.99, free shipping, and if it's not for you we refund you within 30 days
> and you keep it.

> **Overskrift:** Fits in a gym bag. Hits like it doesn't.
> **Beskriving:** Free worldwide shipping

---

## ⚠️ Meta-reglar: ikkje skriv desse

Meta sitt regelverk for helse og velvære er strengt, og massasjepistolar blir
avviste kvar dag på det same. **Ingen av tekstane over inneheld noko av dette —
ikkje legg det til:**

- Ingen «relieves pain», «cures», «treats», «heals», «therapy», «recovery»
- Ingen «reduces inflammation», «improves circulation», «breaks up lactic acid»
- Ingen før/etter-bilete av kroppar
- Ingen «do you suffer from back pain?» — Meta forbyr å tilskrive lesaren ein
  helsetilstand. Det er den vanlegaste avvisingsgrunnen som finst.

Trygt: kva apparatet **er** og **gjer** (hastigheiter, hovud, storleik, lading),
og ord som «tight», «loosen», «relax», «sore muscles after training».

Landingssida er allereie skriven etter same regel, med «ikkje på bein, spør lege
viss gravid / hjarte / pacemaker» i FAQ og vilkår. Det er òg det Meta ser etter
når dei kontrollerer sida bak annonsen.

---

## Oppsett

**Kampanje:** Sales. **Optimalisering:** Purchase — *ikkje* Link Clicks.
Det krev at pikselen er på (sjå under).

**Målgruppe:** Advantage+ eller brei. Ikkje interessestabling på eit produkt som
dette; algoritmen finn kjøparane raskare enn du gjettar dei. Alder 25–55.
Land: start med **UK + US** åleine — der er kjøpekrafta og engelsk er morsmål.

**Plasseringar:** automatiske. Du har både 4:5 og 9:16, så alt er dekt.

**Struktur dag 1:** éin kampanje, éin annonsegruppe, **seks annonsar** (A/B/C som
bilete + dei to videoane + éin til). La Meta fordele.

### Budsjett, rekna frå dine eigne tal

Dekningsbidrag etter mva og 5 % refusjon: **499 kr** per einskildordre.
Det er taket. Over det taper du på kvar ordre.

| Dagsbudsjett | Testperiode | Kva du får vite |
|---|---|---|
| 200 kr | 5 dagar = 1 000 kr | Om nokon i det heile klikkar |
| 350 kr | 7 dagar = 2 450 kr | Nok data til å sjå CPA |

**Stoppregelen:** 1 000 kr brukt og null kjøp → slå av og skriv nye hooks.
CPA over 499 kr → slå av. CPA under 350 kr → auk budsjettet 20 % om dagen,
ikkje meir.

---

## To ting som må vere på plass først

### 1. Pikselen — utan han er annonsane blinde

Koden ligg klar i `shop.js`, øvst, feltet `metaPixel`. Står han tom, blir
ingenting lasta. Fyller du inn ID-en, får du automatisk:

- `PageView` på alle sju sidene
- `ViewContent` på produktsida
- `InitiateCheckout` når nokon trykkjer kjøpsknappen, med farge, antal og beløp

Testa og verifisert. **Purchase** kjem frå Stripe si eiga Meta-kobling, ikkje
herifrå — sjå Stripe → Settings → Integrations.

Hent ID-en i Events Manager. Du har alt eit datasett frå FreshSeal
(`1084094144118262`), men **lag eit nytt for Kneadly** — blandar du dei, lærer
algoritmen på feil produkt. Send meg ID-en, så limer eg han inn.

Utan piksel kan Meta ikkje optimalisere for kjøp. Då betaler du for klikk og
håpar. Det er den dyraste måten å teste eit produkt på.

### 2. Domenet — kjøp det før annonsane, ikkje etter

Du sa du ville kjøpe domenet når du såg at annonsane funka. Problemet er at
**`github.io` ikkje kan domeneverifiserast** — GitHub eig domenet, og du kjem
ikkje til DNS-en. Meta krev domeneverifisering for Aggregated Event Measurement,
som er det som prioriterer Purchase-hendinga etter iOS-sporingsendringane.

Utan det blir konverteringsmålinga degradert frå dag éin, og du kan ikkje stole
på tala du brukar til å avgjere om produktet funkar.

`getkneadly.com` eller `trykneadly.com` kostar rundt **120 kr i året**. Mot eit
testbudsjett på 1 000–2 500 kr er det avrundingsfeil. Kjøp det først, så peikar
eg GitHub Pages på det og du verifiserer i Meta.

---

## Konkurrentar

Eg har ikkje lasta ned annonsevideoar frå andre butikkar, og eg gjer det ikkje:
det er deira opphavsrett, Meta kjenner att innhaldet, og det er ein rask veg til
sperra konto.

Det du derimot kan gjere lovleg og bør: opne **Meta Ad Library**, søk
«massage gun», og sjå kva hooks som har gått lenge. Annonsar som har køyrt i
månader tener pengar. Les dei, forstå vinkelen, og skriv din eigen. Det er
research, ikkje kopiering.
