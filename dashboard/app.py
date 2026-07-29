import streamlit as st
from data_loader import load_data

st.set_page_config(
    page_title="Global EV Analysis Dashboard",
    page_icon="🚗",
    layout="wide"
)

df = load_data()

st.title("🚗 Global EV Analysis Dashboard")

st.markdown("""
### Global Electric Vehicle Adoption (2010–2024)

An interactive dashboard built using the **IEA Global EV Outlook 2025** dataset.
Explore worldwide electric vehicle adoption, country comparisons, and market insights.
""")

st.divider()

# ------------------------
# Executive KPIs
# ------------------------

historical = df[df["category"] == "Historical"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Countries",
        historical["region_country"].nunique()
    )

with col2:
    st.metric(
        "Years",
        f"{historical['year'].min()} - {historical['year'].max()}"
    )

with col3:
    st.metric(
        "Parameters",
        historical["parameter"].nunique()
    )

with col4:
    st.metric(
        "Powertrains",
        historical["powertrain"].nunique()
    )

st.divider()

st.info(
    """
👈 Use the navigation menu on the left to explore:

• Global Trends

• Country Analysis

• Market Insights
"""
)