from src.data_fetcher import fetch_stock_data
from datetime import datetime

print("Final test after fix:")
print("=" * 60)

# Test VNINDEX
df_vn = fetch_stock_data('VNINDEX', datetime(2024, 11, 21), period_days=365, exchange='')
print(f"VNINDEX: {len(df_vn) if df_vn is not None else 0} rows")

# Test stocks from all exchanges
test_stocks = [
    ('SSI', 'HOSE'),
    ('VND', 'HOSE'),
    ('SHS', 'HNX'),
    ('MBS', 'HNX'),
    ('ACV', 'UPCOM')
]

for ticker, exchange in test_stocks:
    df = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange=exchange)
    rows = len(df) if df is not None else 0
    status = '✅' if rows > 0 else '❌'
    print(f"{ticker} ({exchange:5s}): {rows:3d} rows {status}")
