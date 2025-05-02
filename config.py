# config.py

# 変数の命名ルール
NAMING_CONVENTION = "snake_case"

# 日付形式ルール
DATE_FORMAT = "%Y-%m-%d"

# デフォルトのフォント（OSごとに設定、iOS・Androidは後日追加予定）
DEFAULT_FONTS = {
    "macos": "Arial",
    "windowsos": "Segoe UI",
    "ios": None,
    "androidos": None
}

# ファイルの保存場所
JOURNAL_ENTRY_FILE = "journal_entries.db"        # 仕訳データ (SQLite)
JOURNAL_DATA_FILE = "journal_data.db"
LEDGERS_DIR = "ledgers/"                         # 帳簿データ保存先
REPORTS_DIR = "financial_reports/"               # 決算データ保存先
LOGS_DIR = "logs/"                               # 仕訳入力ログ保存先

# 関数名と日本語ラベル（メニュー・画面遷移用）
FUNCTION_NAMES = {
    "main":                                "メイン",                             # メニュー画面呼び出し
    "input_company_info":                  "基礎情報入力",                       # 会社情報入力
    "input_previous_year_data":            "前期繰越",                           # 新年度スタート（前期データ繰越）
    "save_compound_journal_entry_pattern": "複合仕訳パターン登録",               # 複合仕訳パターンを保存
    "save_ledger_entry_pattern":           "元帳入力パターン登録",               # 元帳入力パターンを保存
    "input_compound_journal_entry":        "複合仕訳入力",                       # 複合仕訳入力画面
    "input_ledger_entry":                  "元帳入力",                           # 元帳入力画面
    "input_journal_entry":                 "仕訳入力",                           # 単純仕訳入力画面
    "show_journal_entry":                  "仕訳表示",                           # 仕訳データ一覧表示
    "update_compound_journal_entry":       "複合仕訳更新",                       # 複合仕訳の編集
    "export_ledgers_to_CSV":               "仕訳データCSV出力",                   # CSV出力（仕訳データ）
    "export_ledgers_to_PDF":               "元帳PDF出力",                         # PDF出力（元帳）
    "show_ledgers":                        "元帳表示",                           # 元帳一覧表示
    "show_compound_entry_pattern":         "複合仕訳パターン表示",               # 登録済みパターン一覧表示
    "show_ledger_entry_pattern":           "元帳入力パターン表示",               # 登録済み元帳パターン一覧
    "show_financial_analysis":             "経営分析グラフ出力",                  # グラフ出力（経営分析）
    "export_financial_reports_to_CSV":     "決算書CSV出力",                      # CSV出力（決算書）
    "export_financial_reports_to_PDF":     "決算書PDF出力",                      # PDF出力（決算書）
    "show_financial_reports":              "決算書表示",                        # 決算書一覧表示
    "input_closing_entry":                 "決算整理仕訳入力",                  # 決算整理仕訳入力画面
    "finalize_this_year":                  "次期繰越"                            # 年度締め／次期繰越
}

# ディレクトリ構造
'''
project_root/
├─ main.py                            # エントリポイント
├─ input.py                           # 「入力系」機能をまとめる
│   ├─ input_journal_entry()
│   ├─ input_compound_journal_entry()
│   └─ input_closing_entry()

├─ ledger.py                          # 元帳関連
│   ├─ input_ledger_entry()
│   └─ export_ledgers_to_PDF()/show_ledgers()
├─ pattern.py                         # パターン登録／編集
│   ├─ save_compound_journal_entry_pattern()
│   ├─ show_compound_entry_pattern()
│   ├─ update_compound_journal_entry()
│   └─ （元帳パターンも同様に）
├─ export.py                          # CSV/PDF 出力まとめ
│   ├─ export_ledgers_to_CSV()
│   ├─ export_financial_reports_to_CSV()
│   ├─ export_financial_reports_to_PDF()
│   └─ （必要なら further 分割も可）
├─ view.py                            # 表示系まとめ
│   ├─ show_financial_reports()
│   ├─ show_financial_analysis()
│   └─ （show_ledgers もこちらに入れてもOK）
├─ db_utils.py                       # DB系（ユーザー操作以外）
│   ├─ get_accounts_code_list()
│   └─ update_accounts_name()
├─ db_operations.py                  # DB系（ユーザーの操作に関するもの） 
│   ├─ get_next_entry_num()
│   ├─ save_compound_journal_entry()
│   ├─ fetch_journal_data()
│   ├─ load_trial_balance()
│   ├─ load_income_statement()
│   └─ load_balance_sheet()
├─ create_tables.py　　　　　　　　　　 # 最初のテーブル作成
├─ csv_to_accounts.py                # CSVをaccountsテーブルに変換 
└─ config.py     
'''


# 会計科目カテゴリーを定義（accounts.category_id と対応）
ACCOUNT_CATEGORIES = {
    'assets':       1,   # 資産の部
    'liabilities':  2,   # 負債の部
    'equity':       3,   # 純資産の部
    'revenue':      4,   # 収益の部
    'expense':      5    # 費用の部
}