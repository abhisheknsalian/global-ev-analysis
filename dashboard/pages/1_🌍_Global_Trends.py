import streamlit as st

from data_loader import load_data
from utils import global_sales_chart, global_stock_chart

st.set_page_config(layout="wide")

st.title("🌍 Global Trends")

st.markdown("""
Explore the historical growth of electric vehicles worldwide using the
IEA Global EV Outlook 2025 dataset.
""")

df = load_data()

# Chart 1
st.plotly_chart(
    global_sales_chart(df),
    use_container_width=True
)

# Chart 2
st.plotly_chart(
    global_stock_chart(df),
    use_container_width=True
)

st.subheader("Key Insights")

st.success("""
• Global EV sales accelerated rapidly after 2020.

• Battery Electric Vehicles (BEVs) consistently outsold Plug-in Hybrid Electric Vehicles (PHEVs).

• Global EV stock has grown exponentially, indicating sustained adoption of electric mobility worldwide.
""")