import sqlite3

def load_to_db(df, db_name="transactions.db", table_name="transactions"):
    if df.empty:
        print("Empty DataFrame. Skipping load step.")
        return

    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into {table_name} table.")
