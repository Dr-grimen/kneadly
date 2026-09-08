#!/usr/bin/env python3
"""
Lager dei statiske underside-filene til Kneadly ut frå ein felles mal, slik at
header, footer og <head> aldri kjem ut av synk mellom sidene.

Køyr:  python3 build_pages.py
index.html er handskriven og blir IKKJE rørt av dette skriptet.
"""

import pathlib

EMAIL = "kneadlyhelp@gmail.com"          # <-- byt til di eiga adresse
COMPANY = "Indokalo AS"                 # verifisert mot Brønnøysund 1.9.2026
ORGNR = "937 822 553"
ADDRESS = "Nygardsvegen 36, 5419 Fitjar, Norway"

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Kneadly</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%230f766e'/><text x='16' y='23' font-family='Inter,Arial' font-size='19' font-weight='700' fill='%23fff' text-anchor='middle'>K</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v=4">
</head>
<body>

<div class="announce">Free worldwide shipping &middot; 30-day money back</div>

<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html">Kneadly<span>.</span></a>
    <nav class="nav">
      <a href="index.html">Shop</a>
      <a href="faq.html">FAQ</a>
      <a href="shipping.html">Shipping</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</header>

<div class="crumb">
  <div class="wrap"><a href="index.html">Home</a><span>&rsaquo;</span>{crumb}</div>
</div>

<main class="wrap">
  <div class="page">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
{body}
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html">Kneadly<span>.</span></a>
        <p>One massage gun, sold properly. Free shipping worldwide, 30 days to change your mind, and a
           person on the other end of the email.</p>
      </div>
      <div>
        <h4>Shop</h4>
        <ul>
          <li><a href="index.html">Kneadly Mini</a></li>
        </ul>
      </div>
      <div>
        <h4>Help</h4>
        <ul>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="shipping.html">Shipping &amp; returns</a></li>
          <li><a href="contact.html">Contact us</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About Kneadly</a></li>
          <li><a href="terms.html">Terms of service</a></li>
          <li><a href="privacy.html">Privacy policy</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      <span>&copy; 2026 Kneadly. All rights reserved.</span>
      <span>Prices in US dollars, shipping included.</span>
    </div>
  </div>
</footer>

