import sqlite3

def check_saved_entries(db_path="journal_data.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("【journal_entries】")
    cursor.execute("SELECT * FROM journal_entries")
    entries = cursor.fetchall()
    for entry in entries:
        print(entry)

    print("\n【journal_lines】")
    cursor.execute("SELECT * FROM journal_lines")
    lines = cursor.fetchall()
    for line in lines:
        print(line)

    conn.close()

if __name__ == "__main__":
    check_saved_entries()
