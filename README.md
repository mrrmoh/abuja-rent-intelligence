# Abuja Rent Intelligence System

Real-time rent tracker for Abuja & Lagos  because rent in Masaka vs Wuse is 400% different and no one explains why.
Tracks rent across 10 locations from Masaka (Nasarawa) to Lekki (Lagos).

## Problem
Abuja tenants pay 10% agency + 10% caution + 1 year upfront with no price transparency.
Same Self-Contain ₦210k in Masaka = ₦720k in Wuse 2.
Zero transparency.

## Solution
ETL pipeline that scrapes, cleans, and warehouses rent data to detect overpriced listings.

## Features
- Scrapes 120 listings across 10 locations
- Calculates monthly breakdown & affordability score
- Flags overpriced >20% above location average
- Warehouse aggregated by location + property type

## Key Insight (from this run)
- Masaka avg Self-Contain: ₦210k/yr vs Wuse ₦720k/yr = 242% difference for 30 min drive
- Lekki is 5.7x Masaka
- 242% premium to live 30 mins closer to center
- 18% listings overpriced 20% above location avg

## Stack
Python, Pandas, ETL, Data Warehousing, Market Intelligence

---
## 🔗 Part of Nigeria Intelligence Systems.

This project is part of a 4-pipeline interconnected system tracking Nigeria's real economy + security:

**Market Intelligence:**

- [1. Abuja Price Intelligence]
(https://github.com/mrrmoh/abuja-price-intelligence) 
— Cement & building materials ETL

- [2. Nigeria Fuel Intelligence]
(https://github.com/mrrmoh/nigeria-fuel-intelligence) 
— Fuel & USD/NGN correlation

- [3. Abuja Rent Intelligence (This Repo)]
(https://github.com/mrrmoh/abuja-rent-intelligence) 
— Rent spread & overpricing detection

**Security Intelligence:**
- [4. Phishing Intelligence Pipeline](https://github.com/mrrmoh/phishing-intelligence-pipeline) — Threat Intel IOC feed for SOC

**Master Connector:**
- [5. Nigeria Intelligence Master]
(https://github.com/mrrmoh/nigeria-intelligence-master) — Links all pipelines into Cost-of-Living Index (coming soon)

> All pipelines use same ETL pattern: `scraper.py → etl.py → analyzer.py → warehouse` — demonstrating reusable Data Engineering architecture.