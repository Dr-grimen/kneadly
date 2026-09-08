/* ==========================================================================
   Kneadly — shop logic.

   ⚠️  ALT DU NORMALT TRENG Å ENDRE LIGG I `CONFIG` HER OPPE.
   ========================================================================== */

var CONFIG = {

  /* --- 1. Stripe Payment Links -----------------------------------------
     Éi lenke per farge × antal. Står det "PASTE_..." seier knappen
     "Checkout opens soon" i staden for å sende kunden til ei daud side.
  --------------------------------------------------------------------- */
  stripe: {
    black: { 1: "https://buy.stripe.com/8x25kDc2v2Jfc9kgXJ2oE06", 2: "https://buy.stripe.com/dRm3cvgiL3Nj2yKfTF2oE07" },
    grey:  { 1: "https://buy.stripe.com/cNicN5d6zdnTgpA5f12oE08", 2: "https://buy.stripe.com/dRm4gz4A3erX1uG7n92oE09" }
  },

  /* --- 2. Prisar (USD). `full` = same antal til einingspris. ---------- */
  prices: {
    1: { price: 79.99,  full: 79.99  },
    2: { price: 139.99, full: 159.98 }
  },

  currency: "$",

  /* --- 3. Bilete per farge. Første er hovudbiletet. -------------------- */
  images: {
    grey: [
      ["bilder/produkt-1.webp", "Kneadly Mini in grey with its four heads laid out in front"],
      ["bilder/produkt-3.webp", "The mini massage gun with the ball, bullet, fork and flat heads in a row"],
      ["bilder/produkt-5.webp", "The round display showing speed level 6 and the USB-C port"],
      ["bilder/produkt-4.webp", "Close-up of the four attachment heads"],
      ["bilder/produkt-2.webp", "Kneadly Mini in black"]
    ],
    black: [
      ["bilder/produkt-2.webp", "Kneadly Mini in black with its four heads laid out"],
      ["bilder/produkt-3.webp", "The mini massage gun with the ball, bullet, fork and flat heads in a row"],
      ["bilder/produkt-5.webp", "The round display showing speed level 6 and the USB-C port"],
      ["bilder/produkt-4.webp", "Close-up of the four attachment heads"],
      ["bilder/produkt-1.webp", "Kneadly Mini in grey"]
    ]
  },

  colourNames: { black: "Black", grey: "Grey" },

  /* --- 4. Meta-piksel ---------------------------------------------------
     Lim inn piksel-ID-en frå Events Manager (berre tal). Står han tom,
     blir ingenting lasta og ingen data sendt — sida er da heilt sporfri.
     Med ID sender vi: PageView på alle sider, ViewContent på produktsida,
     og InitiateCheckout når nokon trykkjer kjøpsknappen.
  --------------------------------------------------------------------- */
  metaPixel: ""
};

/* ========================================================================== */

(function () {
  "use strict";

  var el = function (id) { return document.getElementById(id); };

  /* ---- Meta-piksel: berre viss ein ID er fylt inn ---- */
  var PIXEL = (CONFIG.metaPixel || "").trim();
  if (/^\d+$/.test(PIXEL)) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}
    (window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', PIXEL);
    window.fbq('track', 'PageView');
  }
  var track = function (ev, data) { if (window.fbq) window.fbq('track', ev, data || {}); };

  if (!el("bundles")) return;

  var state = { colour: "black", pack: 1 };
  var money = function (n) { return CONFIG.currency + n.toFixed(2); };

  var linkFor = function () {
    var url = (CONFIG.stripe[state.colour] || {})[state.pack] || "";
    return /^https?:\/\//.test(url) ? url : null;
  };

  var thumbs = el("thumbs"), main = el("mainImage");

  function renderGallery() {
    var list = CONFIG.images[state.colour] || [];
    thumbs.innerHTML = "";
    list.forEach(function (item, i) {
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-current", i === 0 ? "true" : "false");
      b.setAttribute("aria-label", "Show image " + (i + 1) + " of " + list.length);
      var img = document.createElement("img");
      img.src = item[0]; img.alt = item[1]; img.loading = "lazy";
      b.appendChild(img); thumbs.appendChild(b);
    });
    if (list.length) showImage(0);
  }

  function showImage(i) {
    var list = CONFIG.images[state.colour] || [];
    if (!list[i]) return;
    main.src = list[i][0]; main.alt = list[i][1];
    Array.prototype.forEach.call(thumbs.children, function (b, n) {
      b.setAttribute("aria-current", n === i ? "true" : "false");
    });
  }

  thumbs.addEventListener("click", function (e) {
    var b = e.target.closest("button"); if (!b) return;
    showImage(Array.prototype.indexOf.call(thumbs.children, b));
  });

  function render() {
    var p = CONFIG.prices[state.pack], saved = p.full - p.price;
    el("price").textContent = money(p.price);
    var was = el("priceWas"), save = el("priceSave");
    if (saved > 0.005) { was.textContent = money(p.full); was.hidden = false; save.textContent = "Save " + money(saved); save.hidden = false; }
    else { was.hidden = true; save.hidden = true; }
    el("colourName").textContent = CONFIG.colourNames[state.colour];
    el("bbColour").textContent = CONFIG.colourNames[state.colour];
    el("bbPrice").textContent = money(p.price);
    var url = linkFor();
    [el("buyButton"), el("bbButton")].forEach(function (btn) {
      if (!btn) return;
      if (url) { btn.href = url; btn.removeAttribute("aria-disabled"); btn.textContent = "Buy now"; }
      else { btn.href = "contact.html"; btn.setAttribute("aria-disabled", "true"); btn.textContent = "Checkout opens soon"; }
    });
  }

  function group(container, attr, key) {
    container.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b || !b.dataset[attr]) return;
      Array.prototype.forEach.call(container.children, function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      state[key] = attr === "pack" ? Number(b.dataset.pack) : b.dataset[attr];
      if (key === "colour") renderGallery();
      render();
    });
  }
  group(el("swatches"), "color", "colour");
  group(el("bundles"), "pack", "pack");

  /* ---- konverteringshendingar ---- */
  track('ViewContent', { content_name: 'Kneadly Mini', content_type: 'product', currency: 'USD', value: CONFIG.prices[1].price });
  [el("buyButton"), el("bbButton")].forEach(function (btn) {
    if (!btn) return;
    btn.addEventListener('click', function () {
      if (btn.getAttribute('aria-disabled') === 'true') return;
      track('InitiateCheckout', {
        content_name: 'Kneadly Mini ' + CONFIG.colourNames[state.colour],
        num_items: state.pack, currency: 'USD', value: CONFIG.prices[state.pack].price
      });
    });
  });

  var bar = el("buybar"), anchor = el("buyButton");
  if (bar && anchor && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      var off = !entries[0].isIntersecting;
      bar.classList.toggle("is-shown", off);
      bar.setAttribute("aria-hidden", off ? "false" : "true");
      el("bbButton").tabIndex = off ? 0 : -1;
    }, { rootMargin: "0px 0px -40px 0px" }).observe(anchor);
  }

  renderGallery(); render();
})();
