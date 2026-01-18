import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Update Dominance | Aadhaar Data Intelligence",
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
# PAGE HEADER (SECTION2 STYLE)
# ===============================
st.markdown("""
<div class="section-title-main">
🔄 Update Dominance
</div>

<div class="section-subtitle">
This page compares <b>new Aadhaar enrolments</b> with <b>update activity</b>
to quantify system pressure after enrolment saturation.
</div>
""", unsafe_allow_html=True)

st.divider()

# ===============================
# LOAD DATA
# ===============================
data_path = Path("data")

updates_df = pd.read_csv(data_path / "aa_updates_all_states_monthly.csv")
enrol_df = pd.read_csv(data_path / "AllStates_MonthWise (2).csv")

# ===============================
# PARSE DATES (ROBUST & SAFE)
# ===============================
updates_df["Month"] = pd.to_datetime(
    updates_df["Month-Year"],
    errors="coerce"
)

enrol_df["Month"] = pd.to_datetime(
    enrol_df["Period"],
    errors="coerce"
)

updates_df = updates_df.dropna(subset=["Month"])
enrol_df = enrol_df.dropna(subset=["Month"])

# ===============================
# STANDARDIZE COLUMNS
# ===============================
updates_df = updates_df.rename(columns={"Value": "Updates"})
enrol_df = enrol_df.rename(columns={"Month Values": "Enrolments"})

# ===============================
# MERGE DATA
# ===============================
df = pd.merge(
    enrol_df[["Month", "Enrolments"]],
    updates_df[["Month", "Updates"]],
    on="Month",
    how="inner"
)

df = df.sort_values("Month")
df["Update_to_Enrolment_Ratio"] = df["Updates"] / df["Enrolments"]

# ===============================
# METRICS
# ===============================
st.markdown('<div class="section-metrics">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Avg Monthly Enrolments", f"{int(df['Enrolments'].mean()):,}")

with col2:
    st.metric("Avg Monthly Updates", f"{int(df['Updates'].mean()):,}")

with col3:
    st.metric(
        "Update / Enrolment Ratio",
        f"{df['Update_to_Enrolment_Ratio'].mean():.1f}×"
    )

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ===============================
# CHART 1 — ENROLMENTS VS UPDATES
# ===============================
st.markdown("""
<div class="chart-title">Enrolments vs Updates (Monthly)</div>
<div class="chart-subtitle">
Update volumes consistently outweigh new Aadhaar creation
</div>
""", unsafe_allow_html=True)

fig1 = px.line(
    df,
    x="Month",
    y=["Enrolments", "Updates"],
    labels={"value": "Count", "variable": "Activity Type"}
)

fig1.update_layout(legend_title_text="", height=420)
st.plotly_chart(fig1, use_container_width=True)

# ===============================
# CHART 2 — UPDATE DOMINANCE RATIO
# ===============================
st.markdown("""
<div class="chart-title">Update Dominance Ratio</div>
<div class="chart-subtitle">
Number of updates processed for every new Aadhaar enrolment
</div>
""", unsafe_allow_html=True)

fig2 = px.bar(
    df,
    x="Month",
    y="Update_to_Enrolment_Ratio",
    labels={"Update_to_Enrolment_Ratio": "Updates per Enrolment"}
)

fig2.update_layout(height=380)
st.plotly_chart(fig2, use_container_width=True)

# ===============================
# INSIGHT BOX
# ===============================
st.markdown("""
<div class="insight-box">
    <h4>Key Insight</h4>
    <p>
    Aadhaar updates consistently exceed new enrolments by a large margin.
    Even after enrolment saturation, the system processes
    <b>multiple updates per new enrolment</b>,
    confirming Aadhaar operates as a high-load,
    living digital infrastructure rather than a one-time registry.
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# NEXT SECTION (TEXT)
# ===============================
st.markdown("""
<div class="section-next">
<b>Next:</b> Living Identity — why individuals repeatedly update Aadhaar data over time.
</div>
""", unsafe_allow_html=True)

# ===============================
# 🔥 FLOATING FORWARD BUTTON (ADDED)
# ===============================
st.markdown("""
<a href="/Living_Identity" class="floating-next">
    &raquo;
</a>
""", unsafe_allow_html=True)
