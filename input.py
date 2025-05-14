import streamlit as st
import sqlite3
import config
from layout import render_layout
from db_utils import get_accounts_code_list
from datetime import date
from input_logic import (
    init_rows, add_row, remove_row, calculate_totals,
    collect_values, save_entries, get_empty_row
)

# ───────────────────────────────────────────
# 仕訳入力画面トップ
# ───────────────────────────────────────────
def input_journal_entry():
    def content():
        cal1, cal2 = st.columns([1,1])
        with cal1:
            if st.button("複合入力"):
                st.session_state.page = "input_compound_journal_entry"
                return
        with cal2:
            st.button("元帳入力", disabled=True)
    render_layout("入力方法選択 - 会計ソフト", content)

# ───────────────────────────────────────────
# 複合仕訳入力画面
# ───────────────────────────────────────────
def input_compound_journal_entry():
    def content():
        st.header("複合仕訳入力")
        accounts_list = get_accounts_code_list()
        entry_date = st.date_input("日付", value=date.today(), key="entry_date")

        init_rows()
        for idx in range(len(st.session_state.rows)):
            cols = st.columns([2, 2, 2, 2, 3])
            with cols[0]:
                st.selectbox("借方科目", options=accounts_list, key=f"debit_account_{idx}")
            with cols[1]:
                st.text_input("借方金額", key=f"debit_amount_{idx}")
            with cols[2]:
                st.selectbox("貸方科目", options=accounts_list, key=f"credit_account_{idx}")
            with cols[3]:
                st.text_input("貸方金額", key=f"credit_amount_{idx}")
            with cols[4]:
                st.text_input("備考", key=f"note_{idx}")
                if st.button("削除", key=f"remove_{idx}", on_click=remove_row, args=(idx,)):
                    st.experimental_rerun()

        st.button("行を追加", on_click=add_row)

        debit_total, credit_total = calculate_totals()
        st.write(f"**借方合計**: {debit_total:,}    **貸方合計**: {credit_total:,}")

        if st.button("保存"):
            if debit_total != credit_total:
                st.warning("借方と貸方の合計が一致しません。")
            else:
                values = collect_values(entry_date)
                if save_entries(values):
                    st.success("保存が完了しました。")
                    st.session_state.rows = [get_empty_row()]
                    st.experimental_rerun()
                else:
                    st.error("保存中にエラーが発生しました。")

    render_layout("複合仕訳入力 - 会計ソフト", content)

# ───────────────────────────────────────────
# 簡易確認画面（任意）
# ───────────────────────────────────────────
def check_saved_entries():
    st.header("保存済み仕訳確認")
    conn = sqlite3.connect(config.JOURNAL_DATA_FILE)
    entries = conn.execute("SELECT * FROM journal_entries ORDER BY entry_num").fetchall()
    lines = conn.execute("SELECT * FROM journal_lines ORDER BY entry_num, line_num").fetchall()
    conn.close()

    st.subheader("journal_entries")
    st.write(entries)
    st.subheader("journal_lines")
    st.write(lines)
