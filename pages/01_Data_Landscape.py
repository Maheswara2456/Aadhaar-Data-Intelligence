import streamlit as st
import pandas as pd
from pathlib import Path

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Aadhaar Data Landscape",
    layout="wide"
)

# ===============================
# LOAD CSS
# ===============================
base_css = Path("styles/base.css").read_text(encoding="utf-8")
page_css = Path("styles/page.css").read_text(encoding="utf-8")

st.markdown(f"<style>{base_css}</style>", unsafe_allow_html=True)
st.markdown(f"<style>{page_css}</style>", unsafe_allow_html=True)

# ===============================
# LOAD DATA
# ===============================
data_path = Path("data")

aadhaar_gen = pd.read_csv(data_path / "aa_generation_all_states_monthly.csv")
population = pd.read_csv(data_path / "state_population.csv")

aadhaar_gen["req_month"] = pd.to_datetime(aadhaar_gen["req_month"])

latest_total_aadhaar = aadhaar_gen["cumulative"].iloc[-1]
total_population = population["Population_2024"].sum()
coverage_pct = (latest_total_aadhaar / total_population) * 100

# ===============================
# MAIN CONTENT
# ===============================
html = f"""
<div class="hero-container page-wrap">

<!-- FLOAT NAV -->
<a href="/Temporal_Behaviour" class="page-forward">»</a>

<!-- PAGE TITLE -->
<div class="page-title">
  Aadhaar Data Landscape
</div>

<!-- INTRO / BRIDGE -->
<div class="page-intro">
  To examine Aadhaar as a <b>living digital identity</b>, we first establish
  the <b>scale, coverage, and continuity</b> of the data that records its
  nationwide operation.
</div>

<!-- METRICS -->
<div class="metrics-row">

  <div class="metric-card">
    <h4>Total Aadhaar Generated</h4>
    <p>{latest_total_aadhaar:,}</p>
  </div>

  <div class="metric-card">
    <h4>India Population (2024)</h4>
    <p>{total_population:,}</p>
  </div>

  <div class="metric-card">
    <h4>Coverage Level</h4>
    <p>{coverage_pct:.2f}%</p>
  </div>

</div>

<!-- COVERAGE NOTE -->
<div class="page-note">
  Coverage exceeding 100% reflects demographic churn, re-issuance,
  and legacy enrolment effects within the Aadhaar system.
</div>

<!-- SECTION DIVIDER -->
<div class="section-divider"></div>

<!-- CHART TITLE -->
<div class="section-title">
  Aadhaar Growth Over Time
</div>
"""

st.markdown(html, unsafe_allow_html=True)

# ===============================
# CHART
# ===============================
st.line_chart(
    aadhaar_gen.set_index("req_month")["cumulative"],
    height=340
)

st.caption("Cumulative Aadhaar generation at the national level")

# ===============================
# EXIT BRIDGE
# ===============================
st.markdown(
    """
    <div class="page-exit">
      With the data landscape established, we now examine how Aadhaar activity
      <b>behaves over time</b> — focusing on monthly variation and operational
      rhythms.
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<a href="/Temporal_Behaviour" class="floating-next">
    &raquo;
</a>
""", unsafe_allow_html=True)