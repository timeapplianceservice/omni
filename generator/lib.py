"""Shared layout, components and schema."""
import hashlib
import html
import json
import os

import config as C
from data_equipment import EQUIPMENT, REFRIG, KITCHEN, FORM_EQUIPMENT_OPTIONS
from data_areas import AREAS, CITIES, HOODS, EXT, place
from reviews import REVIEWS

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_site")
PAGES = []  # (path, priority, group)

e = html.escape
TEL = "tel:" + C.PHONE_E164
BIZ_ID = C.SITE_URL + "/#business"


def pick(options, *key):
    """Deterministic variant choice so pages differ but rebuilds are stable."""
    h = int(hashlib.md5("|".join(key).encode()).hexdigest(), 16)
    return options[h % len(options)]


def shuffle(seq, *key):
    return sorted(seq, key=lambda x: hashlib.md5(("|".join(key) + str(x)).encode()).hexdigest())


def url(path):
    return C.SITE_URL + path


def lower_name(eq):
    return eq["name"].lower().replace("&", "and")


# ---------------------------------------------------------------- schema
def opening_hours_spec():
    groups = {}
    for day, o, c in C.HOURS:
        groups.setdefault((o, c), []).append(day)
    return [{"@type": "OpeningHoursSpecification", "dayOfWeek": days, "opens": o, "closes": c}
            for (o, c), days in groups.items()]


def business_schema():
    area_served = [{"@type": "City", "name": "%s, %s" % (a["name"], a["state"])} for a in CITIES + EXT]
    area_served += [{"@type": "Place", "name": "%s, Charlotte, NC" % a["name"].replace(" Charlotte", "")} for a in HOODS]
    d = {
        "@type": "LocalBusiness",
        "@id": BIZ_ID,
        "name": C.BRAND,
        "description": ("Licensed and insured commercial refrigeration and commercial kitchen equipment repair for "
                        "restaurants, cafés, bars, grocery and convenience stores, hotels, schools and healthcare "
                        "kitchens in Charlotte, NC and the surrounding area."),
        "url": C.SITE_URL + "/",
        "telephone": C.PHONE_E164,
        "email": C.EMAIL,
        "priceRange": "$%d service call" % C.SERVICE_CALL,
        "currenciesAccepted": "USD",
        "address": {"@type": "PostalAddress", "addressLocality": C.CITY, "addressRegion": C.STATE, "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": C.GEO[0], "longitude": C.GEO[1]},
        "openingHoursSpecification": opening_hours_spec(),
        "areaServed": area_served,
        "knowsAbout": [eq["name"] + " repair" for eq in EQUIPMENT],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Commercial equipment repair services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": eq["name"] + " Repair",
                                 "url": url("/services/%s/" % eq["slug"])}} for eq in EQUIPMENT]},
        "makesOffer": [{"@type": "Offer", "name": "Commercial service call / diagnostic", "price": str(C.SERVICE_CALL),
                        "priceCurrency": "USD"},
                       {"@type": "Offer", "name": "$%d off any repair" % C.DISCOUNT,
                        "description": "Mention the website or book online to get $%d off your repair." % C.DISCOUNT}],
    }
    same = [x for x in [C.GOOGLE_PROFILE_URL] if x]
    if same:
        d["sameAs"] = same
    return d


def breadcrumb_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (n, p) in enumerate(crumbs)]}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def service_schema(name, path, area_names, desc):
    return {"@type": "Service", "name": name, "serviceType": name, "url": url(path), "description": desc,
            "provider": {"@id": BIZ_ID},
            "areaServed": [{"@type": "Place", "name": n} for n in area_names],
            "offers": {"@type": "Offer", "price": str(C.SERVICE_CALL), "priceCurrency": "USD",
                       "description": "Service call / diagnostic. $%d off the repair when you book online." % C.DISCOUNT}}


# ---------------------------------------------------------------- components
def hours_table():
    rows = "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (d, fmt_range(o, c)) for d, o, c in C.HOURS)
    return '<table class="hours"><caption>Business hours (Eastern Time)</caption>%s</table>' % rows


def fmt_t(t):
    h, m = map(int, t.split(":"))
    suf = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    return "%d:%02d %s" % (h12, m, suf)


def fmt_range(o, c):
    return "%s – %s" % (fmt_t(o), fmt_t(c))


