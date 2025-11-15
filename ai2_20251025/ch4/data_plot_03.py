import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("數據視覺化")
data = pd.DataFrame({
    "x":np.arange(1,101),
    "y":np.random.randn(100).cumsum()
    }
)
st.line_chart(data)
st.line_chart(data,x="x",y="y")

fig,ax = plt.subplots()
ax.plot(data.x,data.y,label="Random Data")

st.pyplot(fig)
