# Kashmir Geographic and Cultural Data

INDIA_STATES = {
    "Jammu & Kashmir": {
        "Srinagar": (34.0837, 74.7973),
        "Jammu": (32.7266, 74.8570),
        "Anantnag": (33.7311, 75.1487),
        "Baramulla": (34.2099, 74.3450),
        "Pulwama": (33.8799, 74.8942),
        "Kupwara": (34.5213, 74.2613),
        "Budgam": (33.9374, 74.7184),
        "Ganderbal": (34.2285, 74.7776),
        "Shopian": (33.7163, 74.8368),
        "Kulgam": (33.6443, 75.0177),
        "Bandipora": (34.4190, 74.6394),
        "Kathua": (32.3847, 75.5170),
        "Udhampur": (32.9160, 75.1419),
        "Rajouri": (33.3780, 74.3110),
        "Poonch": (33.7730, 74.0930),
        "Doda": (33.1490, 75.5470),
        "Kishtwar": (33.3130, 75.7660),
        "Ramban": (33.2400, 75.2380),
        "Reasi": (33.0820, 74.8310),
        "Samba": (32.5580, 75.1190),
        "Leh": (34.1526, 77.5771),
        "Kargil": (34.5593, 76.1346),
    },
    "Delhi": {
        "New Delhi": (28.6139, 77.2090),
        "North Delhi": (28.7041, 77.1025),
        "South Delhi": (28.5355, 77.3910),
        "East Delhi": (28.6671, 77.2935),
        "West Delhi": (28.6520, 77.0534),
    },
    "Maharashtra": {
        "Mumbai": (19.0760, 72.8777),
        "Pune": (18.5204, 73.8567),
        "Nagpur": (21.1458, 79.0882),
        "Nashik": (20.0059, 73.7757),
        "Aurangabad": (19.8762, 75.3433),
    },
    "Himachal Pradesh": {
        "Shimla": (31.1048, 77.1734),
        "Dharamsala": (32.2190, 76.3234),
        "Manali": (32.2396, 77.1887),
        "Kullu": (31.9574, 77.1096),
        "Mandi": (31.7080, 76.9320),
    },
    "Punjab": {
        "Amritsar": (31.6340, 74.8723),
        "Ludhiana": (30.9010, 75.8573),
        "Jalandhar": (31.3260, 75.5762),
        "Patiala": (30.3398, 76.3869),
        "Chandigarh": (30.7333, 76.7794),
    },
    "Uttar Pradesh": {
        "Lucknow": (26.8467, 80.9462),
        "Varanasi": (25.3176, 82.9739),
        "Agra": (27.1767, 78.0081),
        "Allahabad": (25.4358, 81.8463),
        "Kanpur": (26.4499, 80.3319),
        "Mathura": (27.4924, 77.6737),
        "Ayodhya": (26.7922, 82.1998),
    },
    "Gujarat": {
        "Ahmedabad": (23.0225, 72.5714),
        "Surat": (21.1702, 72.8311),
        "Vadodara": (22.3072, 73.1812),
        "Rajkot": (22.3039, 70.8022),
    },
    "Rajasthan": {
        "Jaipur": (26.9124, 75.7873),
        "Jodhpur": (26.2389, 73.0243),
        "Udaipur": (24.5854, 73.7125),
        "Bikaner": (28.0229, 73.3119),
    },
    "Karnataka": {
        "Bengaluru": (12.9716, 77.5946),
        "Mysuru": (12.2958, 76.6394),
        "Mangaluru": (12.9141, 74.8560),
        "Hubli": (15.3647, 75.1240),
    },
    "Tamil Nadu": {
        "Chennai": (13.0827, 80.2707),
        "Coimbatore": (11.0168, 76.9558),
        "Madurai": (9.9252, 78.1198),
        "Salem": (11.6643, 78.1460),
    },
    "West Bengal": {
        "Kolkata": (22.5726, 88.3639),
        "Darjeeling": (27.0410, 88.2663),
        "Siliguri": (26.7271, 88.3953),
        "Durgapur": (23.5204, 87.3119),
    },
    "Madhya Pradesh": {
        "Bhopal": (23.2599, 77.4126),
        "Indore": (22.7196, 75.8577),
        "Gwalior": (26.2183, 78.1828),
        "Ujjain": (23.1793, 75.7849),
    },
}

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishtha", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

RASHIS = [
    "Mesha (Aries)", "Vrishabha (Taurus)", "Mithuna (Gemini)",
    "Karka (Cancer)", "Simha (Leo)", "Kanya (Virgo)",
    "Tula (Libra)", "Vrishchika (Scorpio)", "Dhanu (Sagittarius)",
    "Makara (Capricorn)", "Kumbha (Aquarius)", "Meena (Pisces)"
]

# ---------------------------------------------------------------------------
# KASHMIR VALLEY — District → Town/Mohalla → Villages/Mauzas
# ---------------------------------------------------------------------------

KP_DISTRICTS = [
    "Srinagar", "Baramulla", "Anantnag", "Pulwama", "Budgam",
    "Kupwara", "Ganderbal", "Shopian", "Kulgam", "Bandipora",
]

KP_TOWNS = {
    # ── SRINAGAR ──────────────────────────────────────────────────────────────
    "Srinagar": [
        # Old City — historic KP mohallas
        "Habba Kadal", "Rainawari", "Zaina Kadal", "Fateh Kadal",
        "Safa Kadal", "Bohri Kadal", "Aali Kadal", "Nawab Bazar",
        "Shehr-e-Khas", "Khanyar", "Nowhatta", "Maisuma",
        "Barbarshah", "Karan Nagar", "Gogji Pathri",
        # New City / Extensions
        "Bemina", "Hyderpora", "Natipora", "Jawahar Nagar",
        "Indira Nagar", "Rajbagh", "Lal Chowk", "Soura",
        "Nishat", "Harwan", "Shalimar", "Brein",
        # Outskirts / Rural
        "Pampore", "Lasjan", "Narbal", "Pantha Chowk",
        "Nowgam", "Humhama", "Rangreth", "Buchpora",
    ],
    # ── BARAMULLA ─────────────────────────────────────────────────────────────
    "Baramulla": [
        "Baramulla Town", "Sopore", "Pattan", "Uri",
        "Tangmarg", "Gulmarg", "Rafiabad", "Kreeri",
        "Kunzer", "Boniyar", "Drugmulla", "Kawanpora",
        "Watergam", "Rohama", "Dangiwacha", "Wagoora",
        "Singhpora", "Chandil Pora", "Nadihal", "Hathlangoo",
    ],
    # ── ANANTNAG ──────────────────────────────────────────────────────────────
    "Anantnag": [
        "Anantnag Town", "Bijbehara", "Kokernag", "Pahalgam",
        "Dooru", "Shangus", "Vailoo", "Srigufwara",
        "Mattan", "Achabal", "Verinag", "Breng Valley",
        "Qazigund", "Banihal", "Dachnipora", "Larnoo",
        "Sagam", "Wanpoh", "Arwani", "Daksum",
        "Khanbal", "Wuyan", "Kulgam Road", "Zainagir",
    ],
    # ── PULWAMA ───────────────────────────────────────────────────────────────
    "Pulwama": [
        "Pulwama Town", "Pampore", "Tral", "Awantipora",
        "Khrew", "Kakapora", "Rajpora", "Newa",
        "Arihal", "Shadimarg", "Lassipora", "Drabgam",
        "Samboora", "Namblabal", "Mir Mohalla", "Nowpora",
    ],
    # ── BUDGAM ────────────────────────────────────────────────────────────────
    "Budgam": [
        "Budgam Town", "Magam", "Beerwah", "Narbal",
        "Chadoora", "Khansahib", "Charar-i-Sharief",
        "Rakh-i-Arth", "Soibugh", "Pakharpora",
        "Manzam", "Nagam", "Ichgam", "Wathoora",
        "Khag", "Yousmarg", "Dobiwan", "Warpora",
    ],
    # ── KUPWARA ───────────────────────────────────────────────────────────────
    "Kupwara": [
        "Kupwara Town", "Handwara", "Karnah", "Lolab",
        "Sogam", "Kralpora", "Drugmulla", "Trehgam",
        "Langate", "Vilgam", "Keran", "Teetwal",
        "Shardi", "Machil", "Tikker", "Ramhal",
    ],
    # ── GANDERBAL ─────────────────────────────────────────────────────────────
    "Ganderbal": [
        "Ganderbal Town", "Kangan", "Lar", "Wakura",
        "Manigam", "Tullamulla", "Shuhama",
        "Gund", "Sonamarg", "Wangath", "Naranag",
        "Safapora", "Nunar", "Gund Brath",
    ],
    # ── SHOPIAN ───────────────────────────────────────────────────────────────
    "Shopian": [
        "Shopian Town", "Keegam", "Hermain", "Zainpora",
        "Hirpora", "Barbugh", "Chitragam",
        "Pinjoora", "Keller", "Wachi", "Imam Sahib",
    ],
    # ── KULGAM ────────────────────────────────────────────────────────────────
    "Kulgam": [
        "Kulgam Town", "D.H. Pora", "Devsar", "Frisal",
        "Pahloo", "Yaripora", "Noorabad",
        "Quimoh", "Manzgam", "Redwani", "Qazigund",
    ],
    # ── BANDIPORA ─────────────────────────────────────────────────────────────
    "Bandipora": [
        "Bandipora Town", "Hajin", "Sumbal", "Gurez",
        "Ajas", "Tulail", "Sonawari",
        "Palhalan", "Kaloosa", "Asham", "Chandusa",
        "Arin", "Bandh Pether",
    ],
}

