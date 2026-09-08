#!/usr/bin/env python3
"""
Importerer Kneadly-butikken til Shopify.

  python3 shopify_import.py            # tørrkøyring: viser kva som blir laga
  python3 shopify_import.py --go       # gjer det på ekte

Lagar: eitt produkt med fire variantar (Black/Grey × 1/2 stk), fem bilete,
seks sider (FAQ, frakt, om, kontakt, vilkår, personvern) og dei fire
butikkpolicyane.

NØKKELEN GÅR ALDRI GJENNOM CHAT. Skriptet spør deg i eit passordfelt og
lagrar svaret i ~/.kneadly-shopify.json med rettar 600.

Slik lagar du nøkkelen i Shopify:
  Settings → Apps and sales channels → Develop apps → Create an app
  → Configure Admin API scopes → hak av:
       write_products, read_products, write_content, read_content
  → Install app → Reveal Admin API access token  (byrjar med shpat_)
"""

import json, os, sys, base64, subprocess, urllib.request, urllib.error, pathlib

CFG = pathlib.Path.home() / ".kneadly-shopify.json"
SITE = "https://dr-grimen.github.io/kneadly"
API_VERSIONS = ["2026-07", "2026-04", "2026-01", "2025-10", "2025-07", "2025-01"]


# ---------------------------------------------------------------- nøkkel

def ask(prompt, hidden=False):
    """Spør i ein GUI-dialog. Hemmelegheiter skal ikkje via chat eller historikk."""
    script = (
        f'display dialog "{prompt}" default answer "" '
        f'{"with hidden answer " if hidden else ""}'
        f'buttons {{"Avbryt","OK"}} default button "OK" with title "Kneadly → Shopify"'
    )
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("Avbrote.")
    out = r.stdout.strip()
    return out.split("text returned:", 1)[1].strip() if "text returned:" in out else ""


def credentials():
    if CFG.exists():
        c = json.loads(CFG.read_text())
        if c.get("shop") and c.get("token"):
            return c["shop"], c["token"]
    shop = ask("Shopify-domenet ditt (t.d. kneadly-mini.myshopify.com):")
    shop = shop.replace("https://", "").replace("http://", "").strip("/ ")
    token = ask("Admin API access token (shpat_...):", hidden=True)
    if not shop or not token:
        sys.exit("Manglar domene eller token.")
    CFG.write_text(json.dumps({"shop": shop, "token": token}))
    CFG.chmod(0o600)
    print(f"Lagra i {CFG} (berre du kan lese fila).")
    return shop, token


# ---------------------------------------------------------------- API

class Shop:
    def __init__(self, shop, token):
        self.shop, self.token, self.ver = shop, token, None
        for v in API_VERSIONS:
            try:
                d = self._call("{ shop { name myshopifyDomain currencyCode } }", ver=v)
                if "shop" in d:
                    self.ver, self.info = v, d["shop"]
                    return
            except urllib.error.HTTPError as e:
                if e.code in (401, 403):
                    sys.exit("Token blei avvist. Sjekk at appen er installert og at "
                             "scopes write_products og write_content er haka av.")
            except Exception:
                continue
        sys.exit("Fann ingen API-versjon som svarte. Sjekk butikkdomenet.")

    def _call(self, query, variables=None, ver=None):
        body = json.dumps({"query": query, "variables": variables or {}}).encode()
        req = urllib.request.Request(
            f"https://{self.shop}/admin/api/{ver or self.ver}/graphql.json",
            data=body, method="POST",
            headers={"Content-Type": "application/json",
                     "X-Shopify-Access-Token": self.token})
        with urllib.request.urlopen(req, timeout=45) as r:
            out = json.loads(r.read())
        if "errors" in out:
            raise RuntimeError(json.dumps(out["errors"])[:400])
        return out["data"]

    def run(self, query, variables=None, field=None):
        d = self._call(query, variables)
        if field:
            node = d[field]
            errs = node.get("userErrors") or []
            if errs:
                raise RuntimeError("; ".join(f"{e.get('field')}: {e['message']}" for e in errs))
            return node
        return d


