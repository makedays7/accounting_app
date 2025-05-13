import sqlite3

conn = sqlite3.connect("journal_data.db")
conn.execute("PRAGMA foreign_keys = ON") #外部キー制約を有効にする
cursor = conn.cursor()

# companyテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS company(
    company_id INTEGER PRIMARY KEY,
    company_name TEXT,
    fiscal_year_start DATE,
    fiscal_year_end DATE,
    fiscal_year INTEGER,
    company_term INTEGER,
    tax_status INTEGER
    )
''')
conn.commit()

# clientテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS client(
    client_num INTEGER PRIMARY KEY,
    client_name TEXT,
    client_note TEXT
    )
''')
conn.commit()

# tax_categoryテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS tax_category(
    tax_category_id INTEGER PRIMARY KEY,
    tax_category_name TEXT,
    tax_rate REAL 
    )
''')
conn.commit()

# categoryテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS category(
    category_id INTEGER PRIMARY KEY,
    category_name TEXT,
    category_sort_order INTEGER NOT NULL UNIQUE
    )
''')
conn.commit()

# accountsテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts(
    accounts_id INTEGER PRIMARY KEY,
    accounts_code INTEGER NOT NULL,
    accounts_name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    accounts_sort_order INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(category_id) REFERENCES category(category_id)
    )
''')
conn.commit()

# sub_accountsテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS sub_accounts(
    sub_accounts_id INTEGER PRIMARY KEY,
    sub_accounts_code INTEGER,
    sub_accounts_name TEXT,
    accounts_id INTEGER,
    sub_accounts_sort_order INTEGER,
    FOREIGN KEY(accounts_id) REFERENCES accounts(accounts_id)
    )
''')
conn.commit()


# journal_entriesテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS journal_entries(
    entry_num INTEGER PRIMARY KEY,
    entry_date DATE NOT NULL,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES company(company_id)    
    )
''')
conn.commit()

# journal_linesテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS journal_lines(
    entry_num INTEGER NOT NULL,
    line_num INTEGER NOT NULL,
    debit_account_id INTEGER,
    debit_sub_account_id INTEGER,
    debit_amount INTEGER,
    debit_tax_category_id INTEGER,
    debit_tax INTEGER,
    debit_note TEXT,
    credit_account_id INTEGER,
    credit_sub_account_id INTEGER,
    credit_amount INTEGER,
    credit_tax_category_id INTEGER,
    credit_tax INTEGER,
    credit_note TEXT,
    client_id INTEGER,
    PRIMARY KEY(entry_num, line_num),
    FOREIGN KEY(entry_num) REFERENCES journal_entries(entry_num),
    FOREIGN KEY(debit_account_id) REFERENCES accounts(accounts_id),
    FOREIGN KEY(debit_sub_account_id) REFERENCES sub_accounts(sub_accounts_id),
    FOREIGN KEY(debit_tax_category_id) REFERENCES tax_category(tax_category_id),
    FOREIGN KEY(credit_account_id) REFERENCES accounts(accounts_id),
    FOREIGN KEY(credit_sub_account_id) REFERENCES sub_accounts(sub_accounts_id),
    FOREIGN KEY(credit_tax_category_id) REFERENCES tax_category(tax_category_id),
    FOREIGN KEY(client_id) REFERENCES client(client_num)
    ) 
''')
conn.commit()

# journal_patternsテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS journal_patterns (
    pattern_num INTEGER PRIMARY KEY,
    pattern_type INTEGER,
    pattern_name TEXT
    )
''')
conn.commit()

# journal_pattern_detailsテーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS journal_pattern_details (
    pattern_num INTEGER NOT NULL,
    line_num INTEGER NOT NULL,
    debit_account_id INTEGER,
    debit_sub_account_id INTEGER,
    debit_amount INTEGER,
    debit_tax_category_id INTEGER,
    debit_tax INTEGER,
    debit_note TEXT,
    credit_account_id INTEGER,
    credit_sub_account_id INTEGER,
    credit_amount INTEGER,
    credit_tax_category_id INTEGER,
    credit_tax INTEGER,
    credit_note TEXT,
    client_id INTEGER,
    PRIMARY KEY(pattern_num, line_num),
    FOREIGN KEY(pattern_num) REFERENCES journal_patterns(pattern_num),
    FOREIGN KEY(debit_account_id) REFERENCES accounts(accounts_id),
    FOREIGN KEY(debit_sub_account_id) REFERENCES sub_accounts(sub_accounts_id),
    FOREIGN KEY(credit_account_id) REFERENCES accounts(accounts_id),
    FOREIGN KEY(credit_sub_account_id) REFERENCES sub_accounts(sub_accounts_id),
    FOREIGN KEY(client_id) REFERENCES client(client_num)
    )
''')
conn.close()