KP_VILLAGES = {
    # ── SRINAGAR — Old City ───────────────────────────────────────────────────
    "Habba Kadal":    ["Habba Kadal (mohalla)", "Kawdara", "Safakadal", "Maharajgunj", "Kral Bazar"],
    "Rainawari":      ["Rainawari", "Dalgate", "Nallabagh", "Sheikh Mohalla", "Nagin"],
    "Zaina Kadal":    ["Zaina Kadal", "Saraf Kadal", "Kathi Darwaza", "Kralpather", "Fateh Kadal North"],
    "Fateh Kadal":    ["Fateh Kadal", "Baba Demb", "Maharaj Gunj", "Naidyar", "Rozabal"],
    "Safa Kadal":     ["Safa Kadal", "Zukura", "Drujan", "Idgah", "Nowpora"],
    "Bohri Kadal":    ["Bohri Kadal", "Chattabal", "Azad Gunj", "Badami Bagh", "Khrew Alichi"],
    "Aali Kadal":     ["Aali Kadal", "Sekidafar", "Guru Bazar", "Khankahi Mohalla", "Makhama"],
    "Nawab Bazar":    ["Nawab Bazar", "Kathi Darwaza", "Sopore Gate", "Noorbagh", "Fateh Kadal South"],
    "Shehr-e-Khas":   ["Shehr-e-Khas", "Lal Chowk Area", "Residency Road", "Polo View", "Maulana Azad Road"],
    "Khanyar":        ["Khanyar", "Bagh-e-Dilawar Khan", "Syed Ali Akbar Mohalla", "Abi Guzar"],
    "Nowhatta":       ["Nowhatta", "Budshah Chowk", "Noor Bagh", "Gaw Kadal", "Barbarshah"],
    "Karan Nagar":    ["Karan Nagar", "Gogji Pathri", "Wazir Bagh", "Buchpora", "Hyderpora North"],
    "Gogji Pathri":   ["Gogji Pathri", "Natipora", "Hyderpora", "Bemina", "Lawaypora"],
    "Soura":          ["Soura", "Baghi Mehtab", "Pantha Chowk", "Nowgam", "Barzulla"],
    "Nishat":         ["Nishat", "Cheshmashahi", "Harwan", "Shalimar", "Naseem Bagh"],
    "Brein":          ["Brein", "Dara", "Manasbal Road", "Hazratbal"],
    # ── SRINAGAR — Outskirts ─────────────────────────────────────────────────
    "Pampore":        ["Pampore", "Lethpora", "Narkara", "Mir Bahri"],
    "Lasjan":         ["Lasjan", "Rangreth", "Humhama", "Ichgam North"],
    "Narbal":         ["Narbal", "Kanihama", "Sempora", "Khrew (Budgam side)"],
    "Nowgam":         ["Nowgam", "Barzulla", "Tengpora", "Batamaloo"],
    "Buchpora":       ["Buchpora", "Rambagh", "Nawa Bazar", "Abi Guzar"],
    # ── BARAMULLA ────────────────────────────────────────────────────────────
    "Baramulla Town": ["Baramulla Town", "Khawajabagh", "Watergam", "Sopore Road", "Azad Gunj Baramulla"],
    "Sopore":         ["Sopore", "Dangiwacha", "Kralagund", "Arampora", "Sherabad"],
    "Pattan":         ["Pattan", "Watlab", "Singhpora", "Nadihal", "Chandil Pora"],
    "Tangmarg":       ["Tangmarg", "Drang", "Kunzer", "Wagoora", "Bagh-e-Sumbul"],
    "Gulmarg":        ["Gulmarg", "Affarwat", "Khilanmarg", "Kongdoori", "Ferozpur Nallah"],
    "Uri":            ["Uri", "Boniyar", "Salamabad", "Churanda", "Hathlangoo"],
    "Kreeri":         ["Kreeri", "Rohama", "Hathlangoo", "Wussan"],
    "Kawanpora":      ["Kawanpora", "Dangerpora", "Palhallan", "Magraypora"],
    # ── ANANTNAG ─────────────────────────────────────────────────────────────
    "Anantnag Town":  ["Anantnag Town", "Khanbal", "Shahabad", "Lal Chowk Anantnag", "Safa Kadal Anantnag"],
    "Bijbehara":      ["Bijbehara", "Wanpoh", "Arwani", "Naina", "Dialgam"],
    "Kokernag":       ["Kokernag", "Daksum", "Verinag", "Brariangan", "Pahalgam Road"],
    "Pahalgam":       ["Pahalgam", "Aru", "Betaab Valley", "Chandanwari", "Baisaran"],
    "Mattan":         ["Mattan", "Martand", "Sagam", "Wanpora", "Bunagam"],
    "Achabal":        ["Achabal", "Watchiloo", "Semthan", "Yaripora (Anantnag)", "Kragsoo"],
    "Dooru":          ["Dooru", "Kokernag Road", "Naina", "Srigufwara"],
    "Shangus":        ["Shangus", "Dachnipora", "Larnoo", "Pahalgam Bypass"],
    "Breng Valley":   ["Breng Valley", "Wandhama", "Nowpora Anantnag", "Zainagir"],
    "Qazigund":       ["Qazigund", "Banihal", "Jawahar Tunnel", "Sangaldan"],
    "Verinag":        ["Verinag", "Kokernag South", "Khul", "Wuyan"],
    # ── PULWAMA ──────────────────────────────────────────────────────────────
    "Pulwama Town":   ["Pulwama Town", "Tral Road", "Rajpora", "Shadimarg", "Awantipora Road"],
    "Awantipora":     ["Awantipora", "Kakapora", "Lassipora", "Mir Bahri", "Pampore South"],
    "Khrew":          ["Khrew", "Drabgam", "Newa", "Arihal", "Sethpora"],
    "Kakapora":       ["Kakapora", "Mir Mohalla", "Namblabal", "Samboora", "Litter"],
    "Tral":           ["Tral", "Noorpora", "Khanpur Tral", "Rajpora Tral"],
    "Shadimarg":      ["Shadimarg", "Tahab", "Sirnoo", "Prichoo"],
    # ── BUDGAM ───────────────────────────────────────────────────────────────
    "Budgam Town":    ["Budgam Town", "Chadoora", "Nagam", "Ichgam", "Soiteng"],
    "Magam":          ["Magam", "Warpora", "Rakh-i-Arth", "Wathoora South"],
    "Beerwah":        ["Beerwah", "Sultanpora", "Khag", "Wathoora", "Panzgam"],
    "Charar-i-Sharief": ["Charar-i-Sharief", "Dobiwan", "Durganag", "Yousmarg", "Charsoo"],
    "Manzam":         ["Manzam", "Soibugh", "Pakharpora", "Narkara Budgam"],
    "Narbal":         ["Narbal", "Kanihama", "Sempora", "Palhalan Budgam"],
    "Chadoora":       ["Chadoora", "Ompora", "Batpora", "Bellow"],
    "Khansahib":      ["Khansahib", "Rathsun", "Wuder", "Nilora"],
    # ── KUPWARA ──────────────────────────────────────────────────────────────
    "Kupwara Town":   ["Kupwara Town", "Drugmulla", "Vilgam", "Kralpora", "Machil Road"],
    "Handwara":       ["Handwara", "Langate", "Khumriyal", "Sogam", "Tikker"],
    "Karnah":         ["Karnah", "Teetwal", "Shardi", "Keran", "Tangdhar"],
    "Lolab":          ["Lolab", "Sogam", "Kralangam", "Maidanpora"],
    "Trehgam":        ["Trehgam", "Ramhal", "Panzgam Kupwara", "Palwama Kupwara"],
    "Drugmulla":      ["Drugmulla", "Kalmoona", "Zaloora", "Woosa"],
    # ── GANDERBAL ────────────────────────────────────────────────────────────
    "Ganderbal Town": ["Ganderbal Town", "Wakura", "Tullamulla (Tulmul)", "Shuhama", "Nunar"],
    "Kangan":         ["Kangan", "Gund", "Sonamarg", "Lar", "Naranag"],
    "Tullamulla":     ["Tullamulla (Tulmul)", "Wakura", "Manigam", "Shuhama", "Safapora"],
    "Wangath":        ["Wangath", "Naranag", "Kangan Upper", "Gund Brath"],
    "Manigam":        ["Manigam", "Lar", "Nundkol", "Shuhama South"],
    # ── SHOPIAN ──────────────────────────────────────────────────────────────
    "Shopian Town":   ["Shopian Town", "Zainpora", "Keegam", "Hermain", "Keller"],
    "Keegam":         ["Keegam", "Pinjoora", "Chitragam", "Barbugh", "Wachi"],
    "Zainpora":       ["Zainpora", "Imam Sahib", "Keller South", "Hirpora"],
    "Hermain":        ["Hermain", "Barbugh", "Rangpora", "Bonpora"],
    # ── KULGAM ───────────────────────────────────────────────────────────────
    "Kulgam Town":    ["Kulgam Town", "Devsar", "D.H. Pora", "Noorabad", "Manzgam"],
    "D.H. Pora":      ["D.H. Pora", "Yaripora", "Frisal", "Pahloo", "Redwani"],
    "Devsar":         ["Devsar", "Frisal", "Quimoh", "Wanpora Kulgam"],
    "Noorabad":       ["Noorabad", "Manzgam", "Chowgam", "Vailoo Kulgam"],
    "Yaripora":       ["Yaripora", "Pahloo", "Wandhama Kulgam", "Qaimoh"],
    # ── BANDIPORA ────────────────────────────────────────────────────────────
    "Bandipora Town": ["Bandipora Town", "Hajin", "Sumbal", "Sonawari", "Chandusa"],
    "Hajin":          ["Hajin", "Ajas", "Palhalan", "Kaloosa", "Arin"],
    "Sumbal":         ["Sumbal", "Asham", "Bandh Pether", "Watlab Bandipora"],
    "Gurez":          ["Gurez", "Dawar", "Tulail", "Achabal Gurez"],
    "Sonawari":       ["Sonawari", "Chandusa", "Palhalan South", "Wadipora"],
}

