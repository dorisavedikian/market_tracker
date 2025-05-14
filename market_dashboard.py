import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📊 Real-Time Market Dashboard")

engine = create_engine("mysql+pymysql://username:password@localhost:3306/market_db")
df = pd.read_sql("SELECT * FROM market_prices ORDER BY timestamp DESC", engine)

st.dataframe(df)

pivot_df = df.pivot_table(index="timestamp", columns="asset", values="price_usd", aggfunc="first")
st.line_chart(pivot_df)