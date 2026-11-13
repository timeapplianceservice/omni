#!/usr/bin/env python3
"""Build the whole site into ../_site.   Usage:  python3 generator/build.py"""
import os
import shutil
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config as C
import lib
from lib import (jobs_block, e, pick, shuffle, page, hero, offer_band, warranty_block, steps_block, hours_block, reviews_block,
                 faq_block, links_block, section, ul, cta_band, lower_name, faq_schema, service_schema, TEL, OUT, PAGES)
from data_equipment import EQUIPMENT, EQ_BY_SLUG, REFRIG, KITCHEN
from data_brands import BRANDS, TOP_BRANDS
from data_areas import AREAS, FULL, CITIES, HOODS, EXT, place
from data_jobs import JOBS
from data_misc import INDUSTRIES, PROBLEMS, KEYWORD_PAGES, LOCAL_CATEGORIES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()
BRAND_SFX = " | Commercial Appliances"
PRICE_LINE = "$%d service call · $%d off repair" % (C.SERVICE_CALL, C.DISCOUNT)


def jobs(eq_slugs, ind, key):
    """Pick up to 8 typical jobs relevant to this page."""
    eq_slugs = eq_slugs or []
    def score(j):
        return -((2 if j["eq"] in eq_slugs else 0) + (1 if j["biz"] == ind else 0))
    ranked = sorted(JOBS, key=lambda j: (score(j), pick(list(range(997)), key, j["problem"])))
    return jobs_block(ranked[:8])


def T(s):
    """Title with brand suffix, trimmed if very long."""
    return s + BRAND_SFX if len(s) + len(BRAND_SFX) <= 62 else s


CHARLOTTE_CAT = {"commercial-refrigeration-repair": "/commercial-refrigeration-repair-charlotte-nc/",
                 "restaurant-equipment-repair": "/restaurant-equipment-repair-charlotte-nc/",
                 "commercial-kitchen-equipment-repair": "/commercial-kitchen-equipment-repair-charlotte-nc/"}


def ap(a, kind, slug):
    """URL of an area combo page. Charlotte (city) combos would duplicate the citywide pages,
    so they point to those instead; restaurants-industry pages point to the category page."""
    a = a if isinstance(a, dict) else AREAS[a]
    base = "/service-areas/%s/" % a["slug"]
    if kind == "industry" and slug == "restaurants":
        kind, slug = "cat", "restaurant-equipment-repair"
    if a["slug"] == "charlotte":
        if kind == "eq":
            return "/services/%s/" % slug
        if kind == "cat":
            return CHARLOTTE_CAT[slug]
        if kind == "brand":
            return "/brands/%s/" % slug
        if kind == "industry":
            return "/industries/%s/" % slug
    return base + {"eq": "%s/", "cat": "%s/", "brand": "brands/%s/", "industry": "industries/%s/",
                   "problem": "problems/%s/"}[kind] % slug


def is_dup(a, kind, slug):
    return ap(a, kind, slug) != "/service-areas/%s/" % a["slug"] + {"eq": "%s/", "cat": "%s/", "brand": "brands/%s/",
                                                                     "industry": "industries/%s/", "problem": "problems/%s/"}[kind] % slug


def eqs_for(cat):
    return {"refrigeration": REFRIG, "kitchen": KITCHEN}.get(cat, EQUIPMENT)


def area_line(a):
    zips = ", ".join(a["zips"][:8])
    return ("We serve businesses near %s, %s and %s, including ZIP codes %s in %s County, %s."
            % (a["spots"][0], a["spots"][1], a["spots"][2], zips, a["county"], a["state"]))


def faq_local(a, thing):
    p = place(a)
    return [
        ("How much does %s cost in %s?" % (thing, p),
         "The service call is a flat $%d, which covers the trip and diagnosis. After diagnosis you get a written price "
         "for the repair before any work starts, and you save $%d on the repair when you book online or mention our website."
         % (C.SERVICE_CALL, C.DISCOUNT)),
        ("What are your hours in %s?" % a["name"],
         "We are open %s. Call %s or send a request online and the first available operator will call you back."
         % (C.HOURS_SENTENCE, C.PHONE_DISPLAY)),
        ("Do you serve ZIP code %s?" % a["zips"][0],
         "Yes. We serve %s and all of %s, including ZIP codes %s." % (a["name"], p, ", ".join(a["zips"][:10]))),
        ("What warranty do you give?",
         "Every repair has a %d-day labor and %d-day parts warranty. Select repairs and installations qualify for an "
         "extended 1-, 3- or 5-year warranty; the term is written on your estimate." % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS)),
    ]


# =============================================================== HOME
def build_home():
    r_cards = "".join('<a class="tile" href="/services/%s/"><b>%s</b><span>%s</span></a>'
                      % (q["slug"], e(q["name"]), e(q["symptoms"][0])) for q in REFRIG)
    k_cards = "".join('<a class="tile" href="/services/%s/"><b>%s</b><span>%s</span></a>'
                      % (q["slug"], e(q["name"]), e(q["symptoms"][0])) for q in KITCHEN)
    ind = "".join('<a class="chip" href="/industries/%s/">%s</a>' % (s, e(i["name"])) for s, i in INDUSTRIES.items())
    cities = "".join('<a class="chip" href="/service-areas/%s/">%s</a>' % (a["slug"], e(a["name"])) for a in CITIES + EXT)
    hoods = "".join('<a class="chip" href="/service-areas/%s/">%s</a>' % (a["slug"], e(a["name"])) for a in HOODS)
    top_b = "".join('<a class="chip" href="/brands/%s/">%s</a>' % (b["slug"], e(b["name"])) for b in TOP_BRANDS)
    facts = """
<section class="band soft"><div class="wrap narrow">
<h2>Quick facts about Commercial Appliances</h2>
<dl class="facts">
<dt>What we do</dt><dd>Repair, maintenance and installation of commercial refrigeration (walk-in coolers and freezers, ice machines, reach-ins, prep tables, display cases, bar and draft equipment) and commercial kitchen equipment (ovens, ranges, fryers, griddles, steamers, dishwashers, holding cabinets, soft serve machines).</dd>
<dt>Who we serve</dt><dd>Restaurants, cafés, bars, breweries, grocery and convenience stores, bakeries, hotels, schools, healthcare and senior living kitchens, caterers and food trucks.</dd>
<dt>Where</dt><dd>Charlotte, NC and 16 Charlotte neighborhoods, plus Ballantyne, Pineville, Matthews, Mint Hill, Stallings, Indian Trail, Weddington, Wesley Chapel, Waxhaw, Monroe, Fort Mill SC, and extended coverage in Concord, Cornelius, Davidson, Huntersville, Mooresville, Marvin, Indian Land SC and Tega Cay SC.</dd>
<dt>Hours</dt><dd>%s.</dd>
<dt>Price</dt><dd>$%d service call (diagnostic). $%d off the repair when you book online or mention the website.</dd>
<dt>Warranty</dt><dd>%d days labor, %d days parts; extended 1, 3 or 5-year warranty on select repairs and installations.</dd>
<dt>Phone</dt><dd><a href="%s">%s</a></dd>
<dt>Email</dt><dd><a href="mailto:%s">%s</a></dd>
<dt>Credentials</dt><dd>Licensed and insured.</dd>
</dl></div></section>""" % (C.HOURS_SENTENCE, C.SERVICE_CALL, C.DISCOUNT, C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS,
                            TEL, C.PHONE_DISPLAY, C.EMAIL, C.EMAIL)
    faqs = [
        ("Who repairs commercial refrigeration in Charlotte, NC?",
         "The Commercial Appliances team repairs commercial refrigeration — walk-in coolers and freezers, ice machines, reach-ins, prep "
         "tables and display cases — for restaurants and businesses across Charlotte and nearby cities. Call %s." % C.PHONE_DISPLAY),
        ("How much is a commercial refrigeration service call?",
         "Our service call is $%d. You receive a written repair price before any work starts, and $%d off the repair "
         "when you book online." % (C.SERVICE_CALL, C.DISCOUNT)),
        ("What are your business hours?", "%s." % C.HOURS_SENTENCE),
        ("Do you offer same-day service?",
         "Yes, same-day service is available when you call early in the day and a technician is open. Our trucks carry "
         "common parts so many repairs are finished on the first visit."),
        ("Are you licensed and insured?", "Yes. We are licensed and insured."),
        ("What brands do you repair?",
         "We repair True, Traulsen, Hoshizaki, Manitowoc, Scotsman, Kolpak, Turbo Air, Beverage-Air, Vulcan, Garland, "
         "Frymaster, Pitco, Hobart, Rational and over %d other commercial brands." % (len(BRANDS) - 14)),
    ]
    body = (hero("Commercial Refrigeration & Kitchen Equipment Repair in Charlotte, NC",
                 "Walk-in coolers, ice machines, reach-ins, fryers, ovens and dish machines repaired fast for restaurants, "
                 "bars, cafés, stores and institutional kitchens. Flat <b>$%d service call</b> and <b>$%d off</b> your repair."
                 % (C.SERVICE_CALL, C.DISCOUNT), "Home")
            + '<section class="band"><div class="wrap"><h2>Commercial refrigeration repair</h2><div class="tiles">%s</div></div></section>' % r_cards
            + offer_band() + jobs(None, None, "home")
            + '<section class="band"><div class="wrap"><h2>Commercial kitchen equipment repair</h2><div class="tiles">%s</div></div></section>' % k_cards
            + steps_block() + warranty_block() + reviews_block()
            + '<section class="band"><div class="wrap"><h2>Businesses we serve</h2><div class="chips">%s</div></div></section>' % ind
            + '<section class="band soft"><div class="wrap"><h2>Service areas</h2><h3>Cities</h3><div class="chips">%s</div>'
              '<h3>Charlotte neighborhoods</h3><div class="chips">%s</div></div></section>' % (cities, hoods)
            + '<section class="band"><div class="wrap"><h2>Brands we repair</h2><div class="chips">%s</div>'
              '<p><a href="/brands/">See all %d brands</a></p></div></section>' % (top_b, len(BRANDS))
            + facts + faq_block(faqs) + hours_block() + cta_band())
    page("/", "Commercial Refrigeration & Restaurant Equipment Repair Charlotte, NC",
         "Commercial refrigeration and restaurant equipment repair in Charlotte, NC. Walk-ins, ice machines, fryers, ovens. "
         "$%d service call, $%d off repair. Open 7 days. Call %s." % (C.SERVICE_CALL, C.DISCOUNT, C.PHONE_DISPLAY),
         body, schema_extra=[faq_schema(faqs)], priority=1.0)