# ---------------------------------------------------------------------------
# KUL DEVI / DEVTA OVERRIDE BY TOWN
# For towns where the kul devi/devta differs from the district default,
# this provides a more precise mapping.
# ---------------------------------------------------------------------------

KUL_DEVI_BY_TOWN = {
    # Srinagar old-city mohallas — all Sharika Devi
    "Habba Kadal": "Sharika Devi (Chakreshwari)",
    "Rainawari":   "Sharika Devi (Chakreshwari)",
    "Zaina Kadal": "Sharika Devi (Chakreshwari)",
    "Fateh Kadal": "Sharika Devi (Chakreshwari)",
    "Safa Kadal":  "Sharika Devi (Chakreshwari)",
    "Bohri Kadal": "Sharika Devi (Chakreshwari)",
    "Aali Kadal":  "Sharika Devi (Chakreshwari)",
    "Nawab Bazar": "Sharika Devi (Chakreshwari)",
    "Shehr-e-Khas":"Sharika Devi (Chakreshwari)",
    "Khanyar":     "Sharika Devi (Chakreshwari)",
    "Nowhatta":    "Sharika Devi (Chakreshwari)",
    "Maisuma":     "Sharika Devi (Chakreshwari)",
    "Barbarshah":  "Sharika Devi (Chakreshwari)",
    "Karan Nagar": "Sharika Devi (Chakreshwari)",
    # Ganderbal — Ragnya Devi (Kheer Bhawani) — temple here
    "Tullamulla":      "Ragnya Devi (Kheer Bhawani) — temple at Tulmul",
    "Ganderbal Town":  "Ragnya Devi (Kheer Bhawani)",
    "Wakura":          "Ragnya Devi (Kheer Bhawani)",
    "Wangath":         "Bhadrakali — Wangath temple (mountain shrine)",
    # Budgam — Manzam has secondary Ragnya Devi spring
    "Manzam":          "Ragnya Devi — Manzam spring (secondary shrine)",
    "Charar-i-Sharief":"Sharika Devi (originally Shaiva site)",
    # Pulwama — Khrew is Jwala Devi seat
    "Khrew":       "Jwala Devi (Jwala Bhagwati) — primary temple at Khrew",
    "Awantipora":  "Jwala Devi / Sharika Devi",
    "Pampore":     "Sharika Devi / Jwala Devi",
    # Anantnag — Mattan is Bhadrakali / Martand area
    "Mattan":      "Bhadrakali — near Martand Sun Temple",
    "Achabal":     "Bhadrakali",
    "Pahalgam":    "Bhadrakali / Ragnya Devi",
    "Kokernag":    "Bhadrakali",
    "Verinag":     "Ragnya Devi — Verinag spring (associated shrine)",
    # Kulgam — Devsar is Tripura Sundari seat
    "Devsar":      "Tripura Sundari (Tripureshwari)",
    "D.H. Pora":   "Tripura Sundari / Bhadrakali",
    "Kulgam Town": "Bhadrakali / Tripura Sundari",
    "Noorabad":    "Tripura Sundari",
    "Yaripora":    "Tripura Sundari",
    # Shopian — Bhadrakali / Jwala Devi
    "Shopian Town": "Bhadrakali",
    "Keegam":       "Bhadrakali / Jwala Devi",
    "Zainpora":     "Bhadrakali",
    # Kupwara — Sharada Devi (proxy shrines at Handwara / Trehgam)
    "Handwara":    "Sharada Devi — proxy shrine at Handwara (original: Sharada Peeth, PoK)",
    "Trehgam":     "Sharada Devi — Trehgam proxy shrine",
    "Karnah":      "Sharada Devi",
    # Bandipora — Ragnya Devi + Nandkeshwar (Sumbal)
    "Sumbal":      "Ragnya Devi (Kheer Bhawani) / Nandkeshwar Bhairava temple",
    "Hajin":       "Ragnya Devi (Kheer Bhawani)",
    "Bandipora Town": "Ragnya Devi (Kheer Bhawani)",
    "Sonawari":    "Ragnya Devi (Kheer Bhawani)",
    "Gurez":       "Sharika Devi / Ragnya Devi",
}

# Comprehensive list of Kashmiri Pandit surnames
KP_SURNAMES = [
    "— Optional —",
    # ── All nick names from the Bhannamasis/Malmasis gotra table (CSV) ───────
    "Aima", "Amhardar", "Artha",
    "Babu", "Badgami", "Bakaya", "Bakhshi", "Bali", "Bamtsunt", "Bamzai",
    "Bandar", "Bangi", "Bangru", "Barbuz", "Bataphalu", "Battiv", "Bazari",
    "Bazaz", "Bhan", "Bhandari", "Bhat", "Bhatt", "Bindri", "Bira",
    "Bradi", "Braru", "Breth", "Buju", "Buni",
    "Chacha", "Chaghat", "Chaka", "Chakan", "Chana", "Chandra", "Chandru",
    "Charangu", "Chhotu", "Chillum", "Choku", "Chothai", "Choudhri", "Chowdhri",
    "Dandar", "Dangar", "Dar", "Dassu", "Deva", "Dewani", "Dhar", "Dhaumyana",
    "Divali", "Dout", "Drabi", "Duda", "Durani", "Duru",
    "Fata", "Fotedar",
    "Gadar", "Gaddu", "Gadwali", "Gagar", "Galikrapa", "Ganju", "Garyali",
    "Ghasi", "Gigu", "Giru", "Gurut",
    "Hak", "Hakachar", "Hakim", "Hangal", "Handu", "Hapa", "Hastiwal", "Hukku",
    "Jala", "Jalali", "Jan", "Jatu", "Jawansher", "Jinsi", "Jogi", "Jota",
    "Kachru", "Kadalabuju", "Kak", "Kala", "Kakapuri", "Kalla", "Kallu",
    "Kalpush", "Kalu", "Kandar", "Kanth", "Kar", "Karawani", "Karihalu",
    "Karnel", "Kasab", "Kasid", "Kashgari", "Kathju", "Kaul", "Kav",
    "Kem", "Kemdal", "Keni", "Khaibri", "Khanakatu", "Khar", "Khari",
    "Khashu", "Khaumush", "Khazanchi", "Khod", "Khoru", "Khosa", "Khoshu",
    "Khurdi", "Kichlu", "Kissu", "Kokru", "Kotar", "Kothdar", "Koul",
    "Kukru", "Kutsru", "Kyani",
    "Labru", "Ladakhi", "Lala", "Lange", "Langer", "Lattu", "Lidi",
    "Machama", "Madan", "Mala", "Malik", "Malla", "Mam", "Mandal",
    "Mantapuri", "Mantu", "Manwotu", "Mattu", "Mazari", "Mekhzin",
    "Meva", "Mich", "Mirakhur", "Miskin", "Misri", "Miyan", "Mogal",
    "Mota", "Moza", "Muj", "Muhtasib", "Muki", "Mukka", "Munga",
    "Munshi", "Mushran", "Muttu",
    "Nagari", "Nakhasi", "Naqib", "Nari",
    "Padar", "Padi", "Padora", "Pahalwan", "Pandita", "Pandit", "Panzu",
    "Parikala", "Parimu", "Partazi", "Pat", "Patar", "Peshen", "Peshin",
    "Piala", "Pir", "Pishen", "Purbi", "Put",
    "Qandahari", "Qazi",
    "Raina", "Rangateng", "Ratiz", "Raval", "Razdan",
    "Sabani", "Safaya", "Sahib", "Said", "Salman", "Sapru", "Sav",
    "Sazawul", "Shah", "Shair", "Shal", "Shali", "Shanglu", "Shargha",
    "Shoga", "Shopuri", "Shora", "Shunglu", "Sibbu", "Sikh", "Singhari",
    "Sopuri-Pandit", "Sultan", "Sulu", "Sum",
    "Taku", "Tangan", "Tarivala", "Tava", "Teng", "Thakur", "Thapal",
    "Thalatsur", "Thela", "Thogan", "Thusu", "Thusoo", "Tickoo", "Tiku",
    "Tikku", "Tilwan", "Tota", "Trakari", "Tritshal", "Tritsha",
    "Tsrungu", "Tsul", "Tshut", "Tulsi", "Tur", "Turi", "Turki",
    "Ugra", "Ukhlu", "Unt", "Uthu",
    "Vangar", "Vankhan", "Vantu", "Variku", "Vashnavi", "Vichari",
    "Waguzari", "Wallu", "Wanchu", "Wanikhan", "Wangani", "Warikoo",
    "Wat", "Watal", "Waza", "Wufa",
    "Yachh", "Yechh",
    "Zadu", "Zahi", "Zalpari", "Zamindar", "Zari", "Zaru",
    "Zithu", "Zitshoo", "Zitu", "Zotan",
    # ── Other common KP surnames ──────────────────────────────────────────────
    "Divan", "Diwan", "Ganjoo", "Gadoo", "Gadu", "Haksar", "Handoo",
    "Jyotishi", "Kaw", "Kilam", "Kilaam", "Malhotra", "Mattoo", "Munsi",
    "Nath", "Nehru", "Ogra", "Purohit", "Raina", "Sapru", "Sharga",
    "Sopori", "Shastri", "Upadhyay", "Vaid", "Vakil", "Wakhloo",
    "Wangnoo", "Wattal", "Wazir", "Zutshi",
]