def usp_list():
    items = [
        ("Licensed &amp; insured", "Commercial refrigeration and kitchen equipment technicians"),
        ("$%d service call" % C.SERVICE_CALL, "Clear price before any work starts"),
        ("$%d off your repair" % C.DISCOUNT, "When you book online or mention the website"),
        ("Warranty on every job", "%d-day labor, %d-day parts, extended 1, 3 or 5 years on select work"
         % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS)),
        ("Open 7 days a week", C.HOURS_SHORT),
        ("Same-day service", "When you call early — trucks stocked with common parts"),
    ]
    return '<ul class="usp">%s</ul>' % "".join(
        '<li><span class="tick" aria-hidden="true">✓</span><span><b>%s</b><small>%s</small></span></li>' % (a, b)
        for a, b in items)


def stats_row():
    n_areas = len(AREAS)
    from data_brands import BRANDS
    items = [("7 days", "open every week"), ("%d+" % len(BRANDS), "brands repaired"),
             ("%d" % n_areas, "cities &amp; neighborhoods"), ("1–5 yr", "extended warranty options")]
    return '<div class="stats">%s</div>' % "".join(
        '<div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in items)


def form_html(context=""):
    opts = "".join('<option>%s</option>' % e(o) for o in FORM_EQUIPMENT_OPTIONS)
    return """
<form class="lead" id="request" action="https://api.web3forms.com/submit" method="POST" novalidate>
  <div class="offer-tag">$%(disc)d OFF your repair</div>
  <h2 class="form-title">Request service</h2>
  <p class="form-sub">Takes 30 seconds. We call you back during business hours.</p>
  <input type="hidden" name="access_key" value="%(key)s">
  <input type="hidden" name="subject" value="New service request — %(brand)s">
  <input type="hidden" name="from_name" value="%(brand)s website">
  <input type="hidden" name="page" value="%(ctx)s">
  <input type="hidden" name="redirect" value="%(site)s/thank-you/">
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="row2">
    <label>First name<input name="first_name" autocomplete="given-name" required></label>
    <label>Last name<input name="last_name" autocomplete="family-name" required></label>
  </div>
  <label>Phone number<input name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(___) ___-____" required></label>
  <label>Service address<input name="address" autocomplete="street-address" placeholder="Street, city, ZIP" required></label>
  <label>Type of equipment<select name="equipment" required><option value="">Choose equipment…</option>%(opts)s</select></label>
  <button type="submit" class="btn btn-primary btn-block">Send request</button>
  <p class="form-note">Prefer to talk? Call <a href="%(tel)s">%(phone)s</a></p>
  <p class="form-error" role="alert" hidden>Something went wrong. Please call us at %(phone)s.</p>
</form>""" % dict(disc=C.DISCOUNT, key=e(C.WEB3FORMS_ACCESS_KEY), brand=e(C.BRAND), ctx=e(context), site=C.SITE_URL,
                  opts=opts, tel=TEL, phone=C.PHONE_DISPLAY)


def hero(h1, sub, context, crumbs=None):
    bc = breadcrumbs_html(crumbs) if crumbs else ""
    rest = ""
    if len(sub) > 200 and ". " in sub:
        first, more = sub.split(". ", 1)
        sub, rest = first + ".", more
    after = ('<section class="band intro"><div class="wrap narrow"><p class="lead-p">%s</p></div></section>' % rest) if rest else ""
    return _hero_html(bc, h1, sub, context) + after


def _hero_html(bc, h1, sub, context):
    return """
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      %s
      <h1>%s</h1>
      <p class="lead-p">%s</p>
      %s
      <div class="hero-cta">
        <a class="btn btn-call" href="%s">📞 Call %s</a>
        <a class="btn btn-ghost hide-sm" href="#request">Request service online</a>
      </div>
    </div>
    <div class="hero-form">%s</div>
  </div>
  <div class="wrap">%s</div>
</section>""" % (bc, e(h1), sub, usp_list(), TEL, C.PHONE_DISPLAY, form_html(context), stats_row())


def breadcrumbs_html(crumbs):
    parts = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append('<span aria-current="page">%s</span>' % e(n))
        else:
            parts.append('<a href="%s">%s</a>' % (p, e(n)))
    return '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % " › ".join(parts)


def offer_band():
    return """
<section class="band offer">
  <div class="wrap offer-grid">
    <div><h2>Save $%d on your repair</h2>
    <p>Book online or mention our website when you call and we take <b>$%d off</b> the repair. The service call is a flat
    <b>$%d</b>, and you get a clear price before any work begins — no surprises.</p></div>
    <div class="offer-cta"><a class="btn btn-call" href="%s">Call %s</a><a class="btn btn-primary" href="#request">Claim $%d off</a></div>
  </div>
</section>""" % (C.DISCOUNT, C.DISCOUNT, C.SERVICE_CALL, TEL, C.PHONE_DISPLAY, C.DISCOUNT)


def warranty_block():
    y = C.EXTENDED_WARRANTY_YEARS
    return """
<section class="band soft">
  <div class="wrap">
    <h2>Our warranty</h2>
    <div class="cards3">
      <div class="card"><b class="big">%d days</b><p>Labor warranty on every repair.</p></div>
      <div class="card"><b class="big">%d days</b><p>Parts warranty on every part we install.</p></div>
      <div class="card"><b class="big">%d · %d · %d years</b><p>Extended warranty available on select repairs and installations.
        The exact term is written on your estimate before work starts.</p></div>
    </div>
    <p class="muted"><a href="/warranty/">Read the full warranty terms</a></p>
  </div>
</section>""" % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS, y[0], y[1], y[2])