# =============================================================== SERVICES
def build_services():
    hub_links = [(q["name"] + " Repair", "/services/%s/" % q["slug"]) for q in EQUIPMENT]
    page("/services/", T("Commercial Equipment Repair Services"),
         "All commercial refrigeration and kitchen equipment repair services in Charlotte, NC. %s." % PRICE_LINE,
         hero("Commercial Equipment Repair Services", "Every kind of commercial refrigeration and cooking equipment, repaired "
              "on-site across the Charlotte area.", "Services hub", [("Home", "/"), ("Services", "/services/")])
         + links_block("Refrigeration", [(q["name"] + " Repair", "/services/%s/" % q["slug"]) for q in REFRIG])
         + links_block("Kitchen equipment", [(q["name"] + " Repair", "/services/%s/" % q["slug"]) for q in KITCHEN])
         + offer_band() + jobs(None, None, "/services/") + cta_band(), crumbs=[("Home", "/"), ("Services", "/services/")], priority=0.9)

    for q in EQUIPMENT:
        path = "/services/%s/" % q["slug"]
        crumbs = [("Home", "/"), ("Services", "/services/"), (q["name"] + " Repair", path)]
        brands = [BRANDS[b] for b in q["brands"]]
        probs = [(p["title"], "/problems/%s/" % s) for s, p in PROBLEMS.items() if p["eq"] == q["slug"]]
        inds = [(i["name"], "/industries/%s/" % s) for s, i in INDUSTRIES.items() if q["slug"] in i["eq"]]
        faqs = q["faq"] + [
            ("How much is %s repair in Charlotte?" % lower_name(q),
             "The service call is $%d. You get a written repair price before work starts and $%d off the repair when you book online."
             % (C.SERVICE_CALL, C.DISCOUNT)),
            ("Which areas do you cover for %s repair?" % lower_name(q),
             "Charlotte and its neighborhoods, Ballantyne, Pineville, Matthews, Mint Hill, Stallings, Indian Trail, Weddington, "
             "Wesley Chapel, Waxhaw, Monroe and Fort Mill, plus Concord, Huntersville, Cornelius, Davidson, Mooresville, Marvin, "
             "Indian Land and Tega Cay.")]
        body = (hero("%s Repair in Charlotte, NC" % q["name"], e(q["intro"]), path, crumbs)
                + section("Signs your %s needs service" % lower_name(q), ul(q["symptoms"]))
                + section("Why it fails — and how we fix it", "<p>%s</p>" % e(q["why"]) + ul(q["tasks"]), "band soft")
                + section("Technician tip", '<p class="tip">%s</p>' % e(q["tip"]))
                + offer_band() + jobs([q["slug"]], None, path)
                + links_block("%s brands we repair" % q["name"], [(b["name"], "/brands/%s/%s/" % (b["slug"], q["slug"])) for b in brands], 4)
                + links_block("Common %s problems" % lower_name(q), probs, 2)
                + links_block("%s repair by city" % q["name"],
                              [("%s repair in %s" % (q["name"], a["name"]), ap(a, "eq", q["slug"])) for a in FULL if a["slug"] != "charlotte"])
                + links_block("Businesses that rely on it", inds)
                + steps_block() + warranty_block() + faq_block(faqs) + hours_block() + cta_band())
        page(path, T("%s Repair Charlotte NC" % q["name"]),
             "%s repair in Charlotte, NC for restaurants and businesses. %s. Same-day service available. Call %s."
             % (q["name"], PRICE_LINE, C.PHONE_DISPLAY), body, crumbs,
             [service_schema(q["name"] + " Repair", path, ["Charlotte, NC"], q["intro"]), faq_schema(faqs)], 0.9, "services")