# ---------------------------------------------------------------------------
# ASHTA BHAIRAVAS OF KASHMIR (Eight directional guardians per Nilamata Purana
# and Trika tradition — each guards a mohalla / zone of the valley)
# ---------------------------------------------------------------------------

ASHTA_BHAIRAVAS = [
    {
        "name": "Vetalraja Bhairava",
        "region": "Rainawari, Dal Lake area",
        "direction": "North",
        "notes": "Guardian of Rainawari and the Dal Lake shore",
    },
    {
        "name": "Anandeshwara Bhairava",
        "region": "Sathu Barbar Shah, Amira Kadal, Ganpatyar, Maisuma",
        "direction": "North-East",
        "notes": "Guardian of central Srinagar mohallas",
    },
    {
        "name": "Tushkaraja (Turushkaraja) Bhairava",
        "region": "Habba Kadal, Doodh Ganga confluence, Habbak-kadal",
        "direction": "East",
        "notes": "Guardian of the Habba Kadal bridge and Doodh Ganga confluence",
    },
    {
        "name": "Bahukhatkeshwara Bhairava",
        "region": "Safa Kadal, Chhattabal",
        "direction": "South-East",
        "notes": "Guardian of Safa Kadal and Chhattabal area",
    },
    {
        "name": "Purnaraja (Pooranraja) Bhairava",
        "region": "Hari Parbat, Ali Kadal, Safa Kadal vicinity",
        "direction": "South",
        "notes": "Guardian of Hari Parbat and surrounding areas",
    },
    {
        "name": "Mangalaraja (Mangaleshwara) Bhairava",
        "region": "Fateh Kadal, Zaina Kadal, Bohri Kadal",
        "direction": "South-West",
        "notes": "Guardian of the old city kadal (bridge) belt",
    },
    {
        "name": "Jayaksena Bhairava",
        "region": "Zaina Kadal (left bank)",
        "direction": "West",
        "notes": "Guardian of the left bank of Zaina Kadal area",
    },
    {
        "name": "Vishvaksena Bhairava",
        "region": "Beyond Zaina Kadal, outer Srinagar",
        "direction": "North-West",
        "notes": "Guardian of areas beyond Zaina Kadal towards the valley",
    },
]

# ---------------------------------------------------------------------------
# OTHER LOCAL / AREA-SPECIFIC BHAIRAVAS
# ---------------------------------------------------------------------------

LOCAL_BHAIRAVAS = [
    {
        "name": "Nandikeshwara Bhairava",
        "region": "Sumbal, Bandipora",
        "notes": "Also known as Nandkishor / Nandkeshwar Bhairava; temple at Sumbal",
    },
    {
        "name": "Bhimareja Bhairava",
        "region": "Prayagraj Shadipura, Srinagar",
        "notes": "Associated with Shadipura area",
    },
    {
        "name": "Bhuteshwara Bhairava",
        "region": "Tulmul (Tullamulla), Ganderbal",
        "notes": "Guardian of the Tulmul (Kheer Bhawani) area",
    },
    {
        "name": "Kalabhairava",
        "region": "Universal / all Kashmir",
        "notes": "Chief of the 64 Bhairavas; widely worshipped across the valley",
    },
    {
        "name": "Batuka Bhairava",
        "region": "Universal / Herath ritual",
        "notes": "Child form of Bhairava; central to Herath (Kashmiri Shivratri) Vatuk Puja",
    },
    {
        "name": "Swarna Akarshana Bhairava",
        "region": "Srinagar / wider valley",
        "notes": "Wealth-conferring form; worshipped in Srinagar households",
    },
    {
        "name": "Samhara Bhairava",
        "region": "Wider valley",
        "notes": "Dissolution aspect; part of the 8-Bhairava cycle in Kashmir Shaivism",
    },
    {
        "name": "Unmatta Bhairava",
        "region": "Wider valley",
        "notes": "The ecstatic form; associated with tantric Trika lineages",
    },
]

# ---------------------------------------------------------------------------
# KUL DEVI BY DISTRICT (regional mapping — tentative)
# ---------------------------------------------------------------------------

