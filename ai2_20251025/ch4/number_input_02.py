import streamlit as st
st.title("數字輸入")
num1 = st.number_input("請輸入第一個數字",value=0)
num2 = st.number_input("請輸入第二個數字",value=0,max_value=100,min_value=0)
sum_result = num1 + num2
st.write(f"和為{sum_result}")