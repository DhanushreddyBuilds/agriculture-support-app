# ---------------- ISSUE DETECTION CONFIG ----------------
LEAF_WORDS = ["leaf", "leaves", "yellow", "spot", "curl", "dry", "black", "rot",
              "ಎಲೆ", "ಹಳದಿ", "ಕಲೆ", "ಒಣಗ", "ಕಪ್ಪು", "ಕುಲುಕು"]

PEST_WORDS = ["pest", "insect", "worm", "bug", "borer", "hopper", "attack",
              "ಕೀಟ", "ಹುಳು", "ಹುಳ", "ಹುಳುಹುಳು"]

FUNGUS_WORDS = ["fungus", "blight", "mold", "rot", "disease", "wilt",
                "ಶಿಲೀಂಧ್ರ", "ರೋಗ", "ಸಾಯುತ್ತಿದೆ"]

YIELD_WORDS = ["size", "small", "growth", "height", "production", "yield", "fruit", "flower", "drop",
               "quantity", "low", "less", "decreasing", "bad", "amount",
               "ಗಾತ್ರ", "ಚಿಕ್ಕ", "ಬೆಳವಣಿಗೆ", "ಇಳುವರಿ", "ಹೂವು", "ಹಣ್ಣು", "ಕಡಿಮೆ"]

SOIL_WORDS = ["soil", "root", "fertilizer", "nutrient", "weak", "strength",
              "ಮಣ್ಣು", "ಬೇರು", "ಗೊಬ್ಬರ", "ಪೋಷಕಾಂಶ"]

WATER_WORDS = ["water", "dry", "wet", "rain", "irrigation", "moisture",
               "ದಿನ", "ಒಣ", "ಮಳೆ", "ನೀರಾವರಿ"]

KNOWN_CROPS = [
    "tomato", "potato", "maize", "rice", "wheat", "cotton", "sugarcane", "chilli", "onion", "groundnut",
    "ginger", "turmeric", "banana", "soybean", "gram", "mustard", "peas", "sunflower", "carrot", "garlic",
    "cucumber", "okra", "watermelon", "muskmelon", "pumpkin", "cabbage", "cauliflower", "brinjal",
    "pineapple", "pomegranate", "mango", "papaya", "grape", "guava", "apple", "orange", "lemon", "coconut",
    "ಟೊಮ್ಯಾಟೋ", "ಆಲೂಗಡ್ಡೆ", "ಭತ್ತ", "ಗೋಧಿ", "ಹತ್ತಿ", "ಕಬ್ಬು", "ಮೆಣಸಿನಕಾಯಿ", "ಈರುಳ್ಳಿ", "ಶೇಂಗಾ", "ಶುಂಠಿ", "ಅರಿಶಿನ", "ಬಾಳೆ"
]

# ---------------- SPECIFIC CROP TIPS ----------------
CROP_SPECIFIC_TIPS = {
    "Ginger": "Ginger often suffers from Rhizome Rot. Ensure NO water stagnation. Treat seeds with Mancozeb before planting.",
    "Turmeric": "For Turmeric, high curcumin content needs good organic matter. Use 'Pratibha' variety if possible.",
    "Banana": "Banana needs high Potassium. Support plants with bamboo poles during fruiting to prevent falling.",
    "Rice": "For Rice, maintain 2-3 cm water level. Drain water completely 10 days before harvesting.",
    "Cotton": "Cotton is sensitive to water logging. If leaves turn red, spray Magnesium Sulphate.",
    "Potato": "Earthing up (covering roots with soil) is huge for Potato size. Do not expose tubers to sunlight.",
    "Tomato": "Tomato likes staking. Keep leaves off the ground to prevent blight.",
    "Sugarcane": "Sugarcane needs frequent irrigation. Detrash (remove dry leaves) to avoid pests.",
    "Pineapple": "Pineapple needs acidic soil (pH 4.5-6.0). Use Ethrel for uniform flowering.",
    "Pomegranate": "Bacterial Blight (Oily Spot) is major. Prune infected branches and spray Streptocycline."
}

