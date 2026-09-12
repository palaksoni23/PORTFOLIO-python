import base64
import difflib
import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Palak Soni | Full Stack Developer & AI Explorer",
    page_icon="✨",
    layout="wide",
)

ASSETS = Path(__file__).parent / "assets"


@st.cache_data
def load_image_b64(filename: str) -> str:
    with open(ASSETS / filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


PHOTO_B64 = load_image_b64("palak.jpg")

# ============================================================
# GLOBAL STYLE — Obsidian + Aurora Coral palette
# (different from a typical navy/violet portfolio: warm
# coral -> amber gradient on a near-black plum background,
# with indigo used only as a quiet secondary accent)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root{
  --coral:#FF6B6B; --amber:#FFB454; --indigo:#7C7CFF;
  --bg:#0F0A13; --bg2:#160F1C;
  --surface:rgba(255,255,255,0.05); --surface-strong:rgba(255,255,255,0.09);
  --border:rgba(255,255,255,0.10);
  --text:#F4EEF2; --text-dim:#A79BAE; --text-faint:#6C6274;
}

html,body,[class*="css"]{ font-family:'Inter', sans-serif; }
h1,h2,h3,h4,h5{ font-family:'Fraunces', serif !important; font-weight:600 !important; }

#MainMenu, footer, header[data-testid="stHeader"]{ visibility:hidden; height:0; }
.block-container{ padding-top:1rem; max-width:1180px; }

[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(650px 520px at 8% -8%, rgba(255,107,107,0.16), transparent 60%),
    radial-gradient(600px 520px at 100% 10%, rgba(255,180,84,0.10), transparent 60%),
    radial-gradient(500px 460px at 50% 100%, rgba(124,124,255,0.10), transparent 60%),
    var(--bg);
}

/* ---- floating pill nav ---- */
.floatnav{
  position:sticky; top:10px; z-index:50; display:flex; justify-content:center; margin-bottom:18px;
}
.floatnav-inner{
  display:flex; gap:22px; align-items:center; padding:10px 26px; border-radius:100px;
  background:rgba(20,14,24,0.7); border:1px solid var(--border); backdrop-filter:blur(14px);
  font-size:13.5px; color:var(--text-dim); flex-wrap:wrap; justify-content:center;
}
.floatnav-inner a{ color:var(--text-dim); text-decoration:none; transition:.2s; }
.floatnav-inner a:hover{ color:var(--text); }
.floatnav-inner b{ color:var(--text); font-family:'Fraunces',serif; margin-right:6px; }

/* ---- shared bits ---- */
.kicker{
  font-family:'JetBrains Mono',monospace; font-size:12.5px; color:var(--coral);
  display:flex; align-items:center; gap:10px; margin:4px 0 8px 0;
}
.kicker::before{content:''; width:20px; height:1px; background:var(--coral); display:inline-block;}
.grad-text{ background:linear-gradient(100deg,var(--coral),var(--amber)); -webkit-background-clip:text; background-clip:text; color:transparent; }
.sec-title{ font-size:32px; margin:0 0 6px 0; }
.sec-lead{ color:var(--text-dim); font-size:15px; margin-bottom:6px; max-width:560px; }

.pill{
  display:inline-flex; align-items:center; gap:8px; font-family:'JetBrains Mono',monospace; font-size:12.5px;
  border:1px solid var(--border); background:var(--surface); padding:6px 13px; border-radius:100px; color:var(--text-dim);
}
.dot-pulse{width:7px; height:7px; border-radius:50%; background:var(--coral); box-shadow:0 0 8px var(--coral); animation:pulse 2s infinite;}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(255,107,107,.55);}70%{box-shadow:0 0 0 8px rgba(255,107,107,0);}100%{box-shadow:0 0 0 0 rgba(255,107,107,0);}}

.stack-chip{
  font-family:'JetBrains Mono',monospace; font-size:12px; padding:5px 11px; border-radius:8px;
  border:1px solid var(--border); color:var(--text-dim); background:var(--surface); margin:3px 5px 3px 0; display:inline-block;
}

