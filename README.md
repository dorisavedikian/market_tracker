# 📊 Market Tracker

A real-time market tracking app that monitors the latest prices for:

- 🟡 Gold (via GLD ETF)
- 🪙 Bitcoin (via CoinGecko API)
- 📈 S&P 500 (via SPY ETF)

This project automates data collection via Python, stores the data in a MySQL database, and visualizes market trends using an interactive dashboard built with Streamlit.

---

## 🚀 Features

- ✅ Pulls real-time financial data from public APIs
- ✅ Stores historical records in a MySQL database
- ✅ Automates hourly updates using a cron job
- ✅ Interactive dashboard for visual exploration

---

## 🧰 Tech Stack

| Layer         | Tool / Library                   |
|---------------|----------------------------------|
| Data Sources  | Yahoo Finance (`yfinance`), CoinGecko |
| Scripting     | Python, `pandas`, `requests`     |
| Storage       | MySQL                            |
| Automation    | Cron Job                         |
| Dashboard     | Streamlit                        |

---

## 🗂️ Project Structure

```
market_tracker/
├── fetch_market_data.py      # Fetches and stores market data
├── market_dashboard.py       # Streamlit dashboard app
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview
└── .gitignore                # Ignore venv, pyc files, etc.
```

---

## ⚙️ Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/dorisavedikian/market_tracker.git
cd market_tracker
```

### 2. 🐍 Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. 🛠️ MySQL Setup

#### Install MySQL (if needed)

```bash
brew install mysql
brew services start mysql
```

#### Log in as root (>> mysql -u root) and create user/database/table than >> exit;

```sql
CREATE DATABASE market_db;

CREATE USER 'marketuser'@'localhost' IDENTIFIED BY 'marketpass';
GRANT ALL PRIVILEGES ON market_db.* TO 'marketuser'@'localhost';
FLUSH PRIVILEGES;

USE market_db;

CREATE TABLE market_prices (
    asset VARCHAR(50),
    symbol VARCHAR(10),
    price_usd DECIMAL(18, 8),
    timestamp DATETIME
);
```

---

## 📥 Fetch Market Data

Run the data collection script manually:

```bash
python fetch_market_data.py
```

This fetches the latest prices for Gold, Bitcoin, and the S&P 500 and stores them in MySQL using UTC timestamps.

---

## ⏰ Schedule Hourly Updates with Cron

📄 See [`cron_schedule.txt`]() for the recommended hourly cron job configuration.

To run the script every hour:

```bash
crontab -e
```

---

## 📊 Launch the Streamlit Dashboard

Start the dashboard locally:

```bash
streamlit run market_dashboard.py
```

Then open the link in your browser (e.g., `http://localhost:8501`) to view the live-updating dashboard.

---

## 🌐 Deploy the Dashboard (Optional)

You can deploy your Streamlit app to the web for free using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Set the main file to `market_dashboard.py`
5. (Optional) Use hosted MySQL like [PlanetScale](https://planetscale.com/) for remote access

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt` includes:**

```
pandas
requests
yfinance
SQLAlchemy
pymysql
streamlit
```

---

## 🙌 Contributing

Pull requests are welcome! You can contribute by:

- Adding support for more assets (e.g., oil, NASDAQ, bonds)
- Enhancing the dashboard (filters, charts)
- Improving error handling and logging

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Credits

Built with ❤️ by Doris Avedikian.