KUL_DEVI_BY_DISTRICT = {
    "Srinagar": {
        "primary": "Sharika Devi (Chakreshwari)",
        "temple": "Hari Parbat (Sharika Parbat), Srinagar",
        "location": "Hilltop shrine, Hari Parbat hill, Srinagar city — accessed via Kathi Darwaza (east) or Makhdoom Sahib path (north)",
        "towns": ["Habba Kadal", "Rainawari", "Zaina Kadal", "Fateh Kadal", "Safa Kadal", "Bohri Kadal", "Nowhatta", "Khanyar", "Maisuma", "Barbarshah", "Karan Nagar", "Gogji Pathri", "Shehr-e-Khas", "Nawab Bazar"],
        "notes": "Principal Kul Devi of all old-city Srinagar mohalla families. The Hari Parbat hill is held to be the goddess herself — she crushed the demon Jalodbhava by becoming a stone. 18-armed form (Chakreshwari). Major mela: Vaishakha Shukla Ashtami.",
        "also": [
            "Ragnya Devi (Kheer Bhawani) — Tulmul, Ganderbal · universally venerated",
            "Annapurna Devi — Dal Lake shore, Rainawari · some Rainawari families",
            "Shiva Bhagwati (Jyeshtheshwara) — Shankaracharya Hill, Srinagar",
        ],
    },
    "Ganderbal": {
        "primary": "Ragnya Devi (Kheer Bhawani / Maharagnya Bhagwati)",
        "temple": "Tullamulla (Tulmul), Ganderbal — 14 km from Srinagar on Srinagar–Ganderbal road",
        "location": "Sacred natural spring (nag) temple at Tullamulla village, Ganderbal. Spring water changes colour as divine omen.",
        "towns": ["Ganderbal Town", "Tullamulla", "Wakura", "Shuhama", "Manigam", "Kangan", "Lar", "Sonamarg", "Gund"],
        "notes": "Most universally venerated KP Kul Devi — families from all 10 districts worship here. Annual Zyeth Ashtami (Jyeshtha Shukla Ashtami) mela is the largest KP pilgrimage gathering. Secondary Ragnya sites: Manzam (Budgam), Naranag (Kangan), Tikker (Kupwara).",
        "also": [
            "Sharika Devi — Hari Parbat, Srinagar · some Ganderbal families",
            "Nanda Devi — Nandimarg, upper Ganderbal · mountain-belt families (Kangan, Sonamarg)",
            "Bhadrakali — Wangath, Kangan area · Wangath village families",
        ],
    },
    "Anantnag": {
        "primary": "Bhadrakali (Bhadra Bhagwati)",
        "temple": "Mattan (near Martand Sun Temple ruins), Anantnag district",
        "location": "Multiple sites — Mattan village near Bijbehara; also Achabal, Kokernag, Wangath (upper valley). Mattan is ~40 km south of Srinagar.",
        "towns": ["Anantnag Town", "Bijbehara", "Mattan", "Achabal", "Kokernag", "Pahalgam", "Shangus", "Dooru", "Vailoo", "Breng Valley", "Qazigund", "Banihal", "Verinag"],
        "notes": "South Kashmir families primarily venerate Bhadrakali. Associated with the ancient Martand Surya region — both Bhadrakali and Surya are Kul Devis/Devtas here. Wangath in Ganderbal has an important Bhadrakali temple for upper valley families.",
        "also": [
            "Tripura Sundari — Devsar, Kulgam · Anantnag–Kulgam border families",
            "Ragnya Devi — Tulmul, Ganderbal · universally worshipped alongside",
            "Jwala Devi — Khrew, Pulwama · some Qazigund / Banihal families",
            "Sharika Devi — Hari Parbat, Srinagar · widely venerated",
        ],
    },
    "Pulwama": {
        "primary": "Jwala Devi (Jwala Bhagwati)",
        "temple": "Khrew village, Pulwama — ~25 km south-east of Srinagar on Srinagar–Pulwama road",
        "location": "Rock-cut shrine at Khrew village on the right bank of the Jhelum. Natural flame traditionally believed to be self-manifest.",
        "towns": ["Pulwama Town", "Khrew", "Pampore", "Awantipora", "Kakapora", "Rajpora", "Tral", "Newa", "Arihal", "Shadimarg"],
        "notes": "Families from Khrew and surrounding Pulwama villages are primary devotees of Jwala Devi. Major mela: Navratri (Ashwina Shukla 1–10). Khrew was historically a prominent KP settlement.",
        "also": [
            "Bhadrakali — Mattan, Anantnag · some Awantipora / Tral families",
            "Ragnya Devi — Tulmul, Ganderbal · universal",
            "Sharika Devi — Hari Parbat, Srinagar · Pampore / Awantipora families",
        ],
    },
    "Baramulla": {
        "primary": "Sharika Devi (Chakreshwari)",
        "temple": "Hari Parbat, Srinagar (primary pilgrimage for north Kashmir families)",
        "location": "North Kashmir families travel to Hari Parbat, Srinagar for Sharika Devi. Local shrines exist in Baramulla and Sopore towns.",
        "towns": ["Baramulla Town", "Sopore", "Pattan", "Tangmarg", "Uri", "Kreeri", "Kunzer", "Boniyar", "Rafiabad"],
        "notes": "North Kashmir KP families generally follow Srinagar-belt Kul Devi traditions. Sopore and Baramulla town families are closely linked with Sharika Devi and Ragnya Devi. Uri and Boniyar belt families also venerate Sharada Devi.",
        "also": [
            "Ragnya Devi — Tulmul, Ganderbal · equally primary for many families",
            "Sharada Devi — Sharada Peeth (PoK) / Trehgam proxy · Uri, Boniyar families",
            "Jwala Devi — Khrew, Pulwama · some families",
        ],
    },
    "Budgam": {
        "primary": "Sharika Devi (Chakreshwari)",
        "temple": "Hari Parbat, Srinagar — central Budgam families worship here",
        "location": "Central Kashmir (Budgam) is closest to Srinagar; families travel to Hari Parbat. Also: Ragnya Devi at Manzam village (Budgam), approx 20 km from Srinagar.",
        "towns": ["Budgam Town", "Magam", "Beerwah", "Narbal", "Chadoora", "Khansahib", "Charar-i-Sharief", "Rakh-i-Arth", "Soibugh", "Pakharpora"],
        "notes": "Central Kashmir Budgam families follow Srinagar-belt Kul Devi tradition. Manzam has a secondary Ragnya Devi spring temple — important for Budgam families. Charar-i-Sharief was originally a Shaiva site.",
        "also": [
            "Ragnya Devi — Manzam, Budgam (secondary spring shrine) · Budgam-belt families",
            "Ragnya Devi — Tulmul, Ganderbal · universally venerated",
            "Shiva Bhagwati — Shankaracharya Hill / Charar-i-Sharief site",
        ],
    },
    "Kupwara": {
        "primary": "Sharada Devi (Sharada Bhagwati)",
        "temple": "Sharada Peeth, Sharda village, Neelum Valley (now PoK) — original seat inaccessible. Proxy shrines at Trehgam and Handwara (Kupwara).",
        "location": "Original temple at Sharda village, at confluence of Madhumati (Kishanganga) and Sargun rivers, ~150 km from Srinagar. Now inaccessible across LoC. Active proxy shrines: Trehgam (~45 km from Kupwara Town), Handwara.",
        "towns": ["Kupwara Town", "Handwara", "Trehgam", "Karnah", "Lolab", "Sogam", "Kralpora", "Drugmulla"],
        "notes": "Far north Kashmir families traditionally venerated Sharada Devi as Kul Devi. She is the goddess of learning and the patron of the Kashmiri script (Sharada lipi). One of 18 Maha Shakti Pithas. Annual Sharada Navami observed at proxy shrines. Tikker village (Handwara belt) has a Ragnya Devi spring.",
        "also": [
            "Ragnya Devi — Tikker, Handwara belt (spring shrine) · Kupwara families",
            "Ragnya Devi — Tulmul, Ganderbal · universal",
            "Sharika Devi — Hari Parbat, Srinagar · widely venerated",
        ],
    },
    "Shopian": {
        "primary": "Bhadrakali (Bhadra Bhagwati)",
        "temple": "South Kashmir temples — Shopian area village shrines; also Khrew (Pulwama) for Jwala Devi",
        "location": "Shopian belt families worship at local Bhadrakali shrines across Zainpora, Keegam, Hermain villages and at Jwala Devi temple in Khrew (Pulwama), ~30 km from Shopian.",
        "towns": ["Shopian Town", "Keegam", "Hermain", "Zainpora", "Hirpora", "Barbugh", "Chitragam"],
        "notes": "South-west Kashmir families primarily venerate Bhadrakali. Shopian belt is closely linked with Pulwama belt for Jwala Devi worship. Some Zainpora and Keegam families have both Bhadrakali and Jwala Devi as Kul Devis depending on lineage.",
        "also": [
            "Jwala Devi — Khrew, Pulwama · Shopian belt families closely linked",
            "Ragnya Devi — Tulmul, Ganderbal · universal",
            "Tripura Sundari — Devsar, Kulgam · Shopian–Kulgam border families",
        ],
    },
    "Kulgam": {
        "primary": "Tripura Sundari (Tripureshwari / Rajrajeshwari)",
        "temple": "Devsar area, Kulgam district — Devsar village and Frisal, Pahloo, Yaripora",
        "location": "Devsar is ~15 km from Kulgam Town. Tripura Sundari shrines also at Frisal, Pahloo and Yaripora villages. Bhadrakali sites across Kulgam and Anantnag border.",
        "towns": ["Kulgam Town", "D.H. Pora", "Devsar", "Frisal", "Pahloo", "Yaripora", "Noorabad"],
        "notes": "Deep south Kashmir families venerate Tripura Sundari and Bhadrakali. Tripura Sundari is the Supreme Goddess of the Kashmir Trika — she represents the three Shaktis (iccha, jnana, kriya). Kulgam families also worship Bhadrakali at Mattan (Anantnag) temples.",
        "also": [
            "Bhadrakali — Mattan, Anantnag · equally primary for most Kulgam families",
            "Ragnya Devi — Tulmul, Ganderbal · universal veneration",
            "Sharika Devi — Hari Parbat, Srinagar · some families",
        ],
    },
    "Bandipora": {
        "primary": "Ragnya Devi (Kheer Bhawani)",
        "temple": "Tulmul (Tullamulla), Ganderbal — primary pilgrimage. Also Nandkeshwar temple, Sumbal (Bandipora).",
        "location": "Tulmul is ~25 km from Bandipora Town via Sumbal. Nandkeshwar temple at Sumbal is a local shrine within Bandipora district itself.",
        "towns": ["Bandipora Town", "Hajin", "Sumbal", "Sonawari", "Ajas", "Tulail", "Gurez"],
        "notes": "North-east Kashmir families venerate Ragnya Devi as primary Kul Devi. Sumbal's Nandkeshwar Bhairava temple is the local Kshetrapala. Gurez and Tulail valley families (remote north) have both Sharika and Ragnya as Kul Devis.",
        "also": [
            "Sharika Devi — Hari Parbat, Srinagar · Bandipora and Hajin families",
            "Bhadrakali — south Kashmir temples · some lineages",
        ],
    },
}

# ---------------------------------------------------------------------------
# KUL DEVTA BY DISTRICT (male deity — tentative)
# ---------------------------------------------------------------------------

KUL_DEVTA_BY_DISTRICT = {
    "Srinagar":  {
        "primary": "Shiva (Shankaracharya / Jyeshtheshwara)",
        "temple":  "Shankaracharya Hill, Srinagar",
        "notes":   "The Shankaracharya Shiva temple (Jyeshtheshwara) atop the hill has "
                   "been the presiding Kul Devta for most old-city Srinagar families.",
    },
    "Ganderbal": {
        "primary": "Shiva (Amarnath / Bhuteshwara)",
        "temple":  "Amarnath, Pahalgam; Bhuteshwara temple Tulmul area",
        "notes":   "Universal Shiva worship; Bhuteshwara Bhairava local guardian.",
    },
    "Anantnag":  {
        "primary": "Surya (Martand)",
        "temple":  "Martand Sun Temple, Mattan, Anantnag",
        "notes":   "Ancient Surya temple (8th c. CE, Lalitaditya) — primary Kul Devta "
                   "for Anantnag-belt families.",
    },
    "Pulwama":   {
        "primary": "Shiva / Surya",
        "temple":  "Awantipur Shiva temple, Avantishwara",
        "notes":   "Awantishwara and Awantiswamin temples (Avantipora) — major Shiva and "
                   "Vishnu shrines for Pulwama-belt families.",
    },
    "Baramulla":  {
        "primary": "Shiva (Bhimashankar)",
        "temple":  "Baramulla area Shiva shrines",
        "notes":   "North Kashmir families predominantly Shaiva.",
    },
    "Budgam":    {
        "primary": "Shiva",
        "temple":  "Charar-i-Sharief (originally Shaiva site)",
        "notes":   "Central Kashmir families — primarily Shaiva Kul Devta.",
    },
    "Kupwara":   {
        "primary": "Shiva / Vishnu",
        "temple":  "Local shrines; Sharada Peeth (PoK)",
        "notes":   "Far north — Shaiva and Vaishnava traditions both present.",
    },
    "Shopian":   {
        "primary": "Shiva",
        "temple":  "South Kashmir Shiva shrines",
        "notes":   "South-west belt — primarily Shaiva tradition.",
    },
    "Kulgam":    {
        "primary": "Shiva / Vishnu",
        "temple":  "South Kashmir temples",
        "notes":   "Deep south — both Shaiva and Vaishnava lineages present.",
    },
    "Bandipora": {
        "primary": "Shiva (Nandikeshwara)",
        "temple":  "Nandkishwar temple, Sumbal",
        "notes":   "Nandikeshwara (Nandi form of Shiva) is presiding Kul Devta for "
                   "Bandipora / Sumbal families.",
    },
}

