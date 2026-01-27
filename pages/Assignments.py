import streamlit as st
import pandas as pd

st.set_page_config(page_title="Assignments", layout="wide")
st.title("Assignments")

PAGES_BASE = "https://JulienneHu.github.io/IOE452CorporateFinance"

def link_url(label: str, url: str) -> str:
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'

df = pd.DataFrame([
    {"Assignment": link_url("HW1", f"{PAGES_BASE}/file/HW1.pdf"), "Solution": ""},
    {"Assignment": link_url("HW2", f"{PAGES_BASE}/file/HW2.pdf"), "Solution": ""},
])

st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)