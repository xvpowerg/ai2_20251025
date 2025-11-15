import streamlit as st
import pandas as pd
st.title("CSV檔案讀取")
uplodad_file = st.file_uploader("選一個CSV文件",type="csv")
#print(uplodad_file)
if uplodad_file:
    df = pd.read_csv(uplodad_file)
    st.subheader("CSV檔案內容")
    st.dataframe(df)

    st.subheader("CSV檔案描述")
    st.dataframe(df.describe())

    st.subheader("視覺化")
    st.line_chart(df)

    colum = st.selectbox("選擇顯示的欄位",df.columns)
    st.dataframe(df[[colum]])