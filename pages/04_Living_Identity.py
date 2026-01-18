import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Living Identity | Aadhaar Data Intelligence",
    layout="wide"
)

# ===============================
# LOAD CSS
# ===============================
base_css = Path("styles/base.css").read_text(encoding="utf-8")
section_css = Path("styles/section2.css").read_text(encoding="utf-8")

st.markdown(f"<style>{base_css}</style>", unsafe_allow_html=True)
st.markdown(f"<style>{section_css}</style>", unsafe_allow_html=True)

# ===============================
# PAGE HEADER
# ===============================
st.markdown("""
<div class="section-title-main">
🧬 Living Identity
</div>

<div class="section-subtitle">
Why Aadhaar update activity continues even after enrolment saturation —
because identity evolves with human life.
</div>
""", unsafe_allow_html=True)

st.divider()

# ===============================
# LOAD DATA  ✅ (UPDATED TO FINAL DATASETS)
# ===============================
data_path = Path("data")

bio = pd.read_csv(data_path / "biometric_sampled_india.csv")
demo = pd.read_csv(data_path / "demographic_sampled_india.csv")

# ===============================
# DATE PARSING (SAFE)
# ===============================
bio["date"] = pd.to_datetime(bio["date"], errors="coerce", dayfirst=True)
demo["date"] = pd.to_datetime(demo["date"], errors="coerce", dayfirst=True)

bio = bio.dropna(subset=["date"])
demo = demo.dropna(subset=["date"])

# ===============================
# AUTO COLUMN DETECTION
# ===============================
bio_cols = [c for c in bio.columns if c.startswith("bio_age")]
demo_cols = [c for c in demo.columns if c.startswith("demo_age")]

# ===============================
# AGGREGATION (NO HARD CODING)
# ===============================
bio["Biometric_Updates"] = bio[bio_cols].sum(axis=1)
demo["Demographic_Updates"] = demo[demo_cols].sum(axis=1)

bio_monthly = bio.groupby("date", as_index=False)["Biometric_Updates"].sum()
demo_monthly = demo.groupby("date", as_index=False)["Demographic_Updates"].sum()

df = pd.merge(bio_monthly, demo_monthly, on="date", how="inner")
df = df.sort_values("date")

# ===============================
# METRICS
# ===============================
st.markdown('<div class="section-metrics">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Avg Monthly Biometric Updates",
        f"{int(df['Biometric_Updates'].mean()):,}"
    )

with col2:
    st.metric(
        "Avg Monthly Demographic Updates",
        f"{int(df['Demographic_Updates'].mean()):,}"
    )

with col3:
    dominant = (
        "Biometric"
        if df["Biometric_Updates"].mean() > df["Demographic_Updates"].mean()
        else "Demographic"
    )
    st.metric("Dominant Update Type", dominant)

# ✅ SCOPE MICRO-CLARIFICATION (NEW)
st.markdown("""
<div class="chart-subtitle" style="margin-top:6px;">
Metrics represent <b>classified biometric and demographic update categories</b>
from a <b>multi-state sampled national dataset</b>, not total Aadhaar transactions.
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# ===============================
# DATASET TRANSPARENCY
# ===============================
with st.expander("📂 Datasets Used on This Page"):
    st.markdown(f"""
**1️⃣ Biometric Updates**
- File: `biometric_sampled_india.csv`
- States covered: Andhra Pradesh, Telangana, Karnataka, Tamil Nadu,
  Uttar Pradesh, Himachal Pradesh, Arunachal Pradesh
- Columns detected: {", ".join(bio_cols[:4])} …

**2️⃣ Demographic Updates**
- File: `demographic_sampled_india.csv`
- Same multi-state coverage for consistency
- Columns detected: {", ".join(demo_cols[:4])} …
""")

st.divider()

# ===============================
# CHART TITLE
# ===============================
st.markdown("""
<div class="chart-title">
Biometric vs Demographic Updates Over Time
</div>

<div class="chart-subtitle">
Life-driven identity updates observed consistently across states
</div>
""", unsafe_allow_html=True)

# ===============================
# CHART
# ===============================
fig = px.line(
    df,
    x="date",
    y=["Biometric_Updates", "Demographic_Updates"],
    labels={
        "value": "Number of Updates",
        "variable": "Update Type",
        "date": "Month"
    }
)

fig.update_layout(
    legend_title_text="",
    height=420
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# DATA COVERAGE NOTE (CRITICAL)
# ===============================
st.markdown("""
<div class="chart-subtitle" style="margin-top:10px;">
Observed decline after mid-2025 reflects <b>category-wise data availability limits</b>
within public datasets — not a reduction in Aadhaar update activity or adoption.
</div>
""", unsafe_allow_html=True)

# ===============================
# INSIGHT BOX
# ===============================
st.markdown("""
<div class="insight-box">
    <h4>Key Insight</h4>
    <p>
    Aadhaar update activity is driven by <b>natural human life events</b> —
    biometric changes during growth and ageing, and demographic changes due to
    relocation, marriage, and access to services.
    <br><br>
    Even with enrolment saturation, Aadhaar functions as a
    <b>living digital identity system</b>, continuously adapting to citizens’ lives
    rather than remaining a static registry.
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# NEXT CONTEXT
# ===============================
st.markdown("""
<div class="section-next">
<b>Next:</b> District Pressure — where Aadhaar update load concentrates geographically.
</div>
""", unsafe_allow_html=True)

if st.button("»", key="next_page"):
    st.switch_page("pages/01_Data_Landscape.py")