import streamlit as st

from data_loader import load_data
from utils import (
    top10_countries_chart,
    choropleth_chart,
    bubble_chart
)


st.set_page_config(layout="wide")

st.title("📊 Country Analysis")

st.markdown("""
Compare Battery Electric Vehicle (BEV) adoption across leading countries in 2024.
""")

df = load_data()

bev_2024 = df[
    (df["category"] == "Historical") &
    (df["parameter"] == "EV sales") &
    (df["powertrain"] == "BEV") &
    (df["year"] == 2024)
].copy()

exclude = [
    "World",
    "Europe",
    "EU27",
    "Asia Pacific",
    "North America",
    "Central and South America",
    "Rest of the world",
    "Other"
]

bev_2024 = bev_2024[
    ~bev_2024["region_country"].isin(exclude)
]

top_country = bev_2024.loc[
    bev_2024["value"].idxmax(),
    "region_country"
]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Countries",
    bev_2024["region_country"].nunique()
)

col2.metric(
    "Top Market",
    top_country
)

col3.metric(
    "Total BEV Sales",
    f"{bev_2024['value'].sum()/1_000_000:.1f} M"
)

col4.metric(
    "Average Sales",
    f"{bev_2024['value'].mean()/1000:.0f} K"
)

st.markdown("---")

st.subheader("🏆 Top 10 Countries")

st.plotly_chart(
    top10_countries_chart(df),
    use_container_width=True
)

st.markdown("---")

st.subheader("🌍 Global Distribution")

st.plotly_chart(
    choropleth_chart(df),
    use_container_width=True
)

st.markdown("---")

st.subheader("🫧 Sales vs Stock")

st.plotly_chart(
    bubble_chart(df),
    use_container_width=True
)

st.markdown("---")

st.success("""
### Key Insights

- China dominates global BEV sales.
- The United States and Germany remain major EV markets.
- Countries with higher BEV sales also tend to have larger cumulative EV stocks.
""")