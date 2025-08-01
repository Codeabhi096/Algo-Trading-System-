import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="6mo", interval="1d"):
    try:
        df = yf.download(ticker, period=period, interval=interval)
        df.dropna(inplace=True)
        df.reset_index(inplace=True)
        df["Ticker"] = ticker  # Ticker column add
        return df
    except Exception as e:
        print(f" Error fetching data for {ticker}: {e}")
        return pd.DataFrame()




