import streamlit as st
import pandas as pd

st.set_page_config(page_title="競輪AI予想ダッシュボード", layout="wide")
st.title("📊 競輪AI予想ダッシュボード（ダミー版）")

st.markdown("## 選手別 着順確率／脚質／信頼度")
df = pd.read_csv("data_dummy.csv")
st.dataframe(df)

st.markdown("### 🧠 AI注目コメント（例）")
st.success("選手7は前回上がりタイムが全体平均より0.4秒早く、今回は好連携選手と再び同乗。信頼度は高い。")
