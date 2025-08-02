import pandas as pd

def compute_rsi(series, period=14):
    """
    Calculates the Relative Strength Index (RSI).
    """
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def apply_strategy(df):
    """
    Applies RSI + Moving Average crossover strategy:
    Buy signal = RSI < 30 AND 20DMA > 50DMA
    """
    df = df.copy()

    # Calculate RSI
    df['RSI'] = compute_rsi(df['Close'], period=14)

      # Generate Buy Signal
    df['Buy_Signal'] = (df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])

    return df


    # Calculate 20-day and 50-day Moving Averages
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()

  
