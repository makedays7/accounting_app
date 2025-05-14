# app_main.py
from layout import render_login_layout, render_layout
from input import input_journal_entry, input_compound_journal_entry
import streamlit as st
import os

from setuptools.command.easy_install import easy_install

import config

# ───────────────────────────────────────────
# 画面 1: ログイン画面
# ───────────────────────────────────────────
def login_screen():
    def content():
        col_login, col_signup = st.columns([1, 1])
        with col_login:
            sub_col1, sub_col2, sub_col3 = st.columns([1, 2, 1])
            with sub_col2:
                if st.button("ログイン"):
                    st.session_state.page = "main_menu"
                    return
        with col_signup:
            if st.button("サインアップ（初めての方はこちら）"):
                pass

    render_login_layout("簡単会計 ログイン", content)


# ───────────────────────────────────────────
# 画面 2: メインメニュー画面
# ───────────────────────────────────────────
def main_menu_screen():
    def content():
        cat1, cat2, cat3 = st.columns(3)
        with cat1:
            st.subheader("設定")
            st.button("会社情報入力", disabled=True)
            st.button("勘定科目登録", disabled=True)
            st.button("CSVインポート", disabled=True)
        with cat2:
            st.subheader("期中処理")
            if st.button("仕訳入力"):
                st.session_state.page = "input_journal_entry"
                return
            st.button("元帳表示", disabled=True)
            st.button("パターン登録／表示", disabled=True)
        with cat3:
            st.subheader("決算処理")
            st.button("決算書表示", disabled=True)
            st.button("決算締め（次期繰越）", disabled=True)

    render_login_layout("簡単会計 メインメニュー", content)


# ───────────────────────────────────────────
# アプリ本体：ページ遷移制御
# ───────────────────────────────────────────
def main():
    # 初期ページ設定
    if "page" not in st.session_state:
        st.session_state.page = "login"

    page = st.session_state.page

    # ページ切り替え
    if page == "login":
        login_screen()
    elif page == "main_menu":
        main_menu_screen()
    elif page == "input_journal_entry":
        input_journal_entry()
    elif page == "input_compound_journal_entry":
        input_compound_journal_entry()
    else:
        main_menu_screen()


if __name__ == "__main__":
    main()
