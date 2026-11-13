"""Equipment types we service. Every field is used to build unique page copy."""

# cat: "refrigeration" | "kitchen"
EQUIPMENT = [
    # ---------------- REFRIGERATION ----------------
    dict(
        slug="walk-in-cooler-repair", name="Walk-In Cooler", cat="refrigeration",
        kw="walk-in cooler repair",
        intro=("A walk-in cooler holds most of a kitchen's inventory, so when the box climbs above 41°F "
               "every hour counts. Our technicians work on the whole system — the condensing unit outside "
               "or on the roof, the evaporator and fans inside the box, the defrost controls, door gaskets, "
               "heater wires and the refrigerant circuit."),
        why=("Most walk-in calls come down to a few causes: a dirty or blocked condenser coil, a failed "
             "evaporator or condenser fan motor, a refrigerant leak, an iced-over evaporator from a defrost "
             "fault, or a door that no longer seals. We test each one instead of guessing, so you pay for the "
             "repair the box actually needs."),
        symptoms=["Box temperature above 41°F or slowly creeping up", "Ice building on the evaporator coil",
                  "Water leaking onto the floor or dripping from the ceiling unit",
                  "Condensing unit running non-stop or short-cycling", "Door not closing or gasket torn",
                  "Loud fan noise, rattling or buzzing"],
        tasks=["Measure box, coil and ambient temperatures and superheat", "Clean condenser and evaporator coils",
               "Test and replace evaporator / condenser fan motors", "Find and repair refrigerant leaks, recharge to spec",
               "Repair defrost timers, heaters and termination switches", "Replace door gaskets, closers, hinges and heater wire",
               "Replace compressors, contactors, capacitors and controls", "Clear frozen or clogged drain lines"],
        tip="Keep at least 4 inches of clearance in front of the evaporator — boxes packed to the ceiling cool unevenly and ice up faster.",
        faq=[("How fast should a walk-in cooler recover after the door is opened?",
              "A healthy walk-in should pull back to 35–38°F within 15–30 minutes of normal door traffic. If it takes hours, the system is low on capacity — usually a dirty coil, low refrigerant or a weak compressor."),
             ("Can you repair a walk-in cooler the same day?",
              "In most cases, yes. Our vans carry common fan motors, capacitors, contactors, defrost parts and gaskets. Compressors and some brand-specific parts may need to be ordered.")],
        brands=["kolpak", "norlake", "master-bilt", "heatcraft", "bally", "american-panel", "copeland", "polar-king", "imperial-brown"],
    ),
    dict(
        slug="walk-in-freezer-repair", name="Walk-In Freezer", cat="refrigeration",
        kw="walk-in freezer repair",
        intro=("A walk-in freezer should hold between -10°F and 0°F. Freezers work harder than coolers: they "
               "rely on a timed defrost cycle, heated door frames and drain line heaters, and any one of those "
               "can fail and leave you with a block of ice and soft product."),
        why=("We see the same pattern again and again — a defrost heater or timer fails, the coil ices solid, "
             "airflow stops and the box warms up even though the compressor never shuts off. We fix the root "
             "cause, clear the ice safely and check the refrigerant charge before we leave."),
        symptoms=["Freezer above 0°F or ice cream turning soft", "Thick frost or ice on the evaporator",
                  "Ice forming on the floor, door frame or ceiling", "Door frozen shut or hard to open",
                  "Compressor running constantly", "Drain line frozen and water pooling"],
        tasks=["Test defrost heaters, timers and termination thermostats", "Replace drain line heaters and clear drains",
               "Repair door frame heaters and pressure relief ports", "Replace evaporator and condenser fan motors",
               "Leak search, repair and recharge", "Compressor and condensing unit replacement",
               "Replace gaskets, strip curtains and hardware", "Controller and sensor replacement"],
        tip="If you see ice on the floor near the door, check the door gasket and frame heater first — that is the most common cause.",
        faq=[("Why is my walk-in freezer icing up?",
              "Usually a failed defrost component (heater, timer or termination thermostat), a leaking door gasket that lets humid air in, or a frozen drain line. All three are repairable."),
             ("Is it worth repairing an older walk-in freezer?",
              "The insulated box usually lasts decades. The refrigeration system is what wears out, and replacing a condensing unit or evaporator is far cheaper than a new walk-in.")],
        brands=["kolpak", "norlake", "master-bilt", "heatcraft", "bally", "american-panel", "copeland", "polar-king", "imperial-brown"],
    ),
    dict(
        slug="ice-machine-repair", name="Ice Machine", cat="refrigeration",
        kw="commercial ice machine repair",
        intro=("Bars, restaurants, hotels and healthcare facilities run through hundreds of pounds of ice a day. "
               "We repair modular, undercounter and self-contained ice machines, nugget and flake ice makers, "
               "remote condensers and the bins and dispensers that go with them."),
        why=("Ice machines fail for a short list of reasons: scale build-up on the evaporator, a bad water inlet "
             "valve or pump, a failing harvest assist, dirty air-cooled condensers, or a bad sensor or thermistor. "
             "We clean, descale and sanitize as part of the repair so the machine keeps producing."),
        symptoms=["Machine not making ice or making very little", "Cubes small, cloudy, hollow or stuck together",
                  "Ice freezing to the evaporator and not harvesting", "Water leaking from the machine or bin",
                  "Error lights or flashing codes", "Bad taste or odor in the ice"],
        tasks=["Diagnose error codes and control boards", "Descale, clean and sanitize evaporator and water system",
               "Replace water pumps, inlet valves and float switches", "Repair harvest assist, hot gas valves and sensors",
               "Clean or repair air- and water-cooled condensers", "Repair remote condensers and line sets",
               "Replace bin thermostats and ice thickness probes", "Water filter replacement"],
        tip="Schedule a cleaning and descale every 6 months — in Charlotte-area water, scale is the number one cause of low ice production.",
        faq=[("How often should a commercial ice machine be cleaned?",
              "Manufacturers recommend at least every 6 months. High-volume bars and restaurants often benefit from every 3–4 months."),
             ("Why does my ice machine make ice but not drop it?",
              "That is a harvest problem — usually scale on the evaporator, a weak harvest assist, a bad hot gas valve or a faulty sensor.")],
        brands=["hoshizaki", "manitowoc", "scotsman", "ice-o-matic", "follett", "kold-draft", "cornelius", "atosa"],
    ),
    dict(
        slug="reach-in-refrigerator-repair", name="Reach-In Refrigerator", cat="refrigeration",
        kw="reach-in refrigerator repair",
        intro=("Reach-in refrigerators sit on the line and get opened hundreds of times a shift. We service one-, "
               "two- and three-door reach-ins, pass-throughs and roll-ins, both top-mount and bottom-mount systems."),
        why=("Most reach-in failures are caused by a clogged condenser coil from kitchen grease and dust, a failed "
             "fan motor, a bad thermostat or controller, worn gaskets, or a compressor start component. These are "
             "often fixed in one visit."),
        symptoms=["Not cold enough or temperature swings", "Frost on the back wall or coil",
                  "Compressor clicking on and off", "Water under the unit", "Gasket torn or door sagging", "Unit loud or vibrating"],
        tasks=["Condenser coil cleaning", "Fan motor and thermostat replacement", "Controller and probe replacement",
               "Start relay, capacitor and compressor repair", "Gasket and hinge replacement", "Leak repair and recharge"],
        tip="Clean the condenser coil monthly in a busy kitchen — grease and flour dust are what kill reach-in compressors.",
        faq=[("What temperature should a reach-in refrigerator hold?",
              "Between 33°F and 40°F. Health inspectors look for 41°F or below on all cold-held foods."),
             ("Why is my reach-in cold at the bottom and warm at the top?",
              "Usually a failed evaporator fan or an iced coil blocking airflow.")],
        brands=["true", "traulsen", "turbo-air", "beverage-air", "delfield", "atosa", "continental", "victory", "arctic-air", "hoshizaki"],
    ),
    dict(
        slug="reach-in-freezer-repair", name="Reach-In Freezer", cat="refrigeration",
        kw="commercial freezer repair",
        intro=("Reach-in freezers keep fries, proteins and desserts at 0°F or below on the line. We repair "
               "single- and multi-door commercial freezers, including units with electronic controllers and "
               "automatic defrost."),
        why=("Freezers fail most often from defrost problems, failed fan motors, dirty condensers and worn door "
             "gaskets that let warm, humid air in. We restore temperature and fix what caused the failure."),
        symptoms=["Product softening or above 0°F", "Heavy frost on the coil or walls", "Door hard to open or not sealing",
                  "Water or ice under the unit", "Constant running", "Controller showing alarms"],
        tasks=["Defrost system repair", "Fan motor and controller replacement", "Gasket and door heater replacement",
               "Condenser cleaning", "Leak repair and recharge", "Compressor replacement"],
        tip="Don't block the air vent at the top of the cabinet with boxes — freezers need that airflow to defrost properly.",
        faq=[("Why does my commercial freezer keep frosting up?",
              "Usually a defrost failure or a door gasket that no longer seals. Both are routine repairs."),
             ("Should I unplug the freezer to defrost it?",
              "Only as a temporary fix. If it ices up again in a few days, a defrost part has failed and needs to be replaced.")],
        brands=["true", "traulsen", "turbo-air", "beverage-air", "delfield", "atosa", "continental", "victory", "arctic-air"],
    ),
    dict(
        slug="prep-table-repair", name="Prep Table & Sandwich Unit", cat="refrigeration",
        kw="refrigerated prep table repair",
        intro=("Sandwich, salad and pizza prep tables are some of the hardest-working refrigeration on the line. "
               "Pans on top have to stay at 41°F or below while the lid is open for hours. We repair sandwich/salad "
               "units, mega-top units and pizza prep tables."),
        why=("Warm rail pans are the classic complaint. The causes are usually a dirty condenser, a weak "
             "evaporator fan, a blocked air duct to the rail, low refrigerant or a failed thermostat."),
        symptoms=["Top rail pans above 41°F", "Cabinet cold but rail warm", "Ice on the coil",
                  "Lid hinge broken or lid not closing", "Water leaking into the cabinet", "Compressor overheating"],
        tasks=["Rail airflow and duct repair", "Fan motor replacement", "Condenser cleaning",
               "Thermostat and controller replacement", "Leak repair and recharge", "Lid hinge and gasket replacement"],
        tip="Close the rail lid during slow periods — it cuts compressor run time and keeps pans at a safe temperature.",
        faq=[("Why are my prep table pans warm but the cabinet is cold?",
              "The rail depends on airflow from the evaporator. A weak fan, iced coil or blocked duct starves the pans first."),
             ("Can a prep table hold food safely overnight in the rail?",
              "Most manufacturers recommend moving pans to the cabinet or a walk-in overnight; rail units are designed for service hours.")],
        brands=["true", "traulsen", "turbo-air", "beverage-air", "delfield", "atosa", "continental", "avantco"],
    ),
    dict(
        slug="undercounter-refrigerator-repair", name="Undercounter & Worktop Refrigerator", cat="refrigeration",
        kw="undercounter refrigerator repair",
        intro=("Undercounter and worktop refrigerators and freezers sit right next to fryers, grills and ovens. "
               "That heat makes them work harder than any other unit in the kitchen. We repair undercounters, "
               "worktops, chef bases and refrigerated drawers."),
        why=("These compact units breathe through small front grilles that clog fast. Overheated compressors, "
             "failed fans and worn drawer gaskets are the top problems we fix."),
        symptoms=["Not holding temperature during service", "Compressor very hot or tripping",
                  "Drawers not sealing", "Chef base sagging or drawers sticking", "Water underneath", "Noisy operation"],
        tasks=["Front grille and condenser cleaning", "Compressor start component repair", "Fan motor replacement",
               "Drawer slide and gasket replacement", "Controller replacement", "Leak repair and recharge"],
        tip="Leave the front grille clear — never store towels or boxes in front of an undercounter unit.",
        faq=[("Why does my chef base stop cooling during the rush?",
              "It sits under hot equipment and pulls in hot air. A clogged condenser or weak fan can't keep up when the line is busy."),
             ("Can drawer gaskets be replaced individually?", "Yes, each drawer gasket is replaced separately.")],
        brands=["true", "traulsen", "turbo-air", "beverage-air", "delfield", "atosa", "continental", "victory"],
    ),
    dict(
        slug="display-case-repair", name="Refrigerated Display Case", cat="refrigeration",
        kw="refrigerated display case repair",
        intro=("Grocery stores, convenience stores, bakeries and delis depend on display cases and merchandisers "
               "to sell product. We repair open multi-deck cases, glass-door merchandisers, deli and bakery cases, "
               "and floral coolers."),
        why=("Display cases fail from dirty coils, failed fans, lighting and anti-sweat heater problems, "
             "defrost faults and refrigerant leaks. Fogged or sweating glass and warm product are the signs "
             "customers notice first."),
        symptoms=["Product warm at the front of the case", "Glass fogging or sweating", "Lights out or flickering",
                  "Ice on the coil", "Water on the floor", "Case running loud"],
        tasks=["Evaporator and condenser cleaning", "Fan motor replacement", "Anti-sweat heater and door heater repair",
               "LED lighting and ballast replacement", "Defrost repair", "Leak repair and recharge"],
        tip="Keep product behind the load line marked in the case — overloading blocks the air curtain.",
        faq=[("Why is my glass-door merchandiser fogging up?",
              "Usually a failed door heater, anti-sweat control or a door that isn't closing fully."),
             ("Do you repair open-air multi-deck cases?", "Yes, both self-contained and remote-condensing open cases.")],
        brands=["true", "hussmann", "hill-phoenix", "beverage-air", "turbo-air", "federal-industries", "structural-concepts"],
    ),
    dict(
        slug="bar-cooler-repair", name="Bar Cooler & Back Bar", cat="refrigeration",
        kw="bar cooler repair",
        intro=("Back-bar coolers, bottle coolers, glass frosters and keg coolers keep a bar running. We repair "
               "every type of bar refrigeration so drinks are cold when the rush starts."),
        why=("Bar coolers sit in tight, warm spaces with little airflow. Condenser cleaning, fan motors, "
             "thermostats and door gaskets are the usual fixes."),
        symptoms=["Beer and bottles not cold enough", "Doors not closing", "Unit running constantly",
                  "Frost inside the cabinet", "Water under the cooler", "Loud fan or compressor"],
        tasks=["Condenser cleaning", "Fan motor and thermostat replacement", "Door gasket and hinge repair",
               "Compressor start repair", "Leak repair and recharge", "Glass froster repair"],
        tip="Let warm cases of beer cool in the walk-in first — loading a bar cooler with warm stock makes it run for hours.",
        faq=[("What temperature should a back-bar cooler be?", "Most bars keep bottle coolers between 34°F and 38°F."),
             ("Do you repair glass frosters?", "Yes, we repair glass and plate frosters as well as bottle and keg coolers.")],
        brands=["true", "beverage-air", "perlick", "turbo-air", "krowne", "glastender", "atosa"],
    ),
    dict(
        slug="draft-beer-system-repair", name="Draft Beer & Keg Cooler", cat="refrigeration",
        kw="draft beer system repair",
        intro=("Foamy pours cost money. We repair kegerators, direct-draw keg coolers and the refrigeration side "
               "of long-draw systems, including glycol power packs that keep beer lines cold."),
        why=("Foam usually means temperature: a keg cooler above 38°F, a glycol chiller that isn't keeping the "
             "trunk line cold, or a failing fan or compressor. We fix the refrigeration and check temperatures "
             "at the tap."),
        symptoms=["Foamy or warm beer", "Glycol chiller running warm or alarming", "Keg cooler above 38°F",
                  "Ice in the glycol bath", "Condensation or ice on lines", "Unit tripping the breaker"],
        tasks=["Keg cooler refrigeration repair", "Glycol power pack repair", "Pump and fan motor replacement",
               "Thermostat and controller replacement", "Leak repair and recharge", "Condenser cleaning"],
        tip="Check the glycol level and bath temperature weekly — a slow drop in glycol is an early warning.",
        faq=[("What temperature should my keg cooler hold?", "Most draft systems are designed for 36–38°F."),
             ("Do you service glycol chillers?", "Yes, we repair glycol power packs and the refrigeration that cools long-draw trunk lines.")],
        brands=["perlick", "true", "beverage-air", "micro-matic", "glastender", "krowne"],
    ),
    dict(
        slug="blast-chiller-repair", name="Blast Chiller", cat="refrigeration",
        kw="blast chiller repair",
        intro=("Blast chillers bring cooked food through the danger zone quickly to meet cooling rules. We repair "
               "reach-in and roll-in blast chillers and shock freezers."),
        why=("Long cycles and failed probe readings usually come from dirty condensers, failed fans, bad food "
             "probes or a controller fault."),
        symptoms=["Cycle takes too long", "Probe errors", "Not reaching target temperature", "Ice on the coil",
                  "Fans not running", "Alarm codes"],
        tasks=["Controller and probe diagnosis", "Fan motor replacement", "Condenser cleaning", "Defrost repair",
               "Leak repair and recharge", "Compressor repair"],
        tip="Don't stack pans tightly — space between pans is what lets a blast chiller hit its cycle times.",
        faq=[("How fast should a blast chiller cool food?",
              "Typically from 160°F to 38°F within 90 minutes, depending on the model and load."),
             ("Can you replace a blast chiller food probe?", "Yes, probes are a common replacement part.")],
        brands=["traulsen", "irinox", "true", "american-panel", "foster"],
    ),
    dict(
        slug="condensing-unit-repair", name="Condensing Unit & Compressor", cat="refrigeration",
        kw="commercial refrigeration compressor repair",
        intro=("The condensing unit is the heart of any walk-in, remote case or ice machine. We repair and replace "
               "condensing units, compressors, refrigeration racks and remote condensers on rooftops, pads and "
               "mechanical rooms."),
        why=("We diagnose electrical and mechanical failures, refrigerant leaks and airflow problems, and we "
             "replace compressors and complete condensing units when repair isn't worth it."),
        symptoms=["Compressor won't start or hums", "Breaker tripping", "Unit short-cycling",
                  "High head pressure on hot days", "Oil stains on lines (possible leak)", "Fans not spinning"],
        tasks=["Compressor diagnosis and replacement", "Contactor, capacitor and relay replacement",
               "Condenser fan motor replacement", "Leak detection and brazing", "Pressure control replacement",
               "Complete condensing unit replacement"],
        tip="Keep leaves, cardboard and grease off rooftop condensers — Carolina summers push them to the limit.",
        faq=[("Is it better to replace the compressor or the whole condensing unit?",
              "It depends on the age of the unit and the refrigerant it uses. We give you both prices so you can decide."),
             ("Do you work with remote refrigeration racks?", "Yes, we service remote condensers, racks and the lines to each case.")],
        brands=["copeland", "heatcraft", "tecumseh", "bitzer", "danfoss", "larkin", "russell"],
    ),
    # ---------------- KITCHEN ----------------
    dict(
        slug="commercial-oven-repair", name="Commercial Oven", cat="kitchen",
        kw="commercial oven repair",
        intro=("We repair gas and electric convection ovens, deck ovens, conveyor pizza ovens, cook-and-hold ovens "
               "and combi ovens. A down oven means a smaller menu, so we carry the common igniters, thermostats, "
               "motors and controls."),
        why=("Ovens that won't heat, heat unevenly or show error codes usually have a failed igniter, gas valve, "
             "thermostat, temperature probe, blower motor or door switch. We test the whole sequence of operation "
             "to find it."),
        symptoms=["Oven won't light or heat", "Uneven baking or hot spots", "Temperature off from the dial",
                  "Convection fan not turning", "Door won't close or seal", "Error codes on the display"],
        tasks=["Igniter, flame sensor and gas valve replacement", "Thermostat and probe calibration/replacement",
               "Convection blower motor replacement", "Door hinge, gasket and switch repair",
               "Control board and display repair", "Conveyor belt and motor repair"],
        tip="Check oven calibration with a separate oven thermometer every month — drift of 25°F is common.",
        faq=[("Why does my convection oven bake unevenly?", "Usually a failing blower motor, a bad element/burner, or a door that no longer seals."),
             ("Do you repair combi ovens?", "Yes, including steam generator, descaling and control faults.")],
        brands=["blodgett", "vulcan", "garland", "southbend", "rational", "lincoln", "middleby-marshall", "alto-shaam", "cleveland", "montague"],
    ),
    dict(
        slug="commercial-range-repair", name="Commercial Range & Cooktop", cat="kitchen",
        kw="commercial range repair",
        intro=("Six-burner, ten-burner and specialty ranges are the backbone of most kitchens. We repair open "
               "burners, French tops, hot tops, wok ranges and the ovens underneath."),
        why=("Burners that won't light, weak flames, bad pilots and oven thermostats are the most common "
             "range repairs. We also adjust air shutters and orifices for a clean blue flame."),
        symptoms=["Burner won't light or keeps going out", "Yellow or uneven flame", "Pilot won't stay lit",
                  "Oven below the range not heating", "Gas smell (call your gas utility first)", "Knobs or valves stuck"],
        tasks=["Pilot, thermocouple and safety valve replacement", "Burner cleaning and orifice adjustment",
               "Gas valve replacement", "Oven thermostat replacement", "Knob and valve repair", "Leveling and leg replacement"],
        tip="Boil-overs clog burner ports — a weekly burner clean keeps flames even.",
        faq=[("Why won't my range pilot stay lit?", "Most often a worn thermocouple or a dirty pilot assembly."),
             ("I smell gas — should I call you?", "Shut off the gas and call your gas utility or 911 first. Once it's safe, we can repair the appliance.")],
        brands=["vulcan", "garland", "southbend", "wolf", "imperial", "jade", "american-range", "montague"],
    ),
    dict(
        slug="fryer-repair", name="Commercial Fryer", cat="kitchen",
        kw="commercial fryer repair",
        intro=("A down fryer can stop a whole menu. We repair gas and electric open fryers, pressure fryers, "
               "filtration systems and computerized fryer controls."),
        why=("Fryers fail from bad pilots, thermopiles, gas valves, high-limit switches, temperature probes and "
             "filter pumps. We fix them fast so oil stays at temperature."),
        symptoms=["Fryer won't light or heat", "Oil overheating or not reaching set point", "Pilot goes out",
                  "High-limit tripping", "Filter pump not running", "Computer showing errors"],
        tasks=["Pilot, thermopile and gas valve replacement", "Temperature probe and thermostat replacement",
               "High-limit switch replacement", "Filter pump and motor repair", "Controller replacement", "Drain valve repair"],
        tip="Filter oil daily and boil out the pot weekly — carbon on the probe throws off temperature.",
        faq=[("Why does my fryer keep shutting off?", "Usually a weak thermopile, a failing gas valve or a high-limit switch tripping."),
             ("Do you repair pressure fryers?", "Yes, including lid, gasket and pressure system repairs.")],
        brands=["frymaster", "pitco", "henny-penny", "dean", "keating", "vulcan", "imperial", "wells"],
    ),
    dict(
        slug="griddle-charbroiler-repair", name="Griddle & Charbroiler", cat="kitchen",
        kw="griddle repair",
        intro=("We repair gas and electric griddles, flat tops, clamshell grills, charbroilers and salamanders "
               "so you get even heat across the whole cooking surface."),
        why=("Cold spots, burners that won't light and thermostats that drift are the usual problems."),
        symptoms=["Cold spots on the griddle", "Burner won't light", "Temperature not matching the dial",
                  "Charbroiler flames uneven", "Pilot going out", "Clamshell platen not heating"],
        tasks=["Burner and pilot repair", "Thermostat replacement and calibration", "Gas valve replacement",
               "Element replacement (electric)", "Radiant and grate replacement", "Clamshell controls repair"],
        tip="Season and scrape the griddle daily; heavy carbon acts as insulation and creates cold spots.",
        faq=[("Why does my griddle have cold spots?", "A clogged burner, failed thermostat or warped plate. Most are repairable."),
             ("Do you repair salamanders and cheese melters?", "Yes.")],
        brands=["vulcan", "garland", "star", "keating", "southbend", "wolf", "imperial", "apw-wyott", "taylor"],
    ),
    dict(
        slug="steamer-kettle-repair", name="Steamer, Kettle & Braising Pan", cat="kitchen",
        kw="commercial steamer repair",
        intro=("Steamers, steam kettles and tilting skillets are workhorses in schools, hospitals and high-volume "
               "kitchens. We repair connectionless and boiler steamers, jacketed kettles and braising pans."),
        why=("Scale, failed water level probes, heating elements, solenoid valves and tilt mechanisms cause most "
             "breakdowns."),
        symptoms=["No steam or slow cooking", "Water leaking", "Low-water alarms", "Kettle not heating",
                  "Tilt mechanism stuck", "Scale build-up"],
        tasks=["Descaling and boiler cleaning", "Water level probe replacement", "Element and burner repair",
               "Solenoid valve replacement", "Tilt gear repair", "Control board replacement"],
        tip="Follow the descaling schedule — hard water scale is the leading cause of steamer failure.",
        faq=[("How often should a steamer be descaled?", "Depends on water hardness; typically monthly to quarterly."),
             ("Do you repair tilt skillets?", "Yes, including tilt gears, elements and controls.")],
        brands=["cleveland", "groen", "vulcan", "market-forge", "accutemp", "southbend"],
    ),
    dict(
        slug="commercial-dishwasher-repair", name="Commercial Dishwasher", cat="kitchen",
        kw="commercial dishwasher repair",
        intro=("When the dish machine goes down, the kitchen runs out of plates. We repair undercounter, door-type, "
               "conveyor and flight-type dishwashers, glass washers and booster heaters."),
        why=("Low rinse temperature, failed booster heaters, pump motors, solenoids, chemical feeders and drain "
             "valves are the most common repairs. We verify final rinse temperature before we leave."),
        symptoms=["Dishes not coming out clean", "Rinse not hot enough (below 180°F on hot-water units)",
                  "Machine not filling or not draining", "Leaking", "Booster heater not heating", "Wash arm not spinning"],
        tasks=["Booster heater element and thermostat repair", "Wash and rinse pump repair",
               "Fill solenoid and drain valve replacement", "Float switch repair", "Door and curtain repair", "Delime and cleaning"],
        tip="Delime on schedule and check final rinse temperature daily — inspectors will.",
        faq=[("Why is my dishwasher rinse not hot enough?", "Usually a failed booster heater element, thermostat or a scale-coated heater."),
             ("Do you repair low-temp chemical machines?", "Yes, both high-temp and low-temp machines.")],
        brands=["hobart", "jackson", "champion", "cma", "insinger", "moyer-diebel", "meiko"],
    ),
    dict(
        slug="food-warmer-repair", name="Food Warmer & Holding Cabinet", cat="kitchen",
        kw="holding cabinet repair",
        intro=("Holding cabinets, heated display cases, steam tables, heat lamps and proofers keep food at a "
               "safe 135°F or above. We repair all of them."),
        why=("Failed elements, thermostats, humidity systems and wiring are the usual causes."),
        symptoms=["Food not staying hot", "Cabinet overheating", "Steam table well not heating", "Humidity not working",
                  "Heat lamp bulbs or elements out", "Breaker tripping"],
        tasks=["Element replacement", "Thermostat and controller repair", "Humidity system repair",
               "Wiring and switch repair", "Door gasket replacement", "Heat lamp repair"],
        tip="Preheat holding cabinets before loading food — loading a cold cabinet drops food below safe temperature.",
        faq=[("What temperature should hot holding be?", "135°F or above for hot-held food."),
             ("Do you repair steam tables?", "Yes, gas and electric steam tables.")],
        brands=["alto-shaam", "hatco", "wells", "apw-wyott", "winston", "metro", "cres-cor"],
    ),
    dict(
        slug="soft-serve-machine-repair", name="Soft Serve & Frozen Drink Machine", cat="kitchen",
        kw="soft serve machine repair",
        intro=("Soft serve, shake, frozen yogurt and frozen beverage machines combine refrigeration and mechanical "
               "parts — exactly what our technicians do. We repair them for ice cream shops, restaurants and "
               "convenience stores."),
        why=("Product too soft or too hard, freeze-ups, drive belts, beater motors and refrigeration faults are "
             "the main problems."),
        symptoms=["Product too soft or runny", "Machine freezing up", "Beater not turning", "Leaking from the door",
                  "Error codes", "Machine running warm"],
        tasks=["Refrigeration diagnosis and repair", "Drive belt and beater motor replacement", "Viscosity control calibration",
               "O-ring and gasket kits", "Control board repair", "Condenser cleaning"],
        tip="Replace O-rings and seals on schedule — a few dollars of rubber protects the whole machine.",
        faq=[("Why is my soft serve too runny?", "Low refrigeration capacity, a dirty condenser or viscosity settings out of adjustment."),
             ("Do you repair frozen beverage (slush) machines?", "Yes.")],
        brands=["taylor", "stoelting", "electro-freeze", "spaceman", "bunn"],
    ),
    dict(
        slug="mixer-slicer-repair", name="Mixer, Slicer & Food Prep", cat="kitchen",
        kw="commercial mixer repair",
        intro=("Planetary mixers, slicers, food processors and dough equipment are built to last decades with the "
               "right service. We repair transmissions, motors, switches and safety interlocks."),
        why=("Worn gears, failed motors and switches, and broken safety interlocks are the most common fixes."),
        symptoms=["Mixer won't start", "Grinding noise from the gearbox", "Speeds slipping", "Slicer blade dull or wobbly",
                  "Bowl lift not working", "Safety interlock fault"],
        tasks=["Transmission and gear repair", "Motor replacement", "Switch and interlock repair",
               "Slicer blade sharpening and bearing repair", "Bowl lift repair", "Electrical repair"],
        tip="Never change mixer speeds while the motor is running — it strips gears.",
        faq=[("Is an older Hobart mixer worth repairing?", "Almost always — older Hobart mixers are rebuildable and worth repairing."),
             ("Do you sharpen slicer blades?", "Yes, as part of slicer service.")],
        brands=["hobart", "globe", "berkel", "robot-coupe", "vollrath"],
    ),
    dict(
        slug="coffee-equipment-repair", name="Coffee & Beverage Equipment", cat="kitchen",
        kw="commercial coffee machine repair",
        intro=("We repair commercial coffee brewers, hot water dispensers, iced tea brewers and beverage "
               "dispensers for cafés, restaurants, offices and convenience stores."),
        why=("Scale, failed heating elements, thermostats, solenoid valves and timers are the common causes."),
        symptoms=["Coffee not hot", "Brewer not filling", "Water overflowing", "Slow brew", "Leaking", "Error lights"],
        tasks=["Descaling", "Element and thermostat replacement", "Inlet solenoid replacement", "Timer and board repair",
               "Sprayhead and valve repair", "Leak repair"],
        tip="Install and change a water filter — it is the cheapest way to protect a brewer.",
        faq=[("Do you repair espresso machines?", "We repair commercial brewers and dispensers; ask us about your espresso model when you call."),
             ("Why is my coffee brewer not hot?", "Usually a failed element, thermostat or heavy scale.")],
        brands=["bunn", "fetco", "curtis", "grindmaster", "cornelius"],
    ),
]

EQ_BY_SLUG = {e["slug"]: e for e in EQUIPMENT}
REFRIG = [e for e in EQUIPMENT if e["cat"] == "refrigeration"]
KITCHEN = [e for e in EQUIPMENT if e["cat"] == "kitchen"]

# Form dropdown options
FORM_EQUIPMENT_OPTIONS = [e["name"] for e in EQUIPMENT] + ["Other / Not sure"]