def steps_block():
    return """
<section class="band">
  <div class="wrap">
    <h2>How it works</h2>
    <ol class="steps">
      <li><b>Call or send the form</b><span>Tell us the equipment and the problem. A dispatcher calls you back.</span></li>
      <li><b>Technician arrives</b><span>Flat $%d service call. We diagnose and give you a written price.</span></li>
      <li><b>You approve the repair</b><span>$%d off the repair when you booked online. Nothing is done without your OK.</span></li>
      <li><b>Covered by warranty</b><span>%d-day labor and %d-day parts on every repair.</span></li>
    </ol>
  </div>
</section>""" % (C.SERVICE_CALL, C.DISCOUNT, C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS)


def hours_block(area_name=None):
    where = area_name or "Charlotte and the surrounding area"
    return """
<section class="band soft" id="hours">
  <div class="wrap hours-grid">
    <div>
      <h2>Hours &amp; contact</h2>
      <p>%s is open <b>%s</b>. We serve %s.</p>
      <p>Phone: <a href="%s"><b>%s</b></a><br>Email: <a href="mailto:%s">%s</a></p>
      <p class="muted">Based in Charlotte, NC. We are a mobile service company — our technicians come to your business.</p>
    </div>
    %s
  </div>
</section>""" % (C.BRAND, C.HOURS_SENTENCE, e(where), TEL, C.PHONE_DISPLAY, C.EMAIL, C.EMAIL, hours_table())


def jobs_block(jobs):
    if not jobs:
        return ""
    from data_equipment import EQ_BY_SLUG
    from data_misc import INDUSTRIES
    cards = []
    for j in jobs:
        q = EQ_BY_SLUG[j["eq"]]
        biz = INDUSTRIES[j["biz"]]["name"]
        cards.append(
            '<li class="job"><div class="job-top"><a class="job-eq" href="/services/%s/">%s</a><span class="job-biz">%s</span></div>'
            '<h3>%s</h3><dl><dt>What we found</dt><dd>%s</dd><dt>What we did</dt><dd>%s</dd></dl>'
            '<p class="job-when">✓ %s</p></li>'
            % (q["slug"], e(q["name"]), e(biz), e(j["problem"]), e(j["found"]), e(j["fixed"]), e(j["when"])))
    return """
<section class="band jobs-band" aria-labelledby="jobs-t">
  <div class="wrap">
    <div class="jobs-head">
      <div><h2 id="jobs-t">Typical jobs we handle</h2>
      <p class="muted">Examples of common repairs on commercial refrigeration and kitchen equipment.</p></div>
      <div class="car-btns"><button class="car-btn" data-dir="-1" aria-label="Previous">‹</button><button class="car-btn" data-dir="1" aria-label="Next">›</button></div>
    </div>
    <ul class="carousel" tabindex="0">%s</ul>
    <p class="muted small">Examples for illustration. Every job is diagnosed on site; parts, time and price depend on the equipment.</p>
  </div>
</section>""" % "".join(cards)


