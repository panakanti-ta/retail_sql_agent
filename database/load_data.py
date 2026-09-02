import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "retail_agent.db"
DATA_DIR = BASE_DIR / "data"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    files = {
        "stores": DATA_DIR / "stores.csv",
        "products": DATA_DIR / "products.csv",
        "customers": DATA_DIR / "customers.csv",
        "sales_transactions": DATA_DIR / "sales_transactions.csv",
        "returns": DATA_DIR / "returns.csv",
    }
    
    for table_name, csv_file in files.items():
        if csv_file.exists():
            df = pd.read_csv(csv_file)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Loaded {len(df)} rows into '{table_name}' table.")
        else:
            print(f"Warning: {csv_file} not found.")
        
    conn.close()

if __name__ == "__main__":
    load_data()
