import streamlit as st
import os

# config.py で COMPANY_NAME, FISCAL_YEAR を定義していれば読み込む
import config

def main_screen():
    st.set_page_config(page_title="会計ソフト メイン画面", layout="wide")

    # ヘッダー
    col_logo, col_title, col_user = st.columns([1, 4, 1])
    with col_logo:
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=80)
    with col_title:
        company_name = getattr(config, "COMPANY_NAME", "サンプル会社")
        fiscal_year = getattr(config, "FISCAL_YEAR", "2025/03")
        st.markdown(f"### {company_name}　|　決算期: {fiscal_year}")
    with col_user:
        st.markdown("[ログアウト](#)", unsafe_allow_html=True)

    st.markdown("---")

    # メニューカテゴリ
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
        st.button("パターン登録表示", disabled=True)
    with cat3:
        st.subheader("決算処理")
        st.button("決算書表示", disabled=True)
        st.button("決算締め（次期繰越）", disabled=True)

    st.markdown("---")
    st.markdown("© 2025 Your Company Name")

if __name__ == "__main__":
    main_screen()
