from src.tcbs_api_fetcher import fetch_tcbs_api_data
from src.data_fetcher import fetch_stock_data
from datetime import datetime

print("Testing TCBS API directly:")
print("-" * 60)

# Test TCBS API raw
df_tcbs = fetch_tcbs_api_data('SHS', days=30)
print(f"TCBS raw SHS: {len(df_tcbs) if df_tcbs is not None else 0} rows")
if df_tcbs is not None and len(df_tcbs) > 0:
    print(f"Date range: {df_tcbs['Date'].min()} to {df_tcbs['Date'].max()}")
    print(df_tcbs[['Date', 'Close']].tail(3))
else:
    print("No data from TCBS")

print("\n" + "=" * 60)
print("Testing via data_fetcher:")
print("-" * 60)

# Test via data_fetcher
df_fetcher = fetch_stock_data('SHS', datetime(2024, 11, 21), period_days=30, exchange='HNX')
print(f"data_fetcher SHS: {len(df_fetcher) if df_fetcher is not None else 0} rows")
if df_fetcher is not None and len(df_fetcher) > 0:
    print(f"Date range: {df_fetcher['Date'].min()} to {df_fetcher['Date'].max()}")
    print(df_fetcher[['Date', 'Close']].tail(3))
else:
    print("No data from data_fetcher")
