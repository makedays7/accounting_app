import streamlit as st
import sqlite3
from datetime import date

import config
from db_utils import get_accounts_code_list
from db_operations import save_compound_journal_entry

# Initialize session state for dynamic rows
if "rows" not in st.session_state:
    st.session_state.rows = [
        {"debit_account": None, "debit_amount": "", "credit_account": None, "credit_amount": "", "note": ""}
        for _ in range(2)
    ]


def add_row():
    st.session_state.rows.append(
        {"debit_account": None, "debit_amount": "", "credit_account": None, "credit_amount": "", "note": ""}
    )


def remove_row(index):
    st.session_state.rows.pop(index)


def input_compound_journal_entry():
    st.header("複合仕訳入力 (Streamlit版)")

    accounts_list = get_accounts_code_list()
    today = date.today().strftime("%Y-%m-%d")
    entry_date = st.date_input("日付", value=date.today(), key="entry_date")

    # Dynamic entry rows
    for idx, row in enumerate(st.session_state.rows):
        cols = st.columns([2, 2, 2, 2, 3])
        with cols[0]:
            st.selectbox("借方科目 (コード 名称)", options=accounts_list, key=f"debit_account_{idx}",
                         index=accounts_list.index(row["debit_account"]) if row[
                                                                                "debit_account"] in accounts_list else 0)
        with cols[1]:
            st.text_input("借方金額", key=f"debit_amount_{idx}", value=row["debit_amount"])
        with cols[2]:
            st.selectbox("貸方科目 (コード 名称)", options=accounts_list, key=f"credit_account_{idx}",
                         index=accounts_list.index(row["credit_account"]) if row[
                                                                                 "credit_account"] in accounts_list else 0)
        with cols[3]:
            st.text_input("貸方金額", key=f"credit_amount_{idx}", value=row["credit_amount"])
        with cols[4]:
            st.text_input("備考", key=f"note_{idx}", value=row["note"])
            if st.button("削除", key=f"remove_{idx}", help="この行を削除", on_click=remove_row, args=(idx,)):
                st.experimental_rerun()

    # Add row button
    st.button("行を追加", on_click=add_row)

    # Calculate totals
    debit_total = sum(
        int(st.session_state.get(f"debit_amount_{i}", "0") or 0) for i in range(len(st.session_state.rows)))
    credit_total = sum(
        int(st.session_state.get(f"credit_amount_{i}", "0") or 0) for i in range(len(st.session_state.rows)))
    st.write(f"**借方合計**: {debit_total:,}    **貸方合計**: {credit_total:,}")

    # Save button
    if st.button("保存"):
        if debit_total != credit_total:
            st.warning("借方と貸方の合計が一致しません。")
        else:
            # Construct values dict similar to PySimpleGUI version
            values = {f"entry_date": entry_date.strftime("%Y-%m-%d")}
            for i in range(len(st.session_state.rows)):
                values[f"debit_account_id_{i}"] = st.session_state.get(f"debit_account_{i}")
                values[f"debit_amount_{i}"] = st.session_state.get(f"debit_amount_{i}", "")
                values[f"credit_account_id_{i}"] = st.session_state.get(f"credit_account_{i}")
                values[f"credit_amount_{i}"] = st.session_state.get(f"credit_amount_{i}", "")
                values[f"note_{i}"] = st.session_state.get(f"note_{i}", "")

            success = save_compound_journal_entry(values)
            if success:
                st.success("保存が完了しました。")
                # Reset rows
                st.session_state.rows = [
                    {"debit_account": None, "debit_amount": "", "credit_account": None, "credit_amount": "",
                     "note": ""}]
                st.experimental_rerun()
            else:
                st.error("保存中にエラーが発生しました。")


def check_saved_entries():
    st.header("保存済み仕訳確認")
    conn = sqlite3.connect(config.JOURNAL_DATA_FILE)
    entries_df = None
    lines_df = None
    try:
        entries_df = conn.execute("SELECT * FROM journal_entries ORDER BY entry_num").fetchall()
        lines_df = conn.execute("SELECT * FROM journal_lines ORDER BY entry_num, line_num").fetchall()
    finally:
        conn.close()
    st.subheader("journal_entries")
    st.write(entries_df)
    st.subheader("journal_lines")
    st.write(lines_df)


# Page selector
page = st.sidebar.selectbox("機能選択", ["複合仕訳入力", "保存済み仕訳確認"])
if page == "複合仕訳入力":
    input_compound_journal_entry()
else:
    check_saved_entries()