<script src="shop.js?v=3"></script>
</body>
</html>
"""

LEGAL_ENTITY = (
    f'    <div class="note"><strong>Who you are buying from.</strong> Kneadly is a trading name of '
    f'{COMPANY}, organisation number {ORGNR}, {ADDRESS}. '
    f'Questions and legal notices go to <a href="mailto:{EMAIL}">{EMAIL}</a>.</div>'
)

PAGES = {}

# --------------------------------------------------------------------------- FAQ

PAGES["faq.html"] = dict(
    title="FAQ", crumb="FAQ", eyebrow="Questions", h1="Frequently asked questions",
    desc="How to use the Kneadly Mini, where not to use it, delivery times, and how returns work.",
    robots="index,follow",
    body="""    <p>If your question is not here, write to us at
       <a href="mailto:{email}">{email}</a> and a person will answer, usually the same day.</p>

    <h2>Using it</h2>
    <div class="faq-list">
      <details class="panel">
        <summary>Is it strong enough to do anything?</summary>
        <div class="body">
          <p>Yes. The most common surprise in the reviews is how hard it hits for its size &mdash; one buyer
             compares the top speed to a rotary hammer. It is not as deep as a full-size gun on the very
             highest setting, but for shoulders, calves and backs it is more than most people want.</p>
        </div>
      </details>
      <details class="panel">
        <summary>Where should I not use it?</summary>
        <div class="body">
          <p>Not on bone &mdash; spine, shoulder blade, kneecap, shin, collarbone. Not on the front or sides
             of the neck. Not on a fresh injury, a bruise, a varicose vein, or anywhere that hurts rather
             than aches.</p>
          <p>If you are pregnant, have a heart condition, a blood-clotting disorder, a pacemaker, or are
             recovering from surgery, ask your doctor before using it. It is a tool for tight muscles.
             It is not a treatment for any condition and we do not claim it is.</p>
        </div>
      </details>
      <details class="panel">
        <summary>Which head do I use for what?</summary>
        <div class="body">
          <ul>
            <li><strong>Ball</strong> &mdash; the default. Shoulders, glutes, thighs, calves, most things.</li>
            <li><strong>Bullet</strong> &mdash; one specific knot. Use it briefly and on a low speed.</li>
            <li><strong>Fork</strong> &mdash; either side of the spine, the Achilles, the neck from behind.</li>
            <li><strong>Flat</strong> &mdash; general use on larger, flatter areas, and anyone who finds the ball too pointed.</li>
          </ul>
        </div>
      </details>
      <details class="panel">
        <summary>How loud is it?</summary>
        <div class="body">
          <p>Quieter than a hairdryer, louder than an electric toothbrush. Fine with the TV on; not next to
             a sleeping baby. We do not quote decibels because the supplier does not publish a tested figure.</p>
        </div>
      </details>
      <details class="panel">
        <summary>How long does the battery last?</summary>
        <div class="body">
          <p>The display shows the charge, so you are never guessing. Buyers describe it lasting a good
             number of sessions between charges. We will not invent an hours figure &mdash; it depends on
             which speed you use and for how long.</p>
        </div>
      </details>
      <details class="panel">
        <summary>The charging cable seems flimsy.</summary>
        <div class="body">
          <p>It is. Several buyers say theirs was weak or stopped working. The gun charges over standard
             USB-C, so the cable from your phone works and is better. If the gun itself will not charge
             with a known-good cable, that is a fault and we refund you.</p>
        </div>
      </details>
      <details class="panel">
        <summary>The box arrived dented.</summary>
        <div class="body">
          <p>That is the most common complaint about this model and almost every one adds &laquo;but the gun
             was fine&raquo;. Open it before you worry. If the gun itself is damaged, write to us and we
             replace or refund it &mdash; no photos of the packaging needed.</p>
        </div>
      </details>
    </div>

    <h2>Ordering and delivery</h2>
    <div class="faq-list">
      <details class="panel">
        <summary>How long does delivery take?</summary>
        <div class="body">
          <p>Eight to sixteen days, with tracking. Orders are processed within one to two business days
             and then ship from our supplier directly to you.</p>
        </div>
      </details>
      <details class="panel">
        <summary>Why so long?</summary>
        <div class="body">
          <p>Because there is no warehouse in the middle. Your order goes from the manufacturer to your
             door. That is the honest reason for both the wait and the price — a shop holding stock
             locally would charge roughly double for the same device.</p>
        </div>
      </details>
      <details class="panel">
        <summary>Will I pay customs or import VAT?</summary>
        <div class="body">
          <p>It depends on where you live, and we would rather say so than promise you something we
             cannot control. Most orders of this value arrive with nothing to pay, but import rules
             change and some countries charge VAT on low-value parcels. If you are charged an import fee
             on a Kneadly order, send us the receipt and we will refund it.</p>
        </div>
      </details>
      <details class="panel">
        <summary>Can I change or cancel my order?</summary>
        <div class="body">
          <p>Yes, within 24 hours of placing it, as long as it has not already shipped. Email us with
             your order number.</p>
        </div>
      </details>
      <details class="panel">
        <summary>My tracking has not moved for a week.</summary>
        <div class="body">
          <p>That is common in the first stretch and usually means the parcel is in transit between
             carriers. If it has not updated for fourteen days, write to us and we will either chase it
             or refund you.</p>
        </div>
      </details>
    </div>

    <h2>Money</h2>
    <div class="faq-list">
      <details class="panel">
        <summary>How do returns work?</summary>
        <div class="body">
          <p>Tell us within 30 days of delivery that you want your money back, and we refund you in full.
             <strong>You keep it.</strong> Posting it back to Asia costs nearly as much as the gun, so we do not ask you to.</p>
        </div>
      </details>
      <details class="panel">
        <summary>What if it never arrives?</summary>
        <div class="body">
          <p>Full refund. Every order is tracked, and if the parcel is lost or undeliverable to your
             address you get all your money back.</p>
        </div>
      </details>
      <details class="panel">
        <summary>Is my card safe?</summary>
        <div class="body">
          <p>Payment is handled end to end by Stripe. Your card number is entered on Stripe's own
             checkout page and never reaches this website or us.</p>
        </div>
      </details>
    </div>
