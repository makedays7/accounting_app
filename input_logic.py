# input_logic.py

import streamlit as st
from db_operations import save_compound_journal_entry
from datetime import date

def get_empty_row():
    return {"debit_account": None, "debit_amount": "", "credit_account": None, "credit_amount": "", "note": ""}

def init_rows():
    if "rows" not in st.session_state:
        st.session_state.rows = [get_empty_row() for _ in range(2)]

def add_row():
    st.session_state.rows.append(get_empty_row())

def remove_row(index):
    st.session_state.rows.pop(index)

def calculate_totals():
    debit_total = sum(
        int(st.session_state.get(f"debit_amount_{i}", "0") or 0)
        for i in range(len(st.session_state.rows))
    )
    credit_total = sum(
        int(st.session_state.get(f"credit_amount_{i}", "0") or 0)
        for i in range(len(st.session_state.rows))
    )
    return debit_total, credit_total

def collect_values(entry_date):
    values = {"entry_date": entry_date.strftime("%Y-%m-%d")}
    for i in range(len(st.session_state.rows)):
        values[f"debit_account_id_{i}"] = st.session_state.get(f"debit_account_{i}")
        values[f"debit_amount_{i}"] = st.session_state.get(f"debit_amount_{i}", "")
        values[f"credit_account_id_{i}"] = st.session_state.get(f"credit_account_{i}")
        values[f"credit_amount_{i}"] = st.session_state.get(f"credit_amount_{i}", "")
        values[f"note_{i}"] = st.session_state.get(f"note_{i}", "")
    return values

def save_entries(values):
    return save_compound_journal_entry(values)
