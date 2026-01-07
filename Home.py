import streamlit as st
import pandas as pd

st.set_page_config(page_title="Course Home", layout="wide")

# ---- Edit these ----
COURSE_NAME = "IOE 452: Corporate Finance"
INSTRUCTOR = "Reza Kamaly"

# --------------------

st.title(COURSE_NAME)
st.subheader(f"{INSTRUCTOR}")

st.markdown("---")
st.header("Semester Schedule")

# Schedule table (from your screenshots) + added column: Assignment / Deliverable
schedule = [
    {"Week": 1, "Date": "1/08/25", "Applications": "Introduction to Corporate Finance: Overview", "Session Details": "Lec0", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 1, "Date": "1/13/25", "Applications": "Time Value of Money, PV, FV, etc.\nAnnuities, Perpetuity", "Session Details": "Lec1, Lec2", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 2, "Date": "1/15/25", "Applications": "NPV\nGrowing Perpetuity, Effective Rates", "Session Details": "Lec3", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 2, "Date": "1/20/25", "Applications": "Amortization, Bonds I", "Session Details": "Lec3 (cont.)", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 3, "Date": "1/22/25", "Applications": "Bonds II\nCorporate Bonds, Credit Agencies", "Session Details": "Lec4", "Assignment / Deliverable": "", "Recording": "" },
    {"Week": 3, "Date": "1/27/25", "Applications": "IRR, IRR/PE, Profitability Index", "Session Details": "Lec5", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 4, "Date": "1/29/25", "Applications": "Bond Sensitivities\nDuration, Call/Put Features", "Session Details": "Lec6", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 4, "Date": "2/03/25", "Applications": "Treasury, Repo, Collateral, FED", "Session Details": "Lec6 (cont.)", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 5, "Date": "2/05/25", "Applications": "Spot Rates, Yield Curve\nNo-Arb., Forward Rates, Swaps", "Session Details": "Lec7", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 5, "Date": "2/10/25", "Applications": "Exam I", "Session Details": "", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 6, "Date": "2/12/25", "Applications": "Equity Valuation, Gordon Model, Dividends", "Session Details": "Lec8", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 6, "Date": "2/17/25", "Applications": "DDM, 2-Stage, Financial Statements, Financial Ratios\nCase Study", "Session Details": "Lec9", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 7, "Date": "2/19/25", "Applications": "Basic Probability, Risk–Return\nTwo-Asset Portfolio", "Session Details": "Lec10, Lec11", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 7, "Date": "2/24/25", "Applications": "Efficient Frontier", "Session Details": "Lec12", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 8, "Date": "2/26/25", "Applications": "Markowitz: Mean–Variance Portfolio\nR–Python Data Retrieval, Risk-free Asset", "Session Details": "Lec13, Lec14", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 8, "Date": "3/03/25", "Applications": "Vacation: No Class!", "Session Details": "", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 9, "Date": "3/05/25", "Applications": "Vacation: No Class!", "Session Details": "Lec15", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 9, "Date": "3/10/25", "Applications": "CAPM, Fama–French, Implementation, OLS\nIndex Models", "Session Details": "Lec16", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 10, "Date": "3/12/25", "Applications": "APT, Efficient Markets\nVC & PE", "Session Details": "Lec17", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 10, "Date": "3/17/25", "Applications": "Exam II", "Session Details": "", "Assignment / Deliverable": "", "Recording": ""},
    
    {"Week": 11, "Date": "3/19/25", "Applications": "Credit Risk, Short–Term Financing\nCapital Structure", "Session Details": "Lec18", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 11, "Date": "3/24/25", "Applications": "Cost of Capital, WACC", "Session Details": "Lec19", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 12, "Date": "3/26/25", "Applications": "Modigliani–Miller, Debt v. Equity\nUncertainty, Taxes, Inflation", "Session Details": "Lec20", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 12, "Date": "3/31/25", "Applications": "Case", "Session Details": "Lec21", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 13, "Date": "4/02/25", "Applications": "Corporate Bankruptcy", "Session Details": "Lec22", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 13, "Date": "4/07/25", "Applications": "Share Buybacks", "Session Details": "Lec22 (cont.)", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 14, "Date": "4/09/25", "Applications": "Leverage", "Session Details": "Lec23", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 14, "Date": "4/14/25", "Applications": "Asymmetric Information\nDebt financing choices", "Session Details": "Lec24", "Assignment / Deliverable": "", "Recording": ""},

    {"Week": 15, "Date": "4/16/25", "Applications": "Securitization, MBS", "Session Details": "Lec25", "Assignment / Deliverable": "", "Recording": ""},
    {"Week": 15, "Date": "4/21/25", "Applications": "Exam III\nCase Study Due", "Session Details": "Lec26", "Assignment / Deliverable": "", "Recording": ""},
]

import base64
from pathlib import Path

# ---- Build df (keep Week as a normal column) ----
df_show = pd.DataFrame(schedule)

# optional: sort by week then date if you want
# df_show = df_show.sort_values(["Week", "Date"], kind="stable")

# Convert line breaks for Applications
df_show["Applications"] = df_show["Applications"].str.replace("\n", "<br>", regex=False)

# ---- helper: make file links that work in HTML (data URL) ----
PDF_DIR = Path("file")   # your folder name in the screenshot: IOE452/file/...

def pdf_data_url(pdf_path: Path) -> str | None:
    if not pdf_path.exists():
        return None
    b64 = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")
    return f"data:application/pdf;base64,{b64}"

LEC_PDF = {
    "Lec0": PDF_DIR / "Lecture0_01082026.pdf",
    "Lec1": PDF_DIR / "Lecture1_01082026.pdf",
    "Lec2": PDF_DIR / "Lecture2_01132026.pdf",
}

def linkify_sessions(s: str) -> str:
    if not isinstance(s, str) or not s.strip():
        return ""
    parts = [p.strip() for p in s.split(",")]
    out = []
    for p in parts:
        if p in LEC_PDF:
            url = pdf_data_url(LEC_PDF[p])
            if url:
                out.append(f'<a href="{url}" target="_blank">{p}</a>')
            else:
                out.append(p)
        else:
            out.append(p)
    return ", ".join(out)

df_show["Session Details"] = df_show["Session Details"].apply(linkify_sessions)

# ---- highlight rows ----
def highlight_rows(row):
    text = str(row["Applications"]).lower()
    if "exam" in text:
        return ["background-color: #fff3cd"] * len(row)
    if "vacation" in text or "no class" in text:
        return ["background-color: #e2f0d9"] * len(row)
    return [""] * len(row)

# ---- style + render as HTML ----
styled = (
    df_show.style
    .apply(highlight_rows, axis=1)
    .set_table_styles([
        {"selector": "th", "props": [("font-size", "18px"), ("text-align", "left"), ("padding", "10px")]},
        {"selector": "td", "props": [("font-size", "16px"), ("padding", "10px"), ("vertical-align", "top"),
                                     ("white-space", "normal"), ("line-height", "1.4")]},
        {"selector": "table", "props": [("width", "100%"), ("border-collapse", "collapse")]},
        {"selector": "td, th", "props": [("border", "1px solid #e6e6e6")]},
    ])
)

styled = styled.hide(axis="index")   # pandas >= 1.4
st.markdown(styled.to_html(escape=False), unsafe_allow_html=True)
