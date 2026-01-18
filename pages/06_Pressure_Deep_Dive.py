import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Pressure Deep Dive | Aadhaar Data Intelligence",
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
📊 Pressure Deep Dive
</div>

<div class="section-subtitle">
Why a small number of districts dominate Aadhaar update demand
</div>
""", unsafe_allow_html=True)

st.divider()

# ===============================
# LOAD DATA (ANDHRA PRADESH ONLY)
# ===============================
data_path = Path("data")

# ✔ Biometric + Demographic sampled state datasets
bio = pd.read_csv(data_path / "biometric_states" / "andra.csv")
demo = pd.read_csv(data_path / "Demographic_states" / "andra_pradesh.csv")

# ===============================
# AUTO COLUMN DETECTION
# ===============================
bio_cols = [c for c in bio.columns if c.startswith("bio_age")]
demo_cols = [c for c in demo.columns if c.startswith("demo_age")]

# ===============================
# AGGREGATION — DISTRICT LEVEL
# ===============================
bio["Biometric_Updates"] = bio[bio_cols].sum(axis=1)
demo["Demographic_Updates"] = demo[demo_cols].sum(axis=1)

bio_d = bio.groupby("district", as_index=False)["Biometric_Updates"].sum()
demo_d = demo.groupby("district", as_index=False)["Demographic_Updates"].sum()

df = pd.merge(bio_d, demo_d, on="district", how="inner")
df["Total_Updates"] = df["Biometric_Updates"] + df["Demographic_Updates"]

df = df.sort_values("Total_Updates", ascending=False).reset_index(drop=True)

# ===============================
# CONCENTRATION METRICS
# ===============================
total_updates = df["Total_Updates"].sum()
top_20_cutoff = max(1, int(len(df) * 0.2))

top_20_share = (
    df.head(top_20_cutoff)["Total_Updates"].sum() / total_updates * 100
)

bio_ratio = df["Biometric_Updates"].sum() / total_updates * 100
demo_ratio = 100 - bio_ratio

# ===============================
# METRICS
# ===============================
st.markdown('<div class="section-metrics">', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Top 20% Districts Handle",
        f"{top_20_share:.1f}%",
        help="Share of total Aadhaar updates concentrated in top 20% districts"
    )

with c2:
    st.metric(
        "Biometric Update Share",
        f"{bio_ratio:.1f}%"
    )

with c3:
    st.metric(
        "Demographic Update Share",
        f"{demo_ratio:.1f}%"
    )

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# ===============================
# DOMINANCE / CONCENTRATION CURVE
# ===============================
df["Cumulative_Share"] = df["Total_Updates"].cumsum() / total_updates * 100
df["District_Rank"] = df.index + 1

fig = px.line(
    df,
    x="District_Rank",
    y="Cumulative_Share",
    labels={
        "District_Rank": "District Rank (High → Low Pressure)",
        "Cumulative_Share": "Cumulative % of Total Updates"
    }
)

fig.update_layout(
    height=420,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# INSIGHT
# ===============================
st.markdown("""
<div class="insight-box">
<h4>Key Insight</h4>
<p>
A small fraction of districts in Andhra Pradesh accounts for a
<strong>disproportionately large share of Aadhaar update activity</strong>.
<br><br>
This concentration is not random — it reflects structural realities:
population density, urban hubs, migration corridors, and dependency on Aadhaar-linked services.
<br><br>
Uniform, state-wide infrastructure planning ignores these pressure hotspots,
leading to queues, service delays, and operational stress in high-demand districts.
</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# NEXT
# ===============================
st.markdown("""
<div class="section-next">
<b>Next:</b> Predictive Insight — anticipating where Aadhaar update pressure will emerge next.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a href="/Predictive_Insight" class="floating-next">
    &raquo;
</a>
""", unsafe_allow_html=True)