# =============================================================== BRANDS
def build_brands():
    def brand_links(bs):
        return [(b["name"] + " Repair", "/brands/%s/" % b["slug"]) for b in sorted(bs, key=lambda x: x["name"].lower())]
    r_b = [b for b in BRANDS.values() if any(EQ_BY_SLUG[x]["cat"] == "refrigeration" for x in b["equipment"])]
    k_b = [b for b in BRANDS.values() if b not in r_b]
    page("/brands/", T("Commercial Equipment Brands We Repair"),
         "We repair %d+ commercial refrigeration and kitchen equipment brands in Charlotte, NC: True, Hoshizaki, Manitowoc, "
         "Vulcan, Frymaster, Hobart and more." % len(BRANDS),
         hero("Commercial Equipment Brands We Repair", "Independent, factory-trained-style service for the brands in "
              "your kitchen — no waiting on a single dealer.", "Brands hub", [("Home", "/"), ("Brands", "/brands/")])
         + links_block("Refrigeration &amp; ice brands", brand_links(r_b), 4)
         + links_block("Cooking, warewashing &amp; prep brands", brand_links(k_b), 4) + cta_band(),
         crumbs=[("Home", "/"), ("Brands", "/brands/")], priority=0.8)

    for b in BRANDS.values():
        path = "/brands/%s/" % b["slug"]
        crumbs = [("Home", "/"), ("Brands", "/brands/"), (b["name"], path)]
        eqs = [EQ_BY_SLUG[x] for x in b["equipment"]]
        eq_names = ", ".join(lower_name(q) for q in eqs)
        intro = ("%s makes %s. We repair %s equipment for restaurants, bars, stores and institutional "
                 "kitchens across Charlotte and nearby cities — %s." % (b["name"], b["lines"], b["name"], PRICE_LINE))
        symptoms = []
        for q in eqs:
            symptoms += ["%s %s: %s" % (b["name"], lower_name(q), s.lower()) for s in q["symptoms"][:3]]
        faqs = [("Do you repair %s equipment in Charlotte?" % b["name"],
                 "Yes. We repair %s %s across Charlotte and surrounding cities." % (b["name"], eq_names)),
                ("Are you a %s authorized service agent?" % b["name"],
                 "No. We are an independent commercial service company. We work on %s equipment using OEM or equivalent "
                 "parts and back our work with a %d-day labor and %d-day parts warranty." % (b["name"], C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS)),
                ("How much does %s repair cost?" % b["name"],
                 "The service call is $%d and includes diagnosis. You approve a written price before the repair, with $%d off when you book online."
                 % (C.SERVICE_CALL, C.DISCOUNT))]
        loc = []
        if b["top"]:
            loc = [("%s repair in %s" % (b["name"], a["name"]), ap(a, "brand", b["slug"])) for a in FULL if a["slug"] != "charlotte"]
        body = (hero("%s Repair in Charlotte, NC" % b["name"], e(intro), path, crumbs)
                + section("%s problems we fix" % b["name"], ul(symptoms))
                + links_block("%s equipment we service" % b["name"],
                              [("%s %s Repair" % (b["name"], q["name"]), "/brands/%s/%s/" % (b["slug"], q["slug"])) for q in eqs], 2)
                + offer_band() + jobs(b["equipment"], None, path) + links_block("%s repair near you" % b["name"], loc)
                + warranty_block() + faq_block(faqs) + hours_block() + cta_band())
        page(path, T("%s Repair Charlotte NC" % b["name"]),
             "%s commercial equipment repair in Charlotte, NC: %s. %s. Call %s." % (b["name"], eq_names, PRICE_LINE, C.PHONE_DISPLAY)[:300],
             body, crumbs, [service_schema(b["name"] + " Repair", path, ["Charlotte, NC"], intro), faq_schema(faqs)], 0.7, "brands")

        # brand x equipment
        for q in eqs:
            p2 = "/brands/%s/%s/" % (b["slug"], q["slug"])
            cr2 = crumbs + [(q["name"], p2)]
            intro2 = ("Need a %s %s repaired? %s Our technicians service %s %s units across Charlotte and nearby cities."
                      % (b["name"], lower_name(q), q["why"], b["name"], lower_name(q)))
            others = [(BRANDS[x]["name"] + " " + q["name"], "/brands/%s/%s/" % (x, q["slug"])) for x in q["brands"] if x != b["slug"]]
            faqs2 = [("Why is my %s %s not working?" % (b["name"], lower_name(q)),
                      "The most common causes are: %s. A technician confirms the cause on site before quoting the repair."
                      % "; ".join(s.lower() for s in q["symptoms"][:3])),
                     q["faq"][0],
                     ("How much is %s %s repair?" % (b["name"], lower_name(q)),
                      "$%d service call with diagnosis, then a written price. $%d off the repair when booked online." % (C.SERVICE_CALL, C.DISCOUNT))]
            body2 = (hero("%s %s Repair in Charlotte, NC" % (b["name"], q["name"]), e(intro2), p2, cr2)
                     + section("Common %s %s problems" % (b["name"], lower_name(q)), ul(q["symptoms"]))
                     + section("What we repair on %s %s units" % (b["name"], lower_name(q)), ul(q["tasks"]), "band soft")
                     + section("Technician tip", '<p class="tip">%s</p>' % e(q["tip"]))
                     + offer_band() + jobs([q["slug"]], None, p2)
                     + links_block("Other %s brands we repair" % lower_name(q), others, 3)
                     + links_block("More", [("All %s repair" % b["name"], path), (q["name"] + " repair", "/services/%s/" % q["slug"])], 2)
                     + warranty_block() + faq_block(faqs2) + cta_band())
            page(p2, T("%s %s Repair Charlotte" % (b["name"], q["name"])),
                 "%s %s repair in Charlotte, NC. %s. Same-day service available. Call %s."
                 % (b["name"], lower_name(q), PRICE_LINE, C.PHONE_DISPLAY), body2, cr2,
                 [service_schema("%s %s Repair" % (b["name"], q["name"]), p2, ["Charlotte, NC"], intro2), faq_schema(faqs2)],
                 0.6, "brand-equipment")


# =============================================================== INDUSTRIES
def build_industries():
    page("/industries/", T("Businesses We Serve"),
         "Commercial refrigeration and kitchen equipment repair for restaurants, bars, cafés, grocery stores, hotels, schools "
         "and healthcare kitchens in Charlotte, NC.",
         hero("Businesses We Serve", "Restaurants, bars, stores and institutional kitchens across the Charlotte area.",
              "Industries hub", [("Home", "/"), ("Industries", "/industries/")])
         + links_block("Industries", [(i["name"], "/industries/%s/" % s) for s, i in INDUSTRIES.items()]) + cta_band(),
         crumbs=[("Home", "/"), ("Industries", "/industries/")], priority=0.8)
    for s, i in INDUSTRIES.items():
        path = "/industries/%s/" % s
        crumbs = [("Home", "/"), ("Industries", "/industries/"), (i["name"], path)]
        eqs = [EQ_BY_SLUG[x] for x in i["eq"]]
        faqs = [("Do you repair equipment for %ss in Charlotte?" % i["short"],
                 "Yes. We repair %s for %ss across Charlotte and nearby cities." % (", ".join(lower_name(q) for q in eqs), i["short"])),
                ("How quickly can a technician come to my %s?" % i["short"],
                 "Same-day service is often available when you call early. We are open %s." % C.HOURS_SENTENCE),
                ("Do you offer maintenance plans for %ss?" % i["short"],
                 "Yes. Scheduled coil cleaning, ice machine cleaning and inspections prevent most emergency breakdowns. Ask us for a quote.")]
        body = (hero("Commercial Equipment Repair for %s in Charlotte" % i["name"], e(i["intro"]), path, crumbs)
                + section("Problems we solve for %ss" % i["short"], ul(i["pains"]))
                + links_block("Equipment we repair for %ss" % i["short"], [(q["name"] + " Repair", "/services/%s/" % q["slug"]) for q in eqs], 2)
                + section("Technician tip", '<p class="tip">%s</p>' % e(i["tip"]), "band soft")
                + offer_band() + jobs(i["eq"], s, path)
                + links_block("%s equipment repair by city" % i["short"].capitalize(),
                              [("%s in %s" % (i["name"], a["name"]), ap(a, "industry", s)) for a in FULL if a["slug"] != "charlotte"])
                + warranty_block() + faq_block(faqs) + hours_block() + cta_band())
        page(path, T("%s Equipment Repair Charlotte" % i["short"].title()),
             "Refrigeration and kitchen equipment repair for %s in Charlotte, NC. %s. Call %s." % (i["name"].lower(), PRICE_LINE, C.PHONE_DISPLAY),
             body, crumbs, [service_schema("Commercial equipment repair for " + i["name"], path, ["Charlotte, NC"], i["intro"]),
                            faq_schema(faqs)], 0.7, "industries")


