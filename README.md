# Abuja Rent Intelligence System

Real-time rent tracker for Abuja & Lagos — because rent in Masaka vs Wuse is 400% different and no one explains why.

## Problem
Abuja tenants pay 10% agency + 10% caution + 1 year upfront with no price transparency.

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

## Stack
Python, Pandas, ETL, Data Warehousing, Market Intelligence