from etl.extract_transactions import extract_transactions
from etl.transform_transactions import transform_transactions
from etl.load_transactions import load_to_db

def run_etl():
    df_raw = extract_transactions('data/fake_transactions.csv')
    df_clean = transform_transactions(df_raw)
    load_to_db(df_clean)

if __name__ == "__main__":
    run_etl()