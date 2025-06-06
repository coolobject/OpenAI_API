import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

#------------
# Line Chart
#------------
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

#------------
# Bar Chart
#------------
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
st.bar_chart(chart_data)

#------------
# matploutlib
#------------
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)


# Plotly
fig = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))
st.plotly_chart(fig, use_container_width=True)

df = pd.read_csv("Health_Data.csv", encoding='cp949')
st.dataframe(df, use_container_width=False)
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

st.line_chart(df[numeric_cols])  # 또는 y=numeric_cols로 명시