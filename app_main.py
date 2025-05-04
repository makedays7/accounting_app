# app_main.py

import streamlit as st
import os
import config

# ───────────────────────────────────────────
# 画面 1: ログイン画面
# ───────────────────────────────────────────
def login_screen():
    st.set_page_config(page_title="ログイン - 会計ソフト", layout="centered")
    # ヘッダー（ロゴ＋タイトル）
    col_logo, col_title, _ = st.columns([1, 3, 1])
    with col_logo:
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)
    with col_title:
        st.markdown("<h1 style='text-align: center;'>会計ソフト ログイン</h1>", unsafe_allow_html=True)

    st.markdown("---")

    # ログインボタン（押したらメイン画面へ遷移）
    if st.button("ログイン"):
        st.session_state.page = "main_menu"
        return



    # フッター
    st.markdown("---")
    st.markdown("© 2025 Your Company Name")


# ───────────────────────────────────────────
# 画面 2: メインメニュー画面
# ───────────────────────────────────────────
def main_menu_screen():
    st.set_page_config(page_title="メインメニュー - 会計ソフト", layout="wide")

    # ヘッダー
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=80)
    with col2:
        company_name = getattr(config, "COMPANY_NAME", "サンプル会社")
        fiscal_year = getattr(config, "FISCAL_YEAR", "2025/03")
        st.markdown(f"### {company_name}　|　決算期: {fiscal_year}")
    with col3:
        st.markdown("[ログアウト](#)", unsafe_allow_html=True)

    st.markdown("---")

    # ３つのカテゴリーを横並びで表示
    cat1, cat2, cat3 = st.columns(3)
    with cat1:
        st.subheader("設定")
        st.button("会社情報入力", disabled=True)
        st.button("勘定科目登録", disabled=True)
        st.button("CSVインポート", disabled=True)
    with cat2:
        st.subheader("期中処理")
        st.button("仕訳入力", disabled=True)
        st.button("元帳表示", disabled=True)
        st.button("パターン登録／表示", disabled=True)
    with cat3:
        st.subheader("決算処理")
        st.button("決算書表示", disabled=True)
        st.button("決算締め（次期繰越）", disabled=True)

    # フッター
    st.markdown("---")
    st.markdown("© 2025 Your Company Name")


# ───────────────────────────────────────────
# アプリ本体：ページ遷移制御
# ───────────────────────────────────────────
def main():
    # 初期ページ設定
    if "page" not in st.session_state:
        st.session_state.page = "login"

    # ページ切り替え
    if st.session_state.page == "login":
        login_screen()
    else:
        main_menu_screen()


if __name__ == "__main__":
    main()
