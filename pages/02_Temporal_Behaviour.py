import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Temporal Behaviour of Aadhaar Updates",
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
updates = pd.read_csv(data_path / "aa_updates_all_states_monthly.csv")

updates["Month-Year"] = pd.to_datetime(updates["Month-Year"])
updates = updates.sort_values("Month-Year")
updates["MoM Change"] = updates["Value"].diff()

# ===============================
# PAGE HEADER (FIXED)
# ===============================
st.markdown("""
<div class="hero-container page-wrap">

<a href="/Update_Dominance" class="page-forward">»</a>

<div class="page-title">
⏳ Temporal Behaviour of Aadhaar Updates
</div>

<div class="page-intro">
This page examines how Aadhaar activity <b>behaves over time</b>
after enrolment saturation.<br/>
We focus purely on <b>monthly update activity</b>,
without drawing conclusions yet.
</div>

</div>
""", unsafe_allow_html=True)


# ===============================
# SECTION 1 — TREND
# ===============================
st.markdown(
    """
    <div class="section-title">Monthly Aadhaar Update Activity</div>
    <div class="section-subtitle">
        Continuous update activity observed across months (All India)
    </div>
    """,
    unsafe_allow_html=True
)

fig_trend = px.area(
    updates,
    x="Month-Year",
    y="Value",
    labels={
        "Month-Year": "Month",
        "Value": "Number of Updates"
    }
)

fig_trend.update_layout(
    height=420,
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(fig_trend, use_container_width=True)

st.caption(
    "Update activity persists every month, indicating Aadhaar functions as an ongoing operational system rather than a completed enrolment exercise."
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ===============================
# SECTION 2 — MOM CHANGE
# ===============================
st.markdown(
    """
    <div class="section-title">Month-over-Month Change in Updates</div>
    <div class="section-subtitle">
        Volatility reveals operational rhythm and external triggers
    </div>
    """,
    unsafe_allow_html=True
)

fig_mom = px.bar(
    updates,
    x="Month-Year",
    y="MoM Change",
    labels={
        "Month-Year": "Month",
        "MoM Change": "Change from Previous Month"
    }
)

fig_mom.update_layout(
    height=380,
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(fig_mom, use_container_width=True)

st.caption(
    "Fluctuations suggest update volumes respond to policy changes, compliance cycles, or service enforcement."
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ===============================
# KEY INSIGHT
# ===============================
st.markdown(
    """
    <div class="insight-box">
        <h4>🔍 Key Temporal Insight</h4>
        <p>
            Aadhaar update activity is <b>continuous, cyclical, and non-random</b>.
            Despite enrolment saturation, sustained monthly updates indicate
            Aadhaar operates as a <b>living digital infrastructure</b>,
            not a static identity registry.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ===============================
# EXIT BRIDGE
# ===============================
st.markdown(
    """
    <div class="page-exit">
        <b>Next:</b> Update Dominance — comparing enrolments vs updates
        to quantify system pressure.
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<a href="/Update_Dominance" class="floating-next">
    &raquo;
</a>
""", unsafe_allow_html=True)