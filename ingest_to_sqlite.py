import sqlite3
import pandas as pd
import os

conn = sqlite3.connect("ecommerce.db")

for file in os.listdir("data"):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "")
        df = pd.read_csv(f"data/{file}")
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"✅ Loaded {file} into table '{table_name}'")

conn.close()
print("🎯 All CSVs loaded into ecommerce.db")