/* ---- hero blob photo ---- */
.blob-wrap{ position:relative; display:flex; justify-content:center; padding:14px; }
.blob-glow{
  position:absolute; inset:0; margin:auto; width:88%; height:88%;
  background:conic-gradient(from 120deg, var(--coral), var(--amber), var(--indigo), var(--coral));
  filter:blur(30px); opacity:.45; animation:spin 14s linear infinite;
}
@keyframes spin{ to{ transform:rotate(360deg); } }
.blob-photo{
  position:relative; width:100%; max-width:300px; aspect-ratio:1/1.05; overflow:hidden;
  border:1px solid var(--border);
  border-radius:42% 58% 63% 37% / 41% 44% 56% 59%;
  animation:blobmorph 10s ease-in-out infinite;
}
@keyframes blobmorph{
  0%,100%{ border-radius:42% 58% 63% 37% / 41% 44% 56% 59%; }
  50%{ border-radius:58% 42% 37% 63% / 55% 60% 40% 45%; }
}
.blob-photo img{ width:100%; height:100%; object-fit:cover; display:block; }

/* ---- buttons ---- */
.btn-row a{
  display:inline-block; font-family:'Inter',sans-serif; font-weight:600; font-size:14px;
  padding:11px 22px; border-radius:100px; margin:4px 8px 4px 0; text-decoration:none; transition:.2s;
}
.btn-primary{ background:linear-gradient(100deg,var(--coral),var(--amber)); color:#160F1C !important; }
.btn-ghost{ border:1px solid var(--border); color:var(--text) !important; }
.btn-primary:hover, .btn-ghost:hover{ transform:translateY(-2px); }

/* ---- scroll reveal + rotate-in (JS toggles .in-view) ---- */
.st-key-hero, .st-key-about, .st-key-skills, .st-key-projects,
.st-key-experience, .st-key-certs, .st-key-contact{
  opacity:0; transform:perspective(1000px) rotateX(10deg) translateY(46px) scale(.97);
  transition:opacity .8s cubic-bezier(.2,.7,.3,1), transform .8s cubic-bezier(.2,.7,.3,1);
}
.st-key-hero.in-view, .st-key-about.in-view, .st-key-skills.in-view, .st-key-projects.in-view,
.st-key-experience.in-view, .st-key-certs.in-view, .st-key-contact.in-view{
  opacity:1; transform:perspective(1000px) rotateX(0) translateY(0) scale(1);
}

/* ---- cards ---- */
.card{
  border:1px solid var(--border); background:var(--surface); border-radius:18px; padding:22px 24px;
  height:100%; transition:.25s;
}
.card:hover{ border-color:var(--coral); transform:translateY(-3px) scale(1.01); }
.card h4{ font-size:16px; margin-bottom:6px; font-family:'Inter',sans-serif !important; font-weight:700 !important;}
.card p{ color:var(--text-dim); font-size:13.5px; margin-bottom:10px; }
.tag-row span{
  font-size:10.5px; color:var(--text-faint); font-family:'JetBrains Mono',monospace;
  border:1px solid var(--border); padding:3px 8px; border-radius:6px; margin:2px 4px 2px 0; display:inline-block;
}
.card-tag{ font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--coral); text-transform:lowercase; }

.featured-card{
  border:1px solid var(--border); border-radius:20px; padding:30px;
  background:linear-gradient(120deg, rgba(255,107,107,0.10), rgba(255,180,84,0.06));
}