# =============================================================== PROBLEMS
def build_problems():
    page("/problems/", T("Commercial Equipment Troubleshooting"),
         "Why is my walk-in cooler not cooling? Why won't my ice machine make ice? Causes, what to do now and when to call.",
         hero("Commercial Equipment Troubleshooting", "Common problems, likely causes and what to do before the technician arrives.",
              "Problems hub", [("Home", "/"), ("Troubleshooting", "/problems/")])
         + links_block("Problems", [(p["title"], "/problems/%s/" % s) for s, p in PROBLEMS.items()], 2) + cta_band(),
         crumbs=[("Home", "/"), ("Troubleshooting", "/problems/")], priority=0.7)
    for s, p in PROBLEMS.items():
        path = "/problems/%s/" % s
        q = EQ_BY_SLUG[p["eq"]]
        crumbs = [("Home", "/"), ("Troubleshooting", "/problems/"), (p["title"], path)]
        intro = ("%s? Here are the most likely causes, what you can safely do right now, and when to call a technician. "
                 "We repair this every week across Charlotte — %s." % (p["title"], PRICE_LINE))
        faqs = [("Why is my %s?" % p["kw"].replace("my ", ""),
                 "Most often: %s." % "; ".join(c.lower() for c in p["causes"][:4])),
                ("Can I fix it myself?",
                 "Simple checks are safe: %s. Refrigerant, gas and electrical repairs should be done by a licensed technician." % "; ".join(n.lower() for n in p["now"][:2])),
                ("How fast can you come?", "Same-day service is often available. Hours: %s." % C.HOURS_SENTENCE)]
        body = (hero(p["title"] + " — Causes & Fix", e(intro), path, crumbs)
                + section("Most likely causes", ul(p["causes"]))
                + section("What to do right now", ul(p["now"]), "band soft")
                + section("When to call", "<p>If the problem comes back, product is above safe temperature, or the fix involves "
                          "refrigerant, gas or electrical parts, call a technician. %s</p>" % e(q["why"]))
                + offer_band() + jobs([p["eq"]], None, path)
                + links_block("Get it fixed in your area",
                              [("%s — %s" % (p["title"], a["name"]), "/service-areas/%s/problems/%s/" % (a["slug"], s)) for a in CITIES])
                + links_block("Related", [(q["name"] + " repair", "/services/%s/" % q["slug"])] +
                              [(o["title"], "/problems/%s/" % os_) for os_, o in PROBLEMS.items() if o["eq"] == p["eq"] and os_ != s], 2)
                + faq_block(faqs) + cta_band())
        page(path, T(p["title"] + " — Causes & Fix"),
             "%s: causes, what to do now and when to call. Repair in Charlotte, NC — %s. Call %s." % (p["title"], PRICE_LINE, C.PHONE_DISPLAY),
             body, crumbs, [faq_schema(faqs)], 0.6, "problems")


# =============================================================== AREAS
OPENERS = [
    "Need {thing} in {place}? We send commercial technicians to restaurants, bars, stores and institutional kitchens across {name} every week.",
    "When a {eq} goes down in {name}, food, sales and inspections are on the line. Our technicians arrive with common parts and fix most problems on the first visit.",
    "{name} businesses call us for fast, honest {thing}. You get a flat ${call} service call and a written price before any work starts.",
    "From {spot0} to {spot1}, we provide {thing} for {name} restaurants, cafés, bars and grocery stores.",
    "Our {thing} service covers all of {place}. We know the local businesses, the building types and how hot a {name} kitchen gets in July.",
    "Looking for reliable {thing} near {spot0}? We serve {place} with same-day service when available.",
]


LOCAL_SENTENCES = [
    "Our technicians are in {name} most days of the week, so a call from a business on {spot2} usually fits into the same day's route.",
    "Many of our {name} customers are along {spot0} and {spot3}, where busy kitchens run {eq} equipment hard from open to close.",
    "Because we also work in {near1} and {near2}, a technician is often already nearby when a {name} business calls.",
    "{county} County health inspectors check cold-holding at 41°F or below and hot-holding at 135°F or above — we repair your {eq} to hold those numbers.",
    "Summer heat in the Charlotte region pushes condensers and compressors to their limit; for {name} kitchens we check airflow, coil condition and electrical parts on every visit.",
    "We document every visit with the temperatures we measured and the parts we replaced, which helps {name} managers with inspections and budgeting.",
    "If a repair is not worth the money, we tell you and quote the replacement — no {name} customer is pushed into a new unit they don't need.",
    "When a part is not on the truck, we order it the same day from Charlotte-area suppliers and come back to {spot1} as soon as it arrives.",
    "Businesses in ZIP {zip0}{zip1} can book online in 30 seconds, and the first available operator calls back during business hours.",
    "From quick-service counters near {spot2} to full kitchens near {spot0}, {name} businesses rely on us for {eq} work.",
]


def local_para(a, key, eq_word):
    near = [AREAS[n]["name"] for n in a["near"]] + ["Charlotte", "Matthews"]
    sp = a["spots"] + a["spots"]
    picks = shuffle(list(range(len(LOCAL_SENTENCES))), *key)[:4]
    z = a["zips"]
    return " ".join(LOCAL_SENTENCES[i].format(name=a["name"], spot0=sp[0], spot1=sp[1], spot2=sp[2], spot3=sp[3],
                                                near1=near[0], near2=near[1], county=a["county"], eq=eq_word,
                                                zip0=z[0], zip1=(" and " + z[1]) if len(z) > 1 else "") for i in picks)


def opener(key, thing, eq_name, a):
    return pick(OPENERS, *key).format(thing=thing, place=place(a), name=a["name"], eq=eq_name,
                                      spot0=a["spots"][0], spot1=a["spots"][1], call=C.SERVICE_CALL)


def near_links(a, kind, slug, label_fmt):
    return [(label_fmt % AREAS[n]["name"], ap(n, kind, slug)) for n in a["near"] if AREAS[n]["kind"] != "ext"]