# ---------------------------------------------------------------- innhald

DESC = """<p>A massage gun the size of your hand. Six speeds, four heads, and enough punch on the
top setting to sort out a shoulder that has been tight for a week.</p>
<p>Sit at a desk all day, or run, or lift, or carry a toddler around, and something goes tight.
You knead at it with a thumb and it does nothing, because thumbs get tired long before a knot does.
The Kneadly Mini does not get tired.</p>
<ul>
<li><strong>Six speeds</strong> — one is gentle enough for a sore neck; six is, in the words of one
buyer, &laquo;like a rotary hammer&raquo;</li>
<li><strong>Four heads</strong> — ball for big muscles, bullet for a single knot, fork for either
side of the spine, flat for everything else</li>
<li><strong>A display</strong> that shows the speed and the charge</li>
<li><strong>USB-C</strong> — the same cable as your phone</li>
<li><strong>Fits in a hand</strong>, a gym bag, a glovebox</li>
</ul>
<p><strong>In the box:</strong> the gun, four heads, a USB-C cable. The included cable is a basic
one — the cable from your phone works better.</p>
<p><strong>Where not to use it:</strong> not on bone, not the front or sides of the neck, not on an
injury. If you are pregnant or have a heart condition, a pacemaker or a clotting disorder, ask your
doctor first. It is a tool for tight muscles, not a treatment for anything.</p>"""

IMAGES = [
    ("produkt-2.webp", "Kneadly Mini in black with its four heads laid out"),
    ("produkt-3.webp", "The mini massage gun with the ball, bullet, fork and flat heads in a row"),
    ("produkt-5.webp", "The round display showing speed level 6 and the USB-C port"),
    ("produkt-4.webp", "Close-up of the four attachment heads"),
    ("produkt-1.webp", "Kneadly Mini in grey with its four heads laid out in front"),
]

VARIANTS = [("Black", "One", "79.99", "KM-BLK-1"), ("Black", "Two", "139.99", "KM-BLK-2"),
            ("Grey", "One", "79.99", "KM-GRY-1"), ("Grey", "Two", "139.99", "KM-GRY-2")]


def page_bodies():
    """Hentar brødteksten ut av dei ferdige HTML-sidene, utan header og footer."""
    import re
    out = {}
    titles = {"faq.html": "FAQ", "shipping.html": "Shipping & returns", "about.html": "About",
              "contact.html": "Contact", "terms.html": "Terms of service",
              "privacy.html": "Privacy policy"}
    here = pathlib.Path(__file__).parent
    for fn, title in titles.items():
        p = here / fn
        if not p.exists():
            continue
        html = p.read_text()
        m = re.search(r'<div class="page">(.*?)</div>\s*</main>', html, re.S)
        if not m:
            continue
        body = re.sub(r'<div class="eyebrow">.*?</div>\s*', "", m.group(1), flags=re.S)
        body = re.sub(r'<h1>.*?</h1>\s*', "", body, flags=re.S)
        out[title] = body.strip()
    return out


# ---------------------------------------------------------------- køyring

Q_PRODUCT = """
mutation ($input: ProductSetInput!) {
  productSet(synchronous: true, input: $input) {
    product { id title handle onlineStoreUrl variants(first: 10) { nodes { title price sku } } }
    userErrors { field message }
  }
}"""

Q_MEDIA = """
mutation ($id: ID!, $media: [CreateMediaInput!]!) {
  productCreateMedia(productId: $id, media: $media) {
    media { alt status }
    mediaUserErrors { field message }
  }
}"""

Q_PAGE = """
mutation ($page: PageCreateInput!) {
  pageCreate(page: $page) { page { id title handle } userErrors { field message } }
}"""

