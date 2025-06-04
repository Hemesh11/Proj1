import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard Overview")

sales_data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"] * 5,
    "Sales": np.random.randint(1000, 5000, 20),
    "Profit": np.random.randint(100, 1000, 20),
    "Quarter": [f"Q{q}" for q in [1, 2, 3, 4, 1]] * 4
})

selected_region = st.selectbox("Select Region", sales_data["Region"].unique())
st.dataframe(sales_data[sales_data["Region"] == selected_region])

st.metric("Total Sales", int(sales_data[sales_data.Region == selected_region]["Sales"].sum()))
st.metric("Total Profit", int(sales_data[sales_data.Region == selected_region]["Profit"].sum()))