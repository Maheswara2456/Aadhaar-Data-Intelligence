import streamlit as st
from pathlib import Path

st.set_page_config(
page_title="Predictive Insight | Aadhaar Data Intelligence",
layout="wide"
)

base_css=Path("styles/base.css").read_text(encoding="utf-8")
section_css=Path("styles/section4.css").read_text(encoding="utf-8")

st.markdown(f"<style>{base_css}</style>",unsafe_allow_html=True)
st.markdown(f"<style>{section_css}</style>",unsafe_allow_html=True)

st.markdown("""
<div class="gov-hero">
<h1>🔮 Predictive Insight</h1>
<p>
Can Aadhaar update behaviour function as an
<b>early warning signal</b>
for future governance and service delivery stress?
</p>
</div>
""",unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="gov-section">
<h2>Purpose of This Page</h2>
<p>
This page evaluates whether <b>historical Aadhaar update behaviour</b>
contains predictive signal value.
</p>
<p>
The objective is not forecasting outcomes,
but identifying <b>early operational patterns</b>
that appear before visible governance stress.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Data Scope & Method Boundary</h2>

<div class="gov-grid">

<div class="gov-card">
<h3>Geographic Scope</h3>
<p><b>Andhra Pradesh</b> (state-level aggregation)</p>
<p class="muted">
Used strictly as a methodological case study.
</p>
</div>

<div class="gov-card">
<h3>Temporal Scope</h3>
<p><b>12 consecutive months</b></p>
<p class="muted">
Sufficient to test persistence and continuity.
</p>
</div>

<div class="gov-card">
<h3>Metric Used</h3>
<p>Monthly <b>Aadhaar update volumes</b></p>
<p class="muted">
Enrollments excluded to isolate operational load.
</p>
</div>

</div>

<p class="note">
⚠ Findings demonstrate <b>predictive methodology</b>, not national conclusions.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Analytical Framework</h2>
<ol>
<li>Identify whether update activity persists across time</li>
<li>Examine whether high-load periods repeat</li>
<li>Test continuity between early and later periods</li>
<li>Interpret persistence as operational signal, not anomaly</li>
</ol>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Observed Evidence</h2>

<div class="gov-grid">

<div class="gov-card">
<h3>Continuous Activity</h3>
<p>
Update volumes never fall to zero.
</p>
<p>
This confirms Aadhaar operates as a
<b>continuous administrative system</b>,
not a completed enrollment program.
</p>
</div>

<div class="gov-card">
<h3>Non-Random Demand</h3>
<p>
Month-to-month fluctuations exist,
but <b>average load remains consistently high</b>.
</p>
<p>
This indicates systemic demand rather than noise.
</p>
</div>

<div class="gov-card">
<h3>Persistence Over Time</h3>
<p>
Early and later periods show comparable intensity.
</p>
<p>
High-pressure phases tend to <b>repeat</b>, not dissipate.
</p>
</div>

</div>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Why This Has Predictive Value</h2>
<ul>
<li>Aadhaar updates reflect ongoing citizen–state interaction</li>
<li>Persistent load today implies service pressure tomorrow</li>
<li>Historical patterns reveal operational rhythm</li>
<li>Stable repetition enables early administrative preparation</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="limitations">
<h2>What This Analysis Does Not Claim</h2>
<ul>
<li>High update volume does not indicate governance failure</li>
<li>Correlation does not imply causation</li>
<li>State-level behaviour is not national evidence</li>
<li>Update counts alone do not explain motivation</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="final-insight">
<h2>Key Predictive Insight</h2>
<p>
Aadhaar update behaviour is
<b>persistent, structured, and repeatable</b>.
</p>
<p>
When interpreted carefully,
it can serve as an
<b>early governance stress signal</b>,
allowing intervention before visible overload emerges.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="section-next">
<b>Next:</b>
Page 8 — Governance Controls & Global-Inspired Solutions
</div>
""",unsafe_allow_html=True)

if st.button("»", key="next_page"):
    st.switch_page("pages/08_Governance_Implications.py")
