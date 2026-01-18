import streamlit as st
from pathlib import Path

st.set_page_config(
page_title="Governance Implications | Aadhaar Data Intelligence",
layout="wide"
)

base_css=Path("styles/base.css").read_text(encoding="utf-8")
section_css=Path("styles/section5.css").read_text(encoding="utf-8")

st.markdown(f"<style>{base_css}</style>",unsafe_allow_html=True)
st.markdown(f"<style>{section_css}</style>",unsafe_allow_html=True)

st.markdown("""
<div class="gov-hero">
<h1>🏛️ Governance Implications</h1>
<p>
How can Aadhaar update signals be transformed into
<b>preventive governance controls</b>
instead of reactive administration?
</p>
</div>
""",unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="gov-section">
<h2>Why Governance Response Is Necessary</h2>
<p>
Aadhaar update activity represents
<b>continuous citizen interaction</b>
with the state.
</p>
<p>
Ignoring this signal leads to
reactive staffing, delayed services,
and stress accumulation.
</p>
<p>
Using it enables
<b>anticipatory governance</b> —
acting before overload becomes visible.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Governance Response Framework</h2>
<ol>
<li>Detect sustained update pressure early</li>
<li>Validate pressure using multiple data sources</li>
<li>Apply targeted administrative controls</li>
<li>Maintain transparency and citizen trust</li>
</ol>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Global Digital Identity Practices</h2>

<div class="gov-grid">

<div class="gov-card">
<h3>Estonia – Transparent Identity Logs</h3>
<p>
Citizens can see
<b>who accessed or modified</b>
their identity data.
</p>
<p class="muted">
Deters misuse through visibility.
</p>
</div>

<div class="gov-card">
<h3>Singapore – Multi-Database Validation</h3>
<p>
Identity changes validated across
<b>multiple government systems</b>.
</p>
<p class="muted">
Reduces single-point failure.
</p>
</div>

<div class="gov-card">
<h3>Poland – Trusted Digital Channels</h3>
<p>
Updates allowed only via
<b>verified digital platforms</b>.
</p>
<p class="muted">
Limits fraudulent access paths.
</p>
</div>

</div>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>Proposed Aadhaar Governance Controls</h2>

<div class="gov-grid">

<div class="gov-card">
<h3>1️⃣ Transparent Update Ledger</h3>
<p>
Every Aadhaar update generates a
<b>citizen-visible audit record</b>.
</p>
<p>
Includes time, channel, and approving authority.
</p>
</div>

<div class="gov-card">
<h3>2️⃣ Multi-Source Address Verification</h3>
<p>
Address updates require
<b>two independent confirmations</b>.
</p>
<p>
Utility records, municipal data, or bank KYC.
</p>
</div>

<div class="gov-card">
<h3>3️⃣ Risk-Based Update Rules</h3>
<p>
High-frequency updates trigger
<b>additional verification layers</b>.
</p>
<p>
Low-risk updates remain friction-light.
</p>
</div>

<div class="gov-card">
<h3>4️⃣ Geo-Temporal Validation</h3>
<p>
Update requests evaluated using
<b>location consistency and timing</b>.
</p>
<p>
Reduces remote or mass misuse.
</p>
</div>

</div>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section">
<h2>How This Changes Governance</h2>
<ul>
<li>Moves administration from reactive to preventive</li>
<li>Enables targeted staffing and infrastructure planning</li>
<li>Reduces identity misuse without increasing friction</li>
<li>Strengthens trust through transparency</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="final-insight">
<h2>Core Governance Insight</h2>
<p>
Aadhaar update data is not merely operational metadata.
</p>
<p>
When combined with
<b>global identity control principles</b>,
it becomes a powerful instrument for
<b>anticipatory, citizen-centric governance</b>.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="section-next">
<b>Next:</b>
Page 9 — Final Conclusions, Limitations & Future Scope
</div>
""",unsafe_allow_html=True)

if st.button("»", key="next_page"):
    st.switch_page("pages/09_Conclusion_Limitations.py")