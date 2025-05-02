# db_utils.py

import sqlite3
import config

def get_accounts_code_list():
    """
    Streamlit の selectbox に渡すリストを返す。
    'コード 名称' の形式の文字列リストを想定。
    """
    conn = sqlite3.connect(config.JOURNAL_DATA_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT accounts_code_id, accounts_name
        FROM accounts
        ORDER BY accounts_sort_order
    """)
    rows = cursor.fetchall()
    conn.close()

    # 例: [(101, '現金'), (102, '普通預金')] → ['101 現金', '102 普通預金']
    return [f"{code} {name}" for code, name in rows]
