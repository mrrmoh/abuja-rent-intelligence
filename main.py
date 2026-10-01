from src.scraper import scrape_rent_listings
from src.etl import transform_rent, load_warehouse
from src.analyzer import generate_insights
import pandas as pd

print("🏠 Abuja Rent Intelligence Starting...")
listings = scrape_rent_listings()
df = pd.DataFrame(listings)

df_clean = transform_rent(df)
warehouse = load_warehouse(df_clean)
generate_insights(df_clean)

print(f"\n✅ ETL Complete: {len(df_clean)} listings warehoused")
print("Check data/warehouse/rent_warehouse.csv and dashboard/rent_by_location.png")