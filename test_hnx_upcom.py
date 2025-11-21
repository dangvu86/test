from src.data_fetcher import fetch_stock_data
from datetime import datetime
import pandas as pd

# Load stock list
df = pd.read_csv('TA_Tracking_List.csv')

# Get HNX and UPCOM stocks
hnx_stocks = df[df['Exchange'] == 'HNX']['Ticker'].tolist()
upcom_stocks = df[df['Exchange'] == 'UPCOM']['Ticker'].tolist()

print("Testing HNX stocks:")
print("-" * 50)
for ticker in hnx_stocks:
    df_data = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange='HNX')
    rows = len(df_data) if df_data is not None else 0
    status = '✅' if rows > 0 else '❌'
    print(f"{ticker:6s}: {rows:3d} rows {status}")

print("\nTesting UPCOM stocks:")
print("-" * 50)
for ticker in upcom_stocks:
    df_data = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange='UPCOM')
    rows = len(df_data) if df_data is not None else 0
    status = '✅' if rows > 0 else '❌'
    print(f"{ticker:6s}: {rows:3d} rows {status}")
