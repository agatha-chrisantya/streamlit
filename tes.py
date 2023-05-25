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

df["order_year"] = df["order_date"].dt.year
CURR_YEAR = df["order_year"].max()
PREV_YEAR = CURR_YEAR - 1

with mx_sales:
    curr_sales = mx_data.loc[mx_data["order_year"] == CURR_YEAR, "sales"].values[0]
    prev_sales = mx_data.loc[mx_data["order_year"] == PREV_YEAR, "sales"].values[0]
    sales_diff_pct = 100 * (curr_sales - prev_sales) / prev_sales
    st.metric(
        label = "Sales",
        value = curr_sales,
        delta = f"{sales_diff_pct:.2f}"
    )

