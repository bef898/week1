import pandas as pd
import talib
import matplotlib.pyplot as plt

def load_stock_data(file_path):
    """
    Load stock price data from a CSV file into a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])  # Ensure 'Date' column is in datetime format
    return data

def calculate_moving_averages(data, window_short=20, window_long=50):
    """
    Calculate short and long period simple moving averages (SMA).
    """
    data['MA_Short'] = talib.SMA(data['Adj Close'], timeperiod=window_short)
    data['MA_Long'] = talib.SMA(data['Adj Close'], timeperiod=window_long)
    return data

def calculate_rsi(data, period=14):
    """
    Calculate Relative Strength Index (RSI).
    """
    data['RSI'] = talib.RSI(data['Adj Close'], timeperiod=period)
    return data

def calculate_macd(data, fastperiod=12, slowperiod=26, signalperiod=9):
    """
    Calculate Moving Average Convergence Divergence (MACD).
    """
    data['MACD'], data['MACD_Signal'], data['MACD_Hist'] = talib.MACD(
        data['Adj Close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
    return data

def apply_all_indicators(data):
    """
    Apply all technical indicators to the stock data.
    """
    data = calculate_moving_averages(data)
    data = calculate_rsi(data)
    data = calculate_macd(data)
    return data
    
def plot_technical_indicators(data):
    """
    Plot the stock data with technical indicators.
    """
    plt.figure(figsize=(14, 8))

    # Plot Adjusted Close and Moving Averages
    plt.subplot(3, 1, 1)
    plt.plot(data['Date'], data['Adj Close'], label='Adjusted Close', color='blue')
    plt.plot(data['Date'], data['MA_Short'], label='20-Day MA', color='red')
    plt.plot(data['Date'], data['MA_Long'], label='50-Day MA', color='green')
    plt.title('Adjusted Close and Moving Averages')
    plt.legend()

    # Plot RSI
    plt.subplot(3, 1, 2)
    plt.plot(data['Date'], data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()

    # Plot MACD
    plt.subplot(3, 1, 3)
    plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
    plt.plot(data['Date'], data['MACD_Signal'], label='Signal Line', color='orange')
    plt.bar(data['Date'], data['MACD_Hist'], label='MACD Histogram', color='gray')
    plt.title('MACD')
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_bollinger_bands(data):
    """
    Plot Bollinger Bands.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Adj Close'], label='Adjusted Close', color='blue')
    plt.plot(data['Date'], data['Bollinger_High'], label='Bollinger High', color='red')
    plt.plot(data['Date'], data['Bollinger_Low'], label='Bollinger Low', color='green')
    plt.fill_between(data['Date'], data['Bollinger_High'], data['Bollinger_Low'], color='gray', alpha=0.3)
    plt.title('Bollinger Bands')
    plt.legend()
    plt.show()