def build_areas():
    def chips(lst):
        return [(a["name"], "/service-areas/%s/" % a["slug"]) for a in lst]
    page("/service-areas/", T("Service Areas — Charlotte NC & SC"),
         "Commercial refrigeration and kitchen equipment repair in Charlotte, 16 Charlotte neighborhoods and 20 cities in "
         "Mecklenburg, Union, Cabarrus, Iredell, York and Lancaster counties.",
         hero("Service Areas", "Charlotte, its neighborhoods and nearby cities in North and South Carolina.", "Areas hub",
              [("Home", "/"), ("Service Areas", "/service-areas/")])
         + links_block("Cities — full service", chips(CITIES), 4) + links_block("Charlotte neighborhoods", chips(HOODS), 4)
         + links_block("Extended coverage", chips(EXT), 4) + hours_block() + cta_band(),
         crumbs=[("Home", "/"), ("Service Areas", "/service-areas/")], priority=0.9)

    for a in AREAS.values():
        base = "/service-areas/%s/" % a["slug"]
        crumbs = [("Home", "/"), ("Service Areas", "/service-areas/"), (a["name"], base)]
        p = place(a)
        full = a["kind"] != "ext"
        intro = opener((a["slug"], "hub"), "commercial refrigeration and kitchen equipment repair", "walk-in cooler", a) + " " + a["blurb"]
        svc_links = [("%s repair in %s" % (q["name"], a["name"]),
                      ap(a, "eq", q["slug"]) if full else "/services/%s/" % q["slug"]) for q in EQUIPMENT]
        body = (hero("Commercial Equipment Repair in %s" % p, e(intro), base, crumbs)
                + section("Serving %s businesses" % a["name"], "<p>%s</p><p>%s</p><p>%s</p>" % (e(a["blurb"]), e(area_line(a)), e(local_para(a, (a["slug"], "hub"), "refrigeration and kitchen"))))
                + (links_block("Repair categories in %s" % a["name"], [("%s in %s" % (n, a["name"]), ap(a, "cat", s)) for s, n, _ in LOCAL_CATEGORIES])
                   if full else "")
                + links_block("Equipment we repair in %s" % a["name"], svc_links)
                + offer_band() + jobs(None, None, base)
                + (links_block("Businesses we serve in %s" % a["name"],
                               [("%s in %s" % (i["name"], a["name"]), ap(a, "industry", s)) for s, i in INDUSTRIES.items()]) if full else "")
                + (links_block("Brands we repair in %s" % a["name"],
                               [("%s repair" % b["name"], ap(a, "brand", b["slug"])) for b in TOP_BRANDS], 4) if full else "")
                + (links_block("Common problems we fix in %s" % a["name"],
                               [(pp["title"], base + "problems/%s/" % s) for s, pp in PROBLEMS.items()], 2) if a["kind"] == "city" else "")
                + links_block("Nearby areas", [(AREAS[n]["name"], "/service-areas/%s/" % n) for n in a["near"]], 4)
                + warranty_block() + faq_block(faq_local(a, "commercial equipment repair")) + hours_block(p) + cta_band())
        page(base, T("Commercial Equipment Repair %s" % p),
             "Commercial refrigeration & restaurant equipment repair in %s. Walk-ins, ice machines, fryers, ovens. %s. Call %s."
             % (p, PRICE_LINE, C.PHONE_DISPLAY), body, crumbs,
             [service_schema("Commercial refrigeration and kitchen equipment repair", base, [p], intro),
              faq_schema(faq_local(a, "commercial equipment repair"))], 0.9 if a["kind"] == "city" else 0.8, "areas")
        if not full:
            continue

        # ---- category x area
        for cs, cname, ccat in LOCAL_CATEGORIES:
            if is_dup(a, "cat", cs):
                continue
            p2 = base + cs + "/"
            cr = crumbs + [(cname, p2)]
            eqs = eqs_for(ccat)
            intro2 = opener((a["slug"], cs), cname.lower(), eqs[0]["name"].lower(), a)
            body2 = (hero("%s in %s" % (cname, p), e(intro2), p2, cr)
                     + section("%s for %s businesses" % (cname, a["name"]), "<p>%s</p><p>%s</p><p>%s</p>" % (e(a["blurb"]), e(area_line(a)), e(local_para(a, (a["slug"], cs), ccat if ccat != "all" else "kitchen"))))
                     + links_block("What we repair", [("%s repair in %s" % (q["name"], a["name"]), ap(a, "eq", q["slug"])) for q in eqs])
                     + offer_band() + jobs([x["slug"] for x in eqs], None, p2) + steps_block()
                     + links_block("%s nearby" % cname, near_links(a, "cat", cs, cname + " in %s"), 3)
                     + warranty_block() + faq_block(faq_local(a, cname.lower())) + hours_block(p) + cta_band())
            page(p2, T("%s %s" % (cname, p)),
                 "%s in %s for restaurants, bars and stores. %s. Same-day service available. Call %s."
                 % (cname, p, PRICE_LINE, C.PHONE_DISPLAY), body2, cr,
                 [service_schema(cname, p2, [p], intro2), faq_schema(faq_local(a, cname.lower()))], 0.8, "area-categories")

        # ---- equipment x area
        for q in EQUIPMENT:
            if is_dup(a, "eq", q["slug"]):
                continue
            p2 = base + q["slug"] + "/"
            cr = crumbs + [(q["name"] + " Repair", p2)]
            thing = lower_name(q) + " repair"
            intro2 = opener((a["slug"], q["slug"]), thing, lower_name(q), a) + " " + q["intro"]
            local = ("%s %s" % (a["blurb"], area_line(a)))
            syms = shuffle(q["symptoms"], a["slug"], q["slug"])
            tasks = shuffle(q["tasks"], q["slug"], a["slug"])
            brands_here = [(BRANDS[b]["name"] + " " + q["name"],
                            ap(a, "brand", b) if BRANDS[b]["top"] else "/brands/%s/%s/" % (b, q["slug"])) for b in q["brands"]]
            inds = [(i["name"] + " in " + a["name"], ap(a, "industry", s)) for s, i in INDUSTRIES.items() if q["slug"] in i["eq"]]
            probs = [(pp["title"], (base if a["kind"] == "city" else "/") + "problems/%s/" % s) for s, pp in PROBLEMS.items() if pp["eq"] == q["slug"]]
            faqs = q["faq"] + faq_local(a, thing)[:3]
            body2 = (hero("%s Repair in %s" % (q["name"], p), e(intro2), p2, cr)
                     + section("%s repair for %s businesses" % (q["name"], a["name"]), "<p>%s</p><p>%s</p>" % (e(local), e(local_para(a, (a["slug"], q["slug"]), lower_name(q)))))
                     + section("Signs you need %s" % thing, ul(syms), "band soft")
                     + section("What our technicians do", "<p>%s</p>" % e(q["why"]) + ul(tasks))
                     + offer_band() + jobs([q["slug"]], None, p2)
                     + links_block("%s brands we repair in %s" % (q["name"], a["name"]), brands_here, 3)
                     + links_block("Common problems", probs, 2)
                     + links_block("Who we serve in %s" % a["name"], inds, 3)
                     + links_block("%s repair nearby" % q["name"], near_links(a, "eq", q["slug"], q["name"] + " repair in %s"), 3)
                     + section("Technician tip", '<p class="tip">%s</p>' % e(q["tip"]), "band soft")
                     + warranty_block() + faq_block(faqs) + hours_block(p) + cta_band())
            page(p2, T("%s Repair %s" % (q["name"], p)),
                 "%s repair in %s. %s. Same-day service available, %d-day parts warranty. Call %s."
                 % (q["name"], p, PRICE_LINE, C.PARTS_WARRANTY_DAYS, C.PHONE_DISPLAY), body2, cr,
                 [service_schema(q["name"] + " Repair", p2, [p], intro2), faq_schema(faqs)], 0.7, "area-services")

        # ---- brand x area (top brands)
        for b in TOP_BRANDS:
            if is_dup(a, "brand", b["slug"]):
                continue
            p2 = base + "brands/%s/" % b["slug"]
            cr = crumbs + [(b["name"] + " Repair", p2)]
            eqs = [EQ_BY_SLUG[x] for x in b["equipment"]]
            thing = "%s repair" % b["name"]
            intro2 = (opener((a["slug"], b["slug"]), thing, b["name"] + " " + lower_name(eqs[0]), a) +
                      " %s makes %s, and we repair them on-site." % (b["name"], b["lines"]))
            syms = []
            for q in eqs:
                syms += ["%s %s: %s" % (b["name"], lower_name(q), s.lower()) for s in shuffle(q["symptoms"], b["slug"], a["slug"])[:2]]
            faqs = [("Do you repair %s equipment in %s?" % (b["name"], a["name"]),
                     "Yes. We repair %s %s for businesses throughout %s." % (b["name"], ", ".join(lower_name(q) for q in eqs), p)),
                    ("Are you an authorized %s dealer?" % b["name"],
                     "No — we are an independent commercial service company. We repair %s equipment and warranty our work "
                     "for %d days labor and %d days parts." % (b["name"], C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS))] + faq_local(a, thing)[:2]
            body2 = (hero("%s Repair in %s" % (b["name"], p), e(intro2), p2, cr)
                     + section("%s service for %s businesses" % (b["name"], a["name"]), "<p>%s</p><p>%s</p>" % (e(a["blurb"] + " " + area_line(a)), e(local_para(a, (a["slug"], b["slug"]), b["name"]))))
                     + section("%s problems we fix in %s" % (b["name"], a["name"]), ul(syms), "band soft")
                     + links_block("%s equipment we repair" % b["name"],
                                   [("%s %s repair in %s" % (b["name"], q["name"], a["name"]), ap(a, "eq", q["slug"])) for q in eqs], 2)
                     + offer_band() + jobs(b["equipment"], None, p2)
                     + links_block("%s repair nearby" % b["name"], near_links(a, "brand", b["slug"], b["name"] + " repair in %s"), 3)
                     + links_block("Other brands in %s" % a["name"],
                                   [(o["name"], ap(a, "brand", o["slug"])) for o in shuffle(TOP_BRANDS, a["slug"], b["slug"])[:12] if o is not b], 4)
                     + warranty_block() + faq_block(faqs) + hours_block(p) + cta_band())
            page(p2, T("%s Repair %s" % (b["name"], p)),
                 "%s commercial equipment repair in %s. %s. Independent service, warranty on every repair. Call %s."
                 % (b["name"], p, PRICE_LINE, C.PHONE_DISPLAY), body2, cr,
                 [service_schema(thing, p2, [p], intro2), faq_schema(faqs)], 0.5, "area-brands")

        # ---- industry x area
        for s, i in INDUSTRIES.items():
            if is_dup(a, "industry", s):
                continue
            p2 = base + "industries/%s/" % s
            cr = crumbs + [(i["name"], p2)]
            eqs = [EQ_BY_SLUG[x] for x in i["eq"]]
            intro2 = opener((a["slug"], s), "%s equipment repair" % i["short"], lower_name(eqs[0]), a) + " " + i["intro"]
            faqs = [("Do you repair equipment for %ss in %s?" % (i["short"], a["name"]),
                     "Yes. We repair %s for %ss throughout %s." % (", ".join(lower_name(q) for q in eqs), i["short"], p))] + faq_local(a, "%s equipment repair" % i["short"])[:3]
            body2 = (hero("%s Equipment Repair in %s" % (i["short"].title(), p), e(intro2), p2, cr)
                     + section("Problems we solve for %s %ss" % (a["name"], i["short"]), ul(shuffle(i["pains"], a["slug"], s)))
                     + section("Local service", "<p>%s</p><p>%s</p>" % (e(a["blurb"] + " " + area_line(a)), e(local_para(a, (a["slug"], s), i["short"]))), "band soft")
                     + links_block("Equipment we repair for %ss in %s" % (i["short"], a["name"]),
                                   [("%s repair" % q["name"], ap(a, "eq", q["slug"])) for q in eqs], 2)
                     + offer_band() + jobs(i["eq"], s, p2)
                     + section("Technician tip", '<p class="tip">%s</p>' % e(i["tip"]))
                     + links_block("Nearby", near_links(a, "industry", s, i["name"] + " in %s"), 3)
                     + warranty_block() + faq_block(faqs) + hours_block(p) + cta_band())
            page(p2, T("%s Equipment Repair %s" % (i["short"].title(), p)),
                 "Refrigeration and kitchen equipment repair for %s in %s. %s. Call %s." % (i["name"].lower(), p, PRICE_LINE, C.PHONE_DISPLAY),
                 body2, cr, [service_schema("Equipment repair for " + i["name"], p2, [p], intro2), faq_schema(faqs)], 0.5, "area-industries")

        # ---- problem x area (cities only)
        if a["kind"] != "city":
            continue
        for s, pp in PROBLEMS.items():
            p2 = base + "problems/%s/" % s
            cr = crumbs + [(pp["title"], p2)]
            q = EQ_BY_SLUG[pp["eq"]]
            intro2 = ("%s in %s? %s" % (pp["title"], p, opener((a["slug"], s), lower_name(q) + " repair", lower_name(q), a)))
            faqs = [("Why is my %s?" % pp["kw"].replace("my ", ""), "Most often: %s." % "; ".join(c.lower() for c in pp["causes"][:4]))] + faq_local(a, lower_name(q) + " repair")[:3]
            body2 = (hero("%s — Repair in %s" % (pp["title"], p), e(intro2), p2, cr)
                     + section("Likely causes", ul(shuffle(pp["causes"], a["slug"], s)))
                     + section("What to do before we arrive", ul(pp["now"]), "band soft")
                     + section("Local service", "<p>%s</p><p>%s</p>" % (e(area_line(a)), e(local_para(a, (a["slug"], s), lower_name(q)))))
                     + offer_band() + jobs([q["slug"]], None, p2)
                     + links_block("Related", [(q["name"] + " repair in " + a["name"], ap(a, "eq", q["slug"])),
                                               (pp["title"] + " — guide", "/problems/%s/" % s)], 2)
                     + links_block("Same problem nearby", [(pp["title"] + " — " + AREAS[n]["name"], "/service-areas/%s/problems/%s/" % (n, s))
                                    for n in a["near"] if AREAS[n]["kind"] == "city"], 2)
                     + faq_block(faqs) + hours_block(p) + cta_band())
            page(p2, T("%s %s" % (pp["title"], p)),
                 "%s in %s? Causes and same-day repair. %s. Call %s." % (pp["title"], p, PRICE_LINE, C.PHONE_DISPLAY),
                 body2, cr, [service_schema(q["name"] + " Repair", p2, [p], intro2), faq_schema(faqs)], 0.5, "area-problems")


