from extract_transactions import extract_transactions
from transform_transactions import transform_transactions
from load_transactions import load_to_db

def run_etl():
    df_raw = extract_transactions('fake_transactions.csv')
    df_clean = transform_transactions(df_raw)
    load_to_db(df_clean)

if __name__ == "__main__":
    run_etl()