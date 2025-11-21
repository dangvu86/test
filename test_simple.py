from src.data_fetcher import fetch_stock_data
from datetime import datetime

print("Testing current state:")
print("=" * 60)

# Test VNINDEX
df_vn = fetch_stock_data('VNINDEX', datetime(2024, 11, 21), period_days=365, exchange='')
print(f"VNINDEX: {len(df_vn) if df_vn is not None else 0} rows")
if df_vn is not None and len(df_vn) > 0:
    print(f"Date range: {df_vn['Date'].min()} to {df_vn['Date'].max()}")
    print(f"Latest close: {df_vn['Close'].iloc[-1]}")
else:
    print("VNINDEX: No data")

print("\n" + "=" * 60)

# Test a few stocks from different exchanges
test_stocks = [
    ('SSI', 'HOSE'),
    ('SHS', 'HNX'),
    ('ACV', 'UPCOM')
]

for ticker, exchange in test_stocks:
    df = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange=exchange)
    rows = len(df) if df is not None else 0
    print(f"{ticker} ({exchange}): {rows} rows")
