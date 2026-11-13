"""Real customer reviews only. The reviews section stays hidden while this list is empty.

Copy reviews from your Google Business Profile as they come in, e.g.:

REVIEWS = [
    dict(name="Jane D.", date="2026-11-03", rating=5, source="Google",
         text="Our walk-in cooler stopped cooling on a Saturday...", tag="Walk-in cooler"),
]

If you add Google reviews, also set GOOGLE_PROFILE_URL in config.py so the
'See all reviews on Google' link works. Never add reviews that did not happen:
fake reviews are illegal under the FTC rule (16 CFR Part 465) and get sites penalized.
"""

REVIEWS = []