# ---------------------------------------------------------------------------
# GOTRAS with associated KP surnames (from traditional records)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME → GOTRA(S) MAP
# Source: Traditional KP gotra table (image provided by user).
# Each surname maps to its possible gotra(s) only — no other surnames listed.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME → GOTRA(S) MAP
# Source: Traditional KP gotra-surname table (image provided).
# Maps each KP surname to its possible gotra(s) only.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME (Nick Name) → GOTRA(S) MAP
# Source: Bhannamasis & Malmasis gotra tables (PDF provided).
# Each entry: Nick Name → list of full compound gotra lineage names exactly
# as they appear in the document. Multiple entries = multiple gotras possible.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME → GOTRA(S) MAP  — rebuilt from Bhannamasis/Malmasis CSV (authoritative)
# Nick Name → list of possible gotra lineage strings.
# Where a nick name appears under multiple gotras, all are listed.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------
SURNAME_GOTRA_MAP = {
    # A
    "Aima":         ["Datthtreya (Koul, Kaul)"],
    "Amhardar":     ["Pat Svamina Kaushika"],
    "Artha":        ["Artha Varshaganya Shandalya"],
    # B
    "Babu":         ["Datthtreya (Koul, Kaul)"],
    "Badgami":      ["Deva Kucha Atreya"],
    "Bakaya":       ["Paladeva Vasgargya"],
    "Bakhshi":      ["Dar Varshaganya", "Svamina Shandalya"],
    "Bali":         ["Svamina Bhargava"],
    "Bamtsunt":     ["Datthtreya (Koul, Kaul)"],
    "Bamzai":       ["Datthtreya (Koul, Kaul)"],
    "Bandar":       ["Kantha Dhaumyana Laugakshi Gautama"],
    "Bangi":        ["Dar Bharadwaja"],
    "Bangru":       ["Paladeva Vasgargya"],
    "Barbuz":       ["Varshayani"],
    "Bataphalu":    ["Deva Shandalya"],
    "Battiv":       ["Svamina Bhargava"],
    "Bazari":       ["Svamina Bharadvaja"],
    "Bazaz":        ["Svamina Gautama"],
    "Bhan":         ["Deva Gargya", "Raj Bhut Logaskhi Deval"],
    "Bhandari":     ["Vasishta Svamina Maudgalya"],
    "Bhat":         ["Dar Kapisthala", "Dat Dat Shalan Kautsa",
                     "Deva Bharadwaja", "Deva Gautama", "Deva Kaushika",
                     "Kautsa Atreya", "Kaushika Bhardwaja",
                     "Kash Aupamanyava", "Mitra Shandalya",
                     "Nanda Koshk", "Raj Dat Atreya Shalan Kautsa",
                     "Sharman Bharadwaja", "Shandalya Bharadwaja",
                     "Sharman Kautsa", "Svamina Koshk Bharadwaja",
                     "Svamina Shandalya", "Svamina Vasishta Bharadwaja",
                     "Svamina Vatsya Aupamanyava", "Wasishta",
                     "Kanth Kasahap"],
    "Bhatt":        ["Dar Kapisthala", "Dat Dat Shalan Kautsa",
                     "Deva Bharadwaja", "Deva Gautama", "Deva Kaushika",
                     "Kautsa Atreya", "Kaushika Bhardwaja",
                     "Kash Aupamanyava", "Mitra Shandalya",
                     "Nanda Koshk", "Raj Dat Atreya Shalan Kautsa",
                     "Sharman Bharadwaja", "Shandalya Bharadwaja",
                     "Sharman Kautsa", "Svamina Koshk Bharadwaja",
                     "Svamina Shandalya", "Svamina Vasishta Bharadwaja",
                     "Svamina Vatsya Aupamanyava", "Wasishta",
                     "Kanth Kasahap"],
    "Bindri":       ["Wasadeva Palagargya"],
    "Bira":         ["Pat Svamina Kaushika"],
    "Bradi":        ["Deva Kashyap Maudgalya Kashyap", "Dev Svamina Maudgalya"],
    "Braru":        ["Pat Svamina Kaushika"],
    "Breth":        ["Kantha Dhaumyana Laugakshi Gautama"],
    "Buju":         ["Datthtreya (Koul, Kaul)"],
    "Buni":         ["Svamina Maudgalya"],
    # C
    "Chacha":       ["Pat Svamina Kaushika", "Ratra Bhargava"],
    "Chaghat":      ["Pat Svamina Kaushika"],
    "Chaka":        ["Svamina Atreya"],
    "Chakan":       ["Svamina Gotam Gosh Vas Aupamanyava"],
    "Chana":        ["Svamina Maudgalya"],
    "Chandra":      ["Bhava Kapishthala"],
    "Chandru":      ["Karchanda Shandale"],
    "Charangu":     ["Svamina Gautama"],
    "Chhotu":       ["Svamina Gotam Laugakshi"],
    "Chillum":      ["Svamina Gautama"],
    "Choku":        ["Svamina Gotam Laugakshi"],
    "Chothai":      ["Svamina Warshaganya"],
    "Choudhri":     ["Artha Varshaganya Shandalya"],
    "Chowdhri":     ["Datthtreya (Koul, Kaul)"],
    # D
    "Dandar":       ["Datthtreya (Koul, Kaul)"],
    "Dangar":       ["Datthtreya (Koul, Kaul)"],
    "Dar":          ["Dar Bharadwaja"],
    "Dassu":        ["Kanth Kasahap"],
    "Deva":         ["Deva Bharadwaja Kaushika"],
    "Dewani":       ["Svamina Maudgalya"],
    "Dhar":         ["Dar Bharadwaja"],
    "Dhaumyana":    ["Dhaumyayana"],
    "Divali":       ["Svamina Bharadwaja Dhuni Kashypa Gautama Laugakshi"],
    "Dout":         ["Datthtreya (Koul, Kaul)"],
    "Drabi":        ["Datthtreya (Koul, Kaul)"],
    "Duda":         ["Svamina Warshaganya"],
    "Durani":       ["Pat Svamina Kaushika"],
    "Duru":         ["Raj Shandalya"],
    # F
    "Fata":         ["Svamina Gautama Laugakshi"],
    "Fotedar":      ["Pat Svamina Kaushika"],
    # G
    "Gadar":        ["Deva Bharadwaja"],
    "Gaddu":        ["Sharman Atreya"],
    "Gadwali":      ["Svamina Atreya"],
    "Gagar":        ["Svamina Gautama"],
    "Galikrapa":    ["Svamina Maudgalya"],
    "Ganju":        ["Pat Svamina Kaushika"],
    "Garyali":      ["Svamina Bharadvaja"],
    "Ghasi":        ["Svamina Vas Atreya"],
    "Gigu":         ["Svamina Aupamanyava"],
    "Giru":         ["Bhuta Aupamanyava Shalan Kayana"],
    "Gurut":        ["Svamina Gautama"],
    # H
    "Hak":          ["Datthtreya (Koul, Kaul)"],
    "Hakachar":     ["Raj Kaushika"],
    "Hakim":        ["Deva Gautama Laugakshi"],
    "Hangal":       ["Svamina Warshaganya"],
    "Handu":        ["Mitra Kashyapa", "Svamina Atreya",
                     "Svamina Vasishta Bharadwaja"],
    "Hapa":         ["Atri Bhargaya"],
    "Hastiwal":     ["Kantha Dhaumyana Laugakshi Gautama"],
    "Hukku":        ["Dev Wasishta", "Svamina Vasishta Bharadwaja"],
    # J
    "Jala":         ["Pat Svamina Kaushika"],
    "Jalali":       ["Datthtreya (Koul, Kaul)"],
    "Jan":          ["Svamina Bharadvaja"],
    "Jatu":         ["Deva Bharadwaja"],
    "Jawansher":    ["Dar Bharadwaja"],
    "Jinsi":        ["Datthtreya (Koul, Kaul)"],
    "Jogi":         ["Dar Shandalya"],
    "Jota":         ["Datthtreya (Koul, Kaul)"],
    # K
    "Kachru":       ["Dar Varshaganya", "Pat Svamina Kaushika"],
    "Kadalabuju":   ["Paladeva Vasgargya"],
    "Kak":          ["Datthtreya (Koul, Kaul)", "Deva Parashara",
                     "Svamina Gautama"],
    "Kala":         ["Svamina Atreya"],
    "Kakapuri":     ["Svamina Gautama"],
    "Kalla":        ["Bhava Kapishthala"],
    "Kallu":        ["Deva Bharadwaja"],
    "Kalpush":      ["Deva Patsvamina Koshk"],
    "Kalu":         ["Pat Svamina Kaushika", "Dev Aupamanyava",
                     "Svamina Bharadwaja Vas Atre"],
    "Kandar":       ["Svamina Maudgalya"],
    "Kanth":        ["Svamina Maudgalya"],
    "Kar":          ["Deva Kantha Kashyapa", "Karchanda Shandale"],
    "Karawani":     ["Deva Shandalya"],
    "Karihalu":     ["Svamina Gotam Bharadwaja"],
    "Karnel":       ["Varshayani"],
    "Kasab":        ["Dat Dat Shalan Kautsa"],
    "Kasid":        ["Svamina Warshaganya"],
    "Kashgari":     ["Rishi Kaushika"],
    "Kathju":       ["Svamina Warshaganya"],
    "Kaul":         ["Svamina Rishi Kanya Gargya",
                     "Shalan Kautsa Sharman Gusha Watsya Aupamanyava",
                     "Datthtreya (Koul, Kaul)"],
    "Kav":          ["Kantha Dhaumyana Laugakshi Gautama",
                     "Paldeva Vasagargya"],
    "Kem":          ["Dev Vishamitra Varshaganya"],
    "Kemdal":       ["Svamina Gotam Bharadwaja"],
    "Keni":         ["Datthtreya (Koul, Kaul)", "Svamina Gautama"],
    "Khaibri":      ["Bhava Kapishthala"],
    "Khanakatu":    ["Svamina Hasya Dvaseya"],
    "Khar":         ["Svamina Bharadvaja", "Svamina Bharadwaja"],
    "Khari":        ["Dat Was"],
    "Khashu":       ["Dev Aupamanyava", "Paladeva Vasgargya"],
    "Khaumush":     ["Dat Dat Shalan Kautsa"],
    "Khazanchi":    ["Svamina Maudgalya"],
    "Khod":         ["Raj Kaushika"],
    "Khoru":        ["Bhava Kapishthala"],
    "Khosa":        ["Svamina Gautama"],
    "Khoshu":       ["Paldeva Vasagargya"],
    "Khurdi":       ["Deva Bharadwaja", "Pat Svamina Kaushika"],
    "Kichlu":       ["Paladeva Vasgargya"],
    "Kissu":        ["Datthtreya (Koul, Kaul)"],
    "Kokru":        ["Paladeva Vasgargya", "Paldeva Vasagargya"],
    "Kotar":        ["Ratra Varshaganya"],
    "Kothdar":      ["Datthtreya (Koul, Kaul)"],
    "Koul":         ["Svamina Rishi Kanya Gargya",
                     "Shalan Kautsa Sharman Gusha Watsya Aupamanyava",
                     "Datthtreya (Koul, Kaul)"],
    "Kukru":        ["Paldeva Vasagargya", "Svamina Koshk Bharadwaja"],
    "Kutsru":       ["Svamina Bharadwaja"],
    "Kyani":        ["Pat Svamina Kaushika"],
    # L
    "Labru":        ["Svamina Kantha Kashyapa", "Svamina Maudgalya",
                     "Svamina Gotam Shandalya"],
    "Ladakhi":      ["Datthtreya (Koul, Kaul)"],
    "Lala":         ["Svamina Maudgalya"],
    "Lange":        ["Svamina Warshaganya"],
    "Langer":       ["Svamina Gautama", "Svamina Vasa Gargya"],
    "Lattu":        ["Bhava Kapishthala"],
    "Lidi":         ["Dar Kapisthala"],
    # M
    "Machama":      ["Svamina Gargya"],
    "Madan":        ["Svamina Maudgalya"],
    "Mala":         ["Paladeva Vasgargya"],
    "Malik":        ["Dat Dat Shalan Kautsa"],
    "Malla":        ["Paldeva Vasagargya"],
    "Mam":          ["Pat Svamina Kaushika", "Paladeva Vasgargya"],
    "Mandal":       ["Datthtreya (Koul, Kaul)"],
    "Mantapuri":    ["Deva Laugakshi"],
    "Mantu":        ["Kara Shandalya"],
    "Manwotu":      ["Svamina Gautama"],
    "Mattu":        ["Pat Svamina Kaushika", "Ratra Vishwamitra Agastya"],
    "Mazari":       ["Svamina Maudgalya"],
    "Mekhzin":      ["Datthtreya (Koul, Kaul)"],
    "Meva":         ["Dev Aupamanyava"],
    "Mich":         ["Dar Kapisthala Upamanuva"],
    "Mirakhur":     ["Paladeva Vasgargya"],
    "Miskin":       ["Svamina Bharadvaja"],
    "Misri":        ["Dar Bharadwaja", "Pat Svamina Kaushika",
                     "Paladeva Vasgargya"],
    "Miyan":        ["Svamina Bharadvaja"],
    "Mogal":        ["Sharman Kautsa"],
    "Mota":         ["Dar Dev Shalan Kapi"],
    "Moza":         ["Datthtreya (Koul, Kaul)"],
    "Muj":          ["Svamina Maudgalya"],
    "Muhtasib":     ["Datthtreya (Koul, Kaul)",
                     "Kantha Dhaumyana Laugakshi Gautama"],
    "Muki":         ["Wardhatta Shalana Kucha"],
    "Mukka":        ["Shalan Kautsa Sharman Gusha Watsya Aupamanyava"],
    "Munga":        ["Paladeva Vasgargya"],
    "Munshi":       ["Svamina Bharadvaja"],
    "Mushran":      ["Svamina Maudgalya"],
    "Muttu":        ["Dar Dev Shalana Kaushika"],
    # N
    "Nagari":       ["Datthtreya (Koul, Kaul)", "Kaushika Bhardwaja"],
    "Nakhasi":      ["Ishwar Shandalya Kusha"],
    "Naqib":        ["Svamina Gautama"],
    "Nari":         ["Svamina Shandalya"],
    # P
    "Padar":        ["Datthtreya (Koul, Kaul)"],
    "Padi":         ["Svamina Gan Kaushika"],
    "Padora":       ["Svamina Gautama"],
    "Pahalwan":     ["Datthtreya (Koul, Kaul)"],
    "Pandita":      ["Pat Svamina Kaushika", "Pat Svamina Deva Ratra Parwara",
                     "Deva Laugakshi", "Dev Aupamanyava",
                     "Nanda Kaushika Bharadwaja", "Vatsya Gusha Aupamanyava",
                     "Paladeva Vasgargya"],
    "Pandit":       ["Pat Svamina Kaushika", "Pat Svamina Deva Ratra Parwara",
                     "Deva Laugakshi", "Dev Aupamanyava",
                     "Nanda Kaushika Bharadwaja", "Vatsya Gusha Aupamanyava"],
    "Panzu":        ["Pat Svamina Kaushika"],
    "Parimu":       ["Svamina Gautama"],
    "Parikala":     ["Dar Bharadwaja"],
    "Partazi":      ["Raj Dhattatreya"],
    "Pat":          ["Paldeva Vasagargya"],
    "Patar":        ["Bhava Kapishthala Kaushika"],
    "Peshen":       ["Bhuta Was Aupamanyava Laugakshi"],
    "Peshin":       ["Bhuta Vatsya Aupamanyava"],
    "Piala":        ["Svamina Gautama"],
    "Pir":          ["Paldeva Vasagargya", "Paladeva Vasgargya"],
    "Pishen":       ["Bhuta Aupamanyava Vatsya Laugakshi"],
    "Purbi":        ["Deva Gautama"],
    "Put":          ["Svamina Maudgalya", "Paladeva Vasgargya"],
    # Q
    "Qandahari":    ["Dar Bharadwaja"],
    "Qazi":         ["Svamina Gautama"],
    # R
    "Raina":        ["Dat Sharman Kantha Kashyapa",
                     "Svamina Gautama Atreya Shalan Kucha"],
    "Rangateng":    ["Wasishta"],
    "Ratiz":        ["Datthtreya (Koul, Kaul)"],
    "Raval":        ["Ishwar Shandalya Kusha"],
    "Razdan":       ["Kantha Dhaumyana Laugakshi Gautama",
                     "Dhaumyayana", "Kanth Kasahap",
                     "Svamina Gautama", "Svamina Gotam Shandalya",
                     "Svamina Gotam Shalan Kucha Atreya",
                     "Svamina Maudgalya",
                     "Dat Sharman Kantha Kashyapa"],
    # S
    "Sabani":       ["Deva Bharadwaja"],
    "Safaya":       ["Dar Varshaganya", "Dar Wasak Shandilya",
                     "Deva Varshaganya Shandilya"],
    "Sahib":        ["Datthtreya (Koul, Kaul)"],
    "Said":         ["Mitra Svamina Kaushika Atreya"],
    "Salman":       ["Pat Svamina Kaushika", "Datthtreya (Koul, Kaul)"],
    "Sapru":        ["Dipat Saman Aupamanyava"],
    "Sav":          ["Sharman Kautsa"],
    "Sazawul":      ["Dat Varshaganya"],
    "Shah":         ["Kantha Dhaumyana Laugakshi Gautama"],
    "Shair":        ["Kantha Dhaumyana Laugakshi Gautama"],
    "Shal":         ["Svamina Atreya"],
    "Shali":        ["Dar Varshaganya"],
    "Shanglu":      ["Pat Svamina Kaushika"],
    "Shargha":      ["Datthtreya (Koul, Kaul)"],
    "Shoga":        ["Datthtreya (Koul, Kaul)"],
    "Shopuri":      ["Dev Wasishta"],
    "Shora":        ["Svamina Maudgalya"],
    "Shunglu":      ["Raj Vasisht"],
    "Sibbu":        ["Bhava Kapishthala"],
    "Sikh":         ["Svamina Atreya"],
    "Singhari":     ["Datthtreya (Koul, Kaul)"],
    "Sopuri-Pandit":["Paladeva Vasgargya"],
    "Sultan":       ["Datthtreya (Koul, Kaul)"],
    "Sulu":         ["Pat Svamina Kaushika"],
    "Sum":          ["Svamina Vasa Gargya"],
    # T
    "Taku":         ["Svamina Maudgalya"],
    "Tangan":       ["Kanth Kasahap"],
    "Tarivala":     ["Svamina Gautama"],
    "Tava":         ["Svamina Gautama"],
    "Teng":         ["Pat Svamina Kaushika"],
    "Thakur":       ["Bhuta Was Aupamanyava Laugakshi", "Svamina Kaushika"],
    "Thapal":       ["Svamina Gautama"],
    "Thalatsur":    ["Dar Bharadwaja", "Svamina Gautama"],
    "Thela":        ["Sharman Kautsa"],
    "Thogan":       ["Deva Parashara"],
    "Thusu":        ["Svamina Was Atreya", "Svamina Vas Atreya"],
    "Thusoo":       ["Svamina Was Atreya", "Svamina Vas Atreya"],
    "Tickoo":       ["Svamina Bharadvaja"],
    "Tiku":         ["Svamina Bharadvaja"],
    "Tikku":        ["Svamina Bharadvaja"],
    "Tilwan":       ["Shalan Kautsa Sharman Gusha Watsya Aupamanyava"],
    "Tota":         ["Datthtreya (Koul, Kaul)"],
    "Trakari":      ["Ratra Vishwamitra Vasishta"],
    "Tritshal":     ["Pat Svamina Kaushika"],
    "Tritsha":      ["Dar Bharadwaja"],
    "Tsrungu":      ["Deva Vardhatta Shalan Kaushika"],
    "Tsul":         ["Svamina Gotam Atreya"],
    "Tshut":        ["Dar Bharadwaja"],
    "Tulsi":        ["Deva Parashara"],
    "Tur":          ["Svamina Laugakshi"],
    "Turi":         ["Svamina Gotam Laugakshi"],
    "Turki":        ["Dar Bharadwaja"],
    # U
    "Ugra":         ["Datthtreya (Koul, Kaul)"],
    "Ukhlu":        ["Dev Wasishta"],
    "Unt":          ["Pat Svamina Kaushika"],
    "Uthu":         ["Dar Bharadwaja"],
    # V
    "Vangar":       ["Dev Vishamitra Varshaganya"],
    "Vankhan":      ["Bhava Kapishthal Aupamanyava"],
    "Vantu":        ["Bhava Kapishthala"],
    "Variku":       ["Bhava Aupamanyava"],
    "Warikoo":      ["Bhava Aupamanyava"],
    "Vashnavi":     ["Pat Svamina Kaushika"],
    "Vichari":      ["Dar Bharadwaja"],
    # W
    "Waguzari":     ["Dar Bharadwaja"],
    "Wanchu":       ["Pat Svamina Kaushika"],
    "Wanikhan":     ["Bhava Kapishthal Aupamanyava"],
    "Wangani":      ["Kantha Dhaumyana Laugakshi Gautama"],
    "Wallu":        ["Svamina Vatsya Aupamanyava"],
    "Wat":          ["Kantha Dhaumyana Laugakshi Gautama"],
    "Watal":        ["Pat Svamina Deva Ratra Parwara", "Svamina Kaushika"],
    "Waza":         ["Svamina Vas Atreya", "Pat Svamina Kaushika"],
    "Wufa":         ["Pat Svamina Kaushika"],
    # Y
    "Yachh":        ["Deva Bharadwaja", "Deva Parashara"],
    "Yechh":        ["(Deva) Parashara"],
    # Z
    "Zadu":         ["Bhava Kapishthala"],
    "Zahi":         ["Svamina Maudgalya"],
    "Zalpari":      ["Bhuta Was Aupamanyava Laugakshi"],
    "Zamindar":     ["Datthtreya (Koul, Kaul)"],
    "Zari":         ["Kantha Dhaumyana Laugakshi Gautama", "Svamina Gautama"],
    "Zaru":         ["Deva Bharadwaja", "Rishi Kavigargya"],
    "Zithu":        ["Pat Svamina Kaushika"],
    "Zitshoo":      ["Ratra Bhargava"],
    "Zitu":         ["Svamina Maudgalya"],
    "Zotan":        ["Svamina Maudgalya"],
}