# =============================================================== KEYWORD PAGES
ANGLES = {
    "core": "Fast, honest repair from technicians who work on commercial equipment every day.",
    "urgent": ("Equipment down during service? Call us — same-day service is available when you call early, and our trucks "
               "carry common parts. We do not advertise 24/7 service: we are open %s." % C.HOURS_SENTENCE),
    "nearme": ("Commercial Appliances is a local, mobile commercial service company based in Charlotte, NC. We come to your "
               "business anywhere in our service area."),
    "maint": ("Scheduled maintenance — coil cleaning, ice machine descaling, gasket and drain checks, temperature and "
              "refrigerant checks — prevents most emergency breakdowns and keeps you ready for inspections."),
    "install": ("We install and replace walk-in refrigeration systems, condensing units, evaporators, reach-ins and ice "
                "machines, and we remove the old equipment."),
}


def build_keyword_pages():
    for slug, h1, kw, cat, angle in KEYWORD_PAGES:
        path = "/%s/" % slug
        crumbs = [("Home", "/"), (h1, path)]
        eqs = eqs_for(cat)
        intro = "%s %s Flat $%d service call and $%d off your repair." % (
            "Looking for %s?" % kw, ANGLES[angle], C.SERVICE_CALL, C.DISCOUNT)
        faqs = [("Who offers %s?" % kw,
                 "The Commercial Appliances team provides %s across Charlotte, NC and nearby cities. Call %s." % (kw, C.PHONE_DISPLAY)),
                ("How much does it cost?", "A $%d service call with diagnosis; you approve a written price before the repair. "
                 "$%d off the repair when you book online." % (C.SERVICE_CALL, C.DISCOUNT)),
                ("When are you open?", C.HOURS_SENTENCE + "."),
                ("What warranty do I get?", "%d-day labor, %d-day parts; extended 1, 3 or 5-year warranty on select work."
                 % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS))]
        body = (hero(h1, e(intro), path, crumbs)
                + links_block("Equipment covered", [(q["name"] + " Repair", "/services/%s/" % q["slug"]) for q in eqs])
                + offer_band() + jobs([x["slug"] for x in eqs], None, path) + steps_block()
                + links_block("Where we work", [(a["name"], "/service-areas/%s/" % a["slug"]) for a in CITIES + HOODS + EXT], 4)
                + links_block("Businesses we serve", [(i["name"], "/industries/%s/" % s) for s, i in INDUSTRIES.items()], 3)
                + warranty_block() + faq_block(faqs) + hours_block() + cta_band())
        page(path, T(h1), "%s — %s. Open 7 days, same-day service available. Call %s." % (h1, PRICE_LINE, C.PHONE_DISPLAY),
             body, crumbs, [service_schema(h1, path, ["Charlotte, NC"], intro), faq_schema(faqs)], 0.9, "keywords")


