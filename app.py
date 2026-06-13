import streamlit as st
import pandas as pd

st.set_page_config(page_title="LLM Business Insights")

st.title("📊 LLM Business Insights Dashboard")

df = pd.read_csv("data/sales.csv")

st.subheader("Sales Data")
st.dataframe(df)

total_revenue = df["Revenue"].sum()
avg_revenue = df["Revenue"].mean()

top_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue}")
col2.metric("Average Revenue", f"${avg_revenue:.2f}")
col3.metric("Top Product", top_product)

st.subheader("Revenue by Product")

product_sales = (
    df.groupby("Product")["Revenue"]
    .sum()
)

st.bar_chart(product_sales)

