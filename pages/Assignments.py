import streamlit as st
import pandas as pd
import base64
from pathlib import Path

st.set_page_config(page_title="Assignments", layout="wide")
st.title("Assignments")

PDF_DIR = Path("file")

def pdf_data_url(pdf_path: Path) -> str | None:
    if not pdf_path.exists():
        return None
    b64 = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")
    return f"data:application/pdf;base64,{b64}"

def link_hw(label: str, filename: str) -> str:
    url = pdf_data_url(PDF_DIR / filename)
    if url:
        return f'<a href="{url}" target="_blank">{label}</a>'
    return label  # fallback if file missing

df = pd.DataFrame([
    {"Assignment": link_hw("HW1", "HW1.pdf"), "Solution": ""},
])

st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)