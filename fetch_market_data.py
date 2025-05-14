import yfinance as yf
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timezone

# Collect prices
data_rows = []

try:
    spy = yf.Ticker("SPY")
    spy_price = spy.history(period="1d").tail(1)["Close"].values[0]
    data_rows.append(("S&P 500", "SPY", float(spy_price)))
except Exception as e:
    print("Error fetching SPY:", e)

try:
    gld = yf.Ticker("GLD")
    gld_price = gld.history(period="1d").tail(1)["Close"].values[0]
    data_rows.append(("Gold", "GLD", float(gld_price)))
except Exception as e:
    print("Error fetching GLD:", e)

try:
    btc = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "bitcoin", "vs_currencies": "usd"}).json()
    btc_price = btc["bitcoin"]["usd"]
    data_rows.append(("Bitcoin", "BTC", float(btc_price)))
except Exception as e:
    print("Error fetching Bitcoin:", e)

df = pd.DataFrame(data_rows, columns=["asset", "symbol", "price_usd"])
df["timestamp"] = datetime.now(timezone.utc)

engine = create_engine("mysql+pymysql://marketuser:marketpass@localhost:3306/market_db")
df.to_sql("market_prices", con=engine, if_exists="append", index=False)

print("✅ Cron ran at:", datetime.now())