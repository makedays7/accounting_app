import sqlite3
import pandas as pd

# SQLiteデータベースに接続
conn = sqlite3.connect("example.db")

# データを取得
query = "SELECT * FROM users"
df = pd.read_sql(query, conn)

# CSVとして保存
df.to_csv("output.csv", index=False, encoding="utf-8")

# データベースを閉じる
conn.close()

print("SQLiteのデータをCSVにエクスポートしました！")
