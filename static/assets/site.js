(function () {
  "use strict";
  var y = document.getElementById("yr");
  if (y) y.textContent = new Date().getFullYear();

  // mobile menu
  var btn = document.querySelector(".menu-btn"), nav = document.getElementById("nav");
  if (btn && nav) btn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // phone mask (US)
  function fmtPhone(v) {
    var d = v.replace(/\D/g, "");
    if (d.length === 11 && d[0] === "1") d = d.slice(1);
    d = d.slice(0, 10);
    if (d.length < 4) return d;
    if (d.length < 7) return "(" + d.slice(0, 3) + ") " + d.slice(3);
    return "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6);
  }

  var modal = document.getElementById("thanks");
  function openModal() {
    if (!modal) return;
    modal.hidden = false;
    var b = modal.querySelector("[data-close]");
    if (b) b.focus();
  }
  function closeModal() { if (modal) modal.hidden = true; }
  if (modal) {
    modal.addEventListener("click", function (ev) {
      if (ev.target === modal || ev.target.hasAttribute("data-close")) closeModal();
    });
    document.addEventListener("keydown", function (ev) { if (ev.key === "Escape") closeModal(); });
  }

  function track(name, params) {
    try { if (window.gtag) window.gtag("event", name, params || {}); } catch (e) {}
  }
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest('a[href^="tel:"]');
    if (a) track("phone_call_click", { link_url: a.href });
  });

  // carousels
  Array.prototype.forEach.call(document.querySelectorAll(".jobs-band"), function (band) {
    var track = band.querySelector(".carousel");
    Array.prototype.forEach.call(band.querySelectorAll(".car-btn"), function (b) {
      b.addEventListener("click", function () {
        var card = track.querySelector(".job");
        var step = card ? card.getBoundingClientRect().width + 16 : track.clientWidth;
        var dir = +b.getAttribute("data-dir");
        var atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
        if (dir > 0 && atEnd) track.scrollTo({ left: 0 });
        else if (dir < 0 && track.scrollLeft <= 0) track.scrollTo({ left: track.scrollWidth });
        else track.scrollBy({ left: dir * step });
      });
    });
  });

  var forms = document.querySelectorAll("form.lead");
  Array.prototype.forEach.call(forms, function (form) {
    var phone = form.querySelector('input[name="phone"]');
    if (phone) phone.addEventListener("input", function () { phone.value = fmtPhone(phone.value); });
    var page = form.querySelector('input[name="page"]');
    if (page) page.value = location.href;

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var ok = true;
      Array.prototype.forEach.call(form.querySelectorAll("[required]"), function (f) {
        var bad = !f.value.trim() || (f.name === "phone" && f.value.replace(/\D/g, "").length < 10);
        f.classList.toggle("invalid", bad);
        if (bad && ok) { f.focus(); ok = false; }
      });
      if (!ok) return;
      var err = form.querySelector(".form-error");
      var submit = form.querySelector('button[type="submit"]');
      submit.disabled = true; submit.textContent = "Sending…";
      var data = {};
      new FormData(form).forEach(function (v, k) { if (k !== "redirect") data[k] = v; });
      data.subject = "New service request: " + (data.equipment || "equipment") + " — " + data.first_name + " " + data.last_name;
      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json(); }).then(function (res) {
        if (!res.success) throw new Error(res.message || "failed");
        form.reset();
        if (err) err.hidden = true;
        openModal();
        track("generate_lead", { equipment: data.equipment });
      }).catch(function () {
        if (err) err.hidden = false;
      }).then(function () {
        submit.disabled = false; submit.textContent = "Send request";
      });
    });
  });
})();
