import streamlit as st
import pandas as pd
st.title("Abuja Rent Intelligence")
df = pd.read_csv("data/warehouse/rent_warehouse.csv")
st.dataframe(df)
location = st.selectbox("Filter location", df.location.unique())
st.write(df[df.location == location])