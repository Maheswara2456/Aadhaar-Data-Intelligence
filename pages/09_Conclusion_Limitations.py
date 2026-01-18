import streamlit as st
from pathlib import Path

st.set_page_config(
page_title="Conclusion | Aadhaar Data Intelligence",
layout="wide"
)

base_css=Path("styles/base.css").read_text(encoding="utf-8")
section_css=Path("styles/section6.css").read_text(encoding="utf-8")

st.markdown(f"<style>{base_css}</style>",unsafe_allow_html=True)
st.markdown(f"<style>{section_css}</style>",unsafe_allow_html=True)

st.markdown("""
<div class="gov-hero">
<h1>🎓 Aadhaar Data Intelligence</h1>
<p>
A study on Aadhaar as a <b>Living Digital Infrastructure</b>
</p>
</div>
""",unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="gov-section center">
<h2>📜 Project Completion Statement</h2>
<p>
This project presents an analytical exploration of
<b>Aadhaar update behaviour</b>
to understand how identity systems operate
<b>beyond enrolment saturation</b>.
</p>
<p>
Through temporal, spatial, and governance-focused analysis,
the study demonstrates that Aadhaar functions as a
<b>continuous, service-linked digital infrastructure</b>.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section center">
<h2>🧠 Key Takeaway</h2>
<p>
Aadhaar update data reflects
<b>real-time citizen–state interaction</b>.
</p>
<p>
When interpreted responsibly,
it enables
<b>anticipatory governance</b>,
improving service delivery
without compromising citizen trust.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="gov-section center">
<h2>⚠️ Limitations Acknowledged</h2>
<ul class="simple-list">
<li>Analysis uses aggregated administrative data</li>
<li>Policy context and individual intent are not directly observable</li>
<li>Findings demonstrate methodology, not absolute conclusions</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="final-insight center">
<h2>🚀 Future Direction</h2>
<p>
The framework developed here can be extended through:
</p>
<ul class="simple-list">
<li>Real-time dashboards for administrators</li>
<li>Machine learning–based load forecasting</li>
<li>Integration with mobility and welfare datasets</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="certificate-box">
<h2>🙏 Acknowledgement</h2>
<p>
We sincerely thank the organizers for the opportunity
to explore Aadhaar data through a
<b>governance intelligence lens</b>.
</p>
<p>
This project was developed with
<b>respect for data ethics, privacy, and public trust</b>,
and aims to contribute constructively
to discussions on digital public infrastructure.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="section-next center">
<b>— ---THANK YOU----- —</b>
</div>
""",unsafe_allow_html=True)
