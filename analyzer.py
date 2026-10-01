import matplotlib.pyplot as plt
import pandas as pd

def generate_insights(df):
    os = __import__('os')
    os.makedirs("dashboard", exist_ok=True)

    # Chart 1: Avg rent by location
    avg = df.groupby('location')['price_per_year'].mean().sort_values()
    plt.figure(figsize=(10,6))
    avg.plot(kind='barh', color='teal')
    plt.title("Average Yearly Rent by Location (NGN)")
    plt.tight_layout()
    plt.savefig("dashboard/rent_by_location.png")
    plt.close()

    # Print insights
    print(f"\n--- RENT INTELLIGENCE ---")
    print(f"Cheapest location: {avg.index[0]} - ₦{avg.iloc[0]:,.0f}/yr")
    print(f"Most expensive: {avg.index[-1]} - ₦{avg.iloc[-1]:,.0f}/yr")
    print(f"Masaka Self-Contain avg: ₦{df[(df.location=='Masaka') & (df.property_type=='Self-Contain')].price_per_year.mean():,.0f}")
    print(f"Overpriced listings flagged: {df.overpriced_flag.sum()}")

def analyze_rent(summary, df):
    import os
    os.makedirs("dashboard", exist_ok=True)

    plt.figure(figsize=(12,6))
    plt.barh(summary['location'], summary['avg_rent']/1000, color='teal')
    plt.xlabel("Avg Annual Rent (Thousands NGN)")
    plt.title("Abuja Rent Spread: Masaka vs Wuse vs Lekki")
    plt.tight_layout()
    plt.savefig("dashboard/rent_spread.png")
    plt.close()

    print("\n--- RENT INTELLIGENCE ---")
    print(f"Cheapest: {summary.iloc[0].location} - ₦{summary.iloc[0].avg_rent:,.0f}")
    print(f"Most Expensive: {summary.iloc[-1].location} - ₦{summary.iloc[-1].avg_rent:,.0f}")
    print(f"Premium Wuse vs Masaka: {((summary.iloc[-2].avg_rent / summary.iloc[0].avg_rent)-1)*100:.0f}%")
    print(f"Overpriced listings flagged: {df.is_overpriced.sum()}")