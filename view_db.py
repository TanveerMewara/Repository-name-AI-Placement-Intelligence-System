import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "placement_ai.db"
)

df = pd.read_sql(
    "SELECT * FROM candidates",
    conn
)

print(df)

conn.close()