# Kneadly — kva som står att før butikken kan ta imot pengar

Bygd 6. september 2026. Produkt: mini massasjepistol, AliExpress-vare
`1005007343958003`, seljar *DAQI Beautylife Store* (4,5★ av 1 174, 5 000+ selde,
93,3 % butikkscore). Variant på sida: **6 GEAR**, svart og grå.

Same arkitektur som Lintly: `shop.js` er einaste staden prisar, fargar og
Stripe-lenkjer bur. `build_pages.py` lagar undersidene. `verktoy/ordre.html`
er ordrepulten (ikkje publisert — viser kostpris).

Kjøpsknappen seier «Checkout opens soon» til Stripe-lenkjene er limt inn.

## Før lansering

1. **E-post.** `support@kneadly.store` er plassholdar; domenet er teke.
   Bruk ein Gmail. Byt overalt:
   `sed -i '' 's/support@kneadly\.store/DIN-ADRESSE/g' *.html build_pages.py`
2. **Stripe.** Fire produkt / fire lenkjer i Kneadly-kontoen (eller ein ny):
   Black 1 ($79.99), Black 2 ($139.99), Grey 1, Grey 2. Collect shipping address på.
   Lim inn i `shop.js`.
3. **Push.** Då blir knappen «Buy now».

## Tala

Varekost **104,19 kr** per stk (ingen mengderabatt sett hos seljaren).
USD = 10,50 kr, Stripe 2,9 % + 2,50 kr.

| | 1 stk | 2 stk |
|---|---:|---:|
| Pris | $79.99 | $139.99 |
| Omsetning | 840 kr | 1 470 kr |
| Vare | −104 kr | −208 kr |
| Stripe | −27 kr | −45 kr |
| **DB før mva** | **709 kr** | **1 216 kr** |
| DB etter mva-registrering | 541 kr | 922 kr |
| DB etter mva, 5 % refusjonsrate | **499 kr** | **849 kr** |

**Stoppregelen:** er faktisk CPA over ~500 kr på ein-stk-ordrar, taper du.
Til samanlikning var taket 141 kr på Lintly. Det er difor dette produktet.

## Det eg har vore ærleg om på sida

- 4,5 av 1 174, inkludert dei 32 som seier «damaged box». Forklart, ikkje gøymt.
- Ingen oppdikta tal: motorhastigheit, mAh, stallkraft og desibel er utelatne
  fordi seljaren ikkje publiserer testa verdiar.
- Tydeleg «ikkje på bein, ikkje framsida av halsen, spør lege viss gravid/
  hjarte/pacemaker». Det er både riktig og det som held Meta-annonsar trygge —
  ingen helsepåstandar.
- Kabelen er dårleg. Står i FAQ og i fraktmailen.

## Bileta

Berre tre av dei ni bileta hos seljaren viser 6 GEAR-modellen (den vesle).
Dei andre seks viser 30/99 GEAR — eit større apparat. Sida brukar berre dei
tre ekte, pluss to utsnitt av dei. Ikkje legg til dei andre; då sel du eit
anna produkt enn du sender.

## Etter lansering

- [ ] Kjøp éin til deg sjølv. Test hastigheit 6 på ei skulder.
- [ ] Første ordre: gjer han saman med Claude, steg for steg.
- [ ] Følg med på 50 000 kr — mva-registrering.
