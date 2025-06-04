import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Sales Performance Chart")

months = pd.date_range(start='2023-01-01', periods=12, freq='ME')
sales = pd.DataFrame({
    "Month": months,
    "Sales": np.random.randint(2000, 10000, 12)
})

chart = alt.Chart(sales).mark_line(point=True).encode(
    x='Month:T',
    y='Sales:Q',
    tooltip=['Month:T', 'Sales:Q']
).properties(
    title="Monthly Sales Overview",
    width=700,
    height=400
)

st.altair_chart(chart, use_container_width=True)
