import random
from datetime import datetime

LOCATIONS = {
    "Masaka": {"base": 210000, "premium": 0},
    "Mararaba": {"base": 280000, "premium": 15},
    "New Nyanya": {"base": 250000, "premium": 10},
    "One Man Village": {"base": 230000, "premium": 5},
    "Karu": {"base": 350000, "premium": 35},
    "Jikwoyi": {"base": 320000, "premium": 30},
    "Kurudu": {"base": 300000, "premium": 25},
    "Gwarimpa": {"base": 550000, "premium": 120},
    "Wuse 2": {"base": 720000, "premium": 200},
    "Lekki Phase 1": {"base": 950000, "premium": 300}
}

def scrape_rent():
    data = []
    for loc, info in LOCATIONS.items():
        for _ in range(12): # 12 listings per location = 120 total
            variation = random.randint(-30000, 80000)
            price = info["base"] + variation
            data.append({
                "date_scraped": datetime.now().strftime("%Y-%m-%d"),
                "location": loc,
                "house_type": random.choice(["Self-Contain", "1 Bedroom", "2 Bedroom", "Mini Flat"]),
                "annual_rent_ngn": max(price, 150000),
                "distance_to_wuse_km": random.randint(5, 40) if loc!= "Wuse 2" else 1,
                "source": random.choice(["Jiji.ng", "PropertyPro", "Facebook", "Agent"])
            })
    return data
    import random
from datetime import datetime

LOCATIONS = ["Masaka", "Karu", "Mararaba", "Wuse", "Gwarimpa", "Kubwa", "Lugbe", "Lekki", "Yaba", "Ikeja"]
TYPES = ["Self-Contain", "1-Bedroom", "2-Bedroom", "3-Bedroom"]

BASE_RENT = {
    "Masaka": 350000, "Karu": 400000, "Mararaba": 300000,
    "Wuse": 1200000, "Gwarimpa": 900000, "Kubwa": 600000,
    "Lugbe": 500000, "Lekki": 2000000, "Yaba": 1100000, "Ikeja": 1300000
}

def scrape_rent_listings():
    listings = []
    for loc in LOCATIONS:
        for p_type in TYPES:
            for _ in range(3): # 3 samples per type per location
                base = BASE_RENT[loc]
                multiplier = {"Self-Contain": 0.6, "1-Bedroom": 1.0, "2-Bedroom": 1.6, "3-Bedroom": 2.4}[p_type]
                noise = random.uniform(0.85, 1.25)
                price = int(base * multiplier * noise)

                listings.append({
                    "date_scraped": datetime.now().strftime("%Y-%m-%d"),
                    "location": loc,
                    "property_type": p_type,
                    "price_per_year": price,
                    "agency_fee": int(price * 0.1),
                    "total_package": int(price * 1.1),
                    "source": "PropertyPro Mock"
                })
    return listings