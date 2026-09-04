(function () {
  "use strict";

  /* ---------- keep mobile nav flush under the (variable-height) header ---------- */
  var header = document.querySelector(".site-header");
  function syncHeaderHeight() {
    if (header) {
      document.documentElement.style.setProperty("--header-h", header.offsetHeight + "px");
    }
  }
  syncHeaderHeight();
  window.addEventListener("resize", syncHeaderHeight);

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.querySelector(".mobile-nav");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      mobileNav.classList.toggle("is-open", !open);
      document.body.classList.toggle("no-scroll", !open);
    });
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("is-open");
        document.body.classList.remove("no-scroll");
      });
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && mobileNav.classList.contains("is-open")) {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("is-open");
        document.body.classList.remove("no-scroll");
        toggle.focus();
      }
    });
  }

  /* ---------- scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal-on-scroll");
  if (revealEls.length) {
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-visible");
              io.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add("is-visible"); });
    }
  }

  /* ---------- opening chess-piece reveal (home page only) ---------- */
  var overlay = document.querySelector(".reveal-overlay");
  if (overlay) {
    var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var alreadySeen = false;
    try {
      alreadySeen = sessionStorage.getItem("gcf-reveal-seen") === "1";
    } catch (e) { /* storage unavailable — treat as not seen */ }

    if (reduced || alreadySeen) {
      overlay.classList.add("is-done");
      document.body.classList.add("is-revealed");
    } else {
      document.body.classList.add("no-scroll");
      requestAnimationFrame(function () {
        overlay.setAttribute("data-stage", "in");
      });
      setTimeout(function () {
        overlay.setAttribute("data-stage", "move");
      }, 520);
      setTimeout(function () {
        overlay.setAttribute("data-stage", "out");
        document.body.classList.remove("no-scroll");
        document.body.classList.add("is-revealed");
      }, 1120);
      setTimeout(function () {
        overlay.classList.add("is-done");
        try { sessionStorage.setItem("gcf-reveal-seen", "1"); } catch (e) {}
      }, 1650);

      overlay.addEventListener("click", skipReveal);
      window.addEventListener("keydown", function skip(e) {
        if (e.key === "Enter" || e.key === " " || e.key === "Escape") {
          skipReveal();
          window.removeEventListener("keydown", skip);
        }
      });
    }
  } else {
    document.body.classList.add("is-revealed");
  }

  function skipReveal() {
    var el = document.querySelector(".reveal-overlay");
    if (!el || el.classList.contains("is-done")) return;
    el.classList.add("is-done");
    document.body.classList.remove("no-scroll");
    document.body.classList.add("is-revealed");
    try { sessionStorage.setItem("gcf-reveal-seen", "1"); } catch (e) {}
  }
})();
