import streamlit as st
from pathlib import Path
import base64

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Aadhaar Data Intelligence",
    layout="wide"
)

# ===============================
# LOAD CSS
# ===============================
css = Path("styles/base.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# ===============================
# SIDEBAR TOP BRAND (SAFE)
# ===============================
with st.sidebar:
    st.markdown("""
    <div style="
        font-size:18px;
        font-weight:900;
        margin-bottom:8px;
        background:linear-gradient(90deg,#ec85a0,#f5e6b8);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    ">
        StartUrs
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<hr style='border:0;border-top:1px solid rgba(255,255,255,0.25);margin-bottom:6px;'>",
        unsafe_allow_html=True
    )

# ===============================
# IMAGE LOADER (STREAMLIT SAFE)
# ===============================
def img_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# Load images (ALL BASE64)
img1 = img_to_base64("assets/story1.png")
img2 = img_to_base64("assets/story2.png")
img3 = img_to_base64("assets/story3.png")
mbu_logo = img_to_base64("assets/mbulogo.png")

# ===============================
# MAIN CONTENT (UNCHANGED)
# ===============================
html = f"""
<div class="hero-container">

<a href="/Data_Landscape" class="page-forward">»</a>

<div class="info-grid">

  <div class="info-left">
    <img src="data:image/png;base64,{mbu_logo}" class="college-logo">
    <div class="info-strong">StartUrs</div>
    <div class="info-muted">Mohan Babu University</div>
  </div>

  <div class="info-center-title">
    Aadhaar Data Intelligence
  </div>

  <div class="info-right">
    <a href="https://github.com/Maheswara2456/Aadhaar-Data-Intelligence" target="_blank">GitHub Repository</a>
    <a href="#" target="_blank">Project Documentation</a>
  </div>

</div>

<div class="thesis-block">
  <h3>Aadhaar as a Living Digital Identity</h3>
</div>

<div class="paragraph-block">
  <p>
    <b>Aadhaar update behavior</b> reveals how identity systems evolve under
    population mobility, service enforcement, and policy pressure —
    making updates a powerful governance intelligence signal.
  </p>
</div>

<div class="grid-2">

  <div class="hero-card">
    <h4>The Problem</h4>
    <p>
      Aadhaar enrolments are nearing saturation across India.
      Yet update volumes continue to grow —
      often exceeding new enrolments by <b>10× or more</b>.
    </p>
  </div>

  <div class="hero-card">
    <h4>The Core Question</h4>
    <p>
      Why does Aadhaar continue to generate massive and sustained
      update activity long after enrolment saturation?
    </p>
  </div>

</div>

<div class="story-row">

  <div class="story-box">
    <div class="story-img-wrap">
      <img src="data:image/png;base64,{img1}" class="story-img">
      <div class="story-overlay">
        <h5>Rural Mobile Enrolment Surges</h5>
        <p>Field-driven updates & access expansion</p>
      </div>
    </div>
  </div>

  <div class="story-box">
    <div class="story-img-wrap">
      <img src="data:image/png;base64,{img2}" class="story-img">
      <div class="story-overlay">
        <h5>Urban Name Update Requests</h5>
        <p>Identity corrections & service compliance</p>
      </div>
    </div>
  </div>

  <div class="story-box">
    <div class="story-img-wrap">
      <img src="data:image/png;base64,{img3}" class="story-img">
      <div class="story-overlay">
        <h5>Age & Demographic Policy Pressure</h5>
        <p>Lifecycle-driven identity changes</p>
      </div>
    </div>
  </div>

</div>

<div class="takeaway-container">

  <a href="/Data_Landscape" class="takeaway-card clickable">
    <h5>System Overview</h5>
    <span>Pages 1–2</span>
  </a>

  <div class="arrow">➜</div>

  <a href="/Update_Dominance" class="takeaway-card clickable">
    <h5>Update Dominance</h5>
    <span>Pages 3–4</span>
  </a>

  <div class="arrow">➜</div>

  <a href="/District_Pressure_AP" class="takeaway-card clickable">
    <h5>Pressure Zones</h5>
    <span>Pages 5–6</span>
  </a>

  <div class="arrow">➜</div>

  <a href="/Predictive_Insight" class="takeaway-card clickable">
    <h5>Governance Signals</h5>
    <span>Pages 7–9</span>
  </a>

</div>

</div>
"""

st.markdown(html, unsafe_allow_html=True)

# ===============================
# SIDEBAR FOOTER (BOTTOM – SAFE)
# ===============================
with st.sidebar:
    st.markdown(
        "<hr style='border:0;border-top:1px solid rgba(255,255,255,0.25);margin-top:12px;'>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="
        font-size:13px;
        font-weight:800;
        color:#f5e6b8;
        margin-top:6px;
    ">
        Aadhaar Hackathon 2026
    </div>

    <div style="
        font-size:12px;
        margin-top:4px;
        color:#93c5fd;
        font-weight:600;
    ">
        Team Code: UIDAI_2279
    </div>
    """, unsafe_allow_html=True)

# ===============================
# FLOATING NEXT
# ===============================
# ===============================
# FLOATING NEXT (STREAMLIT SAFE)
# ===============================
if st.button("»", key="next_page"):
    st.switch_page("pages/01_Data_Landscape.py")

