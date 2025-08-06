from utils import fetch_stock_data
from strategy import apply_strategy
from sheet_updater import update_google_sheet, update_backtest_summary


def run_trading_bot():
    tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    sheet_name = "Algo_Trading System"

    summary_data = []

    for ticker in tickers:
        print(f"\n Backtesting for {ticker}...")
        df = fetch_stock_data(ticker)
        if df.empty:
            print(f" Data not found for {ticker}")
            continue

        df = apply_strategy(df)

        # Buy signals
        df_signals = df[df["Buy_Signal"] == True]
        print(f" Buy signals found: {len(df_signals)}")

        # Update last 10 rows to separate worksheet for each ticker
        update_google_sheet(df.tail(10), sheet_name, worksheet_name=ticker.replace(".NS", ""))

       

        # Prepare summary data
        summary_data.append([
            ticker,
            len(df),
            len(df_signals),
            f"{(len(df_signals) / len(df)) * 100:.2f}%",
           
        ])

    # Update Summary Sheet
    update_backtest_summary(sheet_name, summary_data)