# =============================================================== STATIC PAGES
def build_static():
    def simple(path, title, h1, desc, html_body, faqs=None, pri=0.5, noindex=False, with_hero=True):
        crumbs = [("Home", "/"), (h1, path)]
        b = (hero(h1, desc, path, crumbs) if with_hero else "") + html_body
        if faqs:
            b += faq_block(faqs)
        page(path, title, desc, b + cta_band(), crumbs, [faq_schema(faqs)] if faqs else [], pri, "main", noindex)

    simple("/pricing/", T("Pricing — $%d Service Call" % C.SERVICE_CALL), "Pricing",
           "Commercial service call $%d. $%d off any repair when you book online. Written price before work starts." % (C.SERVICE_CALL, C.DISCOUNT),
           section("How our pricing works",
                   "<ul class='checks'><li><b>$%d service call</b> — trip and diagnosis.</li><li>You get a <b>written repair price</b> before any work starts.</li>"
                   "<li><b>$%d off</b> the repair when you book online or mention the website.</li><li>Nothing is done without your approval.</li>"
                   "<li>%d-day labor and %d-day parts warranty on every repair.</li></ul>" % (C.SERVICE_CALL, C.DISCOUNT, C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS))
           + offer_band() + jobs(None, None, "/pricing/"),
           [("Is the service call applied to the repair?", "The $%d service call covers the trip and diagnosis. The repair is priced separately, with $%d off when you book online." % (C.SERVICE_CALL, C.DISCOUNT)),
            ("Do you charge extra on Sundays?", "Ask your dispatcher when you call — any difference is stated before we come.")], 0.8)
    simple("/warranty/", T("Warranty"), "Warranty",
           "%d-day labor and %d-day parts warranty on every repair. Extended 1, 3 or 5-year warranty on select repairs and installations."
           % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS),
           warranty_block() + section("Warranty terms",
               "<ul class='checks'><li>Labor: %d days from the repair date.</li><li>Parts we install: %d days.</li>"
               "<li>Extended warranty of 1, 3 or 5 years is available on select repairs and installations; the term is written on your estimate and invoice.</li>"
               "<li>Warranty covers the repaired component and our workmanship. It does not cover damage from power surges, misuse, lack of cleaning, or other unrelated failures.</li>"
               "<li>To use your warranty, call %s.</li></ul>" % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS, C.PHONE_DISPLAY)), None, 0.7)
    simple("/about/", T("About Us"), "About Commercial Appliances",
           "Licensed and insured commercial refrigeration and kitchen equipment repair company based in Charlotte, NC.",
           section("Who we are",
                   "<p>Commercial Appliances is a licensed and insured commercial service company based in Charlotte, North Carolina. "
                   "We repair, maintain and install commercial refrigeration and repair commercial kitchen equipment for restaurants, cafés, "
                   "bars, breweries, grocery and convenience stores, bakeries, hotels, schools, healthcare and senior living kitchens.</p>"
                   "<p>We are a mobile service company: our technicians come to your business. We serve Charlotte and its neighborhoods, "
                   "Mecklenburg and Union counties in North Carolina, York County in South Carolina, and extended coverage in Cabarrus, "
                   "Iredell and Lancaster counties.</p><p>Hours: %s. Phone: %s. Email: %s.</p>" % (C.HOURS_SENTENCE, C.PHONE_DISPLAY, C.EMAIL))
           + hours_block(), None, 0.6)
    simple("/contact/", T("Contact & Hours"), "Contact Commercial Appliances",
           "Call %s or send a request online. Open %s." % (C.PHONE_DISPLAY, C.HOURS_SENTENCE),
           hours_block(), None, 0.8)
    gen_faq = [
        ("What equipment do you repair?", "Walk-in coolers and freezers, ice machines, reach-in refrigerators and freezers, prep tables, undercounters, display cases, bar coolers, draft beer systems, blast chillers, condensing units, ovens, ranges, fryers, griddles, steamers, kettles, dishwashers, holding cabinets, soft serve machines, mixers, slicers and coffee equipment."),
        ("Do you repair residential appliances?", "No. We work only on commercial refrigeration and commercial kitchen equipment."),
        ("What are your hours?", C.HOURS_SENTENCE + "."),
        ("Do you work 24/7?", "No. We are open %s. Same-day service is often available when you call early." % C.HOURS_SENTENCE),
        ("How much is a service call?", "$%d. You get a written repair price before work starts, and $%d off the repair when you book online." % (C.SERVICE_CALL, C.DISCOUNT)),
        ("What warranty do you give?", "%d-day labor and %d-day parts; extended 1, 3 or 5 years on select repairs and installations." % (C.LABOR_WARRANTY_DAYS, C.PARTS_WARRANTY_DAYS)),
        ("Where are you located?", "We are based in Charlotte, NC and come to your business. We do not have a walk-in storefront."),
        ("Which areas do you serve?", "Charlotte and 16 Charlotte neighborhoods; Ballantyne, Pineville, Matthews, Mint Hill, Stallings, Indian Trail, Weddington, Wesley Chapel, Waxhaw, Monroe and Fort Mill SC; plus Concord, Cornelius, Davidson, Huntersville, Mooresville, Marvin, Indian Land SC and Tega Cay SC."),
        ("Are you licensed and insured?", "Yes."),
        ("Are you a manufacturer-authorized service agent?", "We are an independent service company and repair all major brands."),
        ("Do you offer maintenance plans?", "Yes — scheduled coil cleaning, ice machine cleaning and inspections. Ask for a quote."),
        ("How do I request service?", "Call %s or fill in the short form with your name, phone, address and equipment type." % C.PHONE_DISPLAY),
    ]
    simple("/faq/", T("FAQ"), "Frequently Asked Questions",
           "Answers about our commercial refrigeration and kitchen equipment repair: pricing, hours, warranty, service area.",
           "", gen_faq, 0.7)
    simple("/privacy-policy/", T("Privacy Policy"), "Privacy Policy", "How Commercial Appliances handles the information you send us.",
           section("Privacy", "<p>When you submit a service request we collect your name, phone number, service address and equipment type. "
                   "We use it only to contact you about your request and to provide service. We do not sell your information. "
                   "Form submissions are delivered to us by email through Web3Forms. If analytics are enabled, Google Analytics collects "
                   "anonymous usage data. To ask about or delete your information, email %s.</p>" % C.EMAIL), None, 0.2, with_hero=False)
    simple("/terms/", T("Terms of Service"), "Terms of Service", "Terms for using this website and our services.",
           section("Terms", "<p>Prices on this site apply to commercial customers in our service area and may change without notice. "
                   "The $%d discount applies to repair charges, not to the service call, and cannot be combined with other offers. "
                   "Warranty terms are described on our <a href='/warranty/'>warranty page</a>. Brand names are trademarks of their owners; "
                   "we are an independent service company.</p>" % C.DISCOUNT), None, 0.2, with_hero=False)
    # thank-you fallback (no-JS form submit)
    page("/thank-you/", "Thank you | Commercial Appliances", "Your request was received.",
         '<section class="band"><div class="wrap narrow center"><div class="modal-ok big-ok">✓</div><h1>Thank you for your request!</h1>'
         '<p class="lead-p">The first available operator will contact you shortly.</p><p>Need help now? Call <a href="%s"><b>%s</b></a>.</p>'
         '<p><a class="btn btn-primary" href="/">Back to home</a></p></div></section>' % (TEL, C.PHONE_DISPLAY),
         noindex=True)


