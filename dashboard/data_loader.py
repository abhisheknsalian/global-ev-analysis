from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "data" / "EV_Data_Explorer2025.xlsx"

    df = pd.read_excel(
        file_path,
        sheet_name="GEVO_EV_2025"
    )

    return df