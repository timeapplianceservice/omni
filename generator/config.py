"""Business facts. Change anything here and rebuild — every page updates."""

SITE_URL = "https://omniservicegruop.com"  # no trailing slash
BRAND = "Commercial Appliances"
BRAND_LONG = "Commercial Appliances — Commercial Refrigeration & Kitchen Equipment Repair"
PHONE_DISPLAY = "(980) 983-2911"
PHONE_E164 = "+19809832911"
EMAIL = "omnicommercialrefrigeration@gmail.com"

# Web3Forms access key: get it free at https://web3forms.com (enter the email above,
# the key arrives by email). Paste it here and rebuild. Requests go to EMAIL.
WEB3FORMS_ACCESS_KEY = "YOUR-WEB3FORMS-ACCESS-KEY"

# Google Analytics 4 measurement ID (e.g. "G-XXXXXXX"). Leave blank to disable.
GA4_ID = ""
# Google Search Console verification token (content of the meta tag). Optional.
GSC_VERIFICATION = ""
# Bing Webmaster verification (msvalidate.01). Optional.
BING_VERIFICATION = ""
# Google Business Profile URL, once it exists. Used in schema sameAs and the review CTA.
GOOGLE_PROFILE_URL = ""

CITY = "Charlotte"
STATE = "NC"
GEO = (35.2271, -80.8431)

SERVICE_CALL = 135          # USD diagnostic / service call
DISCOUNT = 50               # USD off repair
LABOR_WARRANTY_DAYS = 30
PARTS_WARRANTY_DAYS = 90
EXTENDED_WARRANTY_YEARS = (1, 3, 5)

# Opening hours (24h). Used in schema and written out in words on the site.
HOURS = [
    ("Monday", "08:00", "18:00"),
    ("Tuesday", "08:00", "18:00"),
    ("Wednesday", "08:00", "18:00"),
    ("Thursday", "08:00", "18:00"),
    ("Friday", "08:00", "18:00"),
    ("Saturday", "08:00", "18:00"),
    ("Sunday", "10:00", "15:00"),
]
HOURS_SENTENCE = ("Monday through Saturday from 8:00 AM to 6:00 PM, and Sunday from "
                  "10:00 AM to 3:00 PM (Eastern Time)")
HOURS_SHORT = "Mon–Sat 8 AM–6 PM · Sun 10 AM–3 PM"

