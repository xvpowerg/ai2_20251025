import streamlit as st
st.title("Hello Streamlit") 
user_input = st.text_input("請輸入文字")
st.write(f"我的輸入{user_input}")
