
import streamlit as st
import pandas as pd

st.title("競輪AI予想ダッシュボード")
st.subheader("📊 最新データ（自動更新）")

df = pd.read_csv("data/latest_data.csv")
st.dataframe(df)
