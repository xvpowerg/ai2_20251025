import streamlit as st
from datetime import datetime
st.title("選擇元素範例")
option_selectbox = st.selectbox(
    '你喜歡的顏色是什麼?',
    ["紅","綠","藍"]
)
st.write(f"你選擇的顏色是{option_selectbox}")
option_mult = st.multiselect(
    "你喜歡的水果:",
    ["香蕉","蘋果","橘子"],
)
st.write("你選了:",option_mult)

option_radio = st.radio("喜歡的季節?",["春","夏","秋","冬"])
st.write(f"你選擇的季節是{option_radio}")

optData = list(map(str,list(range(1,11))) ) 
select_slider = st.select_slider("請選一個範圍:",options=optData,value=("1","6"))
st.write(f"你選擇的數字是{select_slider}")

agree_checkbox = st.checkbox("是否同意")
if agree_checkbox:
    st.write("同意")
else:
    st.write("不同意")

value_slider = st.slider("請選一個範圍:",0.0,100.0,(25.0,75.0))
st.write(f"你選擇的數字是{value_slider}")

date_input = st.date_input("選一個日期:",datetime.today().date())
st.write(f"你選擇的日期是{date_input}")