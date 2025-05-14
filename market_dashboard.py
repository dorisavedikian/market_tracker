import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta, timezone

st.title("📊 Market Dashboard")

engine = create_engine("mysql+pymysql://marketuser:marketpass@localhost:3306/market_db")
df = pd.read_sql("SELECT * FROM market_prices", engine)

# Make timestamps timezone-aware
df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.tz_localize("UTC")

# Filter last 24 hours
now = datetime.now(timezone.utc)
last_24 = now - timedelta(hours=24)
df = df[df["timestamp"] >= last_24].sort_values("timestamp")

# Set timestamp as index and resample to hourly
df.set_index("timestamp", inplace=True)
# Group by asset and resample to 1-minute price (to match your data frequency)
freq = st.sidebar.selectbox("Resample frequency", ["1min", "1h"])

df_hourly = (
    df[["asset", "price_usd"]]
    .groupby("asset")
    .resample(freq)
    .mean()
    .reset_index()
)

# Display table
st.subheader("📋 Market Data (Last 24 Hours)")
st.dataframe(df.tail(10))

# Pivot for charts
pivot = df_hourly.pivot(index="timestamp", columns="asset", values="price_usd")

# Chart 1
st.subheader("📈 S&P 500")
if "S&P 500" in pivot.columns:
    st.line_chart(pivot["S&P 500"])

# Chart 2
st.subheader("🟡 Gold")
if "Gold" in pivot.columns:
    st.line_chart(pivot["Gold"])

# Chart 3
st.subheader("🪙 Bitcoin")
if "Bitcoin" in pivot.columns:
    st.line_chart(pivot["Bitcoin"])

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download Data", csv, "market_data.csv", "text/csv")