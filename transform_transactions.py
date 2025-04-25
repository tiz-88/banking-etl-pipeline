import pandas as pd

def transform_transactions(df):
    if df.empty:
        print("Empty DataFrame. Skipping transformation.")
        return df

    # Example: remove negative amounts and convert timestamps
    df = df[df['amount'] > 0]
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])

    return df