# ---------------- CROP RECOMMENDATION DATA ----------------
CROP_DATA = {
    "red": {
        "kharif": [
            {"name": "Hybrid Maize", "variety": "Pioneer P3396 / Dekalb 9108", "tips": "High yield potential. Apply NPK 120:60:40."},
            {"name": "Groundnut", "variety": "Kadiri-6 (K-6)", "tips": "Drought tolerant. Treat seeds with Rhizobium."},
            {"name": "Cotton", "variety": "RCH-659 BGII", "tips": "Resistant to bollworm. Initial slow growth."},
            {"name": "Pigeon Pea (Red Gram)", "variety": "ICPL 87119 (Asha)", "tips": "Wilt resistant. Intercrop with Sorghum."},
            {"name": "Ragi (Finger Millet)", "variety": "GPU-28 / Indaf-5", "tips": "Best for red sandy loam. Blast resistant."},
            {"name": "Castor", "variety": "GCH-7", "tips": "Wilt and nematodes resistant high yielder."},
            {"name": "Green Gram (Moong)", "variety": "IPM 02-3", "tips": "Short duration (60-65 days). Mosaic resistant."},
            {"name": "Soybean", "variety": "JS-9560", "tips": "Early maturing. Do not delay harvesting."},
            {"name": "Chilli", "variety": "Byadgi Kaddi", "tips": "High color value. Avoid water logging."},
            {"name": "Tomato", "variety": "Arka Rakshak", "tips": "Triple disease resistant. High staking needed."},
             {"name": "Brinjal", "variety": "Arka Anand", "tips": "Bacterial wilt resistant. Good keeping quality."}
        ],
        "rabi": [
            {"name": "Wheat", "variety": "UAS-304", "tips": "Rust resistant. Requires 4-5 irrigations."},
            {"name": "Mustard", "variety": "Pusa Bold", "tips": "High oil content. Aphid management crucial."},
            {"name": "Chickpea", "variety": "JAKI-9218", "tips": "Wilt resistant. Suitable for mechanical harvesting."},
            {"name": "Onion", "variety": "Arka Kalyan", "tips": "Bulb rot resistant. Good storage quality."},
            {"name": "Potato", "variety": "Kufri Jyoti", "tips": "Late blight tolerant. Earthing up is essential."},
            {"name": "Peas", "variety": "Arkel", "tips": "Early variety. Pods ready in 60 days."},
            {"name": "Coriander", "variety": "CIMAP Haritima", "tips": "Stem gall resistant. Multi-cut variety."},
            {"name": "Sunflower", "variety": "DRSH-1", "tips": "Bird damage protection required at maturity."},
            {"name": "Carrot", "variety": "Pusa Rudhira", "tips": "Rich in lycopene and carotenoids."},
            {"name": "Garlic", "variety": "Yamuna Safed", "tips": "Compact cloves. high pungency."}
        ],
        "summer": [
            {"name": "Groundnut", "variety": "TAG-24", "tips": "Synchronous maturity. Suitable for summer."},
            {"name": "Sesame", "variety": "GT-10 / TKG-22", "tips": "White seeds. Phyllody resistant."},
            {"name": "Okra (Bhindi)", "variety": "Arka Anamika", "tips": "YVMV resistant. Regular picking enhances yield."},
            {"name": "Watermelon", "variety": "Arka Manik", "tips": "Powdery mildew resistant. High sugar content."},
            {"name": "Muskmelon", "variety": "Pusa Madhuras", "tips": "Trailing habit. Needs net support."},
            {"name": "Cowpea", "variety": "C-152", "tips": "Drought tolerant. Vegetable and fodder use."},
            {"name": "Cucumber", "variety": "Pusa Uday", "tips": "Light green fruits. Bitter-free."},
            {"name": "Bitter Gourd", "variety": "Pusa Do Mausami", "tips": "Suitable for both summer and rainy season."},
            {"name": "Cluster Bean", "variety": "Pusa Navbahar", "tips": "Gum content high. Vegetable use."},
            {"name": "Pumpkin", "variety": "Arka Chandan", "tips": "Rich in carotene. Excellent cooking quality."}
        ]
    },
    "black": {
        "kharif": [
            {"name": "Cotton", "variety": "Bunny BGII", "tips": "Suitable for deep black soils. Deep root system."},
            {"name": "Soybean", "variety": "JS-335", "tips": "Most popular variety. Widely adaptable."},
            {"name": "Pigeon Pea", "variety": "BSMR-736", "tips": "Resistant to Sterility Mosaic Disease."},
            {"name": "Hybrid Maize", "variety": "NK-6240", "tips": "Deep orange grains. Heavy yielder."},
            {"name": "Black Gram (Urad)", "variety": "TAU-1", "tips": "Powdery mildew resistant. Bold seeds."},
            {"name": "Green Gram", "variety": "Shining Moong", "tips": "Shiny seeds. Good market price."},
            {"name": "Sunflower", "variety": "KBSH-44", "tips": "Monitor for Heliothis. Hand pollination helps."},
            {"name": "Sugarcane", "variety": "Co-86032", "tips": "High sugar recovery. Drought tolerant."},
            {"name": "Turmeric", "variety": "Pratibha", "tips": "High curcumin. Rhizome rot management needed."},
            {"name": "Chilli", "variety": "Teja (S-17)", "tips": "High pungency. Export quality."}
        ],
        "rabi": [
            {"name": "Chickpea", "variety": "JG-11 / JG-14", "tips": "Heat tolerant. Wilt resistant."},
            {"name": "Sorghum (Jowar)", "variety": "Maldandi (M 35-1)", "tips": "Excellent grain and fodder quality."},
            {"name": "Wheat", "variety": "Lok-1", "tips": "Best for late sowing in black soils."},
            {"name": "Safflower", "variety": "PBNS-12", "tips": "Aphid tolerant. Spiny variety."},
            {"name": "Coriander", "variety": "Hisar Sugandh", "tips": "Aromatic leaves and seeds."},
            {"name": "Linseed", "variety": "NL-97", "tips": "Double purpose (seed and fibre)."},
            {"name": "Onion", "variety": "Bhima Shakti", "tips": "Good bolting tolerance. Late kharif/Rabi."},
            {"name": "Garlic", "variety": "Bhima Purple", "tips": "Purple skin. High keeping quality."},
            {"name": "Fenugreek (Methi)", "variety": "Rmt-1", "tips": "Leafy vegetable and seed purpose."},
            {"name": "Mustard", "variety": "Bio-902", "tips": "Shattering resistant. Bold seeds."}
        ],
        "summer": [
            {"name": "Sunflower", "variety": "DRSH-1", "tips": "Maintain moisture at seed filling."},
            {"name": "Groundnut", "variety": "TG-37A", "tips": "Semi-spreading. High oil content."},
            {"name": "Watermelon", "variety": "Sugar Baby", "tips": "Dark skin, red flesh. Very popular."},
            {"name": "Muskmelon", "variety": "Kajara", "tips": "Local favorite. Netting on fruit."},
            {"name": "Okra", "variety": "Parbhani Kranti", "tips": "YVMV resistant major breakthrough."},
            {"name": "Cluster Bean", "variety": "HG-365", "tips": "Unbranched type. Industrial gum use."},
            {"name": "Cucumber", "variety": "Japanese Long Green", "tips": "Crisp flesh. High yielder."},
            {"name": "Bottle Gourd", "variety": "Arka Bahar", "tips": "Medium long straight fruits."},
            {"name": "Sesame", "variety": "RT-351", "tips": "White seeds. Export quality."},
            {"name": "Fodder Maize", "variety": "African Tall", "tips": "Green fodder for dairy animals."}
        ]
    },
    "clay": {
        "kharif": [
            {"name": "Rice (Paddy)", "variety": "MTU-1010", "tips": "Short duration. Blast resistant."},
            {"name": "Rice (Paddy)", "variety": "BPT-5204 (Sona Masoori)", "tips": "Premium quality. Susceptible to hopper."},
            {"name": "Sugarcane", "variety": "CoM-0265", "tips": "High tonnage. Salinity tolerant."},
            {"name": "Jute", "variety": "JRO-524", "tips": "Fibre crop. Water logging tolerant."},
            {"name": "Colocasia (Arbi)", "variety": "Muktakeshi", "tips": "Blight resistant. Good corm size."},
            {"name": "Banana", "variety": "Grand Naine", "tips": "Tissue culture preferred. High spacing."},
            {"name": "Turmeric", "variety": "Salem", "tips": "Long duration. Deep yellow color."},
            {"name": "Ginger", "variety": "Rio de Janeiro", "tips": "High oleoresin. Soft rot management vital."},
            {"name": "Sweet Potato", "variety": "Sree Arun", "tips": "Red skin. High carotene."},
            {"name": "Betelvine", "variety": "Mysore", "tips": "Requires shade and humidity."}
        ],
        "rabi": [
            {"name": "Wheat", "variety": "HD-2967", "tips": "High biomass. Stripe rust resistant."},
            {"name": "Lentil", "variety": "DPL-62", "tips": "Small seeded. Wilt tolerant."},
            {"name": "Field Pea", "variety": "HFP-4", "tips": "Leaf miner resistant."},
            {"name": "Mustard", "variety": "Varuna", "tips": "Adaptable to various conditions."},
            {"name": "Potato", "variety": "Kufri Bahar", "tips": "Skin peeling issue if harvested early."},
            {"name": "Berseem", "variety": "Mescavi", "tips": "King of fodder crops. Multi-cut."},
            {"name": "Oats", "variety": "Kent", "tips": "Good for fodder and grain."},
            {"name": "Cabbage", "variety": "Golden Acre", "tips": "Round heads. Early variety."},
            {"name": "Cauliflower", "variety": "Pusa Snowball", "tips": "Curds stay white. Late variety."},
            {"name": "Knol Khol", "variety": "White Vienna", "tips": "Harvest before fibers develop."}
        ],
        "summer": [
            {"name": "Rice", "variety": "IR-64", "tips": "Stem borer management needed."},
            {"name": "Okra", "variety": "VRO-6", "tips": "YVMV resistant."},
            {"name": "Ridge Gourd", "variety": "Arka Sumeet", "tips": "Lush green fruits."},
            {"name": "Snake Gourd", "variety": "CO-2", "tips": "Long greenish white fruits."},
            {"name": "Amaranthus", "variety": "Arka Suguna", "tips": "Multi-cut leafy vegetable."},
            {"name": "Sweet Corn", "variety": "Sugar-75", "tips": "Harvest at milky stage."},
            {"name": "Baby Corn", "variety": "HM-4", "tips": "Cob removal at 2-3 days of silk."},
            {"name": "Yard Long Bean", "variety": "Arka Mangala", "tips": "Pole type. Needs staking."},
            {"name": "Ash Gourd", "variety": "Kashi Dhawal", "tips": "Long storage life."},
            {"name": "Pumpkin", "variety": "Arka Suryamukhi", "tips": "Fruit fly management essential."}
        ]
    },
    "sandy": {
        "kharif": [
            {"name": "Pearl Millet (Bajra)", "variety": "Pusa-322", "tips": "Downy mildew resistant. Drought hardy."},
            {"name": "Cluster Bean (Guar)", "variety": "RGC-936", "tips": "Gum content high. Export demand."},
            {"name": "Moth Bean", "variety": "RMO-40", "tips": "Most drought tolerant pulse."},
            {"name": "Cowpea", "variety": "RC-101", "tips": "Fodder and grain purpose."},
            {"name": "Castor", "variety": "GCH-4", "tips": "Deep root system. Drought escape."},
            {"name": "Sesame", "variety": "RT-46", "tips": "White bold seeds."},
            {"name": "Green Gram", "variety": "RMG-62", "tips": "Suitable for arid zones."},
            {"name": "Watermelon", "variety": "Arka Muthu", "tips": "Good for riverbed cultivation."},
            {"name": "Muskmelon", "variety": "Durgapura Madhu", "tips": "High sweetness. Early."},
            {"name": "Date Palm", "variety": "Barhee", "tips": "Tissue culture plants. Saline tolerance."}
        ],
        "rabi": [
            {"name": "Barley", "variety": "RD-2503", "tips": "Malt purpose. Salinity tolerant."},
            {"name": "Mustard (Taramira)", "variety": "T-27", "tips": "Can grow on stored moisture."},
            {"name": "Chickpea", "variety": "RSG-888", "tips": "Best for rainfed sandy areas."},
            {"name": "Cumin (Jeera)", "variety": "GC-4", "tips": "Wilt resistant. Blight sensitive."},
            {"name": "Isabgol", "variety": "GI-2", "tips": "Medicinal crop. Avoid rains at maturity."},
            {"name": "Fennel (Saunf)", "variety": "RF-101", "tips": "Long duration. High value."},
            {"name": "Fenugreek", "variety": "RMt-305", "tips": "Powdery mildew resistant."},
            {"name": "Onion", "variety": "Pusa White Flat", "tips": "Dehydration purpose."},
            {"name": "Carrot", "variety": "Pusa Kesar", "tips": "Red color. Heat tolerant."},
            {"name": "Radish", "variety": "Pusa Chetki", "tips": "Suitable for higher temperatures."}
        ],
        "summer": [
            {"name": "Muskmelon", "variety": "Hara Madhu", "tips": "Late maturing. Very sweet."},
            {"name": "Watermelon", "variety": "Sugar Baby", "tips": "Requires frequent light irrigation."},
            {"name": "Long Melon (Kakri)", "variety": "Punjab Long", "tips": "Cooling effect. Salad use."},
            {"name": "Snap Melon", "variety": "Local", "tips": "Drought hardy. Chutney use."},
            {"name": "Cluster Bean", "variety": "Pusa Sadabahar", "tips": "Vegetable purpose."},
            {"name": "Pumpkin", "variety": "Pusa Vishesh", "tips": "Bushy type. Early."},
            {"name": "Bottle Gourd", "variety": "Pusa Summer Prolific", "tips": "High yielding."},
            {"name": "Round Melon (Tinda)", "variety": "Arka Tinda", "tips": "Tender fruits. Vegetable."},
            {"name": "Summer Bajra", "variety": "GHB-558", "tips": "Fodder purpose mainly."},
            {"name": "Mung Bean", "variety": "SML-668", "tips": "Extra large seeds. 60 days."}
        ]
    }
}

