# app_main.py

import sys, os
import streamlit as st

# ───────────────────────
# 旧プロジェクトへのパスを追加（必要なら）
OLD = os.path.expanduser("~/PycharmProjects/python_learning")
if OLD not in sys.path:
    sys.path.insert(0, OLD)
# ───────────────────────

def render_header():
    st.markdown("## 会計ソフト")

def render_footer():
    st.markdown("---")
    st.markdown("© 2025 Your Company Name")

def main():
    st.set_page_config(page_title="会計ソフト", layout="wide")
    render_header()

    # ─── メニューは「文字列のリスト」に
    menu_items = [
        "基礎情報入力",
        "新年度スタート（前期繰越）",
        "複合仕訳入力",
        "元帳入力",
        "仕訳入力",
        "仕訳表示",
        "複合仕訳更新",
        "複合仕訳パターン登録",
        "複合仕訳パターン表示",
        "元帳パターン登録",
        "元帳パターン表示",
        "仕訳帳表示",
        "試算表表示",
        "試算表PDF出力",
        "経営分析グラフ出力",
        "仕訳データCSV出力",
        "決算書CSV出力",
        "決算書PDF出力",
        "決算書表示",
        "決算整理仕訳入力",
        "年度締め／次期繰越"
    ]

    choice = st.sidebar.selectbox("メインメニュー", menu_items)
    st.sidebar.success(f"▶ {choice} を開いています")

    # ─── 今はスタブで表示
    st.write(f"### 「{choice}」画面（ダミー）")
    st.info("ここに各機能モジュールを呼び出すコードを later に実装します。")

    render_footer()

if __name__ == "__main__":
    main()