""".replace("{email}", EMAIL),
)

# --------------------------------------------------------------------- Shipping

PAGES["shipping.html"] = dict(
    title="Shipping &amp; returns", crumb="Shipping &amp; returns",
    eyebrow="Policies", h1="Shipping &amp; returns",
    desc="Free worldwide shipping with tracking, 8-16 day delivery, and a 30-day refund where you keep the product.",
    robots="index,follow",
    body="""    <p>Short version: shipping is free, it takes eight to sixteen days, and if you want your
       money back within 30 days you get it without posting anything.</p>

    <h2>Shipping</h2>
    <p>Free on every order, with no minimum. Orders are processed within one to two business days, then
       ship from our supplier directly to your address. You get a tracking link by email as soon as the
       parcel moves.</p>

    <table class="ship">
      <tr><th>Method</th><th>Delivery</th><th>Tracking</th><th>Cost</th></tr>
      <tr><td>Standard, worldwide</td><td>8&ndash;16 days</td><td>Yes</td><td>Free</td></tr>
    </table>

    <p>We ship to most countries. If it turns out we cannot deliver to your address, we tell you and
       refund you straight away rather than leaving the order open.</p>

    <h2>Customs and import VAT</h2>
    <p>Parcels of this value usually arrive with nothing to pay, but import rules vary by country and
       they change. We will not promise you something we do not control. If you are charged an import fee
       on a Kneadly order, email us the receipt and we refund the fee.</p>

    <h2>Returns and refunds</h2>
    <p>You have <strong>30 days from the day your parcel arrives</strong> to decide you do not want it.
       Email us within that window and we refund the full amount you paid, shipping included.</p>
    <ul>
      <li><strong>You keep it.</strong> We do not ask you to post it back. Return postage on a
          small parcel to Asia costs more than the device, and making you pay it would be a way of
          making the refund not happen.</li>
      <li>You do not need the original packaging, and it does not matter that you have used it.</li>
      <li>Refunds go back to the card you paid with, and take five to seven business days to appear.</li>
      <li>If it arrived broken, send a photo. Same outcome, no questions.</li>
    </ul>

    <h2>Right of withdrawal (EU, EEA and UK)</h2>
    <p>If you are buying as a consumer in the EU, EEA or UK you have a statutory right to withdraw from
       the purchase within 14 days of receiving it, and this right exists whatever we write here. Our own
       30-day policy above is longer and simpler, so in practice you will want to use that one. Either
       way, one email is enough.</p>

    <h2>Lost, late and undelivered parcels</h2>
    <ul>
      <li>Tracking that has not updated in 14 days: write to us and we chase it or refund you.</li>
      <li>Marked delivered but nothing arrived: tell us within 7 days and we replace or refund.</li>
      <li>Wrong address given at checkout: email us within 24 hours and we can still fix it.</li>
    </ul>

""" + LEGAL_ENTITY,
)

# ------------------------------------------------------------------------ About

PAGES["about.html"] = dict(
    title="About", crumb="About", eyebrow="Our story", h1="About Kneadly",
    desc="A one-product shop. What we sell, how it reaches you, and what we are honest about.",
    robots="index,follow",
    body="""    <p>Kneadly sells one thing: a compact massage gun that gets the knots out of tight muscles.
       That is the entire shop.</p>

    <h2>Why only one product</h2>
    <p>Most shops of this kind list two hundred gadgets, describe none of them properly, and hope
       something sticks. We would rather sell one device, learn it properly, and be able to answer any
       question about it in one email. If we ever add a second product it will be because we use it
       ourselves, not because it was trending.</p>

    <h2>Where it comes from, plainly</h2>
    <p>We do not manufacture this massage gun and we have never claimed to. It is made in China, and your
       order ships from the manufacturer straight to your door rather than through a warehouse we rent.
       That is why delivery takes eight to sixteen days, and it is also why the price is $79.99 with
       shipping included instead of well over a hundred in a high-street shop.</p>
    <p>Plenty of shops run exactly this model and dress it up as a design studio in Copenhagen. We would
       rather tell you and let you decide.</p>

    <h2>What we do add</h2>
    <p>Three things you do not get buying the same device from a marketplace listing:</p>
    <ul>
      <li><strong>A straight description.</strong> Including the parts that are not flattering — see the
          <a href="index.html#evidence">review numbers</a> on the product page, failures and all.</li>
      <li><strong>A refund that actually works.</strong> Thirty days, no return postage, no argument.</li>
      <li><strong>Someone to write to.</strong> A person, in a day, in a language you can read.</li>
    </ul>

    <h2>When something goes wrong</h2>
    <p>It will, occasionally. Small electronics have a failure rate and shipping across the world takes
       time. Our position is simple: if the thing you bought does not work, or does not turn up, you
       should not be out of pocket and you should not have to fight for it.</p>