/* ---- skill rings ---- */
.ring-grid{ display:flex; flex-wrap:wrap; gap:18px; justify-content:flex-start; }
.ring-item{ width:112px; text-align:center; }
.ring{
  width:88px; height:88px; border-radius:50%; margin:0 auto 8px auto; display:flex; align-items:center; justify-content:center;
  background:conic-gradient(var(--ring-color) calc(var(--pct) * 1%), rgba(255,255,255,0.08) 0);
  position:relative;
}
.ring::before{ content:''; position:absolute; inset:7px; border-radius:50%; background:#150F1C; }
.ring span{ position:relative; z-index:1; font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:600; }
.ring-label{ font-size:12px; color:var(--text-dim); line-height:1.3; }

/* ---- fact row ---- */
.fact-row{ display:flex; justify-content:space-between; padding:12px 0; border-top:1px solid var(--border); font-size:13.5px; }
.fact-row span:first-child{ color:var(--text-faint); font-family:'JetBrains Mono',monospace; font-size:11.5px; }
.fact-row span:last-child{ color:var(--text); text-align:right; }

hr{ border-color:var(--border) !important; margin:2.2rem 0 !important; }
a{ color:var(--amber); }

/* ---- chat banner + bubbles ---- */
.chat-banner{
  border:1px solid var(--border); border-radius:18px; padding:16px 20px; margin-bottom:6px;
  background:var(--surface); display:flex; align-items:center; gap:14px;
}
.chat-banner img{ width:42px; height:42px; border-radius:50%; object-fit:cover; border:1px solid var(--border); }
.chat-banner b{ font-family:'Inter',sans-serif; font-size:15px; }
.chat-banner .sub{ font-size:12.5px; color:var(--coral); display:flex; align-items:center; gap:6px; }

[data-testid="stChatMessage"]{
  background:var(--surface) !important; border:1px solid var(--border) !important; border-radius:14px !important;
}

/* buttons (streamlit native) restyle to match palette */
.stButton>button{
  border-radius:100px !important; border:1px solid var(--border) !important; background:var(--surface) !important;
  color:var(--text) !important; font-size:13px !important;
}
.stButton>button:hover{ border-color:var(--coral) !important; color:var(--coral) !important; }

/* ---- floating chat launcher (bottom-right bubble) ---- */
.st-key-launcher{
  position:fixed !important; bottom:26px; right:26px; z-index:999; width:auto !important;
}
.st-key-launcher .stButton{ position:relative; }
.st-key-launcher .stButton::before{
  content:''; position:absolute; inset:-7px; border-radius:50%; border:1.5px solid var(--coral); opacity:.5;
  animation:launch-ring 2.4s ease-out infinite; pointer-events:none;
}
@keyframes launch-ring{ 0%{transform:scale(.9); opacity:.6;} 100%{transform:scale(1.4); opacity:0;} }
.st-key-launcher .stButton>button{
  width:60px !important; height:60px !important; border-radius:50% !important; border:none !important;
  background:linear-gradient(135deg,var(--coral),var(--amber)) !important; color:#160F1C !important;
  font-size:24px !important; box-shadow:0 10px 30px -6px rgba(255,107,107,.65) !important;
  display:flex !important; align-items:center !important; justify-content:center !important;
  padding:0 !important; transition:transform .2s !important;
}
.st-key-launcher .stButton>button:hover{ transform:scale(1.07) !important; }

/* ---- floating chat panel ---- */
.st-key-chatbox{
  position:fixed !important; bottom:98px; right:26px; z-index:998;
  width:380px !important; max-width:90vw;
  background:linear-gradient(180deg, rgba(24,16,30,0.98), rgba(15,10,19,0.99)) !important;
  border:1px solid var(--border) !important; border-radius:20px !important; padding:16px !important;
  box-shadow:0 30px 70px -20px rgba(0,0,0,.7) !important;
  animation:chatpop .25s cubic-bezier(.2,.8,.3,1) both;
}
@keyframes chatpop{ from{ opacity:0; transform:translateY(16px) scale(.96);} to{ opacity:1; transform:translateY(0) scale(1);} }
.st-key-chatbox [data-testid="stVerticalBlockBorderWrapper"]{ background:transparent !important; }
@media (max-width:480px){
  .st-key-chatbox{ right:12px; left:12px; width:auto !important; bottom:92px; }
  .st-key-launcher{ right:18px; bottom:18px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# small script: reveal-on-scroll with a rotate-in effect, applied to
# Streamlit's key-based section containers (.st-key-*). Streamlit reruns
# the DOM often, so we re-scan on an interval rather than once.
components.html(
    """
<script>
(function(){
  function run(){
    try{
      const doc = window.parent.document;
      const els = doc.querySelectorAll(
        '.st-key-hero,.st-key-about,.st-key-skills,.st-key-projects,.st-key-experience,.st-key-certs,.st-key-contact'
      );
      if(!els.length) return;
      if(!window.__revealIO){
        window.__revealIO = new IntersectionObserver((entries)=>{
          entries.forEach(e=>{
            if(e.isIntersecting){ e.target.classList.add('in-view'); }
          });
        }, {threshold:0.12});
      }
      els.forEach(el=>{
        if(!el.dataset.observed){
          el.dataset.observed = '1';
          window.__revealIO.observe(el);
        }
      });
    }catch(err){}
  }
  setInterval(run, 350);
})();
</script>
""",
    height=0,
)

# ============================================================
# FLOATING NAV
# ============================================================
st.markdown(
    """
<div class="floatnav"><div class="floatnav-inner">
  <b>Palak Soni</b>
  <a href="#hero">Home</a><a href="#about">About</a><a href="#skills">Skills</a>
  <a href="#projects">Projects</a><a href="#experience">Experience</a>
  <a href="#certs">Certifications</a><a href="#contact">Contact</a>
</div></div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================
with st.container(key="hero"):
    st.markdown('<div id="hero"></div>', unsafe_allow_html=True)
    col_l, col_r = st.columns([0.85, 1.15], gap="large")

    with col_l:
        st.markdown(
            f"""
        <div class="blob-wrap">
          <div class="blob-glow"></div>
          <div class="blob-photo">
            <img src="data:image/jpeg;base64,{PHOTO_B64}">
          </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_r:
        st.markdown(
            """
        <span class="pill"><span class="dot-pulse"></span> Based in Alwar, India — open to internships</span>
        <h1 style="font-size:50px; line-height:1.08; margin:18px 0 12px 0;">
          Hello, I'm Palak —<br>I build <span class="grad-text">full‑stack products</span> with AI inside.
        </h1>
        <p style="color:var(--text-dim); font-size:16px; max-width:540px; margin-bottom:18px;">
          B.Tech Computer Science student and full stack developer exploring generative AI, prompt engineering
          and autonomous agents — from React interfaces to multi‑agent Python pipelines.
        </p>
        <div style="margin-bottom:18px;">
          <span class="stack-chip">Python</span><span class="stack-chip">React.js</span>
          <span class="stack-chip">Streamlit</span><span class="stack-chip">Groq LLM</span>
          <span class="stack-chip">Google ADK</span>
        </div>
        <div class="btn-row">
          <a class="btn-primary" href="#projects">View projects</a>
          <a class="btn-ghost" href="#ask-my-assistant">Ask my assistant ↓</a>
        </div>
        <div style="margin-top:16px; font-size:13.5px; color:var(--text-dim);">
          ✉️ palaksoni232006@gmail.com &nbsp;·&nbsp;
          <a href="https://github.com/palaksoni23" target="_blank">GitHub</a> &nbsp;·&nbsp;
          <a href="https://www.linkedin.com/in/palak-soni-235401327" target="_blank">LinkedIn</a>
        </div>
        """,
            unsafe_allow_html=True,
        )

st.write("")

# ============================================================
# ABOUT
# ============================================================
with st.container(key="about"):
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">About</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">Curious by default, careful by habit.</h2>', unsafe_allow_html=True)

    a1, a2 = st.columns([1.3, 1], gap="large")
    with a1:
        st.markdown(
            """
        <p style="color:var(--text-dim); font-size:15.5px; margin-bottom:16px;">
        I'm an aspiring <b style="color:var(--text)">full stack developer and AI enthusiast</b> currently pursuing my
        B.Tech in Computer Science at MITRC, Alwar. I like building things that hold up under real use — responsive
        React interfaces, REST APIs, and lately, multi‑agent AI systems that solve problems that actually matter.
        </p>
        <p style="color:var(--text-dim); font-size:15.5px;">
        Outside coursework, I contribute to open source with <b style="color:var(--text)">GirlScript Summer of Code</b>,
        judge student projects for <b style="color:var(--text)">Technovation Girls</b>, and spend a lot of time
        experimenting with prompt engineering, AI agents, and responsible AI practices.
        </p>
        """,
            unsafe_allow_html=True,
        )
    with a2:
        facts = [
            ("education", "B.Tech CSE, MITRC Alwar · 2024–Present"),
            ("location", "Alwar, Rajasthan, India"),
            ("focus", "Full Stack Development + AI Agents"),
            ("exploring", "Google ADK, Groq LLM, Multi‑Agent Systems"),
            ("email", "palaksoni232006@gmail.com"),
        ]
        rows = "".join(f'<div class="fact-row"><span>{k}</span><span>{v}</span></div>' for k, v in facts)
        st.markdown(f"<div>{rows}</div>", unsafe_allow_html=True)

st.write("")

# ============================================================
# SKILLS — radial progress rings (visually distinct from bars/chips)
# ============================================================
with st.container(key="skills"):
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Skills</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">The stack I build with.</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-lead">Frontend interfaces, backend logic, and the AI tooling that connects them.</p>',
        unsafe_allow_html=True,
    )

    def ring(pct, label, color):
        return f"""
        <div class="ring-item">
          <div class="ring" style="--pct:{pct}; --ring-color:{color};"><span>{pct}%</span></div>
          <div class="ring-label">{label}</div>
        </div>"""

    groups = [
        ("Frontend", "#FF6B6B", [("React.js", 90), ("JavaScript", 88), ("Tailwind CSS", 84), ("HTML/CSS", 92)]),
        ("Backend & Data", "#FFB454", [("Node.js", 80), ("Express.js", 78), ("MongoDB", 76), ("MySQL", 75)]),
        ("AI & Tools", "#7C7CFF", [("Python", 85), ("Streamlit", 88), ("Google ADK", 78), ("Prompt Eng.", 86)]),
    ]
    for title, color, items in groups:
        st.markdown(f'<h4 style="margin:16px 0 4px 0; font-size:15px;">{title}</h4>', unsafe_allow_html=True)
        rings_html = "".join(ring(p, n, color) for n, p in items)
        st.markdown(f'<div class="ring-grid">{rings_html}</div>', unsafe_allow_html=True)

st.write("")

# ============================================================
# PROJECTS
# ============================================================
with st.container(key="projects"):
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Projects</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">Things I\'ve shipped.</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-lead">A mix of AI systems, full‑stack apps, and interface work — all on GitHub.</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="featured-card">
      <span class="card-tag">flagship · multi‑agent ai</span>
      <h3 style="margin:8px 0; font-family:'Inter',sans-serif !important; font-weight:800 !important;">🆘 SaharaNet</h3>
      <p style="color:var(--text-dim); font-size:14.5px; max-width:640px;">
        A multilingual AI emergency response system for India's street children and homeless families, powered by a
        pipeline of six autonomous AI agents with live resource lookups.
      </p>
      <div class="tag-row"><span>Streamlit</span><span>Google ADK</span><span>OpenStreetMap</span><span>Multi‑Agent</span></div>
      <a href="https://github.com/palaksoni23" target="_blank" style="font-size:13px; display:inline-block; margin-top:10px;">View on GitHub →</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.write("")

    projects = [
        ("react · deployment", "Portfolio Website", "A responsive personal portfolio built with reusable React components, deployed on Vercel with an automated pipeline.", ["React.js", "Vercel"]),
        ("rest api · ai", "AI Image Generator", "An AI‑powered image generation app with REST API integration and asynchronous data handling.", ["REST API", "Async JS"]),
        ("healthtech", "LifeLink", "An emergency blood availability lookup platform with user registration and search, built for Cerebro Tech Challenge 2026.", ["Full Stack", "Search"]),
        ("api · weather", "Weather App", "A weather forecasting application with real‑time API data fetching and responsive UI components.", ["REST API", "Responsive UI"]),
        ("state management", "Expense Tracker App", "A responsive expense tracking app with transaction management and real‑time state updates.", ["React.js", "State Mgmt"]),
        ("testing", "Softdef Frontend Test", "A frontend test project focused on expense tracking with transaction management features.", ["React.js", "Testing"]),
    ]

    cols = st.columns(3, gap="medium")
    for i, (tag, title, desc, tech) in enumerate(projects):
        tech_html = "".join(f"<span>{t}</span>" for t in tech)
        with cols[i % 3]:
            st.markdown(
                f"""
            <div class="card" style="margin-bottom:18px;">
              <span class="card-tag">{tag}</span>
              <h4 style="margin-top:6px;">{title}</h4>
              <p>{desc}</p>
              <div class="tag-row">{tech_html}</div>
              <a href="https://github.com/palaksoni23" target="_blank" style="font-size:12.5px;">View on GitHub →</a>
            </div>
            """,
                unsafe_allow_html=True,
            )

st.write("")

# ============================================================
# EXPERIENCE
# ============================================================
with st.container(key="experience"):
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Experience</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">Where I\'ve contributed.</h2>', unsafe_allow_html=True)

    experience = [
        ("GirlScript Summer of Code", "Contributor · Open Source", "Participated in collaborative open‑source projects on GitHub — code improvements, GitHub workflows and issue‑based contributions, with hands‑on version control experience."),
        ("Technovation Girls", "Judge Volunteer · Evaluation", "Evaluated innovative technology projects from global student participants, assessing creativity, technical quality and overall implementation."),
        ("Suvidha Foundation", "Intern · Community & Dev", "Contributed to technical and community‑focused virtual internship projects, assisting with collaborative development and coordination."),
    ]
    for org, role, desc in experience:
        st.markdown(
            f"""
        <div class="fact-row" style="align-items:flex-start;">
          <span style="min-width:190px;">{org}</span>
          <span style="text-align:left; flex:1;">
            <b style="color:var(--text); font-family:'Inter',sans-serif;">{role}</b><br>
            <span style="color:var(--text-dim); font-size:13.5px;">{desc}</span>
          </span>
        </div>
        """,
            unsafe_allow_html=True,
        )

st.write("")

# ============================================================
# CERTIFICATIONS
# ============================================================
with st.container(key="certs"):
    st.markdown('<div id="certs"></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Certifications</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">Always learning something new.</h2>', unsafe_allow_html=True)

    certs = [
        ("Build with AI — Agent Builder Camp", "GeeksforGeeks × Google for Developers"),
        ("Introduction to Artificial Intelligence", "Coursera × Google"),
        ("Web Development using React JS", "Skill Oceans"),
        ("AWS Summit Participation", "AWS"),
        ("Basics of Google Cloud Compute", "Google Cloud"),
        ("Use AI Responsibly", "Coursera × Google"),
        ("Maximum Productivity with AI Tools", "Coursera × Google"),
        ("Discover the Art of Prompting", "Coursera × Google"),
        ("Generative AI Mastermind Workshop", "Outskill · 2026"),
        ("Arcade Base Program", "Google Cloud"),
    ]
    cert_cols = st.columns(5, gap="small")
    for i, (title, org) in enumerate(certs):
        with cert_cols[i % 5]:
            st.markdown(
                f"""
            <div class="card" style="padding:14px 16px; margin-bottom:14px; min-height:96px;">
              <h4 style="font-size:12.5px; line-height:1.35; margin-bottom:6px;">🏅 {title}</h4>
              <span style="font-size:10.5px; color:var(--text-faint); font-family:'JetBrains Mono',monospace;">{org}</span>
            </div>
            """,
                unsafe_allow_html=True,
            )

st.write("")

# ============================================================
# CONTACT — a real working form (opens the visitor's email client
# with everything pre-filled, via a mailto link)
# ============================================================
with st.container(key="contact"):
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Contact</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">Let\'s build something worth shipping.</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-lead">Open to internships, collaborations, and interesting problems — especially where full‑stack meets AI.</p>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([1.1, 0.9], gap="large")
    with c1:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            message = st.text_area("Message", height=120)
            submitted = st.form_submit_button("Prepare message →")
            if submitted:
                if name and email and message:
                    import urllib.parse

                    subject = urllib.parse.quote(f"Portfolio inquiry from {name}")
                    body = urllib.parse.quote(f"{message}\n\n— {name} ({email})")
                    mailto = f"mailto:palaksoni232006@gmail.com?subject={subject}&body={body}"
                    st.success("Ready! Click below to send it from your email app.")
                    st.markdown(
                        f'<a class="btn-primary" style="padding:11px 22px; border-radius:100px;" href="{mailto}">Open email to send →</a>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning("Please fill in your name, email and a message first.")
    with c2:
        st.markdown(
            """
        <div class="btn-row">
          <a class="btn-ghost" href="mailto:palaksoni232006@gmail.com">✉️ palaksoni232006@gmail.com</a><br>
          <a class="btn-ghost" href="https://github.com/palaksoni23" target="_blank">GitHub ↗</a>
          <a class="btn-ghost" href="https://www.linkedin.com/in/palak-soni-235401327" target="_blank">LinkedIn ↗</a>
          <a class="btn-ghost" href="tel:+919649820248">📞 +91 96498 20248</a>
        </div>
        """,
            unsafe_allow_html=True,
        )

st.markdown("<hr/>", unsafe_allow_html=True)

# ============================================================
# CHATBOT — rule based, with fuzzy matching for better "understanding".
# Rendered as a floating launcher bubble (bottom-right) that opens a
# floating panel on click, instead of a big inline section.
# Only answers from Palak's data; a clear fallback for anything else.
# ============================================================
st.markdown('<div id="ask-my-assistant"></div>', unsafe_allow_html=True)

# Each topic: a list of natural phrasings (used for fuzzy matching) + the answer.
KB = [
    (["hi", "hello", "hey", "namaste", "hii", "hlo", "good morning", "good evening"],
     "Hey! 👋 I'm Palak's portfolio assistant. Ask me about her skills, projects, experience, education or how to contact her."),
    (["what is your name", "who are you", "tumhara naam", "who is palak", "tell me about palak"],
     "This is **Palak Soni** — a Full Stack Developer and AI Explorer, currently pursuing B.Tech in Computer Science at MITRC, Alwar."),
    (["what are your skills", "tech stack", "technologies you know", "programming languages", "what can you code", "kya aata hai"],
     "Palak works across the stack: **Frontend** — JavaScript, React.js, HTML5, CSS3, Tailwind CSS. **Backend** — Node.js, Express.js, REST APIs, MySQL, MongoDB. **AI & Tools** — Python, Streamlit, Google ADK, Prompt Engineering, Git, Vercel, Google Cloud."),
    (["what projects have you built", "show me your projects", "tell me about your work", "what have you made"],
     "Her key projects: **SaharaNet** (multilingual AI emergency response, 6‑agent pipeline), **LifeLink** (emergency blood availability app), an **AI Image Generator**, a **Weather App**, an **Expense Tracker**, and this portfolio itself. All on GitHub → github.com/palaksoni23"),
    (["tell me about saharanet", "what is saharanet"],
     "**SaharaNet** is Palak's flagship project — a multilingual AI emergency response system for India's street children and homeless families, built with a pipeline of six autonomous AI agents, Streamlit, OpenStreetMap for live resource lookups, and Google ADK for orchestration."),
    (["tell me about lifelink", "what is lifelink", "blood availability app"],
     "**LifeLink** is an emergency blood availability lookup platform with user registration and search functionality, submitted to the Cerebro Tech Challenge 2026."),
    (["where did you study", "what is your education", "which college", "university degree", "btech mitrc"],
     "Palak is pursuing a **B.Tech in Computer Science & Engineering** at MITRC, Alwar (2024 – Present)."),
    (["what is your experience", "have you done any internship", "work history", "where have you worked"],
     "She's been a **Contributor** at GirlScript Summer of Code, a **Judge Volunteer** at Technovation Girls, and an **Intern** at Suvidha Foundation."),
    (["what certifications do you have", "any courses completed", "certificates"],
     "Some highlights: Build with AI Agent Builder Camp (GeeksforGeeks × Google), Introduction to AI (Coursera × Google), Web Development using React JS, and the Generative AI Mastermind Workshop by Outskill."),
    (["how can i contact you", "what is your email", "phone number", "how to reach you", "connect with you"],
     "You can reach Palak at **palaksoni232006@gmail.com** or +91 96498 20248. She's also on GitHub (palaksoni23) and LinkedIn."),
    (["what is your github", "github profile"], "Here's her GitHub → https://github.com/palaksoni23"),
    (["what is your linkedin", "linkedin profile"], "Here's her LinkedIn → https://www.linkedin.com/in/palak-soni-235401327"),
    (["where are you based", "which city do you live in", "your location"],
     "Palak is based in **Alwar, Rajasthan, India**."),
    (["what do you know about ai", "tell me about your ai work", "prompt engineering experience", "google adk groq"],
     "Palak actively explores Generative AI — prompt engineering, AI agent concepts, responsible AI, and multi‑agent systems using Google ADK and Groq LLM. SaharaNet is her biggest AI project so far."),
    (["are you available for hire", "open to internship", "looking for a job"],
     "Yes — Palak is open to internships and collaborations, especially where full‑stack development meets AI. The best way to reach her is palaksoni232006@gmail.com."),
    (["thank you", "thanks", "shukriya", "dhanyavad"],
     "You're welcome! 😊 Anything else you'd like to know about Palak?"),
    (["bye", "goodbye", "see you", "tata"],
     "Bye! 👋 Feel free to reach out to Palak directly at palaksoni232006@gmail.com."),
]

FALLBACK = (
    "Hmm, that's outside what I know about Palak 🙈 I can only answer questions about her skills, projects, "
    "experience, education and contact details. Try asking one of those, or email her directly at "
    "palaksoni232006@gmail.com."
)


def get_reply(user_text: str) -> str:
    """Score every topic by (a) direct keyword containment and
    (b) fuzzy phrase similarity, so close-but-not-exact phrasing
    still matches — without ever answering from outside the KB."""
    q = user_text.lower().strip()
    if not q:
        return FALLBACK

    best_answer, best_score = None, 0.0
    for phrases, answer in KB:
        for phrase in phrases:
            score = 0.0
            if phrase in q or q in phrase:
                score = 0.6 + 0.4 * (len(phrase) / max(len(q), len(phrase)))
            else:
                score = difflib.SequenceMatcher(None, phrase, q).ratio()
                words_overlap = set(phrase.split()) & set(q.split())
                if words_overlap:
                    score = max(score, 0.45 + 0.1 * len(words_overlap))
            if score > best_score:
                best_score, best_answer = score, answer

    return best_answer if best_score >= 0.42 else FALLBACK


def stream_reply(text: str):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.016)


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! 👋 Ask me anything about Palak's skills, projects, experience or how to reach her."}
    ]
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# --- floating launcher bubble (bottom-right) ---
with st.container(key="launcher"):
    if st.button("💬" if not st.session_state.chat_open else "✕", key="chat_toggle_btn"):
        st.session_state.chat_open = not st.session_state.chat_open

# --- floating panel, only rendered while open ---
if st.session_state.chat_open:
    with st.container(key="chatbox"):
        st.markdown(
            f"""
        <div class="chat-banner" style="margin-bottom:10px;">
          <img src="data:image/jpeg;base64,{PHOTO_B64}">
          <div>
            <b>Palak's Assistant</b><br>
            <span class="sub"><span class="dot-pulse"></span> Answers only from her resume</span>
          </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        suggestion_cols = st.columns(4)
        suggestions = ["Skills", "Projects", "Experience", "Contact"]
        clicked = None
        for c, s in zip(suggestion_cols, suggestions):
            if c.button(s, use_container_width=True, key=f"sugg_{s}"):
                clicked = s

        with st.container(height=280):
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"], avatar="✨" if msg["role"] == "assistant" else "🙋"):
                    st.markdown(msg["content"])

        user_input = st.chat_input("Ask about skills, projects, contact…")
        final_input = clicked or user_input

        if final_input:
            st.session_state.messages.append({"role": "user", "content": final_input})
            reply = get_reply(final_input)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()

st.markdown(
    """
<p style="text-align:center; color:var(--text-faint); font-size:12.5px; margin-top:36px;">
© 2026 Palak Soni · Built with Python + Streamlit
</p>
""",
    unsafe_allow_html=True,
)
