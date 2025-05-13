import csv
import sqlite3

# データベース接続
conn = sqlite3.connect("journal_data.db")
cursor = conn.cursor()

# CSVファイルの読み込み
with open("accounts.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # ヘッダーをスキップ
    data = [tuple(row) for row in reader]  # データをリスト化

# データの挿入（executemanyで一括登録）
cursor.executemany("INSERT INTO accounts (accounts_id, accounts_code, category_id, accounts_name, accounts_sort_order) VALUES (?, ?, ?,?,?)", data)

# 変更を保存
conn.commit()
conn.close()

print("CSVからデータをインポートしました。")
