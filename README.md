# omniservicegruop.com

Static website for **Commercial Appliances** — commercial refrigeration and kitchen equipment repair, Charlotte, NC.
A Python generator (no dependencies) builds ~2,600 SEO pages into `_site/`. GitHub Actions builds and publishes to GitHub Pages on every push to `main`.

## Edit content

| What | File |
|---|---|
| Phone, email, prices, discount, warranty, hours, form key, analytics IDs | `generator/config.py` |
| Equipment types (text, symptoms, FAQ, brands per type) | `generator/data_equipment.py` |
| Brands (`top=True` → also gets a page in every area) | `generator/data_brands.py` |
| Cities and Charlotte neighborhoods | `generator/data_areas.py` |
| Industries, troubleshooting pages, keyword landing pages | `generator/data_misc.py` |
| Real customer reviews (section hidden while empty) | `generator/reviews.py` |
| Design | `static/assets/site.css` |
| Form + thank-you popup | `static/assets/site.js` |

You can edit these files right on github.com — the site rebuilds automatically.

## Build locally

```bash
python3 generator/build.py && python3 generator/qa.py
cd _site && python3 -m http.server 8080   # open http://localhost:8080
```

## One-time setup

1. **Form email** — go to https://web3forms.com, enter `omnicommercialrefrigeration@gmail.com`, copy the Access Key from the email, paste it into `WEB3FORMS_ACCESS_KEY` in `generator/config.py`, push.
2. **GitHub Pages** — repo → Settings → Pages → Source: **GitHub Actions**. Custom domain: `omniservicegruop.com`, tick **Enforce HTTPS** once available.
3. **DNS** (at your domain registrar):
   - `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` for `www` → `<your-github-username>.github.io`
4. **Google Search Console** — add the domain, put the token in `GSC_VERIFICATION`, submit `https://omniservicegruop.com/sitemap.xml`. Do the same in Bing Webmaster Tools (Bing feeds ChatGPT search and Copilot).
5. **Google Business Profile** — create it as a service-area business (no address shown), hours identical to the site, then put its URL in `GOOGLE_PROFILE_URL`.
6. **GA4** (optional) — put the Measurement ID in `GA4_ID`. Form sends fire `generate_lead`; phone taps fire `phone_call_click`.

## Page structure

- `/services/{equipment}/`, `/brands/{brand}/`, `/brands/{brand}/{equipment}/`, `/industries/{type}/`, `/problems/{problem}/`
- `/service-areas/{area}/` + `{equipment}/`, `{category}/`, `brands/{brand}/`, `industries/{type}/`, `problems/{problem}/` (problems: cities only)
- Root keyword pages, e.g. `/commercial-refrigeration-repair-charlotte-nc/`, `/walk-in-cooler-repair-near-me/`
- `llms.txt`, `robots.txt` (AI crawlers allowed), split XML sitemaps, JSON-LD (LocalBusiness, Service, FAQPage, BreadcrumbList) on every page.

Charlotte-city combinations intentionally reuse the citywide pages (`/services/…`, `/brands/…`) so two pages never compete for the same search.