Q_POLICY = """
mutation ($policy: ShopPolicyInput!) {
  shopPolicyUpdate(shopPolicy: $policy) { shopPolicy { type } userErrors { field message } }
}"""


def main():
    go = "--go" in sys.argv
    shop, token = credentials()
    s = Shop(shop, token)
    print(f"\nKopla til: {s.info['name']}  ({s.info['myshopifyDomain']}, "
          f"valuta {s.info['currencyCode']}, API {s.ver})")

    pages = page_bodies()
    print("\nDette blir laga:")
    print("  Produkt : Kneadly Mini")
    for c, p, pr, sku in VARIANTS:
        print(f"            {c:5} / {p:3} stk  ${pr:>7}  {sku}")
    print(f"  Bilete  : {len(IMAGES)} (henta frå {SITE}/bilder/)")
    print(f"  Sider   : {', '.join(pages)}")
    print("  Policyar: refund, privacy, terms of service, shipping")

    if s.info["currencyCode"] != "USD":
        print(f"\n  ⚠ Butikkvalutaen er {s.info['currencyCode']}, ikkje USD. Prisane over er i "
              f"dollar. Set valutaen til USD i Settings → Store details før du importerer, "
              f"elles blir 79.99 tolka som {s.info['currencyCode']}.")

    if not go:
        print("\nTørrkøyring — ingenting er endra. Køyr med --go for å gjere det på ekte.")
        return

    print("\n→ lagar produkt…")
    variants = [{"optionValues": [{"optionName": "Colour", "name": c},
                                  {"optionName": "Pack", "name": p}],
                 "price": pr, "sku": sku, "inventoryPolicy": "CONTINUE"}
                for c, p, pr, sku in VARIANTS]
    r = s.run(Q_PRODUCT, {"input": {
        "title": "Kneadly Mini", "descriptionHtml": DESC, "vendor": "Kneadly",
        "productType": "Massage gun", "status": "ACTIVE",
        "tags": ["massage gun", "recovery", "kneadly"],
        "productOptions": [{"name": "Colour", "values": [{"name": "Black"}, {"name": "Grey"}]},
                           {"name": "Pack", "values": [{"name": "One"}, {"name": "Two"}]}],
        "variants": variants}}, field="productSet")
    pid = r["product"]["id"]
    print(f"   {r['product']['title']} → {pid}")
    for v in r["product"]["variants"]["nodes"]:
        print(f"     {v['title']:<16} {v['price']:>8}  {v['sku']}")

    print("→ lastar opp bilete…")
    s.run(Q_MEDIA, {"id": pid, "media": [
        {"originalSource": f"{SITE}/bilder/{fn}", "alt": alt, "mediaContentType": "IMAGE"}
        for fn, alt in IMAGES]}, field="productCreateMedia")
    print(f"   {len(IMAGES)} bilete sende til Shopify")

    print("→ lagar sider…")
    for title, body in pages.items():
        try:
            s.run(Q_PAGE, {"page": {"title": title, "body": body, "isPublished": True}},
                  field="pageCreate")
            print(f"   {title}")
        except RuntimeError as e:
            print(f"   {title}: {e}")

    print("→ set policyar…")
    pol = {"REFUND_POLICY": pages.get("Shipping & returns", ""),
           "PRIVACY_POLICY": pages.get("Privacy policy", ""),
           "TERMS_OF_SERVICE": pages.get("Terms of service", ""),
           "SHIPPING_POLICY": pages.get("Shipping & returns", "")}
    for t, b in pol.items():
        if not b:
            continue
        try:
            s.run(Q_POLICY, {"policy": {"type": t, "body": b}}, field="shopPolicyUpdate")
            print(f"   {t}")
        except RuntimeError as e:
            print(f"   {t}: {e}")

    print(f"\n✓ Ferdig. Sjå produktet i admin: https://{shop}/admin/products")
    print("  Står att i Shopify: tema og forsidetekst, Shopify Payments, "
          "og CJ-appen frå app-butikken.")


if __name__ == "__main__":
    main()
