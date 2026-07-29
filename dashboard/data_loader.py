import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    file_path = "data/EV_Data_Explorer2025.xlsx"

    df = pd.read_excel(
        file_path,
        sheet_name="GEVO_EV_2025"
    )

    return df