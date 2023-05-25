import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Super Store Dashboard",
    layout = "wide"
)

df = pd.read_csv("superstore.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

st.title("Superstore Dashboard")
st.dataframe(df)

