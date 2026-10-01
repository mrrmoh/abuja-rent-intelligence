import pandas as pd
import os

def clean_rent(df):
    df['annual_rent_ngn'] = df['annual_rent_ngn'].astype(int)
    # Affordability: Masaka = baseline
    masaka_avg = df[df.location == "Masaka"]['annual_rent_ngn'].mean()
    df['vs_masaka_premium_%'] = ((df['annual_rent_ngn'] - masaka_avg) / masaka_avg * 100).round(1)
    return df

def warehouse_rent(df):
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/warehouse", exist_ok=True)

    df.to_csv("data/processed/clean_rent.csv", index=False)

    # Flag overpriced: 20% above location mean
    location_avg = df.groupby('location')['annual_rent_ngn'].mean().to_dict()
    df['location_avg'] = df['location'].map(location_avg)
    df['is_overpriced'] = df['annual_rent_ngn'] > (df['location_avg'] * 1.2)

    summary = df.groupby('location').agg(
        avg_rent=('annual_rent_ngn', 'mean'),
        min_rent=('annual_rent_ngn', 'min'),
        listings=('annual_rent_ngn', 'count'),
        overpriced_count=('is_overpriced', 'sum')
    ).reset_index().sort_values('avg_rent')

    summary.to_csv("data/warehouse/rent_summary.csv", index=False)
    return summary, df
    import pandas as pd
import os

def transform_rent(df):
    df['price_per_month'] = (df['price_per_year'] / 12).round(2)
    df['affordability_score'] = pd.cut(df['price_per_year'],
        bins=[0, 400000, 800000, 1500000, 99999999],
        labels=["Budget", "Mid", "High", "Luxury"]
    )
    # Avg per location
    avg_by_loc = df.groupby('location')['price_per_year'].mean().to_dict()
    df['location_avg'] = df['location'].map(avg_by_loc)
    df['overpriced_flag'] = df['price_per_year'] > df['location_avg'] * 1.2
    return df

def load_warehouse(df):
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/warehouse", exist_ok=True)
    df.to_csv("data/processed/clean_rent.csv", index=False)
    # Data Warehouse - aggregated
    warehouse = df.groupby(['location', 'property_type']).agg(
        avg_price=('price_per_year', 'mean'),
        min_price=('price_per_year', 'min'),
        max_price=('price_per_year', 'max'),
        count=('price_per_year', 'count')
    ).reset_index()
    warehouse.to_csv("data/warehouse/rent_warehouse.csv", index=False)
    return warehouse