# main.py
import sys, os

# ───────────────────────
# 旧プロジェクトへのパスを追加
# ※ 実際のパスに書き換えてください
OLD = os.path.expanduser("~PycharmProjects/python_learning")
if OLD not in sys.path:
    sys.path.insert(0, OLD)
# ───────────────────────

# 以下、もともとの import 文…


import streamlit as st
from datetime import datetime
import os
import sqlite3

import config

# 各画面／機能モジュール（Streamlit 対応版にリファクタリングしてください）
from input_company_info import input_company_info
from input_previous_year_data import input_previous_year_data
from input_compound_journal_entry import input_compound_journal_entry
from input_ledger_entry import input_ledger_entry
from input_journal_entry import input_journal_entry

from show_journal_entry import show_journal_entry
from update_compound_journal_entry import update_compound_journal_entry

from save_compound_journal_entry_pattern import save_compound_journal_entry_pattern
from show_compound_entry_pattern import show_compound_entry_pattern
from save_ledger_entry_pattern import save_ledger_entry_pattern
from show_ledger_entry_pattern import show_ledger_entry_pattern

from show_ledgers import show_ledgers
from show_trial_balance import show_trial_balance, export_trial_balance_to_PDF
from show_financial_analysis import show_financial_analysis

from export_ledgers_to_CSV import export_ledgers_to_CSV
from export_financial_reports_to_CSV import export_financial_reports_to_CSV
from export_financial_reports_to_PDF import export_financial_reports_to_PDF

from show_financial_reports import show_financial_reports
from input_closing_entry import input_closing_entry
from finalize_this_year import finalize_this_year


def render_header():
    """画面上部のヘッダー（ロゴや会社名、決算期など）"""
    st.markdown("## 会計ソフト")
    # もしロゴ画像があれば
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)
    # 会社名・決算期表示（config などで定義しておく）
    # st.markdown(f"**{config.COMPANY_NAME}** | 決算期: {config.FISCAL_YEAR}")


def render_footer():
    """画面下部のフッター（コピーライトなど）"""
    st.markdown("---")
    st.markdown("© 2025 Your Company Name")


def main():
    st.set_page_config(page_title="会計ソフト", layout="wide")

    render_header()

    # サイドバーにメニューを定義
    menu_items = [
        ("基礎情報入力", input_company_info),
        ("新年度スタート（前期繰越）", input_previous_year_data),
        ("複合仕訳入力", input_compound_journal_entry),
        ("元帳入力", input_ledger_entry),
        ("仕訳入力", input_journal_entry),
        ("仕訳表示", show_journal_entry),
        ("複合仕訳更新", update_compound_journal_entry),
        ("複合仕訳パターン登録", save_compound_journal_entry_pattern),
        ("複合仕訳パターン表示", show_compound_entry_pattern),
        ("元帳パターン登録", save_ledger_entry_pattern),
        ("元帳パターン表示", show_ledger_entry_pattern),
        ("仕訳帳表示", show_ledgers),
        ("試算表表示", show_trial_balance),
        ("試算表PDF出力", export_trial_balance_to_PDF),
        ("経営分析グラフ出力", show_financial_analysis),
        ("仕訳データCSV出力", export_ledgers_to_CSV),
        ("決算書CSV出力", export_financial_reports_to_CSV),
        ("決算書PDF出力", export_financial_reports_to_PDF),
        ("決算書表示", show_financial_reports),
        ("決算整理仕訳入力", input_closing_entry),
        ("年度締め／次期繰越", finalize_this_year),
    ]
    labels = [label for label, _ in menu_items]
    choice = st.sidebar.selectbox("メインメニュー", labels)

    # コンテンツエリアに選択ページを表示
    for label, func in menu_items:
        if choice == label:
            st.sidebar.success(f"▶ {label} を開いています")
            try:
                func()  # 各モジュール側で Streamlit UI を描画する想定
            except Exception as e:
                st.error(f"{label} の表示に失敗しました: {e}")
            break

    render_footer()


if __name__ == "__main__":
    main()