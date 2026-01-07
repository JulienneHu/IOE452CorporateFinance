import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Syllabus", layout="wide")
st.title("Syllabus")

PDF_PATH = Path("file/IOE452_syllabus.pdf")

if not PDF_PATH.exists():
    st.error(f"Cannot find: {PDF_PATH.resolve()}")
else:
    # Download button
    st.download_button(
        label="Download syllabus PDF",
        data=PDF_PATH.read_bytes(),
        file_name=PDF_PATH.name,
        mime="application/pdf",
    )

    # Embed PDF viewer
    pdf_base64 = base64.b64encode(PDF_PATH.read_bytes()).decode("utf-8")
    pdf_html = f"""
        <iframe
            src="data:application/pdf;base64,{pdf_base64}"
            width="100%"
            height="900"
            style="border: 1px solid #e6e6e6; border-radius: 8px;"
        ></iframe>
    """
    st.markdown(pdf_html, unsafe_allow_html=True)