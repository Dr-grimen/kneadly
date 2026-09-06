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
    black: { 1: "PASTE_BLACK_1", 2: "PASTE_BLACK_2" },
    grey:  { 1: "PASTE_GREY_1",  2: "PASTE_GREY_2"  }
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

  colourNames: { black: "Black", grey: "Grey" }
};

/* ========================================================================== */

(function () {
  "use strict";

  var el = function (id) { return document.getElementById(id); };
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
