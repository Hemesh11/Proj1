import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Table Viewer")

customers = pd.DataFrame({
    "Customer ID": [f"CUST{i:03d}" for i in range(1, 21)],
    "Age": np.random.randint(18, 60, 20),
    "Purchase Amount": np.random.randint(500, 5000, 20),
    "Gender": np.random.choice(["Male", "Female"], 20)
})

if st.checkbox("Show Customer Table"):
    st.dataframe(customers)

if st.checkbox("Show Basic Summary"):
    st.write(customers.describe(include='all'))