from src.data_fetcher import fetch_stock_data
from datetime import datetime

print("Testing after revert:")
print("=" * 60)

# Test VNINDEX
df_vn = fetch_stock_data('VNINDEX', datetime(2024, 11, 21), period_days=365, exchange='')
print(f"VNINDEX: {len(df_vn) if df_vn is not None else 0} rows", '✅' if df_vn is not None and len(df_vn) > 0 else '❌')

# Test HOSE stocks
hose_stocks = ['SSI', 'VND', 'HPG']
print("\nHOSE stocks:")
for ticker in hose_stocks:
    df = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange='HOSE')
    print(f"  {ticker}: {len(df) if df is not None else 0} rows", '✅' if df is not None and len(df) > 0 else '❌')

# Test HNX stocks
hnx_stocks = ['SHS', 'MBS', 'PVS']
print("\nHNX stocks:")
for ticker in hnx_stocks:
    df = fetch_stock_data(ticker, datetime(2024, 11, 21), period_days=365, exchange='HNX')
    print(f"  {ticker}: {len(df) if df is not None else 0} rows", '✅' if df is not None and len(df) > 0 else '❌')

# Test UPCOM
df_acv = fetch_stock_data('ACV', datetime(2024, 11, 21), period_days=365, exchange='UPCOM')
print(f"\nUPCOM (ACV): {len(df_acv) if df_acv is not None else 0} rows", '✅' if df_acv is not None and len(df_acv) > 0 else '❌')