""" + LEGAL_ENTITY,
)

# ---------------------------------------------------------------------- Contact

PAGES["contact.html"] = dict(
    title="Contact", crumb="Contact", eyebrow="Contact us", h1="Get in touch",
    desc="Email Kneadly about an order, a return, or whether the Kneadly Mini is right for a particular ache.",
    robots="index,follow",
    body="""    <p>Questions about an order, a refund, or whether it is right for a particular ache — write to us. A person reads it, normally within one business day.</p>

    <div class="contact-box">
      <div class="eyebrow">Email</div>
      <a class="mail" href="mailto:{email}">{email}</a>
      <p style="margin:16px 0 0">If it is about an existing order, include your <strong>order number</strong>
         and the email address you used at checkout. It roughly halves how long the whole thing takes.</p>
    </div>

    <h2>What we can sort out quickly</h2>
    <ul>
      <li>Where your parcel is, and tracking that has stopped updating</li>
      <li>Changing or cancelling an order within 24 hours of placing it</li>
      <li>Refunds &mdash; including the 30-day one where you keep the gun</li>
      <li>A unit that arrived dead or stopped working</li>
      <li>Which head to use, and where not to use it</li>
    </ul>

    <h2>What we cannot do</h2>
    <ul>
      <li>Speed up a parcel that has already left. We can tell you where it is, and refund you if it is
          genuinely stuck, but we cannot make customs move faster.</li>
      <li>Give medical advice. If something hurts rather than aches, see a doctor, not a massage gun.</li>
    </ul>

""".replace("{email}", EMAIL) + LEGAL_ENTITY,
)

# ------------------------------------------------------------------------ Terms

PAGES["terms.html"] = dict(
    title="Terms of service", crumb="Terms", eyebrow="Legal", h1="Terms of service",
    desc="The terms that apply when you buy from Kneadly.",
    robots="index,follow",
    body="""    <p>Last updated 6 September 2026. These terms apply to every order placed through this
       website. Buying something here means you accept them.</p>

""" + LEGAL_ENTITY + """

    <h2>1. What we sell</h2>
    <p>The Kneadly Mini, a compact rechargeable massage gun, in two colours, singly or in a pack of two.
       We describe it as accurately as we can, including its known weaknesses. Product photographs are
       supplied by the manufacturer; colours on your screen may differ slightly from the item.</p>

    <h2>2. Orders and prices</h2>
    <p>All prices are in US dollars and include worldwide shipping. A price shown on this site is an
       invitation to buy, not a binding offer: if a price is obviously wrong through a technical error we
       may cancel the order and refund you in full rather than honour it. Your order is accepted when we
       send you an order confirmation by email.</p>

    <h2>3. Payment</h2>
    <p>Payment is processed by Stripe. Card details are entered on Stripe's own checkout page and are
       never seen or stored by us. Stripe's terms apply to the payment itself.</p>

    <h2>4. Delivery</h2>
    <p>Orders are processed within one to two business days and typically arrive within eight to sixteen
       days. These are estimates, not guarantees: carriers and customs are outside our control. If a
       parcel is lost or cannot be delivered to the address you gave, you get a full refund. You are
       responsible for giving a correct delivery address; tell us within 24 hours if you got it wrong and
       we will usually still be able to change it.</p>

    <h2>5. Import duties</h2>
    <p>Any import duty or VAT charged in your country is, legally, yours to pay. As a matter of policy we
       refund it: send us the receipt and we will put it back on your card.</p>

    <h2>6. Returns, refunds and your right to withdraw</h2>
    <p>You may cancel any order and claim a full refund within 30 days of the date your parcel arrives,
       for any reason or none. You do not have to return the item. Refunds are made to the original
       payment method within five to seven business days of us agreeing the refund.</p>
    <p>If you are a consumer in the EU, EEA or UK you also have a statutory right of withdrawal of at
       least 14 days from delivery. Nothing on this page limits that right, or any other right you have
       under the consumer law of the country you live in.</p>

    <h2>7. Faults</h2>
    <p>If the gun arrives damaged, dead, or fails in normal use, tell us and we will refund or replace
       it. Statutory guarantee periods under your national consumer law apply on top of our own policy.
       Damage from dropping the unit, immersing it in water, or running it against a hard surface is not
       a fault.</p>

    <h2>8. Safe use</h2>
    <p>The device is a percussive massager. Use it on muscle only &mdash; never on bone, joints, the
       front or sides of the neck, the head, or any injury, bruise, swelling or varicose vein. Do not use
       it if you are pregnant, or have a heart condition, a pacemaker, a blood-clotting disorder or are
       recovering from surgery, without asking a doctor first. It is not a medical device and makes no
       therapeutic claim. Keep it away from children, do not immerse it in water, and charge it only from
       a standard USB-C source. We are not liable for injury caused by use contrary to these instructions.</p>

    <h2>9. Limits on our liability</h2>
    <p>Our liability for any order is limited to the amount you paid for it, except where the law does
       not allow that limit — in particular for death or personal injury caused by negligence, for fraud,
       and for your statutory consumer rights, none of which are excluded or limited here.</p>

    <h2>10. This website</h2>
    <p>The text, layout and photographs on this site are ours or are used with the supplier's permission,
       and may not be copied wholesale. We may change these terms; the version published when you place
       your order is the one that governs it.</p>

    <h2>11. Law and disputes</h2>
    <p>These terms are governed by Norwegian law. If you are a consumer, this does not deprive you of the
       protection of mandatory rules in your own country of residence, and you may bring proceedings
       there. Before that, please email us — nearly everything is fixable in one message. EU consumers
       may also use the European Commission's online dispute resolution platform.</p>
