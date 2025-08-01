
# 🚀 Algo-Trading System with ML & Automation
 This project is a cutting-edge Python-based prototype of an algorithmic trading system, engineered to democratize stock market analysis and strategy execution. It intelligently fetches real-time stock data, deploys a robust technical trading strategy, and automates performance tracking directly into Google Sheets. While the advanced ML prediction and a comprehensive alert system are next on our roadmap, this system provides a powerful, modular, and scalable foundation for any aspiring quant or data-driven trader.

## ✨ Key Highlights

  * **📈 Smart Data Ingestion:** Seamlessly pulls historical daily stock data for top NIFTY 50 blue-chip stocks (e.g., RELIANCE.NS, TCS.NS, INFY.NS) using reliable, free stock data APIs like Yahoo Finance.
  * **🧠 Intelligent Strategy Engine:** Implements a battle-tested rule-based buy signal:
      * **RSI (Relative Strength Index) \< 30:** Identifies potential oversold conditions where a price rebound might be imminent.
      * **20-DMA Crossing Above 50-DMA:** Confirms the strength of an emerging uptrend, filtering out false signals.
  * **📊 Automated Backtesting:** Rigorously backtests the strategy over a 6-month period, providing insights into its historical performance and potential profitability.
  * **☁️ Google Sheets Integration:** Transforms raw data into actionable insights, effortlessly logging and organizing your trading activities:
      * **Real-time Trade Logging:** Every buy signal and relevant data point is meticulously recorded.
      * **Organized Worksheets:** Dedicated tabs for each stock ticker ensure crystal-clear data separation and easy analysis.
      * **Performance Dashboard (Upcoming):** A centralized summary sheet will soon offer portfolio analytics, total data points, buy signal frequency, and ML model accuracy.
  * **🤖 ML-Powered Prediction (Next Frontier):**
      * Currently integrates a **Logistic Regression model** to predict next-day price movements, leveraging key features like RSI, 20-DMA, 50-DMA, and Volume, with accuracy metrics reported.
      * Future work will explore advanced models (e.g., Random Forests, Gradient Boosting) and feature engineering (MACD, Bollinger Bands, sentiment) for sharper predictions.
  * **🏗️ Modular & Clean Architecture:** Built with reusability and clarity in mind. The codebase is neatly organized into distinct modules for data handling, strategy, Google Sheets automation, and ML, making it easy to understand, extend, and debug.

## 📦 Project Structure

```
├── .gitignore             # Files and folders to be ignored by Git (e.g., sensitive credentials, virtual environment)
├── main.py                # The heart of the system; orchestrates the trading bot's operations
├── requirements.txt       # All necessary Python libraries listed for easy installation
├── creds.json             # ⚠️ Google Sheets API credentials (NEVER push this file to public repos!)
├── ml_model.py            # Contains the core Machine Learning model logic for predictions
├── scheduler.py           # (Future Ready) Placeholder for scheduling automated tasks
├── sheet_updater.py       # Manages all communication and data updates to Google Sheets
├── strategy.py            # Defines the technical trading strategy rules
└── utils.py               # Collection of utility functions, including stock data fetching
```

## 🚀 Get Started (Quick Setup)

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Codeabhi096/Algo-Trading-System-.git
    cd Algo-Trading-System-
    ```

2.  **Set Up Your Environment:**

    ```bash
    python -m venv .venv
    # Activate:
    # Windows: .venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Google Sheets API Configuration:**

      * Visit the [Google Cloud Console](https://console.cloud.google.com/).
      * Create a new project or select an existing one.
      * Enable the **"Google Sheets API"** and **"Google Drive API"**.
      * Create a **Service Account** and download its JSON key file.
      * **Rename this file to `creds.json`** and place it directly in the `Algo-Trading-System-` root directory.
      * **Crucially, share your target Google Sheet** with the email address of your newly created service account (this email is found within your `creds.json` file).

5.  **Run the System:**

    ```bash
    python main.py
    ```

## 🛣️ Roadmap & Future Enhancements

  * **Deepen ML Insights:** Explore advanced models (Random Forests, XGBoost) and incorporate more diverse features (e.g., MACD, Bollinger Bands, candlestick patterns, sentiment analysis) for enhanced predictive power.
  * **⚡ Real-Time Alerts:** Implement a Telegram or email-based notification system for instant buy/sell signals and critical error alerts.
  * **Live Trading Integration:** Investigate secure connections with brokerage APIs to enable real-time trade execution (requires extensive testing and robust risk management).
  * **Comprehensive Portfolio Management:** Develop advanced modules for detailed portfolio tracking, sophisticated risk assessment, and dynamic position sizing.
  * **Enhanced Robustness:** Strengthen error handling across all modules for API failures, network interruptions, and data inconsistencies.

## ⚠️ Disclaimer

This project is built as a **prototype for educational and demonstrative purposes only.** It is **NOT intended for real-money trading** without significant further development, rigorous backtesting across diverse market conditions, and a robust risk management framework. Trading in financial markets carries substantial risk, and past performance is not indicative of future results.

-----

## 📞 Connect & Feedback

Got ideas, questions, or just want to chat about algo-trading? I'd love to hear from you\!

  * **LinkedIn:**  `https://www.linkedin.com/in/abhishekbhardwaj01/`
  * **Email:**  `abhishek.pathak0111@gmail.com`

-----
