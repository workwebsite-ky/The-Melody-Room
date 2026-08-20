/* ==========================================================================
   THE MELODY ROOM — behaviour
   No dependencies. Every module guards for missing elements so the same
   file can be loaded on every page.
   ========================================================================== */
(function () {
  "use strict";

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------ preloader */
  function preloader() {
    var el = $("#preloader");
    if (!el) return;
    var lift = function () {
      setTimeout(function () {
        el.classList.add("is-done");
        document.body.style.removeProperty("overflow");
        setTimeout(function () { el.remove(); }, 800);
      }, reduceMotion ? 0 : 700);
    };
    document.body.style.overflow = "hidden";
    if (document.readyState === "complete") lift();
    else window.addEventListener("load", lift);
    // Safety net: never trap the visitor behind the loader
    setTimeout(lift, 3500);
  }

  /* ---------------------------------------------------------- sticky nav */
  function nav() {
    var bar = $(".nav");
    if (!bar) return;
    var onScroll = function () {
      bar.classList.toggle("is-stuck", window.scrollY > 30);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    /* mobile menu */
    var burger = $(".burger"), links = $(".nav-links");
    if (burger && links) {
      burger.addEventListener("click", function () {
        var open = links.classList.toggle("is-open");
        burger.classList.toggle("is-open", open);
        burger.setAttribute("aria-expanded", open ? "true" : "false");
      });
      $$("a", links).forEach(function (a) {
        a.addEventListener("click", function () {
          links.classList.remove("is-open");
          burger.classList.remove("is-open");
          burger.setAttribute("aria-expanded", "false");
        });
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && links.classList.contains("is-open")) burger.click();
      });
    }

    /* mark the current page in the nav */
    var here = location.pathname.split("/").pop() || "index.html";
    $$(".nav-links a[href]").forEach(function (a) {
      var target = a.getAttribute("href").split("#")[0];
      if (target && target === here) a.classList.add("is-current");
    });
  }

  /* ----------------------------------------------- SIGNATURE: the spotlight
     The warm pool of light follows the pointer across the hero. On touch
     devices (and with reduced motion) it drifts slowly on its own instead,
     so the room still feels lit. */
  function spotlight() {
    var light = $(".spotlight");
    if (!light) return;
    var hero = light.closest(".hero") || light.parentElement;
    var canHover = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

    if (canHover && !reduceMotion) {
      hero.addEventListener("pointermove", function (e) {
        var r = hero.getBoundingClientRect();
        light.style.transform =
          "translate3d(" + (e.clientX - r.left) + "px," + (e.clientY - r.top) + "px,0)";
      });
      return;
    }

    /* ambient drift fallback */
    if (reduceMotion) return;
    var t = 0;
    (function drift() {
      t += 0.0045;
      var r = hero.getBoundingClientRect();
      var x = r.width  * (0.5 + 0.26 * Math.sin(t));
      var y = r.height * (0.45 + 0.16 * Math.cos(t * 0.8));
      light.style.transform = "translate3d(" + x + "px," + y + "px,0)";
      requestAnimationFrame(drift);
    })();
  }

  /* ------------------------------------------------------- scroll reveals */
  function reveals() {
    var items = $$("[data-reveal]");
    if (!items.length) return;
    if (!("IntersectionObserver" in window) || reduceMotion) {
      items.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -9% 0px", threshold: 0.08 });

    items.forEach(function (el, i) {
      // Stagger siblings so groups cascade rather than popping together
      if (!el.style.getPropertyValue("--d")) {
        var sibs = el.parentElement ? $$("[data-reveal]", el.parentElement) : [];
        var idx = sibs.indexOf(el);
        el.style.setProperty("--d", (idx > 0 ? Math.min(idx, 5) * 90 : 0) + "ms");
      }
      io.observe(el);
    });
  }

  /* ----------------------------------------------------- animated counters */
  function counters() {
    var nums = $$("[data-count]");
    if (!nums.length) return;

    var run = function (el) {
      var target = parseFloat(el.getAttribute("data-count"));
      var dur = 1500, t0 = null;
      var dec = (target % 1 !== 0) ? 1 : 0;
      if (reduceMotion) { el.textContent = target.toFixed(dec); return; }
      requestAnimationFrame(function step(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);           // easeOutCubic
        el.textContent = (target * eased).toFixed(dec);
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target.toFixed(dec);
      });
    };

    if (!("IntersectionObserver" in window)) { nums.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        run(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.5 });
    nums.forEach(function (n) { io.observe(n); });
  }

  /* ------------------------------------------------------- FAQ accordion */
  function faq() {
    var items = $$(".faq-item");
    if (!items.length) return;

    items.forEach(function (item) {
      var btn = $(".faq-q", item), panel = $(".faq-a", item);
      if (!btn || !panel) return;

      btn.addEventListener("click", function () {
        var isOpen = item.classList.contains("is-open");

        // close siblings — one answer at a time keeps the list scannable
        items.forEach(function (other) {
          if (other === item) return;
          other.classList.remove("is-open");
          var ob = $(".faq-q", other), op = $(".faq-a", other);
          if (ob) ob.setAttribute("aria-expanded", "false");
          if (op) op.style.height = "0px";
        });

        item.classList.toggle("is-open", !isOpen);
        btn.setAttribute("aria-expanded", isOpen ? "false" : "true");
        panel.style.height = isOpen ? "0px" : panel.scrollHeight + "px";
      });
    });

    // keep an open panel correctly sized if the text rewraps
    window.addEventListener("resize", function () {
      items.forEach(function (item) {
        if (!item.classList.contains("is-open")) return;
        var p = $(".faq-a", item);
        if (p) p.style.height = p.scrollHeight + "px";
      });
    });
  }

  /* ---------------------------------------------------------- back to top */
  function toTop() {
    var btn = $(".to-top");
    if (!btn) return;
    var onScroll = function () {
      btn.classList.toggle("is-shown", window.scrollY > 550);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });
  }

  /* -------------------------------------------------------- light parallax */
  function parallax() {
    var els = $$("[data-parallax]");
    if (!els.length || reduceMotion) return;
    var ticking = false;

    var frame = function () {
      var vh = window.innerHeight;
      els.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var speed = parseFloat(el.getAttribute("data-parallax")) || 0.12;
        var offset = (r.top + r.height / 2 - vh / 2) * speed;
        el.style.transform = "translate3d(0," + offset.toFixed(2) + "px,0)";
      });
      ticking = false;
    };

    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(frame);
    }, { passive: true });
    frame();
  }

  /* --------------------------------------------------------- contact form
     No backend is assumed. The form validates in the browser, then hands
     the message to the visitor's own mail client addressed to the venue —
     so it works the moment the site is uploaded, with nothing to configure.
     Swap `handoff()` for a fetch() to Formspree/Netlify Forms later. */
  function contactForm() {
    var form = $("#contact-form");
    if (!form) return;
    var status = $("#form-status");
    var TO = form.getAttribute("data-to") || "themelodyroom417@yahoo.com";

    var fail = function (field, msg) {
      var wrap = field.closest(".field");
      if (!wrap) return;
      wrap.classList.add("has-error");
      var e = $(".field-error", wrap);
      if (e && msg) e.textContent = msg;
    };
    var clear = function (field) {
      var wrap = field.closest(".field");
      if (wrap) wrap.classList.remove("has-error");
    };

    $$("input, textarea, select", form).forEach(function (f) {
      f.addEventListener("input", function () { clear(f); });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      var name = $("#name", form), email = $("#email", form),
          topic = $("#topic", form), message = $("#message", form);

      if (!name.value.trim())  { fail(name, "Tell us who you are."); ok = false; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) {
        fail(email, "Check the email address — we reply to this one."); ok = false;
      }
      if (message.value.trim().length < 10) {
        fail(message, "Add a little more detail so we can help."); ok = false;
      }
      if (!ok) {
        var firstBad = $(".field.has-error input, .field.has-error textarea", form);
        if (firstBad) firstBad.focus();
        return;
      }

      var subject = "[" + (topic ? topic.value : "Website") + "] " + name.value.trim();
      var body =
        "Name: "    + name.value.trim()  + "\n" +
        "Email: "   + email.value.trim() + "\n" +
        (topic ? "About: " + topic.value + "\n" : "") +
        "\n" + message.value.trim() + "\n";

      window.location.href = "mailto:" + TO +
        "?subject=" + encodeURIComponent(subject) +
        "&body="    + encodeURIComponent(body);

      if (status) {
        status.textContent =
          "Your email app is opening with the message ready. Press send and we'll " +
          "reply within two business days. If nothing opened, email " + TO + " directly.";
        status.classList.add("is-shown");
      }
      form.reset();
    });
  }

  /* ------------------------------------------------------ marquee doubling */
  /* Duplicate the track once so the loop has no visible seam. */
  function marquee() {
    $$(".marquee").forEach(function (m) {
      var track = $("ul", m);
      if (!track) return;
      var clone = track.cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      m.appendChild(clone);
    });
  }

  /* ------------------------------------------------------------- misc bits */
  function misc() {
    $$("[data-year]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  /* ------------------------------------------------------------------ init */
  function init() {
    preloader(); nav(); spotlight(); reveals(); counters();
    faq(); toTop(); parallax(); contactForm(); marquee(); misc();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