def reviews_block():
    if not REVIEWS:
        return ""
    cards = []
    for r in REVIEWS[:6]:
        stars = "★" * int(r.get("rating", 5))
        cards.append('<figure class="rev"><div class="rev-head"><span class="ava">%s</span><div><b>%s</b>'
                     '<small>%s · %s</small></div></div><div class="stars" aria-label="%d out of 5 stars">%s</div>'
                     '<blockquote>%s</blockquote>%s</figure>'
                     % (e(r["name"][0]), e(r["name"]), e(r.get("source", "")), e(r.get("date", "")),
                        int(r.get("rating", 5)), stars, e(r["text"]),
                        ('<span class="tag">%s</span>' % e(r["tag"])) if r.get("tag") else ""))
    more = ('<p><a href="%s" rel="noopener" target="_blank">See all reviews on Google</a></p>' % C.GOOGLE_PROFILE_URL
            if C.GOOGLE_PROFILE_URL else "")
    return '<section class="band"><div class="wrap"><h2>What customers say</h2><div class="revs">%s</div>%s</div></section>' % (
        "".join(cards), more)


def faq_block(faqs, title="Frequently asked questions"):
    items = "".join('<details><summary>%s</summary><p>%s</p></details>' % (e(q), e(a)) for q, a in faqs)
    return '<section class="band"><div class="wrap narrow"><h2>%s</h2><div class="faq">%s</div></div></section>' % (title, items)


def links_block(title, links, cols=3):
    if not links:
        return ""
    lis = "".join('<li><a href="%s">%s</a></li>' % (p, e(t)) for t, p in links)
    return '<section class="band"><div class="wrap"><h2>%s</h2><ul class="linkgrid c%d">%s</ul></div></section>' % (title, cols, lis)


def section(title, body, cls="band"):
    return '<section class="%s"><div class="wrap narrow"><h2>%s</h2>%s</div></section>' % (cls, title, body)


def ul(items):
    return '<ul class="checks">%s</ul>' % "".join("<li>%s</li>" % e(i) for i in items)


def cta_band(text="Equipment down? Get a technician on the way."):
    return """
<section class="band cta">
  <div class="wrap cta-grid">
    <h2>%s</h2>
    <div><a class="btn btn-call" href="%s">📞 %s</a> <a class="btn btn-light" href="#request">Request service</a></div>
  </div>
</section>""" % (text, TEL, C.PHONE_DISPLAY)


# ---------------------------------------------------------------- layout
NAV = [("Services", "/services/"), ("Brands", "/brands/"), ("Industries", "/industries/"),
       ("Service Areas", "/service-areas/"), ("Pricing", "/pricing/"), ("Warranty", "/warranty/"), ("Contact", "/contact/")]


def header():
    nav = "".join('<a href="%s">%s</a>' % (p, n) for n, p in NAV)
    return """
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span><span class="hide-sm">Open 7 days · </span>%s</span><span class="hide-sm">Commercial refrigeration &amp; kitchen equipment repair · Charlotte, NC</span>
</div></div>
<header class="site-header"><div class="wrap head-row">
  <a class="wordmark" href="/">Commercial <span>Appliances</span></a>
  <nav class="main-nav" id="nav" aria-label="Main">%s</nav>
  <a class="btn btn-call head-call" href="%s">📞 %s</a>
  <button class="menu-btn" aria-controls="nav" aria-expanded="false" aria-label="Menu">☰</button>
</div></header>""" % (C.HOURS_SHORT, nav, TEL, C.PHONE_DISPLAY)


