"""Service areas. kind: city | hood (Charlotte neighborhood) | ext (extended-coverage city).
`spots` = real commercial corridors / landmarks used to make each page locally specific."""

A = lambda name, kind, county, state, zips, spots, blurb, near: dict(
    name=name, kind=kind, county=county, state=state, zips=zips, spots=spots, blurb=blurb, near=near)

AREAS = {
    # ---------------- 12 full cities ----------------
    "charlotte": A("Charlotte", "city", "Mecklenburg", "NC",
        ["28202", "28203", "28204", "28205", "28206", "28207", "28208", "28209", "28210", "28211", "28212",
         "28213", "28215", "28216", "28217", "28226", "28227", "28262", "28269", "28270", "28273", "28277", "28278"],
        ["Uptown and the Tryon Street hotel corridor", "South End and the Rail Trail", "the airport and Wilkinson Boulevard",
         "Independence Boulevard", "University City", "SouthPark"],
        "Charlotte has one of the fastest-growing restaurant and hospitality scenes in the Southeast — from Uptown hotel "
        "kitchens and South End breweries to grocery stores, schools and hospital cafeterias across Mecklenburg County.",
        ["uptown", "south-end", "southpark", "university-city", "steele-creek", "ballantyne", "matthews", "pineville"]),
    "ballantyne": A("Ballantyne", "city", "Mecklenburg", "NC", ["28277"],
        ["Ballantyne Corporate Park", "Johnston Road", "Ballantyne Village", "the Rea Road and I-485 interchange"],
        "Ballantyne mixes corporate campuses, hotels, corporate cafeterias and a dense row of restaurants along Johnston Road.",
        ["blakeney", "piper-glen", "rea-farms", "pineville", "fort-mill", "providence-plantation"]),
    "pineville": A("Pineville", "city", "Mecklenburg", "NC", ["28134"],
        ["Carolina Place Mall", "Polk Street", "NC-51", "the US-521 corridor"],
        "Pineville is a retail hub on the Charlotte–South Carolina line, packed with chain restaurants, fast casual "
        "concepts and big-box grocery around Carolina Place.",
        ["ballantyne", "charlotte", "fort-mill", "steele-creek", "matthews"]),
    "matthews": A("Matthews", "city", "Mecklenburg", "NC", ["28104", "28105"],
        ["downtown Matthews on Trade Street", "Independence Boulevard (US-74)", "Sycamore Commons", "Matthews Township Parkway"],
        "Matthews combines a walkable downtown restaurant row with heavy retail along US-74 and a busy medical corridor.",
        ["mint-hill", "stallings", "indian-trail", "charlotte", "weddington", "pineville"]),
    "mint-hill": A("Mint Hill", "city", "Mecklenburg", "NC", ["28227"],
        ["Lawyers Road", "Matthews-Mint Hill Road", "the Mint Hill town center", "the Novant Health Mint Hill campus"],
        "Mint Hill's restaurants, grocery stores and medical facilities sit along Lawyers Road and Matthews-Mint Hill Road.",
        ["matthews", "charlotte", "stallings", "indian-trail"]),
    "stallings": A("Stallings", "city", "Union", "NC", ["28104"],
        ["US-74", "Stallings Road", "Idlewild Road", "Matthews-Indian Trail Road"],
        "Stallings sits between Matthews and Indian Trail with restaurants, convenience stores and shopping centers "
        "along US-74.",
        ["matthews", "indian-trail", "mint-hill", "weddington"]),
    "indian-trail": A("Indian Trail", "city", "Union", "NC", ["28079"],
        ["US-74", "Indian Trail Road", "Wesley Chapel–Stouts Road", "Unionville–Indian Trail Road"],
        "Indian Trail is one of Union County's fastest-growing towns, with new restaurants, grocery anchors and "
        "school kitchens opening every year.",
        ["stallings", "monroe", "wesley-chapel", "matthews"]),
    "weddington": A("Weddington", "city", "Union", "NC", ["28104", "28173"],
        ["Providence Road (NC-16)", "Weddington Corners", "Weddington Road", "Weddington–Matthews Road"],
        "Weddington's restaurants, country clubs and shopping centers cluster along Providence Road and Weddington Corners.",
        ["waxhaw", "wesley-chapel", "matthews", "marvin", "stallings"]),
    "wesley-chapel": A("Wesley Chapel", "city", "Union", "NC", ["28104", "28110"],
        ["Wesley Chapel Road", "NC-84", "Waxhaw–Indian Trail Road", "the Wesley Chapel shopping centers"],
        "Wesley Chapel's commercial strip along NC-84 and Wesley Chapel Road serves fast-growing neighborhoods "
        "between Weddington, Waxhaw and Monroe.",
        ["weddington", "waxhaw", "monroe", "indian-trail"]),
    "waxhaw": A("Waxhaw", "city", "Union", "NC", ["28173"],
        ["historic downtown Waxhaw on Main Street", "NC-16 (Providence Road South)", "NC-75", "Cuthbertson Road"],
        "Waxhaw's historic downtown restaurants and the shopping centers on NC-16 serve one of the fastest-growing "
        "parts of the Charlotte region.",
        ["weddington", "wesley-chapel", "marvin", "indian-land", "monroe"]),
    "monroe": A("Monroe", "city", "Union", "NC", ["28110", "28112"],
        ["downtown Monroe on Main Street", "Roosevelt Boulevard (US-74)", "the Charlotte–Monroe Executive Airport area",
         "the Atrium Health Union campus"],
        "Monroe is the Union County seat, with food manufacturing, a hospital, schools and a long restaurant and "
        "grocery corridor along US-74.",
        ["indian-trail", "wesley-chapel", "waxhaw", "stallings"]),
    "fort-mill": A("Fort Mill", "city", "York", "SC", ["29707", "29708", "29715"],
        ["Main Street", "Baxter Village", "Kingsley Town Center", "the I-77 and US-21 corridor near Carowinds"],
        "Fort Mill, just across the state line, has fast-growing restaurant, hotel and grocery development along "
        "I-77 and in its town centers.",
        ["tega-cay", "indian-land", "ballantyne", "pineville", "steele-creek"]),
    # ---------------- 16 Charlotte neighborhoods ----------------
    "uptown": A("Uptown Charlotte", "hood", "Mecklenburg", "NC", ["28202", "28244", "28280"],
        ["Tryon Street", "the Epicentre", "Bank of America Stadium", "Spectrum Center", "the Convention Center hotels"],
        "Uptown is Charlotte's densest commercial district: hotel kitchens, banquet halls, stadium concessions, "
        "bars and high-volume restaurants that can't afford downtime.",
        ["south-end", "dilworth", "elizabeth", "plaza-midwood", "noda"]),
    "south-end": A("South End", "hood", "Mecklenburg", "NC", ["28203"],
        ["the Rail Trail", "Camden Road", "South Boulevard", "Atherton Mill"],
        "South End is packed with breweries, taprooms, cafés and new restaurants along the light rail — draft systems, "
        "ice machines and bar coolers are everywhere.",
        ["uptown", "dilworth", "myers-park", "charlotte"]),
    "dilworth": A("Dilworth", "hood", "Mecklenburg", "NC", ["28203", "28204"],
        ["East Boulevard", "Kenilworth Avenue", "Latta Park", "the Morehead Street corridor"],
        "Dilworth's East Boulevard restaurants, coffee shops and bars sit in historic buildings where equipment space "
        "is tight and reliability matters.",
        ["south-end", "myers-park", "uptown", "elizabeth"]),
    "myers-park": A("Myers Park", "hood", "Mecklenburg", "NC", ["28207", "28209"],
        ["Queens Road", "Selwyn Avenue", "Providence Road", "Queens University of Charlotte"],
        "Myers Park's restaurants, clubs, school dining halls and specialty grocers serve one of Charlotte's oldest "
        "neighborhoods.",
        ["dilworth", "eastover", "southpark", "elizabeth"]),
    "southpark": A("SouthPark", "hood", "Mecklenburg", "NC", ["28209", "28210", "28211"],
        ["SouthPark Mall", "Phillips Place", "Fairview Road", "Sharon Road"],
        "SouthPark is Charlotte's second downtown — upscale restaurants, hotels and grocery stores around the mall "
        "and Phillips Place.",
        ["myers-park", "cotswold", "eastover", "charlotte"]),
    "plaza-midwood": A("Plaza Midwood", "hood", "Mecklenburg", "NC", ["28205"],
        ["Central Avenue", "The Plaza", "Commonwealth Avenue", "Thomas Street"],
        "Plaza Midwood's independent restaurants, bars and cafés line Central Avenue and The Plaza.",
        ["noda", "elizabeth", "uptown", "cotswold"]),
    "noda": A("NoDa", "hood", "Mecklenburg", "NC", ["28205", "28206"],
        ["North Davidson Street", "36th Street", "the Blue Line stations", "the NoDa brewery district"],
        "NoDa, Charlotte's arts district, is full of breweries, music venues, bars and restaurants that live on cold "
        "beer and working ice machines.",
        ["plaza-midwood", "university-city", "uptown"]),
    "university-city": A("University City", "hood", "Mecklenburg", "NC", ["28262", "28213"],
        ["UNC Charlotte", "J.W. Clay Boulevard", "the Atrium Health University City campus", "W.T. Harris Boulevard"],
        "University City's restaurants, hotels, campus dining and hospital kitchens serve tens of thousands of "
        "students and workers every day.",
        ["noda", "charlotte", "concord", "huntersville"]),
    "steele-creek": A("Steele Creek", "hood", "Mecklenburg", "NC", ["28273", "28278"],
        ["Charlotte Premium Outlets", "Steele Creek Road", "the I-485 and South Tryon interchange", "the Westinghouse Boulevard industrial area"],
        "Steele Creek combines outlet shopping and new restaurants with warehouses and food distribution facilities "
        "near the airport and I-485.",
        ["charlotte", "pineville", "fort-mill", "tega-cay"]),
    "cotswold": A("Cotswold", "hood", "Mecklenburg", "NC", ["28211"],
        ["Cotswold Village shopping center", "Randolph Road", "Sharon Amity Road", "Providence Road"],
        "Cotswold Village anchors a cluster of grocery stores, restaurants and cafés serving east Charlotte.",
        ["southpark", "eastover", "plaza-midwood", "myers-park"]),
    "elizabeth": A("Elizabeth", "hood", "Mecklenburg", "NC", ["28204"],
        ["Elizabeth Avenue", "7th Street", "Novant Health Presbyterian Medical Center", "CPCC Central Campus"],
        "Elizabeth's restaurants and bars sit next to a major hospital and college campus with large institutional kitchens.",
        ["uptown", "plaza-midwood", "dilworth", "myers-park"]),
    "eastover": A("Eastover", "hood", "Mecklenburg", "NC", ["28207"],
        ["Providence Road", "Randolph Road", "the Mint Museum Randolph", "Sharon Road"],
        "Eastover is one of Charlotte's most established neighborhoods, with private clubs, schools and nearby "
        "restaurant and grocery corridors.",
        ["myers-park", "cotswold", "southpark", "elizabeth"]),
    "blakeney": A("Blakeney", "hood", "Mecklenburg", "NC", ["28277"],
        ["Blakeney Shopping Center", "Rea Road", "the I-485 and Rea Road interchange", "Providence Road"],
        "Blakeney's shopping center and the Rea Road corridor are full of restaurants, grocery stores and fast casual concepts.",
        ["rea-farms", "piper-glen", "ballantyne", "marvin", "providence-plantation"]),
    "piper-glen": A("Piper Glen", "hood", "Mecklenburg", "NC", ["28277"],
        ["Rea Road", "Piper Glen Drive", "Carmel Road", "the Ballantyne edge of I-485"],
        "Piper Glen sits between Ballantyne and Blakeney, close to country clubs and restaurant corridors on Rea Road.",
        ["ballantyne", "blakeney", "rea-farms", "providence-plantation"]),
    "providence-plantation": A("Providence Plantation", "hood", "Mecklenburg", "NC", ["28270", "28277"],
        ["Providence Road", "the Providence Road and I-485 interchange", "Ardrey Kell Road", "Providence Commons"],
        "Providence Plantation's shopping centers along Providence Road serve fast-growing south Charlotte.",
        ["blakeney", "piper-glen", "rea-farms", "ballantyne", "weddington"]),
    "rea-farms": A("Rea Farms", "hood", "Mecklenburg", "NC", ["28277"],
        ["the Rea Farms village center", "Rea Road", "Williams Pond Lane", "Ardrey Kell Road"],
        "Rea Farms is a newer mixed-use district with restaurants, cafés, a grocery anchor and medical offices.",
        ["blakeney", "piper-glen", "ballantyne", "providence-plantation"]),
    # ---------------- 8 extended-coverage cities ----------------
    "concord": A("Concord", "ext", "Cabarrus", "NC", ["28025", "28027"],
        ["Concord Mills", "Charlotte Motor Speedway", "downtown Union Street", "the George Liles Parkway corridor"],
        "Concord's Concord Mills area and speedway corridor host dozens of restaurants, hotels and grocery stores.",
        ["university-city", "huntersville"]),
    "cornelius": A("Cornelius", "ext", "Mecklenburg", "NC", ["28031"],
        ["Exit 28 and Catawba Avenue", "the Lake Norman waterfront", "West Catawba Avenue", "Torrence Chapel Road"],
        "Cornelius serves Lake Norman with waterfront restaurants, marinas and shopping centers off Exit 28.",
        ["davidson", "huntersville", "mooresville"]),
    "davidson": A("Davidson", "ext", "Mecklenburg", "NC", ["28035", "28036"],
        ["Main Street", "Davidson College", "Griffith Street", "the Exit 30 corridor"],
        "Davidson's Main Street restaurants and college dining serve the north end of Lake Norman.",
        ["cornelius", "huntersville", "mooresville"]),
    "huntersville": A("Huntersville", "ext", "Mecklenburg", "NC", ["28078"],
        ["Birkdale Village", "Gilead Road", "the Exit 23 and Exit 25 corridors", "Sam Furr Road"],
        "Huntersville's Birkdale Village and I-77 exits are lined with restaurants, grocery stores and hotels.",
        ["cornelius", "davidson", "university-city", "concord"]),
    "mooresville": A("Mooresville", "ext", "Iredell", "NC", ["28115", "28117"],
        ["the Lake Norman area off I-77", "Williamson Road", "downtown Main Street", "Morrison Plantation"],
        "Mooresville's restaurants, marinas and grocery stores serve the east side of Lake Norman.",
        ["cornelius", "davidson"]),
    "marvin": A("Marvin", "ext", "Union", "NC", ["28173"],
        ["Marvin Road", "Providence Road (NC-16)", "New Town Road", "the Blakeney edge"],
        "Marvin is a residential village between Waxhaw and Blakeney with nearby restaurants and clubs.",
        ["waxhaw", "weddington", "blakeney"]),
    "indian-land": A("Indian Land", "ext", "Lancaster", "SC", ["29707"],
        ["US-521 (Charlotte Highway)", "the Sun City Carolina Lakes area", "Marvin Road SC", "the Red Ventures campus"],
        "Indian Land's US-521 corridor has grown fast with new restaurants, grocery stores and corporate dining.",
        ["fort-mill", "waxhaw", "ballantyne"]),
    "tega-cay": A("Tega Cay", "ext", "York", "SC", ["29708"],
        ["Gold Hill Road", "the Lake Wylie shoreline", "Stonecrest Boulevard", "Tega Cay Drive"],
        "Tega Cay's lakeside restaurants, clubs and Gold Hill Road shopping centers serve the Lake Wylie area.",
        ["fort-mill", "steele-creek"]),
}

for slug, a in AREAS.items():
    a["slug"] = slug

FULL = [a for a in AREAS.values() if a["kind"] in ("city", "hood")]
CITIES = [a for a in AREAS.values() if a["kind"] == "city"]
HOODS = [a for a in AREAS.values() if a["kind"] == "hood"]
EXT = [a for a in AREAS.values() if a["kind"] == "ext"]


def place(a):
    """Display name with state, e.g. 'Fort Mill, SC' or 'SouthPark, Charlotte'."""
    if a["kind"] == "hood":
        n = a["name"]
        return n if "Charlotte" in n else n + ", Charlotte"
    return "%s, %s" % (a["name"], a["state"])
