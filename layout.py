# layout.py

import streamlit as st
import os
import config

def set_page_config_once(page_title="会計ソフト", layout="wide", icon="💼"):
    if not hasattr(st.session_state, "_page_configured"):
        st.set_page_config(page_title=page_title, layout=layout, page_icon=icon)
        st.session_state._page_configured = True


def render_layout(page_title, content_function):
    """
    全画面共通のヘッダー・フッターを自動表示し、
    中身だけを content_function に渡して表示する。
    """
    set_page_config_once(page_title=page_title)

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

    # 中身（各ページ固有のUI）
    content_function()

    # フッター
    st.markdown("---")
    st.markdown("© 2025 Your Company Name")


# 軽量レイアウト
def render_login_layout(title, content_function):
    set_page_config_once(page_title="会計ソフト", layout="centered", icon="🔒")

    # ロゴとタイトルだけのシンプルなヘッダー
    col_logo, col_title, _ = st.columns([1, 3, 1])
    with col_logo:
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)
    with col_title:
        st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)

    st.markdown("---")

    # 中身（ログインフォームなど）
    content_function()

    st.markdown("---")
    st.markdown("© 2025 Your Company Name")