def footer():
    city_links = "".join('<li><a href="/service-areas/%s/">%s</a></li>' % (a["slug"], e(a["name"])) for a in CITIES + EXT)
    hood_links = "".join('<li><a href="/service-areas/%s/">%s</a></li>' % (a["slug"], e(a["name"])) for a in HOODS)
    r_links = "".join('<li><a href="/services/%s/">%s Repair</a></li>' % (q["slug"], e(q["name"])) for q in REFRIG)
    k_links = "".join('<li><a href="/services/%s/">%s Repair</a></li>' % (q["slug"], e(q["name"])) for q in KITCHEN)
    return """
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <p class="wordmark light">Commercial <span>Appliances</span></p>
      <p>Commercial refrigeration and commercial kitchen equipment repair for restaurants, cafés, bars, stores and
      institutional kitchens in Charlotte, NC and nearby cities in North and South Carolina.</p>
      <p><a href="%s"><b>%s</b></a><br><a href="mailto:%s">%s</a></p>
      <p><b>Hours:</b> %s.</p>
      <p>Service call $%d · $%d off repair · %d-day labor / %d-day parts warranty</p>
    </div>
    <div><h3>Refrigeration</h3><ul>%s</ul></div>
    <div><h3>Kitchen equipment</h3><ul>%s</ul></div>
    <div><h3>Cities</h3><ul>%s</ul></div>
    <div><h3>Charlotte neighborhoods</h3><ul>%s</ul></div>
  </div>
  <div class="wrap foot-bottom">
    <p>© <span id="yr">2026</span> %s. Licensed &amp; insured. Charlotte, NC.
    <a href="/about/">About</a> · <a href="/faq/">FAQ</a> · <a href="/problems/">Troubleshooting</a> ·
    <a href="/privacy-policy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/sitemap/">Sitemap</a></p>
    <p class="muted small">%s is an independent service company and is not affiliated with, endorsed by or an
    authorized agent of the equipment manufacturers named on this site. Brand names are trademarks of their owners.</p>
  </div>
</footer>
<div class="callbar" role="navigation" aria-label="Quick contact">
  <a class="cb-call" href="%s">📞 Call %s</a>
  <a class="cb-req" href="#request">Request service</a>
</div>
<div class="modal" id="thanks" hidden role="dialog" aria-modal="true" aria-labelledby="thanks-t">
  <div class="modal-box">
    <div class="modal-ok" aria-hidden="true">✓</div>
    <h2 id="thanks-t">Thank you for your request!</h2>
    <p>The first available operator will contact you shortly.</p>
    <p class="muted">Need help right now? Call <a href="%s">%s</a>.<br>Hours: %s.</p>
    <button class="btn btn-primary" data-close>OK</button>
  </div>
</div>""" % (TEL, C.PHONE_DISPLAY, C.EMAIL, C.EMAIL, C.HOURS_SENTENCE, C.SERVICE_CALL, C.DISCOUNT,
             C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS, r_links, k_links, city_links, hood_links, C.BRAND, C.BRAND,
             TEL, C.PHONE_DISPLAY, TEL, C.PHONE_DISPLAY, C.HOURS_SHORT)


def page(path, title, desc, body, crumbs=None, schema_extra=None, priority=0.6, group="main", noindex=False):
    graph = [business_schema()]
    if crumbs:
        graph.append(breadcrumb_schema(crumbs))
    graph += schema_extra or []
    graph.append({"@type": "WebPage", "@id": url(path) + "#webpage", "url": url(path), "name": title,
                  "description": desc, "isPartOf": {"@type": "WebSite", "@id": C.SITE_URL + "/#website",
                                                     "url": C.SITE_URL + "/", "name": C.BRAND},
                  "about": {"@id": BIZ_ID}, "inLanguage": "en-US"})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, separators=(",", ":"), ensure_ascii=False)
    verif = ""
    if C.GSC_VERIFICATION:
        verif += '<meta name="google-site-verification" content="%s">' % e(C.GSC_VERIFICATION)
    if C.BING_VERIFICATION:
        verif += '<meta name="msvalidate.01" content="%s">' % e(C.BING_VERIFICATION)
    ga = ""
    if C.GA4_ID:
        ga = ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script><script>window.dataLayer=window.dataLayer||[];'
              'function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","%s");</script>' % (C.GA4_ID, C.GA4_ID))
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="%(robots)s">
<link rel="canonical" href="%(canon)s">
<meta property="og:type" content="website">
<meta property="og:site_name" content="%(brand)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="geo.region" content="US-NC">
<meta name="geo.placename" content="Charlotte">
<meta name="format-detection" content="telephone=yes">
<meta name="theme-color" content="#0b3a5b">
%(verif)s
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css?v=%(ver)s">
<script type="application/ld+json">%(ld)s</script>
%(ga)s
</head>
<body>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
<script src="/assets/site.js?v=%(ver)s" defer></script>
</body>
</html>
""" % dict(title=e(title), desc=e(desc), robots=robots, canon=url(path), brand=e(C.BRAND), verif=verif, ld=ld.replace("</", "<\\/"),
           ga=ga, header=header(), body=body, footer=footer(), ver=ASSET_VERSION)
    out = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    if not noindex:
        PAGES.append((path, priority, group))


ASSET_VERSION = "1"
