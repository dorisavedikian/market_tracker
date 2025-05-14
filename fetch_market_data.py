import yfinance as yf
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timezone


# Collect market prices
data_rows = []

# S&P 500 via SPY ETF
spy_price = yf.Ticker("SPY").history(period="1d").tail(1)["Close"].values[0]
data_rows.append(("S&P 500", "SPY", float(spy_price)))

# Gold via GLD ETF
gld_price = yf.Ticker("GLD").history(period="1d").tail(1)["Close"].values[0]
data_rows.append(("Gold", "GLD", float(gld_price)))

# Bitcoin via CoinGecko
btc_price = requests.get("https://api.coingecko.com/api/v3/simple/price", 
                         params={"ids": "bitcoin", "vs_currencies": "usd"}).json()["bitcoin"]["usd"]
data_rows.append(("Bitcoin", "BTC", float(btc_price)))

# Create DataFrame and insert into MySQL
df = pd.DataFrame(data_rows, columns=["asset", "symbol", "price_usd"])
df["timestamp"] = datetime.now(timezone.utc)

engine = create_engine("mysql+pymysql://marketuser:marketpass@localhost:3306/market_db")
df.to_sql("market_prices", con=engine, if_exists="append", index=False)