def build_404():
    page("/404/", "Page not found | Commercial Appliances", "Page not found.",
         '<section class="band"><div class="wrap narrow center"><h1>Page not found</h1><p>Call <a href="%s">%s</a> or go to the '
         '<a href="/">home page</a>.</p></div></section>' % (TEL, C.PHONE_DISPLAY), noindex=True)
    shutil.move(os.path.join(OUT, "404", "index.html"), os.path.join(OUT, "404.html"))
    os.rmdir(os.path.join(OUT, "404"))


# =============================================================== SITEMAPS / ROBOTS / LLMS
def build_html_sitemap():
    groups = {}
    for path, _, g in PAGES:
        groups.setdefault(g, []).append(path)
    names = {"main": "Main pages", "services": "Services", "brands": "Brands", "industries": "Industries", "problems": "Troubleshooting",
             "areas": "Service areas", "keywords": "Popular searches"}
    body = '<section class="band"><div class="wrap"><h1>Sitemap</h1>'
    for g in ["main", "keywords", "services", "areas", "industries", "brands", "problems"]:
        body += "<h2>%s</h2><ul class='linkgrid c3'>%s</ul>" % (names[g], "".join('<li><a href="%s">%s</a></li>' % (p, p) for p in sorted(groups.get(g, []))))
    body += "<p>Location-specific pages are listed in the XML sitemaps and linked from each service area page.</p></div></section>"
    page("/sitemap/", T("Sitemap"), "All pages on the Commercial Appliances website.", body, priority=0.3)


def build_xml_sitemaps():
    groups = {}
    for path, pri, g in PAGES:
        groups.setdefault(g, []).append((path, pri))
    files = []
    for g, items in groups.items():
        # split large groups at 40k for safety (limit is 50k)
        for n in range(0, len(items), 40000):
            name = "sitemap-%s%s.xml" % (g, "" if n == 0 else "-%d" % (n // 40000 + 1))
            xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
            for path, pri in items[n:n + 40000]:
                xml.append("<url><loc>%s</loc><lastmod>%s</lastmod><priority>%.1f</priority></url>" % (lib.url(path), TODAY, pri))
            xml.append("</urlset>")
            with open(os.path.join(OUT, name), "w") as f:
                f.write("\n".join(xml))
            files.append(name)
    idx = ['<?xml version="1.0" encoding="UTF-8"?>', '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    idx += ["<sitemap><loc>%s/%s</loc><lastmod>%s</lastmod></sitemap>" % (C.SITE_URL, f, TODAY) for f in sorted(files)]
    idx.append("</sitemapindex>")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write("\n".join(idx))


def build_robots_llms():
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("# Search engines and AI assistants are welcome.\nUser-agent: *\nAllow: /\nDisallow: /thank-you/\n\n"
                "User-agent: GPTBot\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: ChatGPT-User\nAllow: /\n\n"
                "User-agent: ClaudeBot\nAllow: /\n\nUser-agent: Claude-SearchBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\n"
                "User-agent: Google-Extended\nAllow: /\n\nUser-agent: Applebot-Extended\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\n"
                "Sitemap: %s/sitemap.xml\n" % C.SITE_URL)
    svc = "\n".join("- [%s Repair](%s/services/%s/): %s" % (q["name"], C.SITE_URL, q["slug"], q["intro"].split(". ")[0] + ".") for q in EQUIPMENT)
    areas = "\n".join("- [%s](%s/service-areas/%s/)" % (place(a), C.SITE_URL, a["slug"]) for a in AREAS.values())
    hours = "\n".join("- %s: %s" % (d, fmt) for d, fmt in [(d, lib.fmt_range(o, c)) for d, o, c in C.HOURS])
    txt = """# Commercial Appliances

> Licensed and insured commercial refrigeration and commercial kitchen equipment repair company based in Charlotte, North Carolina. Serves restaurants, cafés, bars, breweries, grocery and convenience stores, bakeries, hotels, schools, healthcare and senior living kitchens in Charlotte, NC and nearby cities in North and South Carolina.

## Key facts
- Business name: Commercial Appliances
- Website: {site}
- Phone: {phone}
- Email: {email}
- Location: Charlotte, NC (mobile service; technicians come to the customer; no walk-in storefront)
- Service call / diagnostic: ${call}
- Offer: ${disc} off any repair when booked online or when the customer mentions the website
- Warranty: {lab}-day labor, {parts}-day parts on every repair; extended 1, 3 or 5-year warranty on select repairs and installations
- Credentials: licensed and insured
- Same-day service: available when the customer calls early and a technician is free; not a 24/7 service
- Scope: commercial equipment only (no residential appliances)
- Independent service company; not a manufacturer-authorized agent. Repairs {nbrands}+ brands including True, Traulsen, Hoshizaki, Manitowoc, Scotsman, Kolpak, Turbo Air, Beverage-Air, Vulcan, Garland, Frymaster, Pitco, Hobart, Rational.

## Hours (Eastern Time)
{hours}

In words: open {hsent}.

## Services
{svc}

## Service areas
{areas}

## Useful pages
- [Pricing]({site}/pricing/)
- [Warranty]({site}/warranty/)
- [FAQ]({site}/faq/)
- [Contact]({site}/contact/)
- [Troubleshooting guides]({site}/problems/)
- [Sitemap]({site}/sitemap.xml)
""".format(site=C.SITE_URL, phone=C.PHONE_DISPLAY, email=C.EMAIL, call=C.SERVICE_CALL, disc=C.DISCOUNT,
           lab=C.LABOR_WARRANTY_DAYS, parts=C.PARTS_WARRANTY_DAYS, nbrands=len(BRANDS), hours=hours,
           hsent=C.HOURS_SENTENCE, svc=svc, areas=areas)
    with open(os.path.join(OUT, "llms.txt"), "w") as f:
        f.write(txt)


def copy_static():
    shutil.copytree(os.path.join(ROOT, "static"), OUT, dirs_exist_ok=True)
    domain = C.SITE_URL.split("//", 1)[1]
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write(domain + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    import hashlib
    css = open(os.path.join(ROOT, "static", "assets", "site.css"), "rb").read()
    js = open(os.path.join(ROOT, "static", "assets", "site.js"), "rb").read()
    lib.ASSET_VERSION = hashlib.md5(css + js).hexdigest()[:8]
    copy_static()
    build_home(); build_services(); build_brands(); build_industries(); build_problems()
    build_areas(); build_keyword_pages(); build_static(); build_404(); build_html_sitemap()
    build_xml_sitemaps(); build_robots_llms()
    counts = {}
    for _, _, g in PAGES:
        counts[g] = counts.get(g, 0) + 1
    print("Built %d indexable pages into %s" % (len(PAGES), OUT))
    for g, n in sorted(counts.items(), key=lambda x: -x[1]):
        print("  %-18s %d" % (g, n))
    if C.WEB3FORMS_ACCESS_KEY.startswith("YOUR-"):
        print("\n!! WEB3FORMS_ACCESS_KEY is not set in generator/config.py — the form will not deliver email yet.")


if __name__ == "__main__":
    main()