""",
)

# ---------------------------------------------------------------------- Privacy

PAGES["privacy.html"] = dict(
    title="Privacy policy", crumb="Privacy", eyebrow="Legal", h1="Privacy policy",
    desc="What data Kneadly collects, why, and how to have it deleted.",
    robots="index,follow",
    body="""    <p>Last updated 6 September 2026. Short version: we collect what an order needs and nothing
       else, this website sets no cookies of its own, and you can have your data deleted by asking.</p>

""" + LEGAL_ENTITY + """

    <h2>What we collect</h2>
    <ul>
      <li><strong>When you order:</strong> your name, email address, delivery address and what you
          bought. We need these to ship the parcel and to find your order when you write to us.</li>
      <li><strong>When you email us:</strong> your message and your email address.</li>
      <li><strong>Never:</strong> your card number. Payment happens on Stripe's own page. We see that a
          payment succeeded, the last four digits, and nothing more.</li>
    </ul>

    <h2>Why we are allowed to hold it</h2>
    <p>Order data is processed to perform the contract you entered into when you bought something
       (GDPR article 6(1)(b)). Accounting records are kept because Norwegian bookkeeping law requires it
       (article 6(1)(c)). Email correspondence is kept on the basis of our legitimate interest in being
       able to handle your case (article 6(1)(f)).</p>

    <h2>Who else sees it</h2>
    <ul>
      <li><strong>Stripe</strong> — payment processing. Stripe is the controller of the payment data it
          collects; see stripe.com/privacy.</li>
      <li><strong>Our supplier and the carrier</strong> — they receive the name and address needed to
          deliver your parcel, and nothing else. This means your delivery address is transferred outside
          the EEA, to China, which is what makes the shipment possible.</li>
      <li><strong>Our email provider</strong> — to receive and answer your messages.</li>
    </ul>
    <p>We do not sell your data, and we do not share it for advertising.</p>

    <h2>Cookies and tracking</h2>
    <p>This website sets no cookies of its own and runs no analytics. It loads a web font from Google
       Fonts, which means Google's servers see the IP address your browser connects from. That is the
       only third-party request the page makes.</p>
    <p>If we later add advertising or analytics tools, we will say so here and ask for your consent
       first.</p>

    <h2>How long we keep it</h2>
    <p>Accounting records: five years, as Norwegian law requires. Email correspondence: two years.
       Anything else: deleted when it is no longer needed.</p>

    <h2>Your rights</h2>
    <p>You can ask us for a copy of your data, ask us to correct it, ask us to delete it, or object to
       our processing of it. Email us and we will act within 30 days, free of charge. If you think we
       have handled your data badly you can complain to the Norwegian Data Protection Authority
       (Datatilsynet) or to the supervisory authority in your own country.</p>

    <h2>Children</h2>
    <p>This shop is not intended for children, and we do not knowingly collect data from anyone under
       16.</p>
""",
)

# --------------------------------------------------------------------------- go

out = pathlib.Path(__file__).parent
for name, page in PAGES.items():
    html = SHELL.format(**page)
    (out / name).write_text(html, encoding="utf-8")
    print("wrote", name, len(html), "bytes")
