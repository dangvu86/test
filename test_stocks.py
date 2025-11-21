from src.data_fetcher import fetch_stock_data
from datetime import datetime

test_stocks = ['SSI', 'VND', 'VCI', 'HPG', 'VPB', 'TCB', 'MBB']

print("Testing stock data fetching:")
print("-" * 50)

for ticker in test_stocks:
    df = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange='HOSE')
    rows = len(df) if df is not None else 0
    status = '✅' if rows > 0 else '❌'
    print(f"{ticker:6s}: {rows:3d} rows {status}")