# ---------------- EXPERT KNOWLEDGE BASE ----------------
# Structure: Crop -> Category (Pest, Disease, Nutrient, General) -> Advice
KNOWLEDGE_BASE = {
    "Tomato": {
        "pest": {
            "default": "Common tomato pests include Fruit Borer and Whitefly. Use Neem Oil (5ml/l) or install yellow sticky traps.",
            "borer": "Fruit Borer larvae bore into fruits. **Remedy:** Spray Indoxacarb 1ml/liter. Remove damaged fruits.",
            "whitefly": "Whiteflies spread leaf curl virus. **Remedy:** Install yellow sticky traps. Spray Imidacloprid (0.5ml/l)."
        },
        "disease": {
            "default": "Tomatoes often get Blight or Leaf Curl. Ensure drainage and spacing.",
            "blight": "Early Blight causes concentric rings on leaves. **Control:** Spray Mancozeb (2g/l) or Copper Oxychloride.",
            "curl": "Leaf Curl is viral, spread by whitefly. **Critical:** Pull out infected plants immediately to save the rest.",
            "wilt": "Bacterial Wilt causes sudden drooping. **Bio-Fix:** Drench soil with Pseudomonas fluorescens (10g/l)."
        },
        "nutrient": {
             "yellow": "Yellowing lower leaves often means Nitrogen deficiency. **Fix:** Apply Urea or compost.",
             "rot": "Blossom End Rot (black patch on fruit bottom) is Calcium deficiency. **Fix:** Spray Calcium Nitrate (3g/l)."
        },
        "general": "Tomatoes need staking (support). Water regularly but avoid wetting leaves to prevent fungus."
    },
    "Potato": {
        "disease": {
            "blight": "Late Blight is dangerous in cool, wet weather. **Prevention:** Spray Metalaxyl + Mancozeb (2.5g/l).",
            "scab": "Common Scab makes rough skin. **Prevention:** Avoid fresh manure; keep soil slightly acidic."
        },
        "general": "Earthing up (covering base with soil) is crucial. Don't expose tubers to sunlight (they turn green/toxic)."
    },
    "Rice": {
        "pest": {
            "stem borer": "Stem Borer causes 'Dead Heart'. **Control:** Cartap Hydrochloride granules in soil.",
            "hopper": "Brown Plant Hopper (BPH) causes 'Hopper Burn'. **Control:** Drain water for 3-4 days. Spray Buprofezin."
        },
        "disease": {
            "blast": "Blast disease causes spindle spots. **Control:** Spray Tricyclazole (0.6g/l).",
            "sheath": "Sheath Blight attacks the stem base. **Control:** Validamycin (2ml/l)."
        },
        "nutrient": {
            "yellow": "Yellowing can be Nitrogen deficiency. Apply Urea split doses. If tips are orange, it's Potassium deficiency."
        }
    },
    "Cotton": {
        "pest": {
            "bollworm": "Pink Bollworm is a major threat. **IPM:** Use Pheromone traps. Spray Profenophos if severe.",
            "sucking": "Aphids/Thrips cause curling. **Remedy:** Neem Oil or Acetamiprid."
        },
        "general": "Avoid water logging. Cotton needs bright sunshine."
    },
    "Sugarcane": {
        "pest": {
            "borer": "Shoot Borer attacks young cane. **Remedy:** Earthing up in 45 days. Release Trichogramma (egg parasite)."
        },
        "disease": {
            "rot": "Red Rot causes internal redness and sour smell. **Critical:** Use resistant varieties like Co-86032. Treat setts with Carbendazim."
        },
        "general": "Needs frequent irrigation. Propping (tying canes together) prevents lodging."
    },
    "Chilli": {
        "disease": {
            "dieback": "Dieback causes branches to dry from tip. **Control:** Copper Oxychloride spray.",
            "curl": "Leaf Curl is very common. Manage thrips and mites using Fipronil or Diafenthiuron."
        }
    },
    "General": {
        "compost": "**Vermicompost Recipe:** \n1. Collect cow dung and dry leaves.\n2. Layer them in a pit.\n3. Add Earthworms.\n4. Keep moist. Ready in 45-60 days.",
        "soil": "Healthy soil needs organic matter. Add Cow Dung Manure (FYM) once a year. Test soil pH every 2 years.",
        "water": "Drip Irrigation saves 40-60% water and reduces weeds. Best for vegetable crops.",
        "organic": "**Panchagavya:** Mix Cow lung, urine, milk, curd, ghee. Ferment for 21 days. Excellent growth promoter."
    }
}
