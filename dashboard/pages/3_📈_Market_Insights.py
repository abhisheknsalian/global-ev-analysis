import streamlit as st

from data_loader import load_data
from utils import (
    treemap_chart,
    heatmap_chart
)

st.set_page_config(layout="wide")

st.title("📈 Market Insights")

st.markdown("""
Explore regional market composition and long-term Battery Electric Vehicle (BEV) adoption trends.
""")

df = load_data()

st.subheader("🌳 Regional Market Share")

st.plotly_chart(
    treemap_chart(df),
    use_container_width=True
)

st.markdown("---")

st.subheader("🔥 Market Growth Heatmap")

st.plotly_chart(
    heatmap_chart(df),
    use_container_width=True
)

st.markdown("---")

st.success("""
### Key Market Insights

- Asia dominates the global BEV market, driven primarily by China.
- Europe remains the second-largest region with strong contributions from Germany, France, and the United Kingdom.
- BEV sales have accelerated significantly across leading markets since 2020.
- Global EV adoption continues to expand, although growth remains concentrated in a relatively small number of countries.
""")