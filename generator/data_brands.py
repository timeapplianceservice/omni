"""Brands. `top=True` brands also get brand x location pages.
Facts are kept to well-known product lines. We are an independent service company."""

from data_equipment import EQUIPMENT

B = lambda name, lines, top=False, note="": dict(name=name, lines=lines, top=top, note=note)

BRANDS = {
    # --- Walk-in / refrigeration systems ---
    "kolpak": B("Kolpak", "walk-in coolers and freezers and their refrigeration systems", True),
    "norlake": B("Nor-Lake", "walk-in coolers and freezers, reach-ins and refrigeration systems", True),
    "master-bilt": B("Master-Bilt", "walk-ins, ice cream and display freezers, and refrigeration systems", True),
    "heatcraft": B("Heatcraft", "evaporators, unit coolers and condensing units used in walk-ins", True),
    "bally": B("Bally", "walk-in coolers and freezers and refrigeration systems"),
    "american-panel": B("American Panel", "walk-ins and blast chillers"),
    "polar-king": B("Polar King", "outdoor fiberglass walk-in coolers and freezers"),
    "imperial-brown": B("Imperial Brown", "custom walk-in coolers and freezers"),
    "copeland": B("Copeland", "refrigeration compressors and condensing units", True),
    "tecumseh": B("Tecumseh", "compressors and condensing units"),
    "bitzer": B("Bitzer", "semi-hermetic and scroll compressors"),
    "danfoss": B("Danfoss", "compressors, valves and refrigeration controls"),
    "larkin": B("Larkin", "evaporators and unit coolers"),
    "russell": B("Russell", "evaporators, unit coolers and condensing units"),
    # --- Ice ---
    "hoshizaki": B("Hoshizaki", "ice machines, reach-in refrigerators and prep tables", True),
    "manitowoc": B("Manitowoc", "modular, undercounter and nugget ice machines", True),
    "scotsman": B("Scotsman", "cube, nugget and flake ice machines", True),
    "ice-o-matic": B("Ice-O-Matic", "cube and flake ice machines", True),
    "follett": B("Follett", "nugget ice machines, dispensers and storage bins"),
    "kold-draft": B("Kold-Draft", "full-cube ice machines for bars"),
    "cornelius": B("Cornelius", "ice and beverage dispensers"),
    # --- Reach-in / prep ---
    "true": B("True", "reach-ins, prep tables, undercounters, bar coolers and merchandisers", True),
    "traulsen": B("Traulsen", "reach-in and roll-in refrigerators, freezers and blast chillers", True),
    "turbo-air": B("Turbo Air", "reach-ins, prep tables, undercounters and display cases", True),
    "beverage-air": B("Beverage-Air", "reach-ins, prep tables, bar coolers and merchandisers", True),
    "delfield": B("Delfield", "reach-ins, prep tables, chef bases and refrigerated wells", True),
    "atosa": B("Atosa", "reach-ins, prep tables, undercounters and ice machines", True),
    "continental": B("Continental Refrigerator", "reach-ins, prep tables and undercounters"),
    "victory": B("Victory", "reach-in refrigerators and freezers"),
    "arctic-air": B("Arctic Air", "reach-in refrigerators and freezers"),
    "avantco": B("Avantco", "prep tables, reach-ins and undercounter refrigeration"),
    "foster": B("Foster", "reach-ins and blast chillers"),
    "irinox": B("Irinox", "blast chillers and shock freezers"),
    # --- Display / grocery ---
    "hussmann": B("Hussmann", "grocery display cases and refrigeration systems", True),
    "hill-phoenix": B("Hill Phoenix", "grocery display cases and refrigeration racks", True),
    "federal-industries": B("Federal Industries", "bakery and deli display cases"),
    "structural-concepts": B("Structural Concepts", "refrigerated and heated display cases"),
    # --- Bar ---
    "perlick": B("Perlick", "back-bar coolers, draft systems and underbar equipment", True),
    "krowne": B("Krowne", "back-bar coolers and underbar equipment"),
    "glastender": B("Glastender", "back-bar coolers, draft systems and glass washers"),
    "micro-matic": B("Micro Matic", "draft beer systems and kegerators"),
    # --- Cooking ---
    "vulcan": B("Vulcan", "ranges, ovens, fryers, griddles and steamers", True),
    "garland": B("Garland", "ranges, convection ovens and griddles", True),
    "southbend": B("Southbend", "ranges, convection ovens and steamers", True),
    "blodgett": B("Blodgett", "convection, deck and combi ovens", True),
    "rational": B("Rational", "combi ovens and multi-function cooking systems", True),
    "lincoln": B("Lincoln Impinger", "conveyor pizza ovens"),
    "middleby-marshall": B("Middleby Marshall", "conveyor ovens"),
    "alto-shaam": B("Alto-Shaam", "cook-and-hold ovens, combi ovens and holding cabinets", True),
    "cleveland": B("Cleveland", "steamers, kettles and tilting skillets"),
    "montague": B("Montague", "ranges and ovens"),
    "wolf": B("Wolf Commercial", "ranges, griddles and charbroilers"),
    "imperial": B("Imperial", "ranges, fryers and broilers"),
    "jade": B("Jade Range", "heavy-duty ranges and wok ranges"),
    "american-range": B("American Range", "ranges, ovens and broilers"),
    "frymaster": B("Frymaster", "gas and electric fryers and filtration systems", True),
    "pitco": B("Pitco", "gas and electric fryers", True),
    "henny-penny": B("Henny Penny", "pressure fryers, open fryers and holding cabinets", True),
    "dean": B("Dean", "gas fryers"),
    "keating": B("Keating", "fryers and griddles"),
    "star": B("Star", "griddles, charbroilers and countertop cooking"),
    "apw-wyott": B("APW Wyott", "countertop cooking and food warmers"),
    "wells": B("Wells", "fryers, food warmers and countertop equipment"),
    "groen": B("Groen", "steam kettles, braising pans and steamers"),
    "market-forge": B("Market Forge", "steamers"),
    "accutemp": B("AccuTemp", "connectionless steamers and griddles"),
    "taylor": B("Taylor", "soft serve, shake machines and clamshell grills", True),
    "stoelting": B("Stoelting", "soft serve and frozen custard machines"),
    "electro-freeze": B("Electro Freeze", "soft serve and frozen beverage machines"),
    "spaceman": B("Spaceman", "soft serve and frozen yogurt machines"),
    # --- Dish / prep ---
    "hobart": B("Hobart", "dishwashers, mixers and slicers", True),
    "jackson": B("Jackson", "commercial dishwashers", True),
    "champion": B("Champion", "commercial dishwashers"),
    "cma": B("CMA", "commercial dishwashers and glass washers"),
    "insinger": B("Insinger", "dishwashers"),
    "moyer-diebel": B("Moyer Diebel", "glass washers and dishwashers"),
    "meiko": B("Meiko", "warewashing machines"),
    "globe": B("Globe", "slicers and mixers"),
    "berkel": B("Berkel", "slicers"),
    "robot-coupe": B("Robot Coupe", "food processors and immersion blenders"),
    "vollrath": B("Vollrath", "food prep and warming equipment"),
    # --- Holding ---
    "hatco": B("Hatco", "heat lamps, food warmers and booster heaters", True),
    "winston": B("Winston", "CVAP holding cabinets"),
    "metro": B("Metro", "heated holding cabinets"),
    "cres-cor": B("Cres Cor", "heated holding cabinets"),
    # --- Beverage ---
    "bunn": B("BUNN", "coffee brewers, iced tea and frozen beverage machines", True),
    "fetco": B("Fetco", "coffee brewers"),
    "curtis": B("Curtis", "coffee brewers"),
    "grindmaster": B("Grindmaster", "coffee brewers and grinders"),
}

# Which equipment pages each brand appears on (derived from data_equipment)
for slug, b in BRANDS.items():
    b["slug"] = slug
    b["equipment"] = [e["slug"] for e in EQUIPMENT if slug in e["brands"]]

missing = sorted({s for e in EQUIPMENT for s in e["brands"]} - set(BRANDS))
assert not missing, "brands referenced but not defined: %s" % missing

TOP_BRANDS = [b for b in BRANDS.values() if b["top"]]
