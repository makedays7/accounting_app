import sqlite3

# データベースに接続
conn = sqlite3.connect("journal_data.db")
cursor = conn.cursor()

# 初期データの定義
tax_data = [
    (1, "課税売上10%", 0.10),
    (2, "軽減税率8%", 0.08),
    (3, "非課税", 0.00),
    (4, "不課税（対象外）", 0.00),
    (5, "輸出免税", 0.00)
]

# すでに存在するかをチェックして、なければ挿入
for tax_category_id, name, rate in tax_data:
    cursor.execute("SELECT COUNT(*) FROM tax_category WHERE tax_category_id = ?", (tax_category_id,))
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO tax_category (tax_category_id, tax_category_name, tax_rate) VALUES (?, ?, ?)",
            (tax_category_id, name, rate)
        )

# 保存して終了
conn.commit()
conn.close()

print("tax_category テーブルに初期データを登録しました。")
