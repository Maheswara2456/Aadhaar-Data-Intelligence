import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="District Pressure | Aadhaar Data Intelligence",
    layout="wide"
)

# ===============================
# LOAD CSS
# ===============================
base_css = Path("styles/base.css").read_text(encoding="utf-8")
section_css = Path("styles/section3.css").read_text(encoding="utf-8")

st.markdown(f"<style>{base_css}</style>", unsafe_allow_html=True)
st.markdown(f"<style>{section_css}</style>", unsafe_allow_html=True)

# ===============================
# PAGE HEADER
# ===============================
st.markdown("""
<div class="section-title-main">
📍 District Pressure — Andhra Pradesh
</div>

<div class="section-subtitle">
Where Aadhaar update load concentrates geographically and why it matters for governance
</div>
""", unsafe_allow_html=True)

st.divider()

# ===============================
# LOAD DATA
# ===============================
data_path = Path("data")

bio = pd.read_csv(data_path / "biometric_sampled_india.csv")
demo = pd.read_csv(data_path / "demographic_sampled_india.csv")

# ===============================
# BASIC VALIDATION
# ===============================
required_cols = {"state", "district"}

if not required_cols.issubset(bio.columns) or not required_cols.issubset(demo.columns):
    st.error("Required columns (state, district) missing in dataset.")
    st.stop()

# ===============================
# FILTER ANDHRA PRADESH
# ===============================
bio = bio[bio["state"] == "Andhra Pradesh"]
demo = demo[demo["state"] == "Andhra Pradesh"]

if bio.empty and demo.empty:
    st.warning("No Andhra Pradesh data found in the datasets.")
    st.stop()

# ===============================
# AUTO COLUMN DETECTION
# ===============================
bio_cols = [c for c in bio.columns if c.startswith("bio_age")]
demo_cols = [c for c in demo.columns if c.startswith("demo_age")]

if not bio_cols or not demo_cols:
    st.error("Age-wise update columns not found.")
    st.stop()

bio["Biometric_Updates"] = bio[bio_cols].sum(axis=1)
demo["Demographic_Updates"] = demo[demo_cols].sum(axis=1)

# ===============================
# AGGREGATE BY DISTRICT
# ===============================
bio_dist = (
    bio.groupby("district", as_index=False)["Biometric_Updates"]
    .sum()
)

demo_dist = (
    demo.groupby("district", as_index=False)["Demographic_Updates"]
    .sum()
)

df = (
    pd.merge(bio_dist, demo_dist, on="district", how="outer")
    .fillna(0)
)

df["Total_Updates"] = df["Biometric_Updates"] + df["Demographic_Updates"]
df = df.sort_values("Total_Updates", ascending=False).reset_index(drop=True)

# ===============================
# METRICS
# ===============================
st.markdown('<div class="section-metrics">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Biometric Updates (AP)",
        f"{int(df['Biometric_Updates'].sum()):,}"
    )

with c2:
    st.metric(
        "Total Demographic Updates (AP)",
        f"{int(df['Demographic_Updates'].sum()):,}"
    )

with c3:
    st.metric(
        "Districts Covered",
        df.shape[0]
    )

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# ===============================
# TOP DISTRICTS BAR CHART
# ===============================
top_n = 15
top_df = df.head(top_n)

st.markdown("""
<div class="chart-title">
Top Districts by Aadhaar Update Load
</div>

<div class="chart-subtitle">
A small number of districts handle a disproportionate share of updates
</div>
""", unsafe_allow_html=True)

fig1 = px.bar(
    top_df,
    x="Total_Updates",
    y="district",
    orientation="h",
    color="Total_Updates",
    color_continuous_scale="Blues"
)

fig1.update_layout(
    height=500,
    yaxis_title="District",
    xaxis_title="Total Updates",
    coloraxis_showscale=False
)

st.plotly_chart(fig1, use_container_width=True)
st.divider()

# ===============================
# BIOMETRIC VS DEMOGRAPHIC (DISTRICT)
# ===============================
stack_df = top_df.melt(
    id_vars="district",
    value_vars=["Biometric_Updates", "Demographic_Updates"],
    var_name="Update Type",
    value_name="Count"
)

st.markdown("""
<div class="chart-title">
Biometric vs Demographic Pressure by District
</div>

<div class="chart-subtitle">
Different districts exhibit different identity update dynamics
</div>
""", unsafe_allow_html=True)

fig2 = px.bar(
    stack_df,
    x="Count",
    y="district",
    color="Update Type",
    orientation="h"
)

fig2.update_layout(
    height=500,
    xaxis_title="Number of Updates",
    yaxis_title="District",
    legend_title_text=""
)

st.plotly_chart(fig2, use_container_width=True)

# ===============================
# INSIGHT BOX
# ===============================
st.markdown("""
<div class="insight-box">
    <h4>Key Insight</h4>
    <p>
    Aadhaar update demand in Andhra Pradesh is <b>highly concentrated</b> in a limited
    set of districts. These districts experience sustained pressure due to population density,
    mobility, and service dependency.
    <br><br>
    This highlights the need for <b>district-level planning</b> — including targeted infrastructure,
    staffing, and service capacity — rather than uniform state-wide deployment.
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# NEXT PAGE (STREAMLIT-SAFE)
# ===============================
st.markdown("""
<div class="section-next">
<b>Next:</b> Pressure Deep Dive — why certain districts dominate update demand.
</div>
""", unsafe_allow_html=True)

if st.button("»", key="next_page"):
    st.switch_page("pages/06_Pressure_Deep_Dive.py")