GOTRAS = [
    "Kashyapa", "Vasishtha", "Vishwamitra", "Jamadagni", "Bharadwaja",
    "Atri", "Gautama", "Agastya", "Angirasa", "Bhrigu",
    "Kaushika", "Garga", "Shandilya", "Kaundinya", "Vatsya",
    "Harita", "Maudgalya", "Parashara", "Upamanyu", "Vatsa"
]

KUL_DEVIS = [
    "Sharika Devi (Hari Parbat)", "Jwala Devi (Khrew)", "Ragnya Devi (Tulamula)",
    "Bahuchara Mata", "Vaishno Devi (Trikuta Hills)", "Kheer Bhawani (Tulmul)",
    "Maha Kali (Barav)", "Durga Devi", "Saraswati Devi", "Tripura Sundari"
]

KUL_DEVTAS = [
    "Shiva (Amarnath)", "Vishnu (Martand)", "Surya (Martand)",
    "Ganesha", "Skanda", "Indra", "Kubera", "Varuna"
]

BHAIRAVAS = [
    "Kalabhairava", "Asitanga Bhairava", "Ruru Bhairava", "Chanda Bhairava",
    "Krodha Bhairava", "Unmatta Bhairava", "Kapala Bhairava", "Bhishana Bhairava",
    "Samhara Bhairava", "Swarna Akarshana Bhairava", "Batuka Bhairava"
]

# Nakshatra compatibility data for 36 Gunas
NAKSHATRA_GANA = {
    "Ashwini": "Deva", "Bharani": "Manushya", "Krittika": "Rakshasa",
    "Rohini": "Manushya", "Mrigashira": "Deva", "Ardra": "Manushya",
    "Punarvasu": "Deva", "Pushya": "Deva", "Ashlesha": "Rakshasa",
    "Magha": "Rakshasa", "Purva Phalguni": "Manushya", "Uttara Phalguni": "Manushya",
    "Hasta": "Deva", "Chitra": "Rakshasa", "Swati": "Deva",
    "Vishakha": "Rakshasa", "Anuradha": "Deva", "Jyeshtha": "Rakshasa",
    "Mula": "Rakshasa", "Purva Ashadha": "Manushya", "Uttara Ashadha": "Manushya",
    "Shravana": "Deva", "Dhanishtha": "Rakshasa", "Shatabhisha": "Rakshasa",
    "Purva Bhadrapada": "Manushya", "Uttara Bhadrapada": "Manushya", "Revati": "Deva"
}

NAKSHATRA_NADI = {
    "Ashwini": "Aadi", "Bharani": "Madhya", "Krittika": "Antya",
    "Rohini": "Antya", "Mrigashira": "Madhya", "Ardra": "Aadi",
    "Punarvasu": "Aadi", "Pushya": "Madhya", "Ashlesha": "Antya",
    "Magha": "Antya", "Purva Phalguni": "Madhya", "Uttara Phalguni": "Aadi",
    "Hasta": "Aadi", "Chitra": "Madhya", "Swati": "Antya",
    "Vishakha": "Antya", "Anuradha": "Madhya", "Jyeshtha": "Aadi",
    "Mula": "Aadi", "Purva Ashadha": "Madhya", "Uttara Ashadha": "Antya",
    "Shravana": "Antya", "Dhanishtha": "Madhya", "Shatabhisha": "Aadi",
    "Purva Bhadrapada": "Aadi", "Uttara Bhadrapada": "Madhya", "Revati": "Antya"
}

NAKSHATRA_YONI = {
    "Ashwini": ("Horse", "M"), "Bharani": ("Elephant", "M"), "Krittika": ("Goat", "F"),
    "Rohini": ("Serpent", "M"), "Mrigashira": ("Serpent", "F"), "Ardra": ("Dog", "F"),
    "Punarvasu": ("Cat", "F"), "Pushya": ("Goat", "M"), "Ashlesha": ("Cat", "M"),
    "Magha": ("Rat", "M"), "Purva Phalguni": ("Rat", "F"), "Uttara Phalguni": ("Cow", "M"),
    "Hasta": ("Buffalo", "F"), "Chitra": ("Tiger", "F"), "Swati": ("Buffalo", "M"),
    "Vishakha": ("Tiger", "M"), "Anuradha": ("Deer", "F"), "Jyeshtha": ("Deer", "M"),
    "Mula": ("Dog", "M"), "Purva Ashadha": ("Monkey", "F"), "Uttara Ashadha": ("Mongoose", "M"),
    "Shravana": ("Monkey", "M"), "Dhanishtha": ("Lion", "F"), "Shatabhisha": ("Horse", "F"),
    "Purva Bhadrapada": ("Lion", "M"), "Uttara Bhadrapada": ("Cow", "F"), "Revati": ("Elephant", "F")
}

NAKSHATRA_RASHI = {
    "Ashwini": 0, "Bharani": 0, "Krittika": 0, "Rohini": 1, "Mrigashira": 1,
    "Ardra": 2, "Punarvasu": 2, "Pushya": 3, "Ashlesha": 3, "Magha": 4,
    "Purva Phalguni": 4, "Uttara Phalguni": 4, "Hasta": 5, "Chitra": 5,
    "Swati": 6, "Vishakha": 6, "Anuradha": 7, "Jyeshtha": 7, "Mula": 8,
    "Purva Ashadha": 8, "Uttara Ashadha": 8, "Shravana": 9, "Dhanishtha": 9,
    "Shatabhisha": 10, "Purva Bhadrapada": 10, "Uttara Bhadrapada": 11, "Revati": 11
}

RASHI_LORDS = {
    0: "Mars", 1: "Venus", 2: "Mercury", 3: "Moon", 4: "Sun",
    5: "Mercury", 6: "Venus", 7: "Mars", 8: "Jupiter", 9: "Saturn",
    10: "Saturn", 11: "Jupiter"
}

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima/Amavasya"
]

VARA_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

YOGA_NAMES = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana",
    "Atiganda", "Sukarma", "Dhriti", "Shula", "Ganda",
    "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
    "Siddhi", "Vyatipata", "Variyana", "Parigha", "Shiva",
    "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
    "Indra", "Vaidhriti"
]

KARANA_NAMES = [
    "Bava", "Balava", "Kaulava", "Taitila", "Garija",
    "Vanija", "Vishti", "Shakuni", "Chatushpada", "Naga",
    "Kimstughna"
]

RITU_NAMES = {
    (1, 2): "Vasanta (Spring)", (3, 4): "Grishma (Summer)",
    (5, 6): "Varsha (Monsoon)", (7, 8): "Sharad (Autumn)",
    (9, 10): "Hemanta (Pre-winter)", (11, 12): "Shishira (Winter)"
}

MASA_NAMES = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha", "Shravana",
    "Bhadrapada", "Ashwina", "Kartika", "Margashirsha", "Pausha",
    "Magha", "Phalguna"
]

# Muhurats (auspicious times) data
INAUSPICIOUS_TIMES = {
    "Rahu Kaal": {0: (4.5, 6), 1: (7.5, 9), 2: (3, 4.5), 3: (6, 7.5), 
                   4: (1.5, 3), 5: (0, 1.5), 6: (9, 10.5)},  # in 1.5 hour slots from sunrise
}

