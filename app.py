import streamlit as st
from datetime import date, datetime, timedelta, time as time_obj
import sys, os, requests, traceback

sys.path.insert(0, os.path.dirname(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG  (must be first Streamlit call)
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ancient Kashmiri",
    # page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cinzel+Decorative:wght@400;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Noto+Serif+Devanagari:wght@300;400;500&display=swap');

/* ── ROOT PALETTE ── */
:root {
  --saffron:      #D4722A;
  --saffron-lt:   #E8956A;
  --saffron-pale: #FDF0E5;
  --crimson:      #8B1C30;
  --gold:         #B8862A;
  --gold-lt:      #DEB85A;
  --gold-pale:    #FBF5E6;
  --walnut:       #3A2010;
  --walnut-mid:   #6B3A1F;
  --cream:        #FDF8F0;
  --cream2:       #FAF3E8;
  --ink:          #1E0F06;
  --muted:        #7A5F4A;
  --border:       rgba(184,134,42,0.30);
  --teal:         #2A7A6A;
  --lotus:        #C45A7A;
  --shadow:       rgba(58,32,16,0.10);
  --shadow-d:     rgba(58,32,16,0.22);
}

/* ── GLOBAL ── */
html, body, [data-testid="stAppViewContainer"], .stApp {
  background: var(--cream) !important;
  font-family: 'Cormorant Garamond', serif !important;
  color: var(--ink) !important;
}

[data-testid="stAppViewContainer"]::before {
  content: '';
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background:
    radial-gradient(ellipse 700px 500px at 5% 15%, rgba(212,114,42,.05) 0%, transparent 70%),
    radial-gradient(ellipse 600px 600px at 95% 85%, rgba(139,28,48,.04) 0%, transparent 70%),
    url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 2 L33 27 L58 30 L33 33 L30 58 L27 33 L2 30 L27 27Z' fill='%23B8862A' fill-opacity='.03'/%3E%3C/svg%3E");
}

[data-testid="stHeader"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
footer { display: none !important; }
#MainMenu { display: none !important; }

/* ── MAIN PADDING ── */
[data-testid="stMainBlockContainer"] {
  padding: 0 !important;
  max-width: 100% !important;
}
[data-testid="block-container"] {
  padding: 0 !important;
  max-width: 100% !important;
}
.main .block-container {
  padding: 0 2.5rem 4rem !important;
  max-width: 1400px !important;
}
/* Remove ALL top spacing — site-header flush with browser top */
header[data-testid="stHeader"]              { display: none !important; }
.stApp > header                             { display: none !important; }
div[data-testid="stDecoration"]             { display: none !important; }
div[data-testid="stTop"]                    { display: none !important; }
div[data-testid="stStatusWidget"]           { display: none !important; }
div[data-testid="stToolbar"]                { display: none !important; }
div[class*="StatusWidget"]                  { display: none !important; }
#root > div:first-child                     { padding-top: 0 !important; margin-top: 0 !important; }
.stApp                                      { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="stAppViewContainer"]          { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="stAppViewBlockContainer"]     { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="stMainBlockContainer"]        { padding-top: 0 !important; margin-top: 0 !important; }
[data-testid="block-container"]             { padding-top: 0 !important; margin-top: 0 !important; }
.main .block-container                      { padding-top: 0 !important; margin-top: 0 !important; }
div[class*="block-container"]               { padding-top: 0 !important; }
section.main > div                          { padding-top: 0 !important; }
.element-container:first-child             { margin-top: 0 !important; padding-top: 0 !important; }
.site-header                                { margin-top: 0 !important; }
[data-testid="stVerticalBlock"]             { gap: 0 !important; }
[data-testid="stVerticalBlock"] > [data-testid="stElementContainer"]:first-child { margin-top: 0 !important; padding-top: 0 !important; }
[data-testid="stElementContainer"]:first-child { margin-top: 0 !important; padding-top: 0 !important; }

/* ── HEADER ── */
.site-header {
  background: linear-gradient(135deg, #3A2010 0%, #4E2210 45%, #8B1C30 100%);
  padding: 16px 40px 14px;
  position: relative;
  overflow: hidden;
  margin-bottom: 12px;
}
.site-header::before {
  content: '';
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='80' height='80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M40 5C40 5 55 20 55 40 55 60 40 75 40 75 25 60 25 40 25 20 40 5Z' fill='%23DEB85A' fill-opacity='.05'/%3E%3Cpath d='M5 40C5 40 20 25 40 25 60 25 75 40 75 40 60 55 40 55 20 55 5 40Z' fill='%23DEB85A' fill-opacity='.05'/%3E%3C/svg%3E");
  pointer-events: none;
}
.hdr-inner {
  display: flex; align-items: center; justify-content: space-between;
  position: relative; z-index: 1;
}
.hdr-title {
  font-family: 'Cinzel', serif;
  font-size: 26px; font-weight: 500; color: #FDF8F0; letter-spacing: 3px; line-height: 1.1;
}
.hdr-title span { color: #DEB85A; }
.hdr-title-hi {
  font-family: 'Noto Serif Devanagari', serif;
  font-size: 17px; color: rgba(222,184,90,.8); letter-spacing: 1px; margin-top: 2px;
}
.hdr-desc {
  font-size: 10px; color: rgba(253,248,240,.4);
  letter-spacing: 1px; margin-top: 5px; line-height: 1.7; max-width: 540px;
}
.hdr-tagline {
  font-style: italic; font-size: 10px;
  color: rgba(253,248,240,.3); letter-spacing: 1.5px; margin-top: 3px;
}
.hdr-right { text-align: right; }
.hdr-samvat {
  font-family: 'Cinzel', serif;
  font-size: 9px; letter-spacing: 2px; color: rgba(222,184,90,.5); margin-bottom: 1px;
}
.hdr-samvat-num {
  font-family: 'Cinzel', serif;
  font-size: 20px; color: rgba(222,184,90,.85); line-height: 1.1;
}
.hdr-date { font-size: 11px; color: rgba(253,248,240,.45); margin-top: 3px; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
  background: #3A2010 !important;
  border-bottom: 2px solid #B8862A !important;
  gap: 0 !important;
  padding: 0 1.5rem !important;
}
.stTabs [data-baseweb="tab"] {
  font-family: 'Cinzel', serif !important;
  font-size: 10.5px !important;
  letter-spacing: 1.2px !important;
  color: rgba(253,248,240,.55) !important;
  opacity: 1 !important;
  padding: 14px 20px !important;
  border-bottom: 3px solid transparent !important;
  background: transparent !important;
}
.stTabs [aria-selected="true"] {
  color: #DEB85A !important;
  border-bottom-color: #DEB85A !important;
  background: rgba(222,184,90,.06) !important;
}
.stTabs [data-baseweb="tab-panel"] {
  padding: 1.8rem 2rem 4rem !important;
  background: transparent !important;
}

/* Mobile — prevent horizontal overflow */
@media (max-width: 768px) {
  .stTabs [data-baseweb="tab-panel"] {
    padding: 1rem 0.6rem 3rem !important;
  }
  .main .block-container {
    padding: 0 0.5rem 3rem !important;
  }
}

/* ── GLOBAL CONTENT SPACING ── */
/* Breathing room between every Streamlit vertical element inside tabs */
.stTabs [data-baseweb="tab-panel"] [data-testid="stVerticalBlock"] {
  gap: 1rem !important;
}
/* Section headers */
.sec-head { margin-top: 0.2rem !important; margin-bottom: 0.5rem !important; }
.sec-sub  { margin-bottom: 1.4rem !important; padding-bottom: 1rem !important; }
/* Sub-section dividers */
.subsec   { margin: 1.6rem 0 0.9rem !important; padding-bottom: 10px !important; }
/* Styled dividers */
.styled-div { margin: 1.4rem 0 !important; }
/* Muhurta blocks */
.muh-block  { margin-bottom: 10px !important; }
/* Info cards */
.info-card  { padding: 22px 24px !important; }
/* Panchang cells */
.panch-cell { padding: 16px 18px !important; }
/* Lin items (lineage) */
.lin-item   { padding: 14px 0 !important; }
/* Guna rows */
.guna-row   { padding: 10px 16px !important; margin-bottom: 8px !important; }
/* Birthday cards */
.bday-card  { padding: 22px 26px !important; margin-bottom: 16px !important; }
/* Sujhav tab (8th) — distinct border box */
.stTabs [data-baseweb="tab-list"] [data-baseweb="tab"]:nth-child(8) {
  border: 1px solid rgba(184,134,42,.35) !important;
  border-bottom: 3px solid transparent !important;
  border-radius: 6px 6px 0 0 !important;
  margin: 4px 4px 0 !important;
  color: rgba(222,184,90,.75) !important;
  background: rgba(184,134,42,.06) !important;
}
.stTabs [data-baseweb="tab-list"] [data-baseweb="tab"]:nth-child(8)[aria-selected="true"] {
  border-color: #DEB85A !important;
  border-bottom-color: #DEB85A !important;
  color: #DEB85A !important;
  background: rgba(222,184,90,.12) !important;
}

/* ── SECTION HEADERS ── */
.sec-head {
  font-family: 'Cinzel', serif;
  font-size: 20px; font-weight: 500; color: var(--walnut);
  letter-spacing: 2px; margin-bottom: 4px;
  display: flex; align-items: center; gap: 10px;
}
.sec-sub {
  font-style: italic; font-size: 14px; color: var(--muted);
  margin-bottom: 20px; line-height: 1.6;
  border-bottom: 1px solid var(--border); padding-bottom: 14px;
}
.sec-sub .deva {
  font-family: 'Noto Serif Devanagari', serif; display: block; margin-top: 2px;
}
.subsec {
  font-family: 'Cinzel', serif;
  font-size: 11px; letter-spacing: 2px; color: var(--walnut-mid);
  margin: 20px 0 12px; padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: 8px;
}
.subsec .deva { font-family: 'Noto Serif Devanagari', serif; font-size: 12px; color: var(--muted); opacity: .75; }

/* ── PANCH CARDS ── */
.panch-cell {
  background: linear-gradient(135deg, var(--saffron-pale), var(--gold-pale));
  border: 1px solid rgba(212,114,42,.2); border-radius: 10px;
  padding: 14px 16px; text-align: center; position: relative; overflow: hidden;
}
.panch-cell::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 2px; background: linear-gradient(90deg, transparent, var(--saffron), transparent);
}
.pc-lbl {
  font-family: 'Cinzel', serif;
  font-size: 8px; letter-spacing: 2px; color: var(--saffron);
  display: block; margin-bottom: 2px; text-transform: uppercase;
}
.pc-lbl-deva {
  font-family: 'Noto Serif Devanagari', serif;
  font-size: 10px; color: var(--muted); display: block; margin-bottom: 5px; opacity: .8;
}
.pc-val {
  font-size: 15px; font-weight: 500; color: var(--walnut); line-height: 1.3;
}
.pc-val-big {
  font-family: 'Cinzel', serif; font-size: 17px; color: var(--walnut);
}
.pc-sub { font-size: 10px; color: var(--muted); margin-top: 2px; }

/* ── MUHURTA BLOCKS ── */
.muh-block {
  border-radius: 8px; padding: 11px 15px;
  border-left: 3px solid var(--muted); margin-bottom: 8px;
  background: rgba(253,248,240,.5);
}
.muh-block.good  { border-left-color: #4A9A50; background: rgba(74,154,80,.07); }
.muh-block.bad   { border-left-color: #C03030; background: rgba(192,48,48,.06); }
.muh-block.spec  { border-left-color: var(--gold); background: rgba(184,134,42,.08); }
.muh-lbl {
  font-family: 'Cinzel', serif;
  font-size: 9px; letter-spacing: 2px; color: var(--muted);
  margin-bottom: 2px; text-transform: uppercase;
}
.muh-deva { font-family: 'Noto Serif Devanagari', serif; font-size: 11px; color: var(--walnut-mid); opacity: .75; }
.muh-time { font-size: 16px; color: var(--walnut); font-weight: 500; }
.muh-note { font-size: 11px; color: var(--muted); margin-top: 2px; }

/* ── PLANET TABLE ── */
.planet-tbl { width: 100%; border-collapse: collapse; font-size: 14px; }
.planet-tbl th {
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1.5px;
  color: var(--muted); text-transform: uppercase;
  padding: 10px 14px; border-bottom: 1px solid var(--border); text-align: left;
}
.planet-tbl td {
  padding: 9px 14px; border-bottom: 1px solid rgba(212,184,150,.35);
  color: var(--ink); font-size: 14px;
}
.planet-tbl tr:hover td { background: var(--cream2); }
.p-badge {
  display: inline-block; padding: 2px 9px; border-radius: 12px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1px;
}
.p-sun  { background: rgba(212,114,42,.15); color: var(--saffron); }
.p-moon { background: rgba(184,134,42,.15); color: var(--gold); }
.p-mars { background: rgba(192,48,48,.12);  color: #b03030; }
.p-merc { background: rgba(42,122,106,.12); color: var(--teal); }
.p-jup  { background: rgba(139,28,48,.12);  color: var(--crimson); }
.p-ven  { background: rgba(196,90,122,.12); color: var(--lotus); }
.p-sat  { background: rgba(58,32,16,.12);   color: var(--walnut-mid); }
.p-rahu { background: rgba(30,15,6,.08);    color: #555; }
.p-ketu { background: rgba(100,60,20,.1);   color: #885522; }

/* ── INFO CARDS ── */
.info-card {
  background: white; border: 1px solid var(--border); border-radius: 14px;
  padding: 20px 22px; box-shadow: 0 2px 10px var(--shadow);
  transition: transform .2s, box-shadow .2s; height: 100%;
}
.info-card:hover { transform: translateY(-3px); box-shadow: 0 6px 22px var(--shadow-d); }
.ic-icon { font-size: 24px; margin-bottom: 8px; }
.ic-title {
  font-family: 'Cinzel', serif; font-size: 10px; letter-spacing: 1.5px;
  color: var(--walnut-mid); margin-bottom: 6px;
}
.ic-body { font-size: 13.5px; line-height: 1.7; color: var(--muted); }
.ic-accent { display: inline-block; margin-top: 8px; font-size: 12px; color: var(--saffron); font-style: italic; }

/* ── BIRTHDAY CARDS ── */
.bday-card {
  background: linear-gradient(135deg, var(--saffron-pale), var(--gold-pale));
  border: 1px solid rgba(212,114,42,.3); border-radius: 14px;
  padding: 20px 24px; margin-bottom: 14px; position: relative; overflow: hidden;
}
.bday-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 3px; background: linear-gradient(90deg, var(--saffron), var(--gold), var(--saffron));
}
.bday-yr { font-family: 'Cinzel', serif; font-size: 10px; letter-spacing: 2px; color: var(--muted); margin-bottom: 4px; }
.bday-date { font-size: 20px; font-weight: 500; color: var(--walnut); margin-bottom: 3px; }
.bday-deva { font-family: 'Noto Serif Devanagari', serif; font-size: 13px; color: var(--muted); margin-bottom: 10px; }
.bday-detail { font-size: 13px; color: var(--muted); line-height: 1.9; }
.bday-hl { color: var(--walnut); font-weight: 500; }

/* ── GUNA ── */
.guna-row {
  display: flex; align-items: center; gap: 12px; padding: 9px 14px;
  border-radius: 8px; margin-bottom: 6px;
  background: var(--cream2); border: 1px solid rgba(212,184,150,.3);
}
.guna-name {
  font-family: 'Cinzel', serif; font-size: 10.5px; letter-spacing: 1px;
  color: var(--walnut-mid); min-width: 120px;
}
.guna-pts { font-size: 15px; font-weight: 600; min-width: 55px; }
.guna-status { font-size: 13px; color: var(--muted); flex: 1; }

/* ── SCORE CIRCLE ── */
.score-wrap { text-align: center; padding: 1rem; }
.score-circle {
  width: 130px; height: 130px; border-radius: 50%;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  margin: 0 auto 12px; border: 4px solid;
}
.score-num { font-family: 'Cinzel Decorative', serif; font-size: 2.4rem; line-height: 1; }
.score-den { font-size: .85rem; opacity: .6; }
.score-rec { font-family: 'Cinzel', serif; font-size: 10.5px; letter-spacing: 1px; margin-top: 8px; }
.score-bar {
  width: 100%; height: 10px; border-radius: 5px; margin: 12px 0;
  background: linear-gradient(to right, #C03030, #D4882A, #4A9A50);
  position: relative;
}

/* ── LINEAGE ── */
.lin-item {
  display: flex; gap: 14px; padding: 12px 0;
  border-bottom: 1px solid rgba(212,184,150,.35);
}
.lin-item:last-child { border-bottom: none; }
.lin-icon { font-size: 20px; width: 28px; flex-shrink: 0; }
.lin-lbl {
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1.5px;
  color: var(--saffron); text-transform: uppercase; margin-bottom: 3px;
}
.lin-val { font-size: 15px; color: var(--walnut); }
.lin-desc { font-size: 12px; color: var(--muted); font-style: italic; margin-top: 2px; }

/* ── AI BOX ── */
.ai-box {
  background: linear-gradient(135deg, #3A2010 0%, #4E2210 100%);
  border-radius: 14px; padding: 22px 26px; margin-bottom: 20px;
  box-shadow: 0 6px 28px var(--shadow-d), inset 0 1px 0 rgba(222,184,90,.16);
  position: relative;
}
.ai-box::before {
  content: ' AI · अर्क';
  position: absolute; top: 12px; right: 16px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 3px; color: rgba(222,184,90,.4);
}
.ai-lbl {
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 3px;
  color: #DEB85A; margin-bottom: 10px; opacity: .8;
}
.ai-resp {
  margin-top: 16px;
  background: rgba(253,248,240,.07); border: 1px solid rgba(222,184,90,.2);
  border-radius: 10px; padding: 16px 20px; color: #FDF8F0;
  font-size: 15px; line-height: 2;
}

/* ── BADGES ── */
.badge {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 4px 12px; border-radius: 20px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 1.5px;
}
.badge-good { background: rgba(74,154,80,.12); color: #3A7A40; border: 1px solid rgba(74,154,80,.25); }
.badge-avg  { background: rgba(212,114,42,.12); color: var(--saffron); border: 1px solid rgba(212,114,42,.25); }
.badge-bad  { background: rgba(192,48,48,.10); color: #b03030; border: 1px solid rgba(192,48,48,.20); }
.badge-man-yes  { background:rgba(229,57,53,.18); border:1px solid #e53935; color:#ef9a9a; }
.badge-man-mild { background:rgba(255,152,0,.18); border:1px solid #FF9800; color:#ffcc80; }
.badge-man-no   { background:rgba(76,175,80,.18); border:1px solid #4CAF50; color:#a5d6a7; }

/* ── WIDGET OVERRIDES ── */
.stSelectbox label, .stDateInput label, .stTimeInput label,
.stNumberInput label, .stTextInput label, .stTextArea label {
  font-family: 'Cinzel', serif !important;
  font-size: 9.5px !important; letter-spacing: 1.5px !important;
  color: var(--muted) !important; text-transform: uppercase !important;
}
.stSelectbox [data-baseweb="select"] > div,
.stTextInput input, .stNumberInput input, .stTimeInput input {
  background: var(--cream) !important;
  border: 1px solid var(--border) !important;
  color: var(--ink) !important;
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 15px !important;
}
.stDateInput input {
  background: var(--cream) !important;
  border: 1px solid var(--border) !important;
  color: var(--ink) !important;
}
.stTextArea textarea {
  background: var(--cream) !important;
  border: 1px solid var(--border) !important;
  color: var(--ink) !important;
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 15px !important;
}
.stButton > button {
  font-family: 'Cinzel', serif !important;
  font-size: 10px !important; letter-spacing: 2px !important;
  background: linear-gradient(135deg, #3A2010, #8B1C30) !important;
  color: #FDF8F0 !important;
  border: 1px solid rgba(184,134,42,.4) !important;
  border-radius: 8px !important;
  padding: 0.55rem 1.6rem !important;
  transition: all .2s !important;
}
.stButton > button:hover {
  background: linear-gradient(135deg, #8B1C30, #D4722A) !important;
  border-color: #D4722A !important;
}
.stCheckbox label {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 14px !important; color: var(--ink) !important;
}
.stMetric { background: var(--cream2); border: 1px solid var(--border); border-radius: 8px; padding: .5rem !important; }
.stMetric label { font-family:'Cinzel',serif !important; font-size:9px !important; color:var(--muted) !important; letter-spacing:1.5px !important; }
.stMetric [data-testid="stMetricValue"] { font-size:1.1rem !important; color:var(--walnut) !important; }
.stExpander { border: 1px solid var(--border) !important; border-radius: 8px !important; background: white !important; }
.streamlit-expanderHeader {
  font-family:'Cinzel',serif !important; font-size:10px !important;
  color:var(--walnut-mid) !important; letter-spacing:1.5px !important;
}

/* ── DIVIDER ── */
.lotus-div {
  text-align: center; color: var(--saffron);
  opacity: .4; font-size: 1.1rem; margin: 18px 0; letter-spacing: .8rem;
}
.styled-div {
  display: flex; align-items: center; gap: 12px; margin: 20px 0;
  color: var(--muted);
}
.styled-div::before, .styled-div::after { content:''; flex:1; height:1px; background:var(--border); }
.styled-div span { font-family:'Cinzel',serif; font-size:9px; letter-spacing:3px; white-space:nowrap; }

/* ── FOOTER ── */
.site-footer {
  text-align: center; padding: 16px; margin-top: 24px;
  font-family: 'Cinzel', serif; font-size: 9px; letter-spacing: 3px;
  color: var(--muted); opacity: .5; border-top: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS  (after page config)
# ─────────────────────────────────────────────────────────────────────────────
try:
    from astro_engine_fixed import (
        get_full_panchang, match_36_gunas, check_mangalik,
        get_nakshatra_from_dob, NAKSHATRA_NAMES,
        get_planet_lon, _ayanamsa_cached,
    )
    # Clear planet + ayanamsa LRU caches on startup so stale positions don't persist
    get_planet_lon.cache_clear()
    _ayanamsa_cached.cache_clear()
    from kashmir_data import (INDIA_STATES, GOTRAS,
                               KP_DISTRICTS, KP_TOWNS, KP_VILLAGES, KP_SURNAMES,
                               ASHTA_BHAIRAVAS, LOCAL_BHAIRAVAS,
                               KUL_DEVI_BY_DISTRICT, KUL_DEVTA_BY_DISTRICT,
                               KUL_DEVI_BY_TOWN, SURNAME_GOTRA_MAP)
    ASTRO_OK = True
    # Module-level precomputed lookups (built once, reused on every render)
    _STATES_LIST = list(INDIA_STATES.keys())
    _STATE_IDX   = {s: i for i, s in enumerate(_STATES_LIST)}
    _DIST_LISTS  = {s: list(d.keys()) for s, d in INDIA_STATES.items()}
    _DIST_IDX    = {s: {d: i for i, d in enumerate(lst)}
                    for s, lst in _DIST_LISTS.items()}
except ImportError as _ie:
    ASTRO_OK = False
    _import_err = str(_ie)
    _STATES_LIST = []; _STATE_IDX = {}; _DIST_LISTS = {}; _DIST_IDX = {}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def samvat_year(d: date) -> int:
    return d.year + 57 if d.month > 3 else d.year + 56

def saptarishi_samvat(d: date) -> int:
    """Saptarishi (Sapta Rishi / Laukika) Samvat = Gregorian year + 3076."""
    return d.year + 3076

# Panchang cache — today's planets use utcnow() so TTL=60 keeps them live.
# Past/future dates are fully deterministic and re-use the cache for the hour.
@st.cache_data(ttl=60, show_spinner=False)
def _cached_panchang(d: date, lat: float, lon: float, h: int = None, m: int = 0):
    return get_full_panchang(d, lat, lon, time_h=h, time_m=m)

@st.cache_data(ttl=3600, show_spinner=False)
def _cached_nakshatra(d: date, lat: float, lon: float, h: int, m: int):
    return get_nakshatra_from_dob(d, lat, lon, h, m)

@st.cache_data(ttl=3600, show_spinner=False)
def _cached_mangalik(d: date, lat: float, lon: float, h: int, m: int):
    return check_mangalik(d, lat, lon, h, m)

@st.cache_data(ttl=3600, show_spinner=False)
def _cached_gunas(b_nak: str, g_nak: str, b_gotra: str, g_gotra: str):
    return match_36_gunas(b_nak, g_nak, b_gotra, g_gotra)


def call_claude(system: str, user: str, max_tokens: int = 1000) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        try:
            api_key = st.secrets.get("ANTHROPIC_API_KEY", "")
        except Exception:
            pass
    if not api_key:
        return "AI features require ANTHROPIC_API_KEY to be set in environment or Streamlit secrets."
    try:
        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": max_tokens,
                "system": system,
                "messages": [{"role": "user", "content": user}],
            },
            timeout=60,
        )
        data = r.json()
        return data["content"][0]["text"] if data.get("content") else "No response."
    except Exception as ex:
        return f"Error connecting to AI: {ex}"


def state_district_selects(prefix: str, default_state: str = "Jammu & Kashmir", default_dist: str = "Jammu"):
    """Render state + district selects; return (lat, lon, location_name)."""
    state = st.selectbox(
        "State · राज्य",
        _STATES_LIST,
        index=_STATE_IDX.get(default_state, 0),
        key=f"{prefix}_state",
    )
    dists = _DIST_LISTS.get(state, [])
    dist = st.selectbox(
        "District · जिला",
        dists,
        index=_DIST_IDX.get(state, {}).get(default_dist, 0),
        key=f"{prefix}_dist",
    )
    coords = INDIA_STATES[state][dist]
    return coords[0], coords[1], f"{dist}, {state}"


def panch_cell(label: str, deva: str, value: str, sub: str = "") -> str:
    return f"""
<div class="panch-cell">
  <span class="pc-lbl">{label}</span>
  <span class="pc-lbl-deva">{deva}</span>
  <div class="pc-val">{value}</div>
  {f'<div class="pc-sub">{sub}</div>' if sub else ''}
</div>"""


def muh_block(cls: str, label: str, deva: str, time_str: str, note: str = "") -> str:
    return f"""
<div class="muh-block {cls}">
  <div class="muh-lbl">{label}</div>
  <div class="muh-deva">{deva}</div>
  <div class="muh-time">{time_str}</div>
  {f'<div class="muh-note">{note}</div>' if note else ''}
</div>"""


def planet_badge(name: str) -> str:
    mapping = {
        "Sun": "p-sun", "Moon": "p-moon", "Mars": "p-mars", "Mercury": "p-merc",
        "Jupiter": "p-jup", "Venus": "p-ven", "Saturn": "p-sat",
        "Rahu": "p-rahu", "Ketu": "p-ketu",
    }
    icons = {
        "Sun": "", "Moon": "", "Mars": "", "Mercury": "",
        "Jupiter": "", "Venus": "", "Saturn": "", "Rahu": "", "Ketu": "",
    }
    cls = mapping.get(name, "")
    icon = icons.get(name, "⭐")
    return f'<span class="p-badge {cls}">{icon} {name}</span>'


def guna_row_html(key: str, d: dict) -> str:
    pts, mx = d["points"], d.get("max", 8)
    ratio = pts / mx if mx else 0
    col = "#3A7A40" if ratio >= 0.75 else "var(--saffron)" if ratio >= 0.4 else "#b03030"
    extra = ""
    if "boy" in d and "girl" in d:
        extra = f" &nbsp;·&nbsp;  {d['boy']} /  {d['girl']}"
    display = key.replace("_", " ").title()
    return f"""
<div class="guna-row">
  <span class="guna-name">{display}</span>
  <span class="guna-pts" style="color:{col}">{pts}/{mx}</span>
  <span class="guna-status">{d.get('status','')}{extra}</span>
</div>"""


AMAVASYA_NAMES = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha", "Shravana",
    "Bhadrapada", "Ashwina", "Kartika", "Margashirsha", "Pausha",
    "Magha", "Phalguna",
]

MASA_DEVA = {
    "Chaitra": "चैत्र", "Vaishakha": "वैशाख", "Jyeshtha": "ज्येष्ठ",
    "Ashadha": "आषाढ़", "Shravana": "श्रावण", "Bhadrapada": "भाद्रपद",
    "Ashwina": "आश्विन", "Kartika": "कार्तिक", "Margashirsha": "मार्गशीर्ष",
    "Pausha": "पौष", "Magha": "माघ", "Phalguna": "फाल्गुन",
}

MASA_KOSHUR = {
    "Chaitra":      "Tsyetra",
    "Vaishakha":    "Vyakh",
    "Jyeshtha":     "Zyeth",
    "Ashadha":      "Haar",
    "Shravana":     "Shravan",
    "Bhadrapada":   "Bhadon",
    "Ashwina":      "Asuj",
    "Kartika":      "Kartik",
    "Margashirsha": "Mangur",
    "Pausha":       "Poh",
    "Magha":        "Maag",
    "Phalguna":     "Phagun",
}

PAKSHA_KOSHUR = {
    "Shukla": "Zoon Pach",
    "Krishna": "Ghat Pach",
}

PAKSHA_KOSHUR_DEVA = {
    "Shukla": "ज़ून पछ",
    "Krishna": "घट पछ",
}

MASA_KOSHUR_DEVA = {
    "Chaitra":      "च्येत्र",
    "Vaishakha":    "व्याख",
    "Jyeshtha":     "ज्येठ",
    "Ashadha":      "हार",
    "Shravana":     "शरावन",
    "Bhadrapada":   "भादों",
    "Ashwina":      "आसुज",
    "Kartika":      "कार्तिक",
    "Margashirsha": "मंगुर",
    "Pausha":       "पोह",
    "Magha":        "माग",
    "Phalguna":     "फागुन",
}

TITHI_KOSHUR_DEVA = {
    1: "पद", 2: "दोई", 3: "त्रे", 4: "चोरुम", 5: "पंचुम",
    6: "शाशुम", 7: "सतम", 8: "आठम", 9: "नौवम", 10: "दहम",
    11: "काह", 12: "बाह", 13: "त्रुएश", 14: "चौदह", 15: "पूर्णमश",
    16: "पद", 17: "दोई", 18: "त्रे", 19: "चोरुम", 20: "पंचुम",
    21: "शाशुम", 22: "सतम", 23: "आठम", 24: "नौवम", 25: "दहम",
    26: "काह", 27: "बाह", 28: "त्रुएश", 29: "चौदह", 30: "अमावस",
}

TITHI_KOSHUR = {
    1: "Pad", 2: "Doiy", 3: "Tray", 4: "Tsorum", 5: "Panchum",
    6: "Shashum", 7: "Satam", 8: "Aatham", 9: "Nauvam", 10: "Daham",
    11: "Kaah", 12: "Baah", 13: "Truesh", 14: "Choudah", 15: "Purnmash",
    16: "Pad", 17: "Doiy", 18: "Tray", 19: "Tsorum", 20: "Panchum",
    21: "Shashum", 22: "Satam", 23: "Aatham", 24: "Nauvam", 25: "Daham",
    26: "Kaah", 27: "Baah", 28: "Truesh", 29: "Choudah", 30: "Amawas",
}

PLANET_ICONS = {
    "Sun": "", "Moon": "", "Mars": "", "Mercury": "",
    "Jupiter": "", "Venus": "", "Saturn": "", "Rahu": "", "Ketu": "",
}

PLANET_HINDI = {
    "Sun": "सूर्य", "Moon": "चन्द्र", "Mars": "मंगल", "Mercury": "बुध",
    "Jupiter": "गुरु / बृहस्पति", "Venus": "शुक्र", "Saturn": "शनि",
    "Rahu": "राहु", "Ketu": "केतु",
}

PLANET_KOSHUR = {
    "Sun":     "सिरि (Siri)",
    "Moon":    "चंद्र (Chandra)",
    "Mars":    "बोम (Boam)",
    "Mercury": "बोध (Bodh)",
    "Jupiter": "बृहस्पत (Brihaspat)",
    "Venus":   "शुक्र (Shukr)",
    "Saturn":  "शनि (Shani)",
    "Rahu":    "राह (Rah)",
    "Ketu":    "कीट (Keet)",
}

YEAR_RANGE = list(range(1950, 2051))
_YEAR_IDX  = {y: i for i, y in enumerate(YEAR_RANGE)}   # O(1) year lookup

# ── Complete KP festival calendar (Amavasyanta Masa + Paksha + Tithi) ────────
# Format: (masa, paksha, tithi_num, display_name, hex_color)
KP_FESTIVALS = [
    # ── PHALGUNA (Feb-Mar) ────────────────────────────────────────────────────
    ("Phalguna",    "Krishna",  1, "Phalguna Krishna Pratipada",    "#8B1C30"),
    ("Phalguna",    "Krishna", 11, "Phalguna Krishna Ekadashi",     "#7C4DFF"),
    ("Phalguna",    "Krishna", 13, "Herath Eve (Salam)",            "#e53935"),
    ("Phalguna",    "Krishna", 14, "Herath (KP Shivratri)",         "#e53935"),
    ("Phalguna",    "Krishna", 30, "Phalguna Amavasya",             "#555"),
    ("Phalguna",    "Shukla",   5, "Vasant Panchami (if not Magha)","#FFD700"),
    ("Phalguna",    "Shukla",  11, "Phalguna Shukla Ekadashi",      "#7C4DFF"),
    ("Phalguna",    "Shukla",  15, "Phalguna Purnima / Holi",       "#FF7043"),
    # ── CHAITRA (Mar-Apr) ─────────────────────────────────────────────────────
    ("Chaitra",     "Shukla",   1, "Navreh (KP New Year)",          "#4CAF50"),
    ("Chaitra",     "Shukla",   3, "Chaitra Tritiya",               "#B8862A"),
    ("Chaitra",     "Shukla",   7, "Sonth (Sheetala Saptami)",      "#26C6DA"),
    ("Chaitra",     "Shukla",   8, "Chaitra Ashtami / Durga Puja",  "#9C27B0"),
    ("Chaitra",     "Shukla",   9, "Ram Navami",                    "#FF9800"),
    ("Chaitra",     "Shukla",  11, "Chaitra Shukla Ekadashi",       "#7C4DFF"),
    ("Chaitra",     "Shukla",  13, "Pradosh",                       "#8B1C30"),
    ("Chaitra",     "Shukla",  15, "Chaitra Purnima / Hanuman Jayanti","#B8862A"),
    ("Chaitra",     "Krishna", 11, "Chaitra Krishna Ekadashi",      "#7C4DFF"),
    ("Chaitra",     "Krishna", 30, "Chaitra Amavasya",              "#555"),
    # ── VAISHAKHA (Apr-May) ───────────────────────────────────────────────────
    ("Vaishakha",   "Shukla",   3, "Akshaya Tritiya",               "#FFD700"),
    ("Vaishakha",   "Shukla",   6, "Shankaracharya Jayanti",        "#8B1C30"),
    ("Vaishakha",   "Shukla",   8, "Vaishakha Ashtami (Sharika Devi)","#9C27B0"),
    ("Vaishakha",   "Shukla",  10, "Ganga Dashami (Gangavataran)",  "#2A7A6A"),
    ("Vaishakha",   "Shukla",  11, "Vaishakha Shukla Ekadashi (Mohini)","#7C4DFF"),
    ("Vaishakha",   "Shukla",  14, "Narasimha Jayanti",             "#FF9800"),
    ("Vaishakha",   "Shukla",  15, "Vaishakha Purnima / Buddha Purnima","#B8862A"),
    ("Vaishakha",   "Krishna", 11, "Vaishakha Krishna Ekadashi (Apara)","#7C4DFF"),
    ("Vaishakha",   "Krishna", 30, "Vaishakha Amavasya",            "#555"),
    # ── JYESHTHA (May-Jun) ────────────────────────────────────────────────────
    ("Jyeshtha",    "Shukla",   5, "Skanda Shashthi (Kumar Shashthi)","#FF9800"),
    ("Jyeshtha",    "Shukla",   8, "Zyeth Ashtami (Kheer Bhawani)", "#DEB85A"),
    ("Jyeshtha",    "Shukla",  10, "Ganga Dashami",                 "#2A7A6A"),
    ("Jyeshtha",    "Shukla",  11, "Nirjala Ekadashi",              "#7C4DFF"),
    ("Jyeshtha",    "Shukla",  13, "Pradosh / Jyeshtha Pradosh",    "#8B1C30"),
    ("Jyeshtha",    "Shukla",  15, "Jyeshtha Purnima / Vat Purnima","#B8862A"),
    ("Jyeshtha",    "Krishna",  8, "Jee Kounth (Shitalashtami)",    "#26C6DA"),
    ("Jyeshtha",    "Krishna", 11, "Jyeshtha Krishna Ekadashi",     "#7C4DFF"),
    ("Jyeshtha",    "Krishna", 30, "Jyeshtha Amavasya (Shani Amavasya)","#555"),
    # ── ASHADHA (Jun-Jul) ─────────────────────────────────────────────────────
    ("Ashadha",     "Shukla",   2, "Ratha Yatra",                   "#FF7043"),
    ("Ashadha",     "Shukla",  11, "Ashadha Shukla Ekadashi (Devshayani)","#7C4DFF"),
    ("Ashadha",     "Shukla",  15, "Guru Purnima / Ashadha Purnima","#B8862A"),
    ("Ashadha",     "Krishna",  8, "Kaalashtami / Kalabhairava Ashtami","#8B1C30"),
    ("Ashadha",     "Krishna", 11, "Ashadha Krishna Ekadashi (Kamika)","#7C4DFF"),
    ("Ashadha",     "Krishna", 30, "Ashadha Amavasya",              "#555"),
    # ── SHRAVANA (Jul-Aug) ────────────────────────────────────────────────────
    ("Shravana",    "Shukla",   3, "Hariyali Teej",                 "#4CAF50"),
    ("Shravana",    "Shukla",   5, "Nag Panchami",                  "#2A7A6A"),
    ("Shravana",    "Shukla",  11, "Shravana Shukla Ekadashi (Putrada)","#7C4DFF"),
    ("Shravana",    "Shukla",  13, "Pradosh (Shravana)",            "#8B1C30"),
    ("Shravana",    "Shukla",  15, "Raksha Bandhan / Shravana Purnima","#FF7043"),
    ("Shravana",    "Krishna",  8, "Janmashtami",                   "#3F51B5"),
    ("Shravana",    "Krishna",  9, "Dahi Handi / Gopastami",        "#FF9800"),
    ("Shravana",    "Krishna", 11, "Shravana Krishna Ekadashi (Aja)","#7C4DFF"),
    ("Shravana",    "Krishna", 30, "Shravana Amavasya / Pithori Amavasya","#555"),
    # ── BHADRAPADA (Aug-Sep) ──────────────────────────────────────────────────
    ("Bhadrapada",  "Shukla",   3, "Hartalika Teej",                "#4CAF50"),
    ("Bhadrapada",  "Shukla",   4, "Ganesh Chaturthi",              "#FF9800"),
    ("Bhadrapada",  "Shukla",   6, "Skanda Shashthi",               "#FF9800"),
    ("Bhadrapada",  "Shukla",   8, "Radha Ashtami",                 "#FF7043"),
    ("Bhadrapada",  "Shukla",  11, "Bhadrapada Shukla Ekadashi (Parivartini)","#7C4DFF"),
    ("Bhadrapada",  "Shukla",  15, "Bhadrapada Purnima / Anant Chaturdashi","#B8862A"),
    ("Bhadrapada",  "Krishna",  1, "Pitru Paksha Begins",           "#8B1C30"),
    ("Bhadrapada",  "Krishna",  3, "Pitru Paksha Tritiya Shraddha", "#8B1C30"),
    ("Bhadrapada",  "Krishna",  5, "Pitru Paksha Panchami Shraddha","#8B1C30"),
    ("Bhadrapada",  "Krishna",  8, "Jee Kounth Satam / Thar Satam / Ashtami Shraddha","#8B1C30"),
    ("Bhadrapada",  "Krishna", 11, "Bhadrapada Krishna Ekadashi / Indira Ekadashi","#7C4DFF"),
    ("Bhadrapada",  "Krishna", 13, "Magdala Trayodashi Shraddha",   "#8B1C30"),
    ("Bhadrapada",  "Krishna", 14, "Chaturdashi Shraddha",          "#8B1C30"),
    ("Bhadrapada",  "Krishna", 30, "Mahalaya Amavasya / Sarva Pitru Amavasya","#555"),
    # ── ASHWINA (Sep-Oct) ─────────────────────────────────────────────────────
    ("Ashwina",     "Shukla",   1, "Navratri Begins / Ghatasthapana","#D4722A"),
    ("Ashwina",     "Shukla",   2, "Chandra Darshan",               "#B8862A"),
    ("Ashwina",     "Shukla",   3, "Sindhara Dooj",                 "#FF7043"),
    ("Ashwina",     "Shukla",   6, "Saraswati Avahan",              "#D4722A"),
    ("Ashwina",     "Shukla",   7, "Saraswati Puja / Maha Saptami", "#D4722A"),
    ("Ashwina",     "Shukla",   8, "Maha Ashtami / Durga Puja",     "#D4722A"),
    ("Ashwina",     "Shukla",   9, "Maha Navami",                   "#D4722A"),
    ("Ashwina",     "Shukla",  10, "Vijaya Dashami / Dussehra",     "#D4722A"),
    ("Ashwina",     "Shukla",  11, "Ashwina Shukla Ekadashi (Pashataka)","#7C4DFF"),
    ("Ashwina",     "Shukla",  13, "Pradosh (Ashwina)",             "#8B1C30"),
    ("Ashwina",     "Shukla",  15, "Sharad Purnima / Kojagiri Purnima","#B8862A"),
    ("Ashwina",     "Krishna", 11, "Ashwina Krishna Ekadashi (Rama Ekadashi)","#7C4DFF"),
    ("Ashwina",     "Krishna", 13, "Dhanteras / Dhanvantari Trayodashi","#FFD700"),
    ("Ashwina",     "Krishna", 14, "Choti Diwali / Naraka Chaturdashi","#FFD700"),
    ("Ashwina",     "Krishna", 30, "Diwali / Deepavali / Lakshmi Puja","#FFD700"),
    # ── KARTIKA (Oct-Nov) ─────────────────────────────────────────────────────
    ("Kartika",     "Shukla",   1, "Govardhan Puja / Annakut",      "#FF9800"),
    ("Kartika",     "Shukla",   2, "Bhai Dooj / Yama Dvitiya",      "#FF7043"),
    ("Kartika",     "Shukla",   5, "Labh Panchami / Gyan Panchami", "#FFD700"),
    ("Kartika",     "Shukla",   6, "Chhat Puja (Sandhya Arghya)",   "#FF9800"),
    ("Kartika",     "Shukla",   7, "Chhat Puja (Usha Arghya)",      "#FF9800"),
    ("Kartika",     "Shukla",   8, "Gopa Ashtami",                  "#4CAF50"),
    ("Kartika",     "Shukla",  11, "Chourams / Dev Uthani Ekadashi","#7C4DFF"),
    ("Kartika",     "Shukla",  12, "Tulsi Vivah",                   "#4CAF50"),
    ("Kartika",     "Shukla",  13, "Pradosh (Kartika)",             "#8B1C30"),
    ("Kartika",     "Shukla",  14, "Vaikuntha Chaturdashi",         "#9C27B0"),
    ("Kartika",     "Shukla",  15, "Kartika Purnima / Dev Diwali",  "#B8862A"),
    ("Kartika",     "Krishna", 11, "Kartika Krishna Ekadashi (Utpanna)","#7C4DFF"),
    ("Kartika",     "Krishna", 30, "Kartika Amavasya",              "#555"),
    # ── MARGASHIRSHA (Nov-Dec) ────────────────────────────────────────────────
    ("Margashirsha","Shukla",   3, "Vivah Panchami",                "#FF7043"),
    ("Margashirsha","Shukla",   5, "Gita Panchami",                 "#8B1C30"),
    ("Margashirsha","Shukla",  11, "Gita Jayanti / Mokshada Ekadashi","#7C4DFF"),
    ("Margashirsha","Shukla",  13, "Pradosh (Margashirsha)",        "#8B1C30"),
    ("Margashirsha","Shukla",  15, "Margashirsha Purnima / Dattatreya Jayanti","#B8862A"),
    ("Margashirsha","Krishna",  8, "Bhairava Ashtami (Kalabhairava Jayanti)","#8B1C30"),
    ("Margashirsha","Krishna", 11, "Margashirsha Krishna Ekadashi (Saphala)","#7C4DFF"),
    ("Margashirsha","Krishna", 30, "Margashirsha Amavasya",         "#555"),
    # ── PAUSHA (Dec-Jan) ──────────────────────────────────────────────────────
    ("Pausha",      "Krishna",  8, "Tila Ashtami (Til Oil Lamp Ritual)","#FF9800"),
    ("Pausha",      "Krishna", 11, "Pausha Krishna Ekadashi (Saphatala)","#7C4DFF"),
    ("Pausha",      "Krishna", 30, "Pausha Amavasya / Makar Amavasya","#555"),
    ("Pausha",      "Shukla",   5, "Pausha Shukla Panchami",        "#B8862A"),
    ("Pausha",      "Shukla",  11, "Pausha Shukla Ekadashi (Putrada)","#7C4DFF"),
    ("Pausha",      "Shukla",  14, "Makar Sankranti Eve",           "#FF9800"),
    ("Pausha",      "Shukla",  15, "Pausha Purnima / Shakambhari Purnima","#B8862A"),
    # ── MAGHA (Jan-Feb) ───────────────────────────────────────────────────────
    ("Magha",       "Krishna",  8, "Bhishma Ashtami",               "#8B1C30"),
    ("Magha",       "Krishna", 11, "Magha Krishna Ekadashi (Jaya)","#7C4DFF"),
    ("Magha",       "Krishna", 14, "Maha Shivratri",                "#e53935"),
    ("Magha",       "Krishna", 30, "Magha Amavasya / Mauni Amavasya","#555"),
    ("Magha",       "Shukla",   5, "Vasant Panchami / Saraswati Puja","#FFD700"),
    ("Magha",       "Shukla",  11, "Magha Shukla Ekadashi (Vijaya)","#7C4DFF"),
    ("Magha",       "Shukla",  13, "Pradosh (Magha)",               "#8B1C30"),
    ("Magha",       "Shukla",  15, "Magha Purnima / Guru Ravidas Jayanti","#B8862A"),
]
# Build a fast lookup: (masa, paksha, tithi) -> list of (name, color)
_FEST_LOOKUP: dict = {}
for _fm, _fp, _ft, _fn, _fc in KP_FESTIVALS:
    _key = (_fm, _fp, _ft)
    _FEST_LOOKUP.setdefault(_key, []).append((_fn, _fc))


# ─────────────────────────────────────────────────────────────────────────────
# KP JANTRI — Gregorian date → KP events from the printed Jantri calendar
# Format: {(year, month, day): [(event_text, color), ...]}
# Colors: #e53935=red/important  #7C4DFF=ekadashi/vrat  #B8862A=purnima
#         #555=amavasya  #4CAF50=green/auspicious  #FF9800=orange/festival
#         #2A7A6A=teal/yatra  #8B1C30=crimson/shaiva  #26C6DA=cyan/special
# ─────────────────────────────────────────────────────────────────────────────
KP_JANTRI: dict = {
    # ── MARCH 2026 ──────────────────────────────────────────────────────────
    (2026,3,19): [("Navreh · नवरेह — KP New Year","#4CAF50"),("Thalus Buth Wuchun","#8B1C30"),("Navratra Starts","#D4722A"),("Vichar Nag Yatra","#2A7A6A"),("Chitra Amavasya","#555")],
    (2026,3,20): [("Panchak Ends 2.27 Night","#888"),("Samrat Lalita Ditya Day","#B8862A")],
    (2026,3,21): [("Zangh त्रय","#8B1C30")],
    (2026,3,23): [("Kumar Shastee व्रत","#26C6DA")],
    (2026,3,25): [("Chandi Gram Mahatma Day","#888")],
    (2026,3,26): [("Durga Ashtami","#9C27B0"),("Hari Parbat Yatra Sgr & Jmu","#2A7A6A"),("Ram Navami","#FF9800"),("Uma Bhagwati – Brari Angan","#8B1C30")],
    (2026,3,27): [("Nav Durga Visarjan","#D4722A"),("Matuka Pujan","#8B1C30"),("Mangla/Bhadrakali/Uma/Shiva Jayanti","#e53935"),("Naagdandi Yagya","#2A7A6A"),("Chakreshwari Yatra — Paloura, J&K, Delhi","#2A7A6A")],
    (2026,3,28): [("Sw. Bhai Toth Ji Divas","#888")],
    (2026,3,29): [("Kamda Ekadashi शुक्ल","#7C4DFF")],
    (2026,3,31): [("Madan Trayodashi — Day of Kamdev","#8B1C30")],
    # ── APRIL 2026 ──────────────────────────────────────────────────────────
    (2026,4,2):  [("Hanuman Jayanti","#FF9800"),("Purnima व्रत","#B8862A")],
    (2026,4,5):  [("Sankata Nivarni चतुर्थी चंद्र 10.15 PM","#888")],
    (2026,4,7):  [("Panchami — Mangleswar Bhairav Jayanti","#8B1C30"),("Munghama/Pulwama/Sirnu Bhairav Bagh Mandir Yatra","#2A7A6A")],
    (2026,4,8):  [("Rishipeer Shraadh","#8B1C30"),("Kamla Naag Yatra","#2A7A6A"),("Vaital Shastee","#888")],
    (2026,4,12): [("Laxmi Narayan–Bulbul Lankar Yagya","#FF9800"),("Panchak Starts 3.44 Night","#888"),("Sw. Soordas Ji Day","#888")],
    (2026,4,13): [("Varuthinī Ekadashi कृष्ण","#7C4DFF")],
    (2026,4,14): [("Sankrati व्रत — Sun Enters Mesha","#FF9800"),("Shevachary Lakshan Ji Jayanti","#8B1C30"),("Baisakhi","#4CAF50")],
    (2026,4,17): [("Panchak Ends 12.01 Day","#888"),("Amavasya व्रत","#555")],
    (2026,4,18): [("Sw. Soordas Ji / Sw. Shankar Sahab Ji Day","#888")],
    (2026,4,19): [("Akshaya Tritiya","#FFD700"),("Parshuram Jayanti","#FF9800")],
    (2026,4,21): [("Sri Shankaracharya Jayanti","#8B1C30")],
    (2026,4,22): [("Kumar Shastee व्रत","#26C6DA"),("Sarwanand Premi Balidan Divas","#e53935")],
    (2026,4,24): [("Sw. Moti Lal Brahmchari Ji Day","#888")],
    (2026,4,27): [("Narad/Sharda Ekadashi शुक्ल","#7C4DFF"),("Dumtbal Yatra","#2A7A6A")],
    (2026,4,30): [("Narasimha Chaturdashi","#FF9800"),("Ganpatyar/Ganeshbal/Hanand Chowlgam Yatra","#2A7A6A")],
    # ── MAY 2026 ────────────────────────────────────────────────────────────
    (2026,5,1):  [("Budh Purnima व्रत","#B8862A")],
    (2026,5,2):  [("Trisnadya Yatra Starts","#2A7A6A")],
    (2026,5,3):  [("Kak Ji Sradh Hangulgond & Nagrota","#8B1C30"),("Narad Jayanti","#888")],
    (2026,5,5):  [("Sankata Nivarni चतुर्थी चंद्र 10.54 Night","#888")],
    (2026,5,7):  [("Jyesta Devi Yagya/Yatra — Jeethyar","#2A7A6A"),("Sw. Govind Koul Jalali Day","#888")],
    (2026,5,10): [("Panchak Starts 12.12 Day","#888")],
    (2026,5,13): [("Apara Ekadashi कृष्ण","#7C4DFF"),("Sri Bhadrakali Jayanti","#8B1C30")],
    (2026,5,14): [("Panchak Ends 10.33 Night","#888")],
    (2026,5,15): [("Sankrati व्रत — Sun Enters Vrishabha","#FF9800"),("Vat Savitri Vrat","#9C27B0")],
    (2026,5,16): [("Amavasya व्रत","#555"),("Harishwar/Nandkeshwar/Sumbal Yatra","#2A7A6A"),("MALMASS STARTS","#e53935")],
    (2026,5,21): [("Kumar Shastee व्रत","#26C6DA")],
    (2026,5,23): [("Ashtami व्रत","#8B1C30")],
    (2026,5,25): [("Ganga Dashhara","#2A7A6A")],
    (2026,5,27): [("Purshotam Kamla Ekadashi शुक्ल","#7C4DFF")],
    (2026,5,31): [("Purnima व्रत","#B8862A")],
    # ── JUNE 2026 ───────────────────────────────────────────────────────────
    (2026,6,3):  [("Sankata Nivarni चतुर्थी चंद्र 10.27","#888")],
    (2026,6,6):  [("Panchak Starts 7.03 Evening","#888")],
    (2026,6,11): [("Purshotam Kamla Ekadashi कृष्ण","#7C4DFF"),("Panchak Ends 8.15 Mor.","#888")],
    (2026,6,15): [("Sankrati व्रत — Sun Enters Mithuna","#FF9800"),("Som Amavasya व्रत","#555"),("Nandkeswar Day","#8B1C30"),("MALMASS ENDS","#4CAF50")],
    (2026,6,16): [("Bw. Gopi Nath Ji Yagya","#8B1C30")],
    (2026,6,18): [("Kashi Nath Ji Day","#888")],
    (2026,6,19): [("Kumar Shastee व्रत","#26C6DA"),("Sw. Rughnath Kukiloo Jayanti","#888"),("Brahmacari Gopinath Jayanti","#888")],
    (2026,6,22): [("Zyeth Ashtami — Kheer Bhawani","#DEB85A"),("Tulmul/Manzgam/Tikker/Ravyar/Loktipur Yatra","#2A7A6A"),("Harishwer Yatra","#2A7A6A"),("Sw. Hemraj Day","#888")],
    (2026,6,23): [("Swami Syed Bab Jayanti","#888")],
    (2026,6,25): [("Nirjala Ekadashi शुक्ल","#7C4DFF"),("Sri Abhinavgupt Jayanti","#8B1C30")],
    (2026,6,29): [("Purnima Vrat","#B8862A"),("Mata Roop Bhawani Jayanti","#9C27B0"),("Sw. Mahadev Kak Jayanti","#888")],
    # ── JULY 2026 ───────────────────────────────────────────────────────────
    (2026,7,3):  [("Panchk Starts 12.47 Night","#888"),("Shravana Soomwar","#8B1C30"),("Sankata Nivarni चतुर्थी चंद्र 10.08","#888")],
    (2026,7,7):  [("Sw. Kin Toth Ji Day","#888")],
    (2026,7,8):  [("Panchk Ends 3.59 Day","#888")],
    (2026,7,10): [("Yogni Ekadashi कृष्ण","#7C4DFF")],
    (2026,7,14): [("Amavasya व्रत","#555"),("Tara Bhagwati Jayanti","#8B1C30"),("Targoum Kajigund Yatra","#2A7A6A")],
    (2026,7,16): [("Shiva Bhagwati Jayanti","#8B1C30"),("Sankrati व्रत — Sun Enters Karka","#FF9800")],
    (2026,7,19): [("Kumar Shastee व्रत","#26C6DA"),("Sw. Syamanad Day","#888")],
    (2026,7,20): [("Haar Saptami","#8B1C30"),("Sw. Anand Ji — Velgam Day","#888")],
    (2026,7,21): [("Haar Ashtami","#e53935"),("Pyath Darbar Yatra Kishtwar","#2A7A6A")],
    (2026,7,23): [("Haar Navami","#8B1C30"),("Sharika & Jaya Devi Jayanti","#8B1C30"),("Hari Parbat Kmr/Jmu/Bijbihara Yatra","#2A7A6A")],
    (2026,7,25): [("Hari Swapdevshayani Ekadashi शुक्ल","#7C4DFF")],
    (2026,7,26): [("Haar Baah","#8B1C30"),("Bw. Gopinath Jayanti","#8B1C30"),("Lokbhawan/Pushkar Nath Ji Day Yatra","#2A7A6A"),("Krishan Joo Pandita","#888")],
    (2026,7,27): [("Mata Bhuvaneshwari Day — Chandpura, Kashmir","#9C27B0")],
    (2026,7,28): [("Jwala Chaturdashi","#e53935"),("Krew/Gangyal/Jmu Yatra","#2A7A6A")],
    (2026,7,29): [("Guru Purnima","#B8862A"),("Vyas Puja","#8B1C30"),("Martand Tirth Yatra","#2A7A6A"),("Acharya Vasugupt Day","#8B1C30"),("Sw. Posh Bub Yagya","#888")],
    (2026,7,31): [("Panchk Starts 6.37 Mor.","#888"),("Master Zinda Koul Jayanti","#888")],
    # ── AUGUST 2026 ─────────────────────────────────────────────────────────
    (2026,8,1):  [("Sw. Lal Ji Day","#888")],
    (2026,8,2):  [("Sankata Nivarni चतुर्थी चंद्र 9.30","#888")],
    (2026,8,3):  [("Shravana Soomwar","#8B1C30")],
    (2026,8,4):  [("Panchk Ends 9.53 Night","#888")],
    (2026,8,5):  [("Sheetla Saptami","#26C6DA")],
    (2026,8,9):  [("Kamla Ekadashi कृष्ण","#7C4DFF"),("Annual Hawan at Vyesu","#FF9800")],
    (2026,8,10): [("Shravana Soomwar","#8B1C30"),("Sh. Grat Bab Day","#888")],
    (2026,8,12): [("Amavasya व्रत","#555")],
    (2026,8,15): [("Independence Day","#4CAF50")],
    (2026,8,17): [("Shravana Soomwar","#8B1C30"),("Naag Panchami","#2A7A6A"),("Kumar Shastee व्रत","#26C6DA"),("Sankrati व्रत — Sun Enters Simha","#FF9800"),("Panjath/Kramsar Yatra","#2A7A6A"),("Naag Dandi Yagya","#8B1C30"),("Sw. Kash Kak Day","#888")],
    (2026,8,20): [("Ashtami व्रत","#8B1C30")],
    (2026,8,23): [("Pavitra Ekadashi शुक्ल","#7C4DFF")],
    (2026,8,24): [("Shravana Baah","#8B1C30"),("Kapal Mochan Shopian Yatra","#2A7A6A"),("Shravana Soomwar","#8B1C30")],
    (2026,8,27): [("Panchk Starts 1.35 Day","#888"),("Sw. Govind Koul Day","#888")],
    (2026,8,28): [("Purnima व्रत","#B8862A"),("Raksha Bandhan","#FF7043"),("Amarnath/Verinag/Mattan/Harnaag Yatra","#2A7A6A"),("Vamu Yatra","#2A7A6A")],
    (2026,8,29): [("Jaya–Vijay Bhaghwati Yatra — Brijbihara","#2A7A6A")],
    (2026,8,31): [("Sankata Nivarni चतुर्थी चंद्र 8.31 Night","#888"),("Panchk Ends 3.23 Night","#888")],
    # ── SEPTEMBER 2026 ──────────────────────────────────────────────────────
    (2026,9,1):  [("Navdal Yatra — Tral","#2A7A6A")],
    (2026,9,2):  [("Chandan Shastee चंद्र 9.38","#26C6DA")],
    (2026,9,4):  [("Zaram Janm","#888"),("Saptami Krishna Janamotsav चंद्र 11.42 PM","#8B1C30")],
    (2026,9,7):  [("Aja Ekadashi कृष्ण","#7C4DFF")],
    (2026,9,11): [("Kusha/Dharab Amavasya","#555"),("Pawan Sandya/Sharda Peeth Yatra","#2A7A6A")],
    (2026,9,14): [("Hari Talika Tritiya","#4CAF50"),("Vinayak Chaturthi","#FF9800"),("Sri Tikalal Taploo/KP Balidan Day","#e53935")],
    (2026,9,15): [("Rishi/Sw. Paramand Ji Day Yagya","#8B1C30"),("Krishan Joo Razdan Jayanti","#888")],
    (2026,9,16): [("Kumar Shastee व्रत","#26C6DA"),("Varah Panchami","#888")],
    (2026,9,17): [("Sankrati व्रत — Sun Enters Kanya","#FF9800")],
    (2026,9,19): [("Ganga/Sharda/Lal Ded Jayanti","#8B1C30"),("Uma Devi/Gangabal Yatra","#2A7A6A"),("Ganga Asthapan/Pokhri Bal Yagya","#8B1C30")],
    (2026,9,22): [("Narayani/Padhma Ekadashi शुक्ल","#7C4DFF"),("Goutam Naag Yatra — Anantnaag","#2A7A6A")],
    (2026,9,23): [("Panchk Starts 9.58 Day","#888"),("Indra Baah","#8B1C30")],
    (2026,9,24): [("Vitasta Trayodashi","#8B1C30"),("Vyetvotur–Verinaag Yatra (Birth of Vitasta)","#2A7A6A"),("Mata Bhuvnehswari Day","#9C27B0")],
    (2026,9,25): [("Anant Chaturdashi","#FF9800"),("Anant/Papharan/Karkut Naag Yatra","#2A7A6A")],
    (2026,9,26): [("Purnima व्रत","#B8862A")],
    (2026,9,27): [("Pitrupaksha Starts","#8B1C30"),("Sw. Shakar Sahib","#888")],
    (2026,9,28): [("Panchk Ends 10.15 PM","#888"),("Pt. Keshvnath Day — Jyotirvid & Karmkand Scholar","#888")],
    (2026,9,29): [("Sankata Nivarni चतुर्थी चंद्र 7.41","#888"),("Sw. Laxman Joo Day","#8B1C30")],
    # ── OCTOBER 2026 ────────────────────────────────────────────────────────
    (2026,10,2):  [("Sahib Saptami","#888")],
    (2026,10,3):  [("Mahalakshmi Ashtami कृष्ण","#9C27B0")],
    (2026,10,6):  [("Indra Ekadashi कृष्ण","#7C4DFF")],
    (2026,10,9):  [("Sw. Kral Bab Day","#888")],
    (2026,10,10): [("Pitu Amavasya","#555"),("Vijayeswar/Somyar Yatra","#2A7A6A")],
    (2026,10,11): [("Navratra Starts","#D4722A")],
    (2026,10,16): [("Kumar Shashtee व्रत","#26C6DA")],
    (2026,10,17): [("Sankrati — Sun Enters Tula","#FF9800")],
    (2026,10,19): [("Durga Ashtami व्रत","#D4722A")],
    (2026,10,20): [("Maha Navami","#D4722A"),("Navdurga Visarjan","#D4722A"),("Bhadra Kali Yatra Handwara/Pallan Mandal","#2A7A6A")],
    (2026,10,21): [("Panchk Starts 6.59 PM","#888"),("Vijay Dashami — Dussehra","#D4722A"),("Mangla Bhagwati Yagya","#8B1C30")],
    (2026,10,22): [("Paapankusha Ekadashi शुक्ल","#7C4DFF")],
    (2026,10,24): [("Sw. Nandlal Ji Sahib Day","#888")],
    (2026,10,25): [("Panchak Ends 7.21 Night","#888")],
    (2026,10,26): [("Lawangh Purnima व्रत","#B8862A")],
    (2026,10,27): [("Sw. Syedh Bab Day","#888")],
    (2026,10,29): [("Sankata Nivarni चतुर्थी चंद्र 8.12","#888")],
    # ── NOVEMBER 2026 ───────────────────────────────────────────────────────
    (2026,11,5):  [("Rama Ekadashi कृष्ण","#7C4DFF")],
    (2026,11,6):  [("Dhan Triyodashi","#FFD700")],
    (2026,11,7):  [("Danwantri/Hanuman Jayanti","#FF9800")],
    (2026,11,8):  [("Deepawali — Mahalaxmi Pujan","#FFD700")],
    (2026,11,9):  [("Som Amavasya व्रत","#555")],
    (2026,11,10): [("Annakut — Govardhan Puja","#FF9800")],
    (2026,11,11): [("Vishvikarma Puja","#FF9800")],
    (2026,11,13): [("Sw. Mahtab Kak Day","#888")],
    (2026,11,15): [("Kumar Shastee व्रत","#26C6DA")],
    (2026,11,16): [("Sankrati — Sun Enters Vrishchika","#FF9800")],
    (2026,11,17): [("Gopal Ashtami व्रत","#8B1C30"),("Panchk Starts 3.29 Day","#888")],
    (2026,11,18): [("Parikrama Navami","#2A7A6A")],
    (2026,11,20): [("Haribhodni Ekadashi शुक्ल","#7C4DFF"),("Tulsi Vivah","#4CAF50")],
    (2026,11,21): [("Panchak Ends 5.54 Night","#888")],
    (2026,11,24): [("Kartik Purnima","#B8862A"),("Guru Nanak Ji","#FF9800"),("Sw. Surdas Ji/Chandi Gram Mahatma Day","#888")],
    (2026,11,27): [("Sankata Nivarni चतुर्थी चंद्र 8.12","#888")],
    # ── DECEMBER 2026 ───────────────────────────────────────────────────────
    (2026,12,1):  [("Mahakaal Bhairav Ashtami","#8B1C30"),("Utpanna Ekadashi कृष्ण","#7C4DFF")],
    (2026,12,8):  [("Amavasya व्रत","#555")],
    (2026,12,11): [("Sw. Jeewan Sahib Day","#888")],
    (2026,12,12): [("Sw. Vidyadhar Jayanti","#888")],
    (2026,12,14): [("Panchk Starts 10.35 Evening","#888"),("Guru Teg Bhadur Day","#FF9800")],
    (2026,12,15): [("Kumar Shastee व्रत","#26C6DA")],
    (2026,12,16): [("Sankrati व्रत — Sun Enters Dhanu","#FF9800")],
    (2026,12,17): [("Ashtami व्रत","#8B1C30"),("Sw. Krishnjoo Razdan Day","#888"),("Sw. Mast Ram Patoli Day","#888")],
    (2026,12,20): [("Sri Geeta Jayanti","#8B1C30"),("Mokshada Ekadashi शुक्ल","#7C4DFF")],
    (2026,12,21): [("Pt. Kripa Ram Balidan Day","#e53935")],
    (2026,12,23): [("Purnima व्रत","#B8862A"),("Mata Annpurna Jayanti","#9C27B0"),("Bw. Dattatrey Jayanti","#8B1C30")],
    (2026,12,24): [("Mojhor Tahar Matruka Pujan","#8B1C30")],
    (2026,12,26): [("Sankata Nivarni चतुर्थी चंद्र 8.17","#888")],
    (2026,12,27): [("Chetna Divas — Pt. Prem Nath Bhatt Divas","#e53935")],
    (2026,12,29): [("Viatal & Puran Raj Bhairav Jayanti","#8B1C30")],
    (2026,12,31): [("Bhadra Kali / Mahakali Jayanti","#8B1C30")],
    # ── JANUARY 2027 ────────────────────────────────────────────────────────
    (2027,1,1):   [("Ragunath Kukloo & Mata Prabha Devi Day","#888")],
    (2027,1,2):   [("Mata Matura Devi Day","#888"),("Nand Bab Sahib Jayanti","#888"),("Anandeshawar Bhairav Jayanti","#8B1C30"),("Abhinavgupt Nirwan Jayanti","#8B1C30")],
    (2027,1,3):   [("Safala Ekadashi कृष्ण","#7C4DFF")],
    (2027,1,4):   [("Maha Maheswar Shaiv Acharaya Sri Ram Ji Jayanti","#8B1C30")],
    (2027,1,7):   [("Yaksha Amavasya","#555"),("Kuber Puja","#B8862A"),("Sw. Ashokanad Ji Day","#888")],
    (2027,1,8):   [("Sw. Mirja Kak Jayanti — Nagrota","#888"),("Kukar Naag/Hangul Gond Yatra","#2A7A6A")],
    (2027,1,10):  [("Panchk Starts 4.34 Day","#888")],
    (2027,1,13):  [("Kumar Shastee व्रत","#26C6DA")],
    (2027,1,14):  [("Makar Sankrati व्रत — Sun Enters Makara","#FF9800"),("Shisher Sankrati","#FF9800")],
    (2027,1,15):  [("Panchak Ends 11.50 PM","#888")],
    (2027,1,16):  [("Ashtami व्रत","#8B1C30")],
    (2027,1,19):  [("Putrda Ekadashi शुक्ल","#7C4DFF"),("Kashmiri Pandit Nirvasan Day","#e53935")],
    (2027,1,22):  [("Purnima व्रत","#B8862A")],
    (2027,1,25):  [("Sankata Nivarni चतुर्थी चंद्र 9.22","#888")],
    (2027,1,28):  [("Sahib Saptami","#888"),("Sw. Vivekanand Jayanti","#888")],
    # ── FEBRUARY 2027 ───────────────────────────────────────────────────────
    (2027,2,2):   [("Shath Tila Ekadashi कृष्ण","#7C4DFF")],
    (2027,2,4):   [("Shiv Chaturdashi — Daham","#8B1C30")],
    (2027,2,5):   [("Shiv Chaturdashi — Kaah","#8B1C30"),("Maha Maheswar Acharaya Sri Ram Ji Nirvan Divas","#e53935")],
    (2027,2,6):   [("Shiv Chaturdashi — Baah","#8B1C30"),("Amavasya व्रत","#555")],
    (2027,2,7):   [("Panchk Starts 10.36 Day","#888"),("Sw. Kash Kak Manigam Day","#888")],
    (2027,2,9):   [("Gouri Tritiya","#4CAF50"),("Sw. Nandlal Ji Day","#888")],
    (2027,2,10):  [("Tripura/Shuk Chaturthi","#888"),("Bala Devi/Balhom Day","#8B1C30")],
    (2027,2,11):  [("Basant Panchami","#FFD700"),("Panchak Ends 5.41 Night","#888")],
    (2027,2,12):  [("Kumar Shastee व्रत","#26C6DA")],
    (2027,2,13):  [("Surya Saptami","#FF9800"),("Martand Tirth Yatra","#2A7A6A"),("Sankrati व्रत — Sun Enters Kumbha","#FF9800")],
    (2027,2,14):  [("Bheesham Ashtami व्रत","#8B1C30")],
    (2027,2,17):  [("Bheemsen/Jaya Ekadashi शुक्ल","#7C4DFF")],
    (2027,2,20):  [("Yakshhani Chaturdashi","#8B1C30"),("Maag/Kaw Purnima व्रत","#B8862A"),("Yagya — Kumar Ji Ashram Muthi","#8B1C30")],
    (2027,2,21):  [("Hur Okdoh","#8B1C30")],
    (2027,2,24):  [("Sankata Nivarni चतुर्थी चंद्र 10.15","#888")],
    (2027,2,28):  [("Hora Ashtami","#8B1C30"),("Chakreswar/Pokhri Bal Yatra Sgr./Jmu","#2A7A6A")],
    # ── MARCH 2027 ──────────────────────────────────────────────────────────
    (2027,3,2):   [("Dyar Daham","#8B1C30")],
    (2027,3,4):   [("Vijaya Ekadashi कृष्ण","#7C4DFF"),("Vagur Bah","#8B1C30")],
    (2027,3,5):   [("Haar Ratri","#8B1C30")],
    (2027,3,6):   [("Shiv Chaturdashi — Day of Rejoice","#e53935"),("Panchk Starts 5.34 Evening","#888")],
    (2027,3,8):   [("Doony/Som Amavasya","#555"),("Vatuk Parmojun — Herath","#e53935")],
    (2027,3,11):  [("Panchak Ends 11.19 Day","#888")],
    (2027,3,13):  [("Kumar Shastee व्रत","#26C6DA")],
    (2027,3,14):  [("Thaal Bharun","#8B1C30")],
    (2027,3,15):  [("Teel Ashtami — Pitur Kriya","#8B1C30"),("Sankrati व्रत — Sun Enters Meena","#FF9800"),("Thalus Buth Wuchun / Soonth","#8B1C30")],
    (2027,3,16):  [("Ashtami व्रत","#8B1C30")],
    (2027,3,18):  [("Amla Ekadashi शुक्ल","#7C4DFF")],
    (2027,3,19):  [("Sw. Nandlal Budgam Day","#888")],
    (2027,3,22):  [("Holi","#FF7043"),("Purnima व्रत","#B8862A"),("Sw. Kral Bub Day","#888")],
    (2027,3,25):  [("Sankata Nivarni चतुर्थी चंद्र 9.30","#888")],
    (2027,3,26):  [("Sw. Mastram Nirvan Day","#888")],
    (2027,3,29):  [("Sw. Har Kak Day","#888")],
    (2027,3,31):  [("Sw. Kash Kak Wadipora Day","#888")],
    # ── APRIL 2027 ──────────────────────────────────────────────────────────
    (2027,4,2):   [("Paap Nashini Ekadashi कृष्ण","#7C4DFF"),("Panchk Starts 1.32 Day","#888")],
    (2027,4,5):   [("Chitra Chaturdashi","#8B1C30"),("Sw. Gashkak Ji Yagya","#888")],
    (2027,4,6):   [("Amavasya Vrat","#555"),("Vichar Naag/Zanpur/Var Nag Yatra","#2A7A6A"),("Sreya Bhat Day","#888"),("Lunar Year Ends — Thaal Barun","#e53935")],
}

def get_jantri_events(d: date) -> list:
    """Return list of (event_text, color) for a Gregorian date from KP_JANTRI."""
    return KP_JANTRI.get((d.year, d.month, d.day), [])


def build_events_card_html(ref_date: date) -> str:
    """Build the HTML block for the events section inside a dark panchang card.

    Shows today's events prominently if present, then upcoming events (next 3 event-days).
    Returns empty string if nothing to show.
    """
    ctx = get_events_context(ref_date)
    parts = []

    if ctx["today"]:
        rows = "".join(
            '<div style="display:flex;align-items:flex-start;gap:7px;'
            'padding:3px 0;border-bottom:1px solid rgba(222,184,90,.06)">'
            '<span style="width:7px;height:7px;border-radius:50%;background:' + fc + ';'
            'flex-shrink:0;margin-top:3px"></span>'
            '<span style="font-size:10px;color:rgba(253,248,240,.9);line-height:1.45">' + fn + '</span>'
            '</div>'
            for fn, fc in ctx["today"]
        )
        parts.append(
            '<div style="background:rgba(212,114,42,.13);border-radius:8px;'
            'padding:8px 10px;margin-bottom:6px;border:1px solid rgba(212,114,42,.25)">'
            '<div style="font-family:Cinzel,serif;font-size:7px;letter-spacing:2px;'
            'color:rgba(212,114,42,.9);margin-bottom:5px"> TODAY\'S EVENTS · आज के कार्यक्रम</div>'
            + rows + '</div>'
        )

    if ctx["upcoming"]:
        up_rows = ""
        for days_away, evt_date, evts in ctx["upcoming"]:
            day_lbl = (
                "Tomorrow" if days_away == 1
                else f"In {days_away} days"
            )
            date_str = evt_date.strftime("%d %b")
            evt_names = " · ".join(e for e, _ in evts[:2]) + (" +" + str(len(evts)-2) + " more" if len(evts) > 2 else "")
            first_color = evts[0][1]
            up_rows += (
                '<div style="display:flex;align-items:center;gap:8px;'
                'padding:4px 0;border-bottom:1px solid rgba(222,184,90,.06)">'
                '<span style="font-family:Cinzel,serif;font-size:8px;color:' + first_color + ';'
                'min-width:52px;flex-shrink:0">' + day_lbl + '</span>'
                '<span style="font-size:9px;color:rgba(253,248,240,.45);min-width:36px;flex-shrink:0">'
                + date_str + '</span>'
                '<span style="font-size:9.5px;color:rgba(253,248,240,.75);line-height:1.4">'
                + evt_names + '</span>'
                '</div>'
            )
        parts.append(
            '<div style="background:rgba(253,248,240,.04);border-radius:8px;'
            'padding:8px 10px;border:1px solid rgba(184,134,42,.1)">'
            '<div style="font-family:Cinzel,serif;font-size:7px;letter-spacing:2px;'
            'color:rgba(222,184,90,.5);margin-bottom:5px"> UPCOMING EVENTS · आगामी कार्यक्रम</div>'
            + up_rows + '</div>'
        )

    if not parts:
        return ""
    return (
        '<div style="margin-top:10px;border-top:1px solid rgba(222,184,90,.12);padding-top:10px">'
        + "".join(parts) + '</div>'
    )


def get_events_context(ref_date: date, lookahead: int = 45) -> dict:
    """Return today's events (if any) and the next upcoming event dates within lookahead days.

    Returns:
      {
        'today':    [(text, color), ...],          # events on ref_date itself
        'upcoming': [(days_away, date, [(text,color),...]), ...],  # next 3 event-days
      }
    """
    today_evts = get_jantri_events(ref_date)
    upcoming = []
    for delta in range(1, lookahead + 1):
        d = ref_date + timedelta(days=delta)
        evts = get_jantri_events(d)
        if evts:
            upcoming.append((delta, d, evts))
        if len(upcoming) >= 3:
            break
    return {"today": today_evts, "upcoming": upcoming}


# ─────────────────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────────────────
today = date.today()
samvat_now = samvat_year(today)
saptarishi_now = saptarishi_samvat(today)
today_label = f"{today.strftime('%A')}, {today.day} {today.strftime('%B %Y')}"

_header_html = (
    '<div class="site-header"><div class="hdr-inner">'

    # LEFT — English title + description
    '<div class="hdr-left">'
    '<div class="hdr-title">Ancient <span>Kashmiri</span></div>'
    '<div class="hdr-desc">A living portal of Kashmiri Pandit heritage'
    ' &mdash; Vedic Panchanga, Janma Tithi, Guna Milana,'
    ' Vamsha lineage, Shastra library and Samskrti guide.</div>'
    '<div class="hdr-tagline">Jyotisha &middot; Panchanga &middot; Vamsha'
    ' &middot; Shastra &middot; Samskrti &nbsp;&middot;&nbsp;'
    ' ज्योतिष &middot; पंचांग &middot; वंश &middot; शास्त्र &middot; संस्कृति</div>'
    '</div>'

    # RIGHT — Hindi title same style + samvats + date
    '<div class="hdr-right">'
    '<div class="hdr-title" style="font-size:19px;margin-bottom:6px">प्राचीन <span>कश्मीरी</span></div>'
    '<div style="display:flex;align-items:baseline;gap:12px;justify-content:flex-end">'
    '<div style="text-align:center">'
    '<div class="hdr-samvat">VIKRAMA</div>'
    f'<div class="hdr-samvat-num" style="font-size:18px">{samvat_now}</div>'
    '</div>'
    '<div style="color:rgba(222,184,90,.25);font-size:16px">&middot;</div>'
    '<div style="text-align:center">'
    '<div class="hdr-samvat">SAPTARSHI</div>'
    f'<div class="hdr-samvat-num" style="font-size:18px">{saptarishi_now}</div>'
    '</div></div>'
    f'<div class="hdr-date" style="margin-top:4px">{today_label}</div>'
    '</div>'

    '</div></div>'
)
st.markdown(_header_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORT ERROR GUARD
# ─────────────────────────────────────────────────────────────────────────────
if not ASTRO_OK:
    st.error(f"Could not import astro_engine_fixed or kashmir_data: {_import_err}")
    st.info("Place `astro_engine_fixed.py` and `kashmir_data.py` in the same folder as this app.")
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
TAB_NAMES = [
    "  Home · गृह",
    "  Pañcāṅga · पंचांग",
    "  Janam Din · जन्म दिन",
    "  Guṇa Milāna · गुण मिलान",
    "  Kul · कुल",
    "  Śāstra · शास्त्र",
    "  Saṃskṛti · संस्कृति",
    "  Sujhav · सुझाव",
    "  Koshurpedia · कोशुरपीडिया",
]
tabs = st.tabs(TAB_NAMES)



# ══════════════════════════════════════════════════════════════════════════════
# TAB 0 — HOME
# ══════════════════════════════════════════════════════════════════════════════
with tabs[0]:

    # ── Top row: mission statement left, today's panchang right ──
    home_l, home_r = st.columns([3, 1.4])

    with home_l:
        st.markdown(f"""
        <div style="padding: 10px 0 4px">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;
               color:var(--saffron);margin-bottom:8px">
            PRĀCĪNA KASHMĪRĪ · प्राचीन कश्मीरी
          </div>
          <div style="font-family:'Cinzel',serif;font-size:22px;font-weight:500;
               color:var(--walnut);letter-spacing:2px;line-height:1.3;margin-bottom:14px">
            Reviving the Ancient Wisdom<br>
            <span style="color:var(--saffron)">of Kashmir</span>
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:15px;
               color:var(--walnut-mid);line-height:1.8;margin-bottom:16px">
            प्राचीन कश्मीरी ज्ञान का पुनरुद्धार
          </div>

          <div style="font-size:14px;color:var(--ink);line-height:2;
               border-left:3px solid var(--saffron);padding-left:16px;
               margin-bottom:20px;font-style:italic">
            "The mountains of Kashmir have always been a seat of wisdom —
            where sages composed the Shiva Sutras, where Lalleshwari sang
            of liberation, where the Vitasta river nourished a civilisation
            that gave the world Kashmir Shaivism, the Rajatarangini, and a
            way of life rooted in the sacred."
          </div>

          <div style="font-size:13.5px;color:var(--muted);line-height:2;margin-bottom:20px">
            Over centuries — through invasions, migrations and displacement —
            much of this living knowledge became fragmented. The festivals lost
            their depth. The gotra lineages became uncertain. The panchang
            calculations moved to printed almanacs that few could read. The
            Vakhs of Lal Ded survived in memory but their meaning faded.
            <br><br>
            <strong style="color:var(--walnut)">Prācīna Kāśmīrī</strong> is
            a humble attempt to restore this knowledge — not in museum glass,
            but as a living, breathing resource for every Kashmiri Pandit and
            every curious mind. Built for the young generation who may not know
            their gotra, may never have heard a Wanwun song, may not know when
            Herath falls this year — but who carry this heritage in their blood
            and deserve to know its depth.
          </div>

          <div style="background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));
               border:1px solid rgba(212,114,42,.2);border-radius:12px;
               padding:16px 20px;margin-bottom:20px">
            <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2px;
                 color:var(--saffron);margin-bottom:8px">OUR INTENT · हमारा उद्देश्य</div>
            <div style="font-size:13px;color:var(--walnut);line-height:2">
              To rewrite ancient Kashmiri knowledge in a form that young minds
              can explore — the astronomy of the panchang, the poetry of Lal Ded,
              the philosophy of the Shiva Sutras, the rituals of Herath, the
              lineages of the gotra system. To make the <em>Jantri</em> accessible,
              the <em>Vakhs</em> understandable, the <em>Bhairava</em> recognisable,
              and the <em>Kul Devi</em> remembered. One page at a time.
            </div>
            <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
                 color:var(--muted);margin-top:8px;line-height:1.8">
              युवा पीढ़ी के लिए — गोत्र से लेकर श्लोक तक, पंचांग से लेकर शास्त्र तक,
              हेरठ से लेकर वाख तक — एक जीवित ज्ञान-कोश।
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with home_r:
        # Today's panchang summary card
        try:
            home_p = _cached_panchang(today, 32.7266, 74.8570)  # Jammu default
            home_masa = MASA_DEVA.get(home_p['masa'], home_p['masa'])
            home_masa_koshur = MASA_KOSHUR.get(home_p['masa'], home_p['masa'])
            home_adhik = home_p.get('is_adhik', False)
            home_masa_label = ('Adhika ' if home_adhik else '') + home_masa_koshur
            home_masa_hi    = ('अधिक ' if home_adhik else '') + home_masa

            # Build events block (today's events + upcoming) — pre-built to avoid f-string backslash issues
            _home_events_html = build_events_card_html(today)

            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#3A2010,#4E2210);
                 border-radius:14px;padding:18px 16px;
                 box-shadow:0 4px 20px rgba(58,32,16,.3);
                 border:1px solid rgba(184,134,42,.2);margin-top:10px">
              <div style="font-family:'Cinzel',serif;font-size:8px;letter-spacing:3px;
                   color:rgba(222,184,90,.5);margin-bottom:6px;text-align:center">
                TODAY'S PANCHANG · आज का पंचांग
              </div>
              <div style="text-align:center;font-size:11px;color:rgba(253,248,240,.4);
                   margin-bottom:12px;border-bottom:1px solid rgba(222,184,90,.1);
                   padding-bottom:10px">
                {today.strftime('%A')}, {today.day} {today.strftime('%B %Y')}
              </div>
              <div style="display:flex;flex-direction:column;gap:8px">
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:10px 12px;
                     border:1px solid rgba(184,134,42,.12)">
                  <div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap">
                    <div>
                      <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                           color:rgba(212,114,42,.7);margin-bottom:2px">MĀSA</div>
                      <div style="font-size:17px;font-weight:600;color:#FDF8F0;line-height:1.1">
                        {home_masa_label}</div>
                      <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                           color:rgba(222,184,90,.7);margin-top:1px">
                        {'अधिक ' if home_adhik else ''}{MASA_KOSHUR_DEVA.get(home_p['masa'], home_masa_koshur)}</div>
                      <div style="font-family:'Noto Serif Devanagari',serif;font-size:10px;
                           color:rgba(253,248,240,.4);margin-top:1px">{home_masa_hi}</div>
                    </div>
                    <div style="color:rgba(222,184,90,.25);font-size:20px;line-height:1">·</div>
                    <div>
                      <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                           color:rgba(212,114,42,.7);margin-bottom:2px">TITHI</div>
                      <div style="font-size:17px;font-weight:600;color:#FDF8F0;line-height:1.1">
                        {PAKSHA_KOSHUR.get(home_p['paksha'], home_p['paksha'])} · {TITHI_KOSHUR.get(home_p['tithi_num'], home_p['tithi'])}</div>
                      <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                           color:rgba(222,184,90,.7);margin-top:1px">
                        {PAKSHA_KOSHUR_DEVA.get(home_p['paksha'], '')} · {TITHI_KOSHUR_DEVA.get(home_p['tithi_num'], '')}</div>
                      <div style="font-size:10px;color:rgba(253,248,240,.4);margin-top:1px">
                        {home_p['paksha']} · {home_p['tithi']}</div>
                    </div>
                  </div>
                </div>
              </div>
              {_home_events_html}
              <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px">
                <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:rgba(212,114,42,.7)">NAKṢATRA · नक्षत्र</div>
                  <div style="font-size:12px;font-weight:500;color:#FDF8F0;margin-top:2px">
                    {home_p['nakshatra']}</div>
                  <div style="font-size:9px;color:rgba(253,248,240,.4)">
                    Pāda {home_p['nakshatra_pada']}</div>
                </div>
                <div style="background:rgba(184,134,42,.12);border-radius:8px;padding:8px 10px;
                     border:1px solid rgba(184,134,42,.2)">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:#DEB85A">SUNRISE · SUNSET</div>
                  <div style="font-size:11px;color:#FDF8F0;margin-top:2px">
                    {home_p['sunrise']} &nbsp;·&nbsp; {home_p['sunset']}</div>
                </div>
                <div style="background:rgba(184,134,42,.08);border-radius:8px;padding:8px 10px">
                  <div style="font-family:'Cinzel',serif;font-size:7px;letter-spacing:2px;
                       color:rgba(212,114,42,.7)">ABHIJIT MUHŪRTA</div>
                  <div style="font-size:11px;color:#FDF8F0;margin-top:2px">
                    {home_p['abhijit_muhurta'][0]} – {home_p['abhijit_muhurta'][1]}</div>
                </div>
              </div>
              <div style="text-align:center;margin-top:10px;font-size:9px;
                   color:rgba(253,248,240,.25);font-style:italic">
                Jammu · Lahiri · Amāvasyānta
              </div>
            </div>
            """, unsafe_allow_html=True)
        except Exception:
            pass

    # ── What's inside — tab cards ─────────────────────────────────
    st.markdown('<div class="styled-div"><span>WHAT IS INSIDE · क्या है इसमें</span></div>',
                unsafe_allow_html=True)

    TAB_CARDS = [
        {
            "tab": "Pañcāṅga · पंचांग",
            "heading": "Vedic Pañcāṅga",
            "hi": "वैदिक पंचांग",
            "desc": (
                "A precise Vedic calendar for any date and location — Tithi, Vara, Nakshatra, "
                "Yoga, Karana. Masa calculated by the authentic Amāvasyānta (new-moon-ending) "
                "system with Lahiri ayanamsha. Muhurtas: Brahma, Abhijit, Rahu Kaal, Gulika, "
                "Yamaganda. Complete planetary positions with sidereal longitudes. "
                "Monthly calendar with Kashmiri festival highlights."
            ),
            "why": "Know the auspicious time for every ritual, ceremony and daily life.",
            "color": "var(--saffron)",
        },
        {
            "tab": "Janam Din · जन्म दिन",
            "heading": "Janam Din Calendar",
            "hi": "जन्म दिन कैलेंडर",
            "desc": (
                "Find your Vedic birthday — the Janma Masa, Tithi and Nakshatra — "
                "for any year from 1950 to 2050. The Amāvasyānta masa is used so the "
                "lunar birthday falls in the correct month as observed in KP tradition. "
                "Birth chart snapshot: Chandra Rashi, Surya Rashi, Lagna Rashi."
            ),
            "why": "Observe your Vedic birthday on the correct Tithi each year.",
            "color": "#4A9A50",
        },
        {
            "tab": "Guṇa Milāna · गुण मिलान",
            "heading": "36-Guna Marriage Matching",
            "hi": "गुण मिलान · विवाह संगतता",
            "desc": (
                "Ashtakoot (36-point) Kundali Milan using classical Kashmiri Pandit nakshatra "
                "tables. All 8 Kutas: Varna, Vashya, Tara, Yoni, Graha Maitri, Gana, Bhakoot, "
                "Nadi. Mangala Dosha check from D1, Moon chart and D9 Navamsha. "
                "Gotra compatibility — same-gotra marriage warning as per KP tradition."
            ),
            "why": "Ensure a compatible and blessed union as per Vedic and KP tradition.",
            "color": "var(--lotus)",
        },
        {
            "tab": "Kul · कुल",
            "heading": "Kul — Lineage & Ancestry",
            "hi": "कुल परम्परा",
            "desc": (
                "Trace your Kashmiri Pandit lineage — select your district, town and village "
                "to discover your probable Gotra (from the traditional Bhannamasis table), "
                "Kul Devi, Kul Devta and Bhairava. The complete KP surname-to-Gotra map "
                "from classical records. Ashta Bhairavas of Kashmir with their guardian regions."
            ),
            "why": "Know your roots — gotra, kul devi, bhairava — before they are forgotten.",
            "color": "#2A7A6A",
        },
        {
            "tab": "Śāstra · शास्त्र",
            "heading": "Kashmiri Śāstra Library",
            "hi": "कश्मीरी शास्त्र ग्रन्थालय",
            "desc": (
                "A curated library of Kashmir Shaivism, Trika philosophy and Kashmiri literature. "
                "Texts: Shiva Sutras, Spanda Karikas, Tantraloka, Pratyabhijnahridayam, "
                "Nilamata Purana, Rajatarangini. Saints: Lal Ded, Nund Rishi, Abhinavagupta, "
                "Swami Lakshmanjoo. With references, archive links and study guides."
            ),
            "why": "Access the world's greatest tantric and philosophical texts — in one place.",
            "color": "var(--crimson)",
        },
        {
            "tab": "Saṃskṛti · संस्कृति",
            "heading": "Kashmiri Culture Guide",
            "hi": "कश्मीरी संस्कृति",
            "desc": (
                "A comprehensive guide to every aspect of Kashmiri Pandit culture — "
                "Festivals with complete puja vidhi and samagri (Herath, Navreh, Zyeth Ashtami), "
                "Sacred sites with GPS coordinates (50+ temples, Bhairava mandirs, Nag tirthas), "
                "Music traditions (Sufiana Kalam, Chakri, Wanwun, Santoor), "
                "Cuisine, Dress, Language and Sharada script."
            ),
            "why": "Keep the living traditions alive — festival rituals, sacred sites, music.",
            "color": "var(--gold)",
        },
        {
            "tab": "Koshurpedia · कोशुरपीडिया",
            "heading": "Koshurpedia",
            "hi": "कोशुरपीडिया",
            "desc": (
                "Your wise Kashmiri Pandit guide — coming in the next update. "
                "Will cover rituals, panchang queries, mantras, Kul Devi puja guidance, "
                "festival significance, Kashmir Shaivism and the Vakhs of Lalleshwari. "
                "A living encyclopaedia of Kashmiri knowledge."
            ),
            "why": "One resource for every question about Kashmiri Pandit tradition.",
            "color": "var(--muted)",
        },
    ]

    cols_cards = st.columns(3)
    for i, card in enumerate(TAB_CARDS):
        cols_cards[i % 3].markdown(f"""
        <div style="background:white;border:1px solid var(--border);border-radius:12px;
             padding:16px 18px;margin-bottom:14px;box-shadow:0 2px 8px var(--shadow);
             border-top:3px solid {card['color']}">
          <div style="font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:1.5px;
               color:{card['color']};margin-bottom:4px">{card['tab']}</div>
          <div style="font-family:'Cinzel',serif;font-size:13px;font-weight:500;
               color:var(--walnut);margin-bottom:3px">{card['heading']}</div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
               color:var(--muted);margin-bottom:10px">{card['hi']}</div>
          <div style="font-size:12.5px;color:var(--ink);line-height:1.75;
               margin-bottom:10px">{card['desc']}</div>
          <div style="font-size:11px;color:{card['color']};font-style:italic;
               border-top:1px solid var(--border);padding-top:8px">
            {card['why']}
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Closing note ─────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:14px;
         padding:24px 32px;margin-top:10px;text-align:center;
         box-shadow:0 4px 20px rgba(58,32,16,.25)">
      <div style="font-family:'Cinzel',serif;font-size:11px;letter-spacing:3px;
           color:rgba(222,184,90,.6);margin-bottom:10px">ॐ नमः शिवाय</div>
      <div style="font-size:14px;color:rgba(253,248,240,.75);line-height:2;
           max-width:600px;margin:0 auto">
        This portal is dedicated to every Kashmiri Pandit who carries the memory
        of the Valley — and to every young mind curious enough to ask:
        <em style="color:#DEB85A">"Who are we, and where did we come from?"</em>
      </div>
      <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
           color:rgba(222,184,90,.5);margin-top:12px;line-height:1.8">
        यह पोर्टल उन सभी कश्मीरी पण्डितों को समर्पित है जो घाटी की स्मृति अपने
        हृदय में संजोये हुए हैं।
      </div>
      <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;
           color:rgba(222,184,90,.3);margin-top:14px">
        VIKRAMA SAṂVAT {samvat_now} &nbsp;·&nbsp; LAHIRI AYANĀṂŚA &nbsp;·&nbsp; AMĀVASYĀNTA
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — PANCHANG
# ══════════════════════════════════════════════════════════════════════════════
with tabs[1]:
    # ── Header row: title left, Full Year Calendar button right ──
    _pan_hdr_l, _pan_hdr_r = st.columns([5, 1])
    with _pan_hdr_l:
        st.markdown("""
        <div class="sec-head"> Pañcāṅga · पंचांग</div>
        <div class="sec-sub">
          Vedic Pañcāṅga using Lahiri Ayanāṃśa · Amāvasyānta Chandra Māsa system
          <span class="deva">लाहिरी अयनांश · अमावस्यान्त चन्द्र मास · वैदिक सूर्योदय–अस्त गणना</span>
        </div>
        """, unsafe_allow_html=True)
    with _pan_hdr_r:
        st.markdown('<div style="height:18px"></div>', unsafe_allow_html=True)
        if st.button("📅 Full Year", key="pan_fullcal", use_container_width=True):
            st.session_state["pan_show_fullcal"] = not st.session_state.get("pan_show_fullcal", False)

    # ── Full-year carousel (shown/hidden by button) ───────────────
    if st.session_state.get("pan_show_fullcal", False):
        import calendar as _cal

        _sv_year = samvat_now          # current Vikrama Samvat year shown in header
        # Build all 12 months of the current Gregorian year (the year that contains today)
        _fy_year = today.year
        _month_names = ["January","February","March","April","May","June",
                        "July","August","September","October","November","December"]
        _masa_for_month = {
            1:"Pausha–Magha", 2:"Magha–Phalguna", 3:"Phalguna–Chaitra",
            4:"Chaitra–Vaishakha", 5:"Vaishakha–Jyeshtha", 6:"Jyeshtha–Ashadha",
            7:"Ashadha–Shravana", 8:"Shravana–Bhadrapada", 9:"Bhadrapada–Ashwina",
            10:"Ashwina–Kartika", 11:"Kartika–Margashirsha", 12:"Margashirsha–Pausha",
        }

        # Build HTML for each month card — uses CSS classes defined in the iframe stylesheet
        def _build_month_html(yr, mo):
            mn = _month_names[mo - 1]
            masa_lbl = _masa_for_month.get(mo, "")
            cal_obj = _cal.monthcalendar(yr, mo)
            wd_hdr = "".join(f'<th>{d}</th>' for d in ["Mo","Tu","We","Th","Fr","Sa","Su"])
            rows_html = ""
            for week in cal_obj:
                rows_html += "<tr>"
                for day in week:
                    if day == 0:
                        rows_html += "<td></td>"
                    else:
                        d_obj  = date(yr, mo, day)
                        evts   = KP_JANTRI.get((yr, mo, day), [])
                        is_td  = (d_obj == today)
                        fc_day = "#DEB85A" if is_td else ("#FDF8F0" if evts else "rgba(253,248,240,.55)")
                        cls    = "day-cell" + (" is-today" if is_td else (" has-evt" if evts else ""))
                        # event names listed directly in the cell
                        evt_html = ""
                        if evts:
                            evt_html = "".join(
                                f'<div class="evt-line" style="border-left:2px solid {c}">{e}</div>'
                                for e, c in evts
                            )
                        rows_html += (
                            f'<td><div class="{cls}">'
                            f'<div class="day-num" style="color:{fc_day}">{day}</div>'
                            f'{evt_html}</div></td>'
                        )
                rows_html += "</tr>"
            return (
                f'<div class="month-card">'
                f'<div class="month-title">{mn} {yr}</div>'
                f'<div class="month-masa">{masa_lbl}</div>'
                f'<table><thead><tr>{wd_hdr}</tr></thead><tbody>{rows_html}</tbody></table>'
                f'</div>'
            )

        months_html = "".join(_build_month_html(_fy_year, m) for m in range(1, 13))

        # Scroll to current month on load (0-indexed)
        _cur_month_idx = today.month - 1

        full_cal_html = f"""<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #FDF8F0; font-family: 'Cinzel', serif; padding: 8px 0; }}
  #header {{ font-size:9px; letter-spacing:2px; color:#D4722A;
             margin-bottom:10px; font-family:'Cinzel',serif; }}
  #track-wrap {{ position:relative; }}
  #fycal-track {{
    display:flex; gap:12px; overflow-x:auto; padding-bottom:12px;
    scroll-behavior:smooth;
    scrollbar-width:thin; scrollbar-color:#B8862A #3A2010;
  }}
  #fycal-track::-webkit-scrollbar {{ height:6px; }}
  #fycal-track::-webkit-scrollbar-track {{ background:#3A2010; border-radius:3px; }}
  #fycal-track::-webkit-scrollbar-thumb {{ background:#B8862A; border-radius:3px; }}
  .month-card {{
    background:linear-gradient(135deg,#3A2010,#4E2210);
    border-radius:12px; padding:14px;
    border:1px solid rgba(184,134,42,.2);
    min-width:220px; flex-shrink:0;
  }}
  .month-title {{ font-family:'Cinzel',serif; font-size:12px; font-weight:500;
                  color:#DEB85A; margin-bottom:2px; text-align:center; }}
  .month-masa  {{ font-family:'Cinzel',serif; font-size:8px;
                  color:rgba(222,184,90,.5); text-align:center;
                  margin-bottom:8px; letter-spacing:1px; }}
  table {{ width:100%; border-collapse:collapse; }}
  th {{ font-family:'Cinzel',serif; font-size:8px; color:#DEB85A;
        padding:4px 2px; text-align:center; }}
  td {{ padding:2px; }}
  .day-cell {{
    border-radius:5px; padding:4px 3px 4px;
    vertical-align:top; min-width:28px;
  }}
  .day-cell.has-evt {{ background:rgba(184,134,42,.10); }}
  .day-cell.is-today {{ background:#8B1C30 !important; }}
  .day-num {{
    font-family:'Cinzel',serif; font-size:12px; font-weight:600;
    line-height:1; text-align:center; margin-bottom:3px;
  }}
  .evt-line {{
    font-size:8px; line-height:1.35; color:rgba(253,248,240,.85);
    padding:1px 0 1px 4px; margin-top:2px;
    border-radius:0 2px 2px 0; display:block;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
    max-width:100%;
  }}
  td {{ padding:2px; vertical-align:top; }}
  .btn-row {{ display:flex; gap:8px; justify-content:center; margin-top:10px; }}
  .nav-btn {{
    background:#3A2010; border:1px solid #B8862A; color:#DEB85A;
    font-family:'Cinzel',serif; font-size:11px; padding:5px 16px;
    border-radius:6px; cursor:pointer; transition:background .15s;
  }}
  .nav-btn:hover {{ background:#8B1C30; }}
  .hint {{ font-size:9px; color:#7A5F4A; text-align:center; margin-top:6px;
           font-family:'Cinzel',serif; letter-spacing:.5px; }}
</style>
</head>
<body>
<div id="header">VIKRAMA SAMVAT {_sv_year} &nbsp;·&nbsp; FULL YEAR CALENDAR &nbsp;·&nbsp; {_fy_year} CE</div>
<div id="track-wrap">
  <div id="fycal-track">{months_html}</div>
</div>
<div class="btn-row">
  <button class="nav-btn" onclick="document.getElementById('fycal-track').scrollBy({{left:-240,behavior:'smooth'}})">&#8592; Prev Month</button>
  <button class="nav-btn" onclick="document.getElementById('fycal-track').scrollBy({{left:240,behavior:'smooth'}})">Next Month &#8594;</button>
</div>
<div class="hint">Coloured left border = event type &nbsp;·&nbsp; &#9632; dark red = today</div>
<script>
  (function(){{
    var track = document.getElementById('fycal-track');
    var cards = track.querySelectorAll('.month-card');
    if(cards.length > {_cur_month_idx}) {{
      track.scrollLeft = cards[{_cur_month_idx}].offsetLeft - 12;
    }}
  }})();
</script>
</body>
</html>"""
        import streamlit.components.v1 as _stc
        _stc.html(full_cal_html, height=560, scrolling=False)
        st.markdown('<div style="height:4px"></div>', unsafe_allow_html=True)

    # ── TOP ROW: Controls (compact) | Centre panel | Calendar (large) ──
    left_col, centre_col, right_col = st.columns([1.2, 1.6, 3.0])

    with left_col:
        p_lat, p_lon, p_loc = state_district_selects("pan", default_dist="Jammu")
        p_date = st.date_input("Date · तारीख", value=today, key="pan_date")
        _pc1, _pc2 = st.columns(2)
        p_hour = _pc1.number_input("Hour (0–23)", min_value=0, max_value=23,
                                    value=12, step=1, key="pan_hr")
        p_min  = _pc2.number_input("Min (0–59)",  min_value=0, max_value=59,
                                    value=0, step=1, key="pan_min")
        _use_time = st.checkbox("Use this time for Graha Sthiti · ग्रह समय",
                                value=False, key="pan_use_time")
        p_time_h = int(p_hour) if _use_time else None
        p_time_m = int(p_min)  if _use_time else 0
        _pan_go = st.button("Calculate Pañcāṅga ·  OK", key="pan_go",
                            use_container_width=True)

    # ── Store inputs in session_state on button click; use stored values to render ──
    if _pan_go:
        st.session_state["pan_calc_date"]   = p_date
        st.session_state["pan_calc_lat"]    = p_lat
        st.session_state["pan_calc_lon"]    = p_lon
        st.session_state["pan_calc_loc"]    = p_loc
        st.session_state["pan_calc_time_h"] = p_time_h
        st.session_state["pan_calc_time_m"] = p_time_m

    # Seed defaults on first load (today, Jammu, no explicit time)
    if "pan_calc_date" not in st.session_state:
        st.session_state["pan_calc_date"]   = today
        st.session_state["pan_calc_lat"]    = p_lat
        st.session_state["pan_calc_lon"]    = p_lon
        st.session_state["pan_calc_loc"]    = p_loc
        st.session_state["pan_calc_time_h"] = None
        st.session_state["pan_calc_time_m"] = 0

    _p_date   = st.session_state["pan_calc_date"]
    _p_lat    = st.session_state["pan_calc_lat"]
    _p_lon    = st.session_state["pan_calc_lon"]
    _p_loc    = st.session_state["pan_calc_loc"]
    _p_time_h = st.session_state["pan_calc_time_h"]
    _p_time_m = st.session_state["pan_calc_time_m"]

    # ── Calculate panchang ───────────────────────────────────────
    try:
        panchang = _cached_panchang(_p_date, _p_lat, _p_lon, _p_time_h, _p_time_m)
        sv = samvat_year(_p_date)

        masa_deva   = MASA_DEVA.get(panchang["masa"], panchang["masa"])
        masa_koshur = MASA_KOSHUR.get(panchang["masa"], panchang["masa"])
        is_adhik    = panchang.get("is_adhik", False)
        adhik_label = "ADHIKA " if is_adhik else ""
        adhik_hi    = "अधिक " if is_adhik else ""
        auspicious_badge = (
            '<span class="badge badge-good">Auspicious · शुभ</span>'
            if panchang["auspicious"]
            else '<span class="badge badge-bad">Caution · सावधान</span>'
        )

        # ── Centre: Masa + Tithi + Abhijit ───────────────────────
        with centre_col:
            masa_full_name = f"{'Adhika ' if is_adhik else ''}{masa_koshur}"
            masa_full_hi   = f"{'अधิक ' if is_adhik else ''}{masa_deva} ({panchang['masa']})"
            adhik_pill     = '<span class="badge badge-avg" style="font-size:8px;margin-left:6px">ADHIKA</span>' if is_adhik else ""
            _pan_events_html = build_events_card_html(_p_date)
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:14px;
                 padding:18px 20px;height:100%;box-shadow:0 4px 18px rgba(58,32,16,.25);
                 border:1px solid rgba(184,134,42,.2)">
              <div style="text-align:center;border-bottom:1px solid rgba(222,184,90,.15);
                   padding-bottom:12px;margin-bottom:12px">
                <div style="font-family:'Cinzel',serif;font-size:8px;letter-spacing:3px;
                     color:rgba(222,184,90,.5);margin-bottom:4px">VIKRAMA SAṂVAT</div>
                <div style="font-family:'Cinzel Decorative',serif;font-size:22px;
                     color:rgba(222,184,90,.9);line-height:1">{sv}</div>
                <div style="font-size:10px;color:rgba(253,248,240,.4);margin-top:2px">
                  {_p_date.strftime('%A')}, {_p_date.day} {_p_date.strftime('%B %Y')}
                </div>
              </div>
              <div style="background:rgba(253,248,240,.06);border-radius:10px;
                   padding:14px 12px;margin-bottom:12px;
                   border:1px solid rgba(184,134,42,.15)">
                <div style="display:flex;align-items:flex-start;gap:12px;flex-wrap:wrap">
                  <div style="flex:1;min-width:80px">
                    <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                         color:rgba(212,114,42,.7);margin-bottom:3px">MĀSA · मास</div>
                    <div style="font-size:20px;font-weight:600;color:#FDF8F0;line-height:1.1">
                      {masa_full_name}{adhik_pill}</div>
                    <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
                         color:rgba(222,184,90,.75);margin-top:2px">
                      {'अधिक ' if is_adhik else ''}{MASA_KOSHUR_DEVA.get(panchang['masa'], masa_koshur)}</div>
                    <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                         color:rgba(253,248,240,.4);margin-top:1px">{masa_full_hi}</div>
                  </div>
                  <div style="color:rgba(222,184,90,.2);font-size:28px;line-height:1;
                       align-self:center">·</div>
                  <div style="flex:1;min-width:80px">
                    <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                         color:rgba(212,114,42,.7);margin-bottom:3px">TITHI · तिथि</div>
                    <div style="font-size:20px;font-weight:600;color:#FDF8F0;line-height:1.1">
                      {PAKSHA_KOSHUR.get(panchang['paksha'], panchang['paksha'])} · {TITHI_KOSHUR.get(panchang['tithi_num'], panchang['tithi'])}</div>
                    <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
                         color:rgba(222,184,90,.75);margin-top:2px">
                      {PAKSHA_KOSHUR_DEVA.get(panchang['paksha'], '')} · {TITHI_KOSHUR_DEVA.get(panchang['tithi_num'], '')}</div>
                    <div style="font-size:10px;color:rgba(253,248,240,.45);margin-top:1px">
                      {panchang['paksha']} · {panchang['tithi']}</div>
                    <div style="font-size:9.5px;color:rgba(253,248,240,.35)">
                      ends {panchang.get('tithi_end','')}</div>
                  </div>
                </div>
              </div>
              {_pan_events_html}
              <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:8px 10px;
                   border:1px solid rgba(184,134,42,.15);margin-bottom:12px;margin-top:10px">
                <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                     color:rgba(212,114,42,.7);margin-bottom:3px">NAKṢATRA · नक्षत्र</div>
                <div style="font-size:13px;font-weight:500;color:#FDF8F0;line-height:1.3">
                  {panchang['nakshatra']}</div>
                <div style="font-size:9.5px;color:rgba(253,248,240,.45);margin-top:1px">
                  Pāda {panchang['nakshatra_pada']}</div>
              </div>
              <div style="background:rgba(184,134,42,.12);border-radius:8px;padding:9px 12px;
                   border:1px solid rgba(184,134,42,.25);margin-bottom:8px">
                <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                     color:#DEB85A;margin-bottom:3px">ABHIJIT MUHŪRTA</div>
                <div style="font-size:13px;font-weight:500;color:#FDF8F0">
                  {panchang['abhijit_muhurta'][0]} – {panchang['abhijit_muhurta'][1]}</div>
                <div style="font-size:9px;color:rgba(253,248,240,.45)">
                  Auspicious midday window · मध्याह्न शुभ काल</div>
              </div>
              <div style="text-align:center;margin-top:8px">{auspicious_badge}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Right: Monthly Calendar — always open, full size ─────
        with right_col:
            cal_year, cal_month = _p_date.year, _p_date.month
            month_name = _p_date.strftime("%B %Y")
            first_day  = date(cal_year, cal_month, 1)
            if cal_month == 12:
                last_day = date(cal_year + 1, 1, 1) - timedelta(days=1)
            else:
                last_day = date(cal_year, cal_month + 1, 1) - timedelta(days=1)

            AM_CLR = "#888"; PU_CLR = "#B8862A"; SEL_CLR = "#3A2010"

            day_data = {}
            probe_d = first_day
            while probe_d <= last_day:
                try:
                    pp = _cached_panchang(probe_d, _p_lat, _p_lon)
                    fests = _FEST_LOOKUP.get(
                        (pp['masa'], pp['paksha'], pp['tithi_num']), []
                    )
                    day_data[probe_d] = {
                        'tnum': pp['tithi_num'], 'paksha': pp['paksha'],
                        'fests': fests, 'ausp': pp['auspicious'],
                    }
                except Exception:
                    day_data[probe_d] = {'tnum': 0, 'paksha': '', 'fests': [], 'ausp': True}
                probe_d += timedelta(days=1)

            WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            first_wd = first_day.weekday()

            wd_cells = "".join(
                f'<th style="font-family:Cinzel,serif;font-size:9px;'
                f'color:var(--walnut-mid);font-weight:500;letter-spacing:1px;'
                f'padding:8px 4px;text-align:center;'
                f'background:var(--cream2);'
                f'border-bottom:2px solid var(--border)">{w}</th>'
                for w in WD
            )

            cells = [
                f'<td style="padding:4px;vertical-align:top">'
                f'<div style="min-height:62px;background:transparent;'
                f'border-radius:8px"></div></td>'
            ] * first_wd

            for dn in range(1, last_day.day + 1):
                d_obj  = date(cal_year, cal_month, dn)
                dd     = day_data.get(d_obj, {})
                tnum   = dd.get('tnum', 0)
                paksha = dd.get('paksha', '')
                fests  = dd.get('fests', [])
                ausp   = dd.get('ausp', True)
                is_sel = (d_obj == _p_date)
                is_td  = (d_obj == today)

                bg  = SEL_CLR if is_sel else ("rgba(184,134,42,.12)" if is_td else
                      ("rgba(192,48,48,.05)" if not ausp else "white"))
                nc  = "#DEB85A" if is_sel else "var(--walnut)"
                brd = "2px solid #DEB85A" if is_sel else (
                      "1.5px solid rgba(184,134,42,.4)" if is_td else
                      "1px solid rgba(184,134,42,.15)")
                shd = "box-shadow:0 0 0 3px rgba(222,184,90,.15);" if is_sel else ""

                if tnum == 30:
                    ts = "Amawas"; tc = AM_CLR if not is_sel else "#DEB85A"
                elif tnum == 15:
                    ts = "Purnima"; tc = PU_CLR if not is_sel else "#DEB85A"
                else:
                    pk = "S" if paksha == "Shukla" else "K"
                    ts = f"{pk}{tnum}"
                    tc = "var(--saffron)" if not is_sel else "rgba(222,184,90,.8)"

                dots = "".join(
                    f'<span style="display:inline-block;width:6px;height:6px;'
                    f'border-radius:50%;background:{fc};margin:0 1px"></span>'
                    for _, fc in fests[:2]
                )
                fest_name = ""
                if fests:
                    fc0 = "#DEB85A" if is_sel else fests[0][1]
                    fest_name = (
                        f'<div style="font-size:8px;color:{fc0};line-height:1.2;'
                        f'margin-top:2px;overflow:hidden;text-overflow:ellipsis;'
                        f'white-space:nowrap;font-weight:500">{fests[0][0]}</div>'
                    )

                cells.append(
                    f'<td style="padding:4px;vertical-align:top">'
                    f'<div style="background:{bg};border:{brd};border-radius:8px;'
                    f'{shd}'
                    f'padding:7px 5px 5px;text-align:center;min-height:62px;'
                    f'transition:background .12s">'
                    f'<div style="font-family:Cinzel,serif;font-size:13px;font-weight:600;'
                    f'color:{nc};line-height:1">{dn}</div>'
                    f'<div style="font-size:8.5px;color:{tc};margin-top:2px;'
                    f'line-height:1.2;letter-spacing:.3px">{ts}</div>'
                    f'<div style="margin-top:3px">{dots}</div>'
                    f'{fest_name}'
                    f'</div></td>'
                )

            rem = (7 - (first_wd + last_day.day) % 7) % 7
            cells += [
                f'<td style="padding:4px;vertical-align:top">'
                f'<div style="min-height:62px;background:rgba(253,248,240,.3);'
                f'border-radius:8px;border:1px solid rgba(184,134,42,.06)"></div></td>'
            ] * rem

            rows_html = "".join(
                f'<tr>{"".join(cells[i:i+7])}</tr>'
                for i in range(0, len(cells), 7)
            )

            legend_items = [
                ("S# Shukla · K# Krishna", "var(--muted)"),
                ("Purnima", PU_CLR),
                ("Amavasya", AM_CLR),
                ("Herath / Shivratri", "#e53935"),
                ("Navreh / KP New Year", "#4CAF50"),
                ("Zyeth Ashtami", "#DEB85A"),
                ("Navratri / Dussehra", "#D4722A"),
                ("Diwali / Dhanteras", "#FFD700"),
                ("Janmashtami", "#3F51B5"),
                ("Ekadashi", "#7C4DFF"),
                ("Nag Panchami / Ganga", "#2A7A6A"),
                ("Pitru Paksha", "#8B1C30"),
                ("Sharika / Ganesh", "#9C27B0"),
                ("Ratha Yatra / Raksha", "#FF7043"),
                ("Ganesh Chaturthi / Chourams", "#FF9800"),
            ]
            legend_dots = "".join(
                f'<span style="display:inline-flex;align-items:center;gap:4px;'
                f'font-size:9px;color:var(--muted)">'
                f'<span style="display:inline-block;width:7px;height:7px;border-radius:50%;'
                f'background:{lc}"></span>{ln}</span>'
                if i > 1 else
                f'<span style="font-size:9px;color:{lc}">{ln}</span>'
                for i, (ln, lc) in enumerate(legend_items)
            )
            legend = (
                f'<div style="display:flex;flex-wrap:wrap;gap:8px;'
                f'margin-top:10px;padding-top:10px;border-top:1px solid var(--border)">'
                f'{legend_dots}</div>'
            )

            st.markdown(
                f'<div style="background:var(--cream);border:1.5px solid var(--border);'
                f'border-radius:14px;padding:18px 16px 14px;'
                f'box-shadow:0 4px 16px var(--shadow),0 1px 4px var(--shadow)">'

                # Month header
                f'<div style="display:flex;align-items:center;justify-content:center;'
                f'margin-bottom:12px;padding-bottom:10px;'
                f'border-bottom:1.5px solid var(--border)">'
                f'<div style="font-family:Cinzel,serif;font-size:12px;font-weight:500;'
                f'letter-spacing:3px;color:var(--walnut-mid)">'
                f'{month_name.upper()}</div>'
                f'</div>'

                # Scrollable wrapper for mobile
                f'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;'
                f'scrollbar-width:thin;scrollbar-color:var(--border) transparent;">'
                f'<table style="width:100%;min-width:340px;border-collapse:separate;border-spacing:0">'
                f'<thead><tr>{wd_cells}</tr></thead>'
                f'<tbody>{rows_html}</tbody>'
                f'</table>'
                f'</div>'

                # Legend
                f'{legend}</div>',
                unsafe_allow_html=True
            )

        # ── Banner line (below the 3 columns) ────────────────────
        adhik_badge = (
            ' &nbsp;<span class="badge badge-avg" style="font-size:9px;letter-spacing:1px">'
            ' ADHIKA MĀSA · अधिक मास</span>'
            if is_adhik else ""
        )
        st.markdown(f"""
        <div style="background:var(--cream2);border:1px solid var(--border);
             border-radius:10px;padding:12px 20px;margin:14px 0 0;
             display:flex;align-items:center;justify-content:center;
             flex-wrap:wrap;gap:10px;
             box-shadow:0 1px 6px var(--shadow)">
          <span style="font-family:'Cinzel',serif;font-size:10px;letter-spacing:2px;color:var(--muted)">
            {adhik_label}{panchang['masa'].upper()} MĀSA &nbsp;·&nbsp; SAṂVAT {sv} &nbsp;·&nbsp;
            {_p_date.strftime('%A')}, {_p_date.day} {_p_date.strftime('%B %Y')}
          </span>
          {auspicious_badge}{adhik_badge}
        </div>
        <div style="height:18px"></div>
        """, unsafe_allow_html=True)

        # ── Jantri events for selected date ───────────────────────
        _pan_jantri = get_jantri_events(_p_date)
        if _pan_jantri:
            _pan_evt_html = "".join(
                f'<span style="display:inline-flex;align-items:center;gap:5px;'
                f'background:{fc}22;border:1px solid {fc}55;'
                f'color:{fc};font-size:10px;padding:3px 10px;border-radius:14px;'
                f'margin:2px;font-family:Cinzel,serif;letter-spacing:0.3px">'
                f'<span style="width:6px;height:6px;border-radius:50%;background:{fc};flex-shrink:0"></span>'
                f'{fn}</span>'
                for fn, fc in _pan_jantri
            )
            st.markdown(
                f'<div style="background:var(--cream2);border:1px solid var(--border);'
                f'border-radius:10px;padding:10px 16px;margin-bottom:6px">'
                f'<div style="font-family:Cinzel,serif;font-size:8px;letter-spacing:2px;'
                f'color:var(--saffron);margin-bottom:6px"> ĀJA KE KĀRYAKRAMA · आज के कार्यक्रम</div>'
                f'<div style="display:flex;flex-wrap:wrap;gap:4px">{_pan_evt_html}</div></div>',
                unsafe_allow_html=True
            )

        # ── Five Elements ─────────────────────────────────────────
        cols5 = st.columns(5)
        items5 = [
            ("TITHI · तिथि",    "तिथि",    f"{panchang['paksha']} {panchang['tithi']}",
             f"#{panchang['tithi_num']} · ends {panchang.get('tithi_end','')}"),
            ("VĀRA · वार",      "दिन",     panchang["vara"], ""),
            ("NAKṢATRA · नक्षत्र","नक्षत्र",panchang["nakshatra"],
             f"Pāda {panchang['nakshatra_pada']} · ends {panchang.get('nakshatra_end','')}"),
            ("YOGA · योग",      "योग",     panchang["yoga"], ""),
            ("KARAṆA · करण",   "करण",     panchang["karana"], ""),
        ]
        for col, (lbl, deva, val, sub) in zip(cols5, items5):
            col.markdown(panch_cell(lbl, deva, val, sub), unsafe_allow_html=True)

        # ── Masa row (full width, highlights Adhik Masa) ─────────
        masa_full_name = f"{'Adhika ' if is_adhik else ''}{panchang['masa']}"
        masa_full_hi   = f"{'अधिक ' if is_adhik else ''}{masa_deva}"
        masa_note      = "अधिक मास — पुण्यकाल · Extra merit; no new auspicious starts" if is_adhik else "Amāvasyānta system · अमावस्यान्त"
        masa_style     = "border:2px solid var(--saffron);background:linear-gradient(135deg,#FDF0E5,#FBF5E6)" if is_adhik else ""
        _adhik_span = '<span class="badge badge-avg" style="font-size:9px"> ADHIKA MĀSA</span>' if is_adhik else ""
        _masa_html = (
            f'<div style="{masa_style};border-radius:10px;padding:10px 18px;margin:10px 0 4px;display:flex;align-items:center;gap:16px">'
            f'<span style="font-family:Cinzel,serif;font-size:9px;letter-spacing:2px;color:var(--saffron);text-transform:uppercase">MĀSA · मास</span>'
            f'<span style="font-size:16px;font-weight:500;color:var(--walnut)">{masa_full_name}</span>'
            '<span style="font-family:\'Noto Serif Devanagari\',serif;font-size:15px;color:var(--muted)">'
            f'{masa_full_hi}</span>'
            f'{_adhik_span}'
            f'<span style="font-size:11px;color:var(--muted);margin-left:auto;font-style:italic">{masa_note}</span>'
            '</div>'
        )
        st.markdown(_masa_html, unsafe_allow_html=True)

        # ── Sunrise / Sunset / Day info ───────────────────────────
        st.markdown('<div class="styled-div"><span>SŪRYODAYA & SŪRYĀSTA · सूर्योदय – सूर्यास्त</span></div>', unsafe_allow_html=True)
        sc1, sc2, sc3, sc4 = st.columns(4)
        sc1.markdown(panch_cell("SUNRISE · सूर्योदय", "वैदिक उदय", panchang["sunrise"], _p_loc), unsafe_allow_html=True)
        sc2.markdown(panch_cell("SUNSET · सूर्यास्त", "वैदिक अस्त", panchang["sunset"], _p_loc), unsafe_allow_html=True)
        sc3.markdown(panch_cell("MOON RĀŚI · राशि", "चन्द्र राशि", panchang["moon_rashi"], ""), unsafe_allow_html=True)
        sc4.markdown(panch_cell("SUN RĀŚI · सूर्य", "सूर्य राशि", panchang["sun_rashi"], ""), unsafe_allow_html=True)

        # ── Muhurtas ─────────────────────────────────────────────
        st.markdown('<div class="subsec">MUHŪRTA · मुहूर्त <span class="deva">शुभ एवं अशुभ काल</span></div>', unsafe_allow_html=True)
        mc1, mc2 = st.columns(2)
        with mc1:
            st.markdown(
                muh_block("good", "BRAHMĀ MUHŪRTA · ब्रह्म मुहूर्त", "प्रातः कालीन साधना",
                          f"{panchang['brahma_muhurta'][0]} – {panchang['brahma_muhurta'][1]}",
                          "Most auspicious · सर्वोत्तम") +
                muh_block("spec", "ABHIJIT MUHŪRTA · अभिजित", "मध्याह्न शुभ काल",
                          f"{panchang['abhijit_muhurta'][0]} – {panchang['abhijit_muhurta'][1]}",
                          "Auspicious midday"),
                unsafe_allow_html=True,
            )
        with mc2:
            st.markdown(
                muh_block("bad", "RĀHU KĀLA · राहु काल", "वर्जित समय — नए कार्य न करें",
                          f"{panchang['rahu_kaal'][0]} – {panchang['rahu_kaal'][1]}",
                          "Avoid new beginnings") +
                muh_block("bad", "GULIKA KĀLA · गुलिक काल", "वर्जित",
                          f"{panchang['gulika_kaal'][0]} – {panchang['gulika_kaal'][1]}") +
                muh_block("bad", "YAMĀGAṆḌA · यमगण्ड", "यात्रा वर्जित",
                          f"{panchang['yamaganda'][0]} – {panchang['yamaganda'][1]}",
                          "Avoid travel"),
                unsafe_allow_html=True,
            )

        # ── Divider between muhurta and graha sthiti ─────────────
        st.markdown("""
        <div style="background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));
             border:1px solid var(--border);border-radius:10px;
             padding:10px 20px;margin:16px 0 12px;
             display:flex;align-items:center;gap:12px">
          <span style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2.5px;
                color:var(--saffron)">GRAHA STHITI · ग्रह स्थिति</span>
          <span style="flex:1;height:1px;background:var(--border)"></span>
          <span style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                color:var(--muted)">ग्रह स्थिति — Planetary Positions</span>
        </div>
        """, unsafe_allow_html=True)

        # ── Planetary Positions — always open ─────────────────────
        if True:
            p_rows = "".join([
                f"""<tr>
                  <td>
                    {planet_badge(name)}
                    <span style="display:block;font-family:'Noto Serif Devanagari',serif;
                          font-size:12px;color:var(--walnut-mid);margin-top:2px">
                      {PLANET_HINDI.get(name, '')}</span>
                    <span style="display:block;font-size:10px;color:var(--muted);
                          margin-top:1px;font-style:italic">
                      {PLANET_KOSHUR.get(name, '')}</span>
                  </td>
                  <td>
                    <span style="font-weight:500">{data['rashi']}</span>
                    <span style="display:block;font-family:'Noto Serif Devanagari',serif;font-size:12px;color:var(--muted)">{data['rashi_hi']}</span>
                  </td>
                  <td>
                    <span>{data['nakshatra']} (P{data['pada']})</span>
                    <span style="display:block;font-family:'Noto Serif Devanagari',serif;font-size:12px;color:var(--muted)">{data['nakshatra_hi']} पाद {data['pada']}</span>
                  </td>
                  <td style="font-size:13px;font-variant-numeric:tabular-nums">
                    <span style="font-weight:500">{data['longitude']:.4f}°</span>
                    <span style="display:block;font-size:11px;color:var(--muted)">{data['degree']:.4f}° in rashi</span>
                    <span style="display:block;font-size:11px;color:var(--muted)">{data.get('nak_degree', 0):.4f}° in nak</span>
                  </td>
                </tr>"""
                for name, data in panchang["planets"].items()
            ])
            st.markdown(f"""
            <table class="planet-tbl">
              <thead><tr>
                <th>GRAHA · ग्रह</th>
                <th>RĀŚI · राशि</th>
                <th>NAKṢATRA · नक्षत्र</th>
                <th>LONGITUDE · अंश</th>
              </tr></thead>
              <tbody>{p_rows}</tbody>
            </table>
            """, unsafe_allow_html=True)

        # ── Kashmiri Festivals ───────────────────────────────────
        with st.expander(" Kāśmīra Parva · कश्मीरी पर्व — Festivals & Significance"):
            festivals = [
                (" Herath (Shivarātri · हेरथ)",
                 "Most sacred KP festival. Krishna Chaturdashi of Phalguna. Shiva worshipped with water-filled earthen pots (Vatak). Includes Salām, Vatuk Puja, and ritual breaking of fast."),
                (" Navreh · नवरेह",
                 "Kashmiri New Year on Chaitra Shukla Pratipada. A Thali (plate) with rice, walnut, salt, flowers, curd, pen, and Jantri (almanac) is kept the previous night."),
                (" Kheer Bhawani · खीर भवानी",
                 "Annual mela at Tulmul spring temple (Ragnya Devi). Milk and kheer are offered; the colour of the spring water is believed to foretell events."),
                (" Zyeth Ashtami · ज्येष्ठ अष्टमी",
                 "Pilgrimage to the Kheer Bhawani temple on Jyeshtha Shukla Ashtami — one of the most attended gatherings for Kashmiri Pandits."),
                (" Pann · पान्न",
                 "Kashmiri harvest festival. Community bonfire, seasonal foods, and songs marking the end of winter."),
                (" Gada Bata · गड बत",
                 "Ritual of placing clay waterpots (Vatak) during Herath, symbolising the twelve Shiva lingas and the cosmic Shiva–Shakti union."),
            ]
            for title, desc in festivals:
                st.markdown(f"""
                <div class="muh-block spec" style="margin-bottom:8px">
                  <div class="muh-lbl">{title}</div>
                  <div style="font-size:13.5px;color:var(--ink);margin-top:4px;line-height:1.7">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Panchang calculation error: {e}")
        st.code(traceback.format_exc())

    # ── AI Query ─────────────────────────────────────────────────
    st.markdown('<div class="styled-div"><span>AI PAÑCĀṄGA QUERY · पंचांग प्रश्न</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">ASK THE JYOTIṢĪ · ज्योतिषी से पूछें</div>
      <div style="margin-top:18px;text-align:center;padding:18px 0 10px">
        <div style="font-size:28px;margin-bottom:10px"></div>
        <div style="font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
             color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14px;color:rgba(253,248,240,.65);line-height:1.8;max-width:480px;margin:0 auto">
          Your wise Kashmiri Pandit — for muhurtas, nakshatra guidance, festival significance
          and personalised panchang insights — will be available in the next release.
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
             color:rgba(222,184,90,.45);margin-top:10px">
          ज्योतिषी शीघ्र ही उपलब्ध होंगे — अगले अपडेट में
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Info cards ───────────────────────────────────────────────
    st.markdown('<div class="styled-div"><span>ABOUT THIS SYSTEM</span></div>', unsafe_allow_html=True)
    ic1, ic2, ic3 = st.columns(3)
    ic1.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">VEDIC SUNRISE · वैदिक सूर्योदय</div>
      <div class="ic-body">Computed from exact geodetic coordinates with atmospheric refraction. 
      All muhurta divisions (Rahu Kala, Gulika, Yamaganda) are derived from actual local sunrise.</div>
      <div class="ic-accent">सूर्योदय से दिनमान</div>
    </div>""", unsafe_allow_html=True)
    ic2.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">AMĀVASYĀNTA · अमावस्यान्त</div>
      <div class="ic-body">The lunar month begins and ends at Amāvasyā (new moon). Shukla Paksha
      (waxing) comes first, followed by Krishna Paksha (waning). Used in traditional panchang
      reckoning — Navreh falls on Chaitra Śukla Pratipada.</div>
      <div class="ic-accent">कश्मीरी पण्डित परम्परा</div>
    </div>""", unsafe_allow_html=True)
    ic3.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">LAHIRI AYANĀṂŚA · लाहिरी</div>
      <div class="ic-body">Official ayanamsha adopted by the Government of India in 1955 
      (Rashtriya Panchang). Used for all sidereal calculations including nakshatra and rashi.</div>
      <div class="ic-accent">भारत सरकार द्वारा मान्य</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — JANMA TITHI (BIRTHDAY)
# ══════════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown("""
    <div class="sec-head"> Janam Din · जन्म दिन</div>
    <div class="sec-sub">
      Find your Vedic birthday (Tithi + Nakshatra) for any year from 1950 to 2050 ·
      Amāvasyānta system · Precise to the minute
      <span class="deva">जन्म नक्षत्र-तिथि खोजें · 1950 से 2050 तक · मिनट-स्तरीय शुद्धता</span>
    </div>
    """, unsafe_allow_html=True)

    _jt1, _jt2, _jt3, _jt4 = st.columns([1.4, 1.0, 1.4, 1.4])
    with _jt1:
        b_dob = st.date_input(
            "Date of Birth · जन्म तिथि",
            value=date(1990, 1, 1),
            min_value=date(1900, 1, 1),
            max_value=date(2025, 12, 31),
            key="jt_dob",
        )
    with _jt2:
        st.markdown('<div style="font-family:Cinzel,serif;font-size:9px;letter-spacing:1.5px;color:var(--muted);margin-bottom:4px">BIRTH TIME · जन्म समय</div>', unsafe_allow_html=True)
        _jt2a, _jt2b = st.columns(2)
        _jt_hr  = _jt2a.number_input("Hour (0–23)", min_value=0, max_value=23, value=6,  step=1, key="jt_hr",  label_visibility="visible")
        _jt_min = _jt2b.number_input("Min (0–59)",  min_value=0, max_value=59, value=0,  step=1, key="jt_min", label_visibility="visible")
        b_time = time_obj(_jt_hr, _jt_min)
    with _jt3:
        _jt_state = st.selectbox("State · राज्य", _STATES_LIST,
                                  index=_STATE_IDX.get("Jammu & Kashmir", 0),
                                  key="jt_state")
    with _jt4:
        _jt_dists = _DIST_LISTS.get(_jt_state, [])
        _jt_dist  = st.selectbox("District · जिला", _jt_dists,
                                  index=_DIST_IDX.get(_jt_state, {}).get("Jammu", 0),
                                  key="jt_dist")
    _jt_coords = INDIA_STATES[_jt_state][_jt_dist]
    jt_lat, jt_lon = _jt_coords[0], _jt_coords[1]
    jt_loc = f"{_jt_dist}, {_jt_state}"

    # ── Year-range selector ──────────────────────────────────────
    st.markdown('<div class="styled-div"><span>SELECT YEAR RANGE FOR BIRTHDAY CALENDAR · जन्म तिथि कैलेंडर वर्ष</span></div>', unsafe_allow_html=True)
    yr_col1, yr_col2, yr_col3 = st.columns([1, 1, 2])
    with yr_col1:
        _yr_from_list = YEAR_RANGE[_YEAR_IDX.get(today.year, 0):]
        yr_from = st.selectbox(
            "From Year · वर्ष से",
            _yr_from_list,
            index=0,
            key="jt_yr_from",
        )
    with yr_col2:
        _yr_to_list = YEAR_RANGE[_YEAR_IDX.get(today.year, 0):]
        yr_to = st.selectbox(
            "To Year · वर्ष तक",
            _yr_to_list,
            index=min(2, len(_yr_to_list) - 1),
            key="jt_yr_to",
        )
    with yr_col3:
        pass  # search is always Masa + Tithi; nakshatra shown as info only

    do_bday = st.button(" Find Janma Tithī Calendar · जन्म तिथि कैलेंडर खोजें", key="jt_calc")

    if do_bday:
        if yr_from > yr_to:
            st.warning("'From Year' must be ≤ 'To Year'.")
        elif (yr_to - yr_from) > 20:
            st.warning("Please limit range to 20 years or fewer for faster results.")
        else:
            # Snapshot all inputs into session_state so result persists across re-renders
            st.session_state["jt_snap"] = {
                "b_dob": b_dob, "bh": b_time.hour, "bm": b_time.minute,
                "lat": jt_lat, "lon": jt_lon, "loc": jt_loc,
                "yr_from": yr_from, "yr_to": yr_to,
            }

    if "jt_snap" in st.session_state:
        _s = st.session_state["jt_snap"]
        try:
            bh, bm_val = _s["bh"], _s["bm"]
            b_dob      = _s["b_dob"]
            jt_lat     = _s["lat"];  jt_lon = _s["lon"];  jt_loc = _s["loc"]
            yr_from    = _s["yr_from"];  yr_to = _s["yr_to"]
            birth_data  = _cached_nakshatra(b_dob, jt_lat, jt_lon, bh, bm_val)
            birth_panch = _cached_panchang(b_dob, jt_lat, jt_lon)
            birth_sv    = samvat_year(b_dob)

            # Masa and tithi come from birth_data (exact birth JD), not birth_panch
            target_masa      = birth_data["masa"]
            target_tithi     = birth_data["tithi_num"]
            target_nakshatra = birth_data["nakshatra"]

            birth_masa_deva  = MASA_DEVA.get(target_masa, target_masa)
            birth_masa_adhik = birth_data.get("is_adhik", False)
            birth_masa_label = f"{'Adhika ' if birth_masa_adhik else ''}{target_masa}"
            birth_masa_hi    = f"{'अधिक ' if birth_masa_adhik else ''}{birth_masa_deva}"

            # ── Birth snapshot (7 cells) ──────────────────────────
            st.markdown('<div class="subsec">JANMA VIVARA​ṆA · जन्म विवरण <span class="deva">जन्म का पंचांग</span></div>', unsafe_allow_html=True)
            bc = st.columns(7)
            bc[0].markdown(panch_cell("JANMA MĀSA", "जन्म मास",
                birth_masa_label, birth_masa_hi), unsafe_allow_html=True)
            bc[1].markdown(panch_cell("JANMA NAKṢATRA", "जन्म नक्षत्र",
                birth_data["nakshatra"], f"Pāda {birth_data['nakshatra_pada']}"), unsafe_allow_html=True)
            bc[2].markdown(panch_cell("JANMA TITHI", "जन्म तिथि",
                f"{birth_data['paksha']} {birth_data['tithi']}",
                f"#{birth_data['tithi_num']} · ends {birth_data.get('tithi_end','')}"), unsafe_allow_html=True)
            bc[3].markdown(panch_cell("CHANDRA RĀŚI", "जन्म राशि",
                birth_data["moon_rashi"], ""), unsafe_allow_html=True)
            bc[4].markdown(panch_cell("SŪRYA RĀŚI", "सूर्य राशि",
                birth_data["sun_rashi"], ""), unsafe_allow_html=True)
            bc[5].markdown(panch_cell("LAGNA RĀŚI", "लग्न राशि",
                birth_data["lagna_rashi"], ""), unsafe_allow_html=True)
            bc[6].markdown(panch_cell("VIKRAMA SAṂVAT", "जन्म संवत",
                str(birth_sv), ""), unsafe_allow_html=True)

            # ── Search all matching years ──────────────────────────
            sv_from = samvat_year(date(yr_from, 4, 1))
            sv_to   = samvat_year(date(yr_to,   4, 1))
            st.markdown(
                f'<div class="styled-div"><span>JANMA TITHĪ CALENDAR · जन्म तिथि कैलेंडर · '
                f'{yr_from}–{yr_to} CE &nbsp;·&nbsp; Vikrama Saṃvat {sv_from}–{sv_to}</span></div>',
                unsafe_allow_html=True,
            )

            results_found = 0
            with st.spinner(f"Scanning {yr_from}–{yr_to}…"):
                for yr in range(yr_from, yr_to + 1):
                    search_start = date(yr, 1, 1) - timedelta(days=32)
                    search_end   = date(yr, 12, 31) + timedelta(days=32)
                    cal_start    = date(yr, 1, 1)
                    cal_end      = date(yr, 12, 31)
                    COARSE_STEP  = 13

                    masa_dates = []
                    probe = search_start
                    while probe <= search_end:
                        try:
                            pp = _cached_panchang(probe, jt_lat, jt_lon)
                            if pp["masa"] == target_masa:
                                masa_dates.append(probe)
                        except Exception:
                            pass
                        probe += timedelta(days=COARSE_STEP)

                    if not masa_dates:
                        continue

                    fine_dates = set()
                    for c in masa_dates:
                        for delta in range(-15, 16):
                            d = c + timedelta(days=delta)
                            if cal_start <= d <= cal_end:
                                fine_dates.add(d)

                    masa_window = []
                    for d in sorted(fine_dates):
                        try:
                            pp = _cached_panchang(d, jt_lat, jt_lon)
                            if pp["masa"] == target_masa:
                                masa_window.append((d, pp))
                        except Exception:
                            pass

                    if not masa_window:
                        continue

                    best_date, best_diff, best_pp = None, 999, None
                    for d, pp in masa_window:
                        tithi_match = (pp["tithi_num"] == target_tithi)
                        diff = abs(pp["tithi_num"] - target_tithi)
                        if tithi_match and (best_date is None or diff < best_diff):
                            best_date, best_diff, best_pp = d, diff, pp
                            break

                    if best_date and best_pp:
                        results_found += 1
                        pp2         = best_pp
                        sv2         = samvat_year(best_date)
                        masa_d      = MASA_DEVA.get(pp2["masa"], pp2["masa"])
                        adhik2      = pp2.get("is_adhik", False)
                        masa_label2 = f"{'Adhika ' if adhik2 else ''}{pp2['masa']}"
                        masa_hi2    = f"{'अधिक ' if adhik2 else ''}{masa_d}"
                        nak_also    = (pp2["nakshatra"] == target_nakshatra)
                        nak_info    = (f' &nbsp;<span style="font-size:10px;color:var(--teal);'
                                       f'font-style:italic">· nakshatra also matches</span>'
                                       if nak_also else "")
                        st.markdown(f"""
                        <div class="bday-card">
                          <div class="bday-yr">
                            {yr} CE &nbsp;·&nbsp; Vikrama Saṃvat {sv2}
                          </div>
                          <div class="bday-date">
                            {best_date.strftime('%A')}, {best_date.day} {best_date.strftime('%B %Y')}
                          </div>
                          <div class="bday-deva">
                            {masa_label2} ({masa_hi2}) मास · {pp2['paksha']} पक्ष
                          </div>
                          <div class="bday-detail">
                            <span class="bday-hl">{pp2['paksha']} {pp2['tithi']}</span>
                            (ends&nbsp;{pp2.get('tithi_end','')})
                            &nbsp;·&nbsp; {pp2['vara']}
                            &nbsp;·&nbsp; <b>{pp2['nakshatra']}</b> Pāda&nbsp;{pp2['nakshatra_pada']}
                            (ends&nbsp;{pp2.get('nakshatra_end','')}){nak_info}
                            <br>
                            <span style="font-size:12px">
                               Sunrise: <b>{pp2['sunrise']}</b>
                              &nbsp;&nbsp;  Sunset: <b>{pp2['sunset']}</b>
                              &nbsp;&nbsp;  {jt_loc}
                            </span>
                          </div>
                        </div>
                        """, unsafe_allow_html=True)

            if results_found == 0:
                st.info(f"No match for {birth_masa_label} masa in {yr_from}–{yr_to}. "
                        "This can happen in Kshaya (suppressed) years — try adjacent years.")
            else:
                st.caption(
                    f" Found {results_found} result(s) in {yr_from}–{yr_to} · "
                    f"All dates fall in {birth_masa_label} Māsa ({birth_masa_hi}) "
                    f"on {birth_data['paksha']} {birth_data['tithi']} (Tithi #{target_tithi}). "
                    "· nakshatra also matches = rare alignment noted in small text."
                )

        except Exception as e:
            st.error(f"Error: {e}")
            st.code(traceback.format_exc())

    # ── AI Jyotisha reading ──────────────────────────────────────
    st.markdown('<div class="styled-div"><span>AI JYOTIṢA READING · ज्योतिष विश्लेषण</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">ASK ABOUT YOUR BIRTH CHART · जन्म कुण्डली</div>
      <div style="margin-top:18px;text-align:center;padding:18px 0 10px">
        <div style="font-size:28px;margin-bottom:10px"></div>
        <div style="font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
             color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14px;color:rgba(253,248,240,.65);line-height:1.8;max-width:480px;margin:0 auto">
          Your wise Kashmiri Pandit — personalised reading of your Janma Nakshatra,
          Vimshottari Dasha, Rashi characteristics and spiritual significance —
          will be available in the next release.
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
             color:rgba(222,184,90,.45);margin-top:10px">
          जन्म कुण्डली विश्लेषण — शीघ्र आ रहा है
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — GUNA MILAN
# ══════════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div class="sec-head"> Guṇa Milāna · गुण मिलान</div>
    <div class="sec-sub">
      36-Guṇa (Aṣṭakoota) Vedic marriage compatibility with Maṅgala Doṣa check · Gotra verification
      <span class="deva">अष्टकूट मिलान · मंगल दोष · गोत्र परीक्षा · कश्मीरी पण्डित विवाह परम्परा</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Input columns ─────────────────────────────────────────────
    boy_col, gap_col, girl_col = st.columns([5, 0.3, 5])

    with boy_col:
        st.markdown("""
        <div style="font-family:'Cinzel',serif;color:var(--teal);font-size:12px;
             letter-spacing:1.5px;margin-bottom:12px;border-bottom:1px solid var(--border);padding-bottom:8px">
           VARA · वर — GROOM
        </div>""", unsafe_allow_html=True)
        b_dob2 = st.date_input("Date of Birth · जन्म तिथि", value=date(1995, 6, 15), key="gm_b_dob")
        bc1, bc2 = st.columns(2)
        b_hour = bc1.number_input("Hour (0–23)", 0, 23, 6, key="gm_b_hour")
        b_min2 = bc2.number_input("Min (0–59)", 0, 59, 0, key="gm_b_min")
        b_lat2, b_lon2, b_loc2 = state_district_selects("gm_b", default_dist="Jammu")
        st.markdown('<div style="height:14px;border-top:1px solid var(--border);margin-top:12px"></div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family:Cinzel,serif;font-size:8.5px;letter-spacing:1.5px;color:var(--saffron);margin-bottom:6px">OPTIONAL · वैकल्पिक</div>', unsafe_allow_html=True)
        b_nak_known = st.checkbox("Nakshatra known? · नक्षत्र ज्ञात है?", key="gm_b_nak_k")
        b_nak_manual = st.selectbox("Nakshatra · नक्षत्र", NAKSHATRA_NAMES, key="gm_b_nak_m") if b_nak_known else None
        b_gotra = st.selectbox("Gotra · गोत्र", ["— Select —"] + GOTRAS, key="gm_b_gotra")

    with gap_col:
        st.markdown('<div style="border-left:1px solid var(--border);height:100%;min-height:420px"></div>', unsafe_allow_html=True)

    with girl_col:
        st.markdown("""
        <div style="font-family:'Cinzel',serif;color:var(--lotus);font-size:12px;
             letter-spacing:1.5px;margin-bottom:12px;border-bottom:1px solid var(--border);padding-bottom:8px">
           VADHŪ · वधू — BRIDE
        </div>""", unsafe_allow_html=True)
        g_dob2 = st.date_input("Date of Birth · जन्म तिथि", value=date(1998, 3, 22), key="gm_g_dob")
        gc1, gc2 = st.columns(2)
        g_hour = gc1.number_input("Hour (0–23)", 0, 23, 6, key="gm_g_hour")
        g_min2 = gc2.number_input("Min (0–59)", 0, 59, 0, key="gm_g_min")
        g_lat2, g_lon2, g_loc2 = state_district_selects("gm_g", default_dist="Jammu")
        st.markdown('<div style="height:14px;border-top:1px solid var(--border);margin-top:12px"></div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family:Cinzel,serif;font-size:8.5px;letter-spacing:1.5px;color:var(--saffron);margin-bottom:6px">OPTIONAL · वैकल्पिक</div>', unsafe_allow_html=True)
        g_nak_known = st.checkbox("Nakshatra known? · नक्षत्र ज्ञात है?", key="gm_g_nak_k")
        g_nak_manual = st.selectbox("Nakshatra · नक्षत्र", NAKSHATRA_NAMES, key="gm_g_nak_m") if g_nak_known else None
        g_gotra = st.selectbox("Gotra · गोत्र", ["— Select —"] + GOTRAS, key="gm_g_gotra")

    st.markdown('<div class="lotus-div">  </div>', unsafe_allow_html=True)
    _, mid_btn, _ = st.columns([3, 2, 3])
    with mid_btn:
        do_match = st.button(" Calculate Guṇa Milāna · गुण मिलान करें", key="gm_calc")

    if do_match:
        try:
            boy_data  = _cached_nakshatra(b_dob2, b_lat2, b_lon2, int(b_hour), int(b_min2))
            girl_data = _cached_nakshatra(g_dob2, g_lat2, g_lon2, int(g_hour), int(g_min2))

            b_nak = b_nak_manual if b_nak_manual else boy_data["nakshatra"]
            g_nak = g_nak_manual if g_nak_manual else girl_data["nakshatra"]
            b_gotra_v = b_gotra if b_gotra != "— Select —" else ""
            g_gotra_v = g_gotra if g_gotra != "— Select —" else ""

            # ── Nakshatra summary ─────────────────────────────────
            st.markdown('<div class="subsec">JANMA NAKṢATRA · जन्म नक्षत्र</div>', unsafe_allow_html=True)
            ns1, ns2 = st.columns(2)
            ns1.markdown(f"""
            <div class="panch-cell" style="text-align:left;padding:16px 20px">
              <span class="pc-lbl"> VARA · वर — GROOM</span>
              <div class="pc-val-big" style="margin:8px 0">{b_nak}</div>
              <div style="font-size:13px;color:var(--muted)">
                Moon: {boy_data['moon_rashi']} &nbsp;·&nbsp; Lagna: {boy_data['lagna_rashi']}
                {f" &nbsp;·&nbsp; Gotra: {b_gotra_v}" if b_gotra_v else ""}
              </div>
            </div>""", unsafe_allow_html=True)
            ns2.markdown(f"""
            <div class="panch-cell" style="text-align:left;padding:16px 20px">
              <span class="pc-lbl"> VADHŪ · वधू — BRIDE</span>
              <div class="pc-val-big" style="margin:8px 0">{g_nak}</div>
              <div style="font-size:13px;color:var(--muted)">
                Moon: {girl_data['moon_rashi']} &nbsp;·&nbsp; Lagna: {girl_data['lagna_rashi']}
                {f" &nbsp;·&nbsp; Gotra: {g_gotra_v}" if g_gotra_v else ""}
              </div>
            </div>""", unsafe_allow_html=True)

            # ── 36 Gunas ─────────────────────────────────────────
            result = _cached_gunas(b_nak, g_nak, b_gotra_v, g_gotra_v)
            score = result["total"]
            pct = result["percentage"]

            score_color = "#4CAF50" if pct >= 75 else "var(--saffron)" if pct >= 50 else "#e53935"

            st.markdown('<div class="subsec">ṢAṬTRIṂŚAT GUṆA MILĀPA · 36 गुण मिलान <span class="deva">अष्टकूट विश्लेषण</span></div>', unsafe_allow_html=True)

            score_col, detail_col = st.columns([1, 2])
            with score_col:
                st.markdown(f"""
                <div class="score-wrap">
                  <div class="score-circle" style="border-color:{score_color};box-shadow:0 0 30px {score_color}30">
                    <div class="score-num" style="color:{score_color}">{score}</div>
                    <div class="score-den">/ 36</div>
                  </div>
                  <div class="score-rec" style="color:{score_color}">{result['recommendation']}</div>
                  {f'<div style="margin-top:10px;font-size:13px;color:var(--muted)">{result["gotra_note"]}</div>' if result.get("gotra_note") else ''}
                  <div class="score-bar">
                    <div style="position:absolute;width:18px;height:18px;border-radius:50%;
                         background:white;border:3px solid var(--walnut);top:-4px;
                         left:{pct}%;transform:translateX(-50%)"></div>
                  </div>
                  <div style="font-size:12px;color:var(--muted)">{pct:.0f}% compatibility</div>
                </div>
                """, unsafe_allow_html=True)

            with detail_col:
                st.markdown("".join(guna_row_html(k, v) for k, v in result["details"].items()), unsafe_allow_html=True)

            # ── Mangalik — compute once, reuse for display + note + AI report ──
            b_mg = _cached_mangalik(b_dob2, b_lat2, b_lon2, int(b_hour), int(b_min2))
            g_mg = _cached_mangalik(g_dob2, g_lat2, g_lon2, int(g_hour), int(g_min2))

            st.markdown('<div class="subsec">MAṄGALA DOṢA · मंगल दोष <span class="deva">D1 · Moon Chart · D9 (Navāṃśa)</span></div>', unsafe_allow_html=True)
            mc1, mc2 = st.columns(2)
            for col, (mg, lbl, lbl_deva) in zip(
                [mc1, mc2],
                [
                    (b_mg, " Vara (Groom)", "वर"),
                    (g_mg, " Vadhū (Bride)", "वधू"),
                ]
            ):
                with col:
                    try:
                        badge_cls = (
                            "badge-man-yes"  if mg["is_mangalik"] and mg["mangalik_count"] >= 2
                            else "badge-man-mild" if mg["is_mangalik"]
                            else "badge-man-no"
                        )
                        cancels_html = ""
                        if mg["cancellations"]:
                            cancels_html = "".join(f'<div style="font-size:11px;color:#a5d6a7;margin-top:2px"> {c}</div>' for c in mg["cancellations"])
                        st.markdown(f"""
                        <div class="panch-cell" style="text-align:left;padding:16px 20px">
                          <span class="pc-lbl">{lbl} · {lbl_deva}</span>
                          <div style="margin:8px 0">
                            <span class="badge {badge_cls}">{mg['severity']}</span>
                          </div>
                          <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">
                            <span style="font-size:12px;padding:2px 8px;border-radius:4px;
                                  background:{'rgba(229,57,53,.15)' if mg['d1_mangalik'] else 'rgba(76,175,80,.12)'};
                                  border:1px solid {'#e5393550' if mg['d1_mangalik'] else '#4caf5050'}">
                              D1: H{mg['d1_house']} {'' if mg['d1_mangalik'] else ''}
                            </span>
                            <span style="font-size:12px;padding:2px 8px;border-radius:4px;
                                  background:{'rgba(229,57,53,.15)' if mg['moon_chart_mangalik'] else 'rgba(76,175,80,.12)'};
                                  border:1px solid {'#e5393550' if mg['moon_chart_mangalik'] else '#4caf5050'}">
                              Moon: H{mg['moon_chart_house']} {'' if mg['moon_chart_mangalik'] else ''}
                            </span>
                            <span style="font-size:12px;padding:2px 8px;border-radius:4px;
                                  background:{'rgba(229,57,53,.15)' if mg['d9_mangalik'] else 'rgba(76,175,80,.12)'};
                                  border:1px solid {'#e5393550' if mg['d9_mangalik'] else '#4caf5050'}">
                              D9: H{mg['d9_house']} {'' if mg['d9_mangalik'] else ''}
                            </span>
                          </div>
                          <div style="font-size:11px;margin-top:6px;color:var(--muted)">
                            Lagna: {mg['asc_rashi']} &nbsp;·&nbsp; Moon: {mg['moon_rashi']}
                          </div>
                          {cancels_html}
                        </div>
                        """, unsafe_allow_html=True)
                    except Exception as me:
                        col.error(f"Mangalik error: {me}")

            # Mangalik compatibility note
            same = b_mg["is_mangalik"] == g_mg["is_mangalik"]
            st.markdown(f"""
            <div class="muh-block {'good' if same else 'bad'}" style="margin-top:12px">
              <div class="muh-time">{' Both same Mangalik status — Compatible' if same else ' Different Mangalik status — Remedies recommended'}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── AI Marriage Report ───────────────────────────────
            st.markdown("""
            <div class="ai-box" style="margin-top:16px">
              <div class="ai-lbl"> FULL COMPATIBILITY REPORT · विस्तृत विवाह विश्लेषण</div>
              <div style="margin-top:16px;text-align:center;padding:14px 0 8px">
                <div style="font-size:24px;margin-bottom:8px"></div>
                <div style="font-family:'Cinzel',serif;font-size:12px;letter-spacing:2px;
                     color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
                <div style="font-size:13.5px;color:rgba(253,248,240,.65);line-height:1.8;max-width:460px;margin:0 auto">
                  Your wise Kashmiri Pandit — full compatibility with dosha remedies,
                  auspicious wedding months and KP-specific guidance —
                  available in the next release.
                </div>
                <div style="font-family:'Noto Serif Devanagari',serif;font-size:11px;
                     color:rgba(222,184,90,.4);margin-top:8px">
                  विस्तृत विवाह विश्लेषण — शीघ्र आ रहा है
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Matching error: {e}")
            st.code(traceback.format_exc())


# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — LINEAGE
# ══════════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("""
    <div class="sec-head"> Kul Paramparā · कुल परम्परा</div>
    <div class="sec-sub">
      Trace your Kashmiri Pandit lineage — Gotra, Kul Devī, Kul Devatā, Bhairava
      <span class="deva">गोत्र · कुल देवी · कुल देवता · भैरव · ग्राम देवता</span>
    </div>
    """, unsafe_allow_html=True)

    _d1, _d2, _d3, _d4 = st.columns(4)
    with _d1:
        lin_district = st.selectbox(
            "District in Kashmir · जिला",
            KP_DISTRICTS,
            key="lin_dist",
        )
    with _d2:
        _towns = KP_TOWNS.get(lin_district, ["— Select town first —"])
        lin_town = st.selectbox(
            "Town / Mohalla · नगर",
            _towns,
            key="lin_town",
        )
    with _d3:
        _villages = KP_VILLAGES.get(lin_town, [lin_town])
        lin_village = st.selectbox(
            "Village / Mauza · गाँव",
            _villages,
            key="lin_vill",
        )
    with _d4:
        lin_surname = st.selectbox(
            "Family Surname · कुल नाम (Optional)",
            KP_SURNAMES,
            key="lin_name",
        )

    do_lin = st.button(" Trace Kul · कुल खोजें", key="lin_calc")

    if do_lin:
        surname_val = lin_surname if lin_surname != "— Optional —" else ""
        _result_title = lin_village
        if lin_town and lin_town != lin_village:
            _result_title += f", {lin_town}"
        _result_title += f", {lin_district}"

        st.markdown(f'<div class="subsec" style="margin-top:18px">VAṂŚA VIVARA​ṆA · वंश विवरण — {_result_title}</div>', unsafe_allow_html=True)

        # ── Tentative disclaimer ──────────────────────────────────
        st.markdown("""
        <div style="background:rgba(212,114,42,.08);border:1px solid rgba(212,114,42,.35);
             border-left:4px solid var(--saffron);border-radius:8px;padding:12px 18px;
             margin-bottom:18px;font-size:13px;color:var(--walnut-mid);line-height:1.7">
          <span style="font-family:Cinzel,serif;font-size:9px;letter-spacing:2px;
                color:var(--saffron);display:block;margin-bottom:4px">DISCLAIMER · सूचना</span>
           <b>Tentative information</b> — Also need to verify with a Pandit of the region
          for all the data shared below.
          यह जानकारी अनुमानित है। कृपया इसे स्थानीय पण्डित से भी सत्यापित करें।
        </div>
        """, unsafe_allow_html=True)

        lin_r1, lin_r2 = st.columns(2)

        # ── Kul Devi — town-level override takes precedence over district ────
        kd = KUL_DEVI_BY_DISTRICT.get(lin_district, {})
        town_kul_devi = KUL_DEVI_BY_TOWN.get(lin_town, "") or KUL_DEVI_BY_TOWN.get(lin_village, "")

        with lin_r1:
            if town_kul_devi:
                # Town-specific — show clean, precise info
                also_html = ""
                if kd.get('also'):
                    also_items = "".join(
                        f'<div style="padding:3px 0;border-bottom:1px solid rgba(184,134,42,.1);'
                        f'font-size:11px;color:var(--muted)">{a}</div>'
                        for a in kd['also']
                    )
                    also_html = (
                        f'<div style="margin-top:8px">'
                        f'<div style="font-family:Cinzel,serif;font-size:8px;letter-spacing:1px;'
                        f'color:var(--walnut-mid);margin-bottom:4px">OTHER POSSIBLE KUL DEVIS</div>'
                        f'{also_items}</div>'
                    )
                st.markdown(f"""
                <div class="lin-item">
                  <div class="lin-icon"></div>
                  <div>
                    <div class="lin-lbl">KUL DEVĪ · कुल देवी</div>
                    <div class="lin-val">{town_kul_devi}</div>
                    <div class="lin-desc" style="color:var(--saffron);font-size:11px;margin-top:2px">
                      {lin_town} · {lin_district}</div>
                    <div class="lin-desc" style="color:var(--teal);margin-top:3px">
                       {kd.get('temple', '—')}</div>
                    {also_html}
                  </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # District-level fallback — show primary + temple + notes only
                also_html = ""
                if kd.get('also'):
                    also_items = "".join(
                        f'<div style="padding:3px 0;border-bottom:1px solid rgba(184,134,42,.1);'
                        f'font-size:11px;color:var(--muted)">{a}</div>'
                        for a in kd['also']
                    )
                    also_html = (
                        f'<div style="margin-top:8px">'
                        f'<div style="font-family:Cinzel,serif;font-size:8px;letter-spacing:1px;'
                        f'color:var(--walnut-mid);margin-bottom:4px">OTHER POSSIBLE KUL DEVIS</div>'
                        f'{also_items}</div>'
                    )
                st.markdown(f"""
                <div class="lin-item">
                  <div class="lin-icon"></div>
                  <div>
                    <div class="lin-lbl">KUL DEVĪ · कुल देवी</div>
                    <div class="lin-val">{kd.get('primary', 'Sharika Devi / Ragnya Devi')}</div>
                    <div class="lin-desc" style="color:var(--teal);margin-top:2px">
                       {kd.get('temple', '—')}</div>
                    <div class="lin-desc" style="margin-top:4px">{kd.get('notes', '')}</div>
                    {also_html}
                  </div>
                </div>
                """, unsafe_allow_html=True)

        # ── Kul Devta ────────────────────────────────────────────
        kt = KUL_DEVTA_BY_DISTRICT.get(lin_district, {})
        with lin_r2:
            st.markdown(f"""
            <div class="lin-item">
              <div class="lin-icon"></div>
              <div>
                <div class="lin-lbl">KUL DEVATĀ · कुल देवता</div>
                <div class="lin-val">{kt.get('primary', 'Shiva')}</div>
                <div class="lin-desc"> {kt.get('temple', '—')}</div>
                <div class="lin-desc">{kt.get('notes', '')}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Bhairava (Ashta + Local matching district/town) ──────
        st.markdown('<div class="subsec" style="margin-top:14px">BHAIRAVA · भैरव <span class="deva">क्षेत्रपाल</span></div>', unsafe_allow_html=True)

        # Find relevant Ashta Bhairavas for the selected town
        town_lower = lin_town.lower()
        district_lower = lin_district.lower()
        relevant_ashta = [b for b in ASHTA_BHAIRAVAS
                          if any(w in b["region"].lower() for w in town_lower.split()
                                 if len(w) > 3)
                          or any(w in b["region"].lower() for w in district_lower.split()
                                 if len(w) > 3)]
        # Always show all 8 with relevant ones highlighted
        bh_cols = st.columns(2)
        for i, b in enumerate(ASHTA_BHAIRAVAS):
            is_relevant = b in relevant_ashta
            highlight = "border-left:3px solid var(--saffron);" if is_relevant else ""
            bh_cols[i % 2].markdown(f"""
            <div class="muh-block" style="margin-bottom:7px;{highlight}">
              <div class="muh-lbl">{b['direction']} · {b['region']}</div>
              <div class="muh-time" style="font-size:14px">{b['name']}</div>
              <div class="muh-note">{b['notes']}</div>
            </div>
            """, unsafe_allow_html=True)

        # Local Bhairavas
        st.markdown('<div style="font-family:Cinzel,serif;font-size:9px;letter-spacing:2px;color:var(--muted);margin:14px 0 8px">LOCAL BHAIRAVAS · स्थानीय भैरव</div>', unsafe_allow_html=True)
        lb_cols = st.columns(2)
        for i, b in enumerate(LOCAL_BHAIRAVAS):
            is_relevant = (lin_district.lower() in b["region"].lower()
                           or lin_town.lower() in b["region"].lower()
                           or any(w in b["region"].lower()
                                  for w in lin_town.lower().split() if len(w) > 3))
            highlight = "border-left:3px solid var(--saffron);" if is_relevant else ""
            lb_cols[i % 2].markdown(f"""
            <div class="muh-block" style="margin-bottom:7px;{highlight}">
              <div class="muh-lbl">{b['region']}</div>
              <div class="muh-time" style="font-size:14px">{b['name']}</div>
              <div class="muh-note">{b['notes']}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Gotra (from selected surname only) ───────────────────
        st.markdown('<div class="subsec" style="margin-top:14px">GOTRA · गोत्र <span class="deva">सप्तर्षि वंश</span></div>', unsafe_allow_html=True)

        # Look up gotras directly from SURNAME_GOTRA_MAP using the selected surname
        gotras_for_surname = []
        if surname_val:
            # Exact match first
            gotras_for_surname = SURNAME_GOTRA_MAP.get(surname_val, [])
            # If no exact match, try case-insensitive
            if not gotras_for_surname:
                for key, val in SURNAME_GOTRA_MAP.items():
                    if key.lower() == surname_val.lower():
                        gotras_for_surname = val
                        break

        if surname_val and gotras_for_surname:
            gt_cols = st.columns(len(gotras_for_surname)) if len(gotras_for_surname) <= 4 else st.columns(4)
            for i, gotra in enumerate(gotras_for_surname):
                gt_cols[i % len(gt_cols)].markdown(f"""
                <div class="panch-cell" style="text-align:center;padding:18px 14px">
                  <span class="pc-lbl">GOTRA FOR {surname_val.upper()}</span>
                  <div class="pc-val-big" style="margin:10px 0;font-size:20px">{gotra}</div>
                </div>
                """, unsafe_allow_html=True)
        elif surname_val and not gotras_for_surname:
            st.markdown(f"""
            <div style="font-size:13px;color:var(--muted);font-style:italic;padding:10px 0">
              Gotra for <b>{surname_val}</b> not found in our current table.
              Please verify with a Pandit of your region.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="font-size:13px;color:var(--muted);font-style:italic;padding:10px 0">
              Select a family surname above to see the possible Gotra(s).
            </div>
            """, unsafe_allow_html=True)

    # Info cards
    st.markdown('<div class="styled-div"><span>ABOUT KASHMIRI PANDIT LINEAGE</span></div>', unsafe_allow_html=True)
    ic1, ic2, ic3 = st.columns(3)
    ic1.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">GOTRA · गोत्र</div>
      <div class="ic-body">Patrilineal Vedic clan traced to one of the Sapta Rishis. 
      Gotras determine marriageability — same-gotra marriage is strictly forbidden in KP tradition 
      (sagotra vivaha varjya).</div>
    </div>""", unsafe_allow_html=True)
    ic2.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">KUL DEVĪ · कुल देवी</div>
      <div class="ic-body">Family goddess, distinct for each district cluster of Kashmir. 
      Major Kul Devis: Sharika (Hari Parbat), Ragnya/Kheer Bhawani (Tulmul), 
      Jwala (Khrew), Bhadrakali. Worshipped at all family ceremonies.</div>
    </div>""", unsafe_allow_html=True)
    ic3.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">BHAIRAVA · भैरव</div>
      <div class="ic-body">Village or mohalla-specific protective deity in the Trika tradition 
      of Kashmir Shaivism. The eight Bhairavas (Ashtabhairava) guard the eight directions 
      of the sacred landscape.</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 — SHASTRA
# ══════════════════════════════════════════════════════════════════════════════
with tabs[5]:
    st.markdown("""
    <div class="sec-head"> Kāśmīrī Śāstra · कश्मीरी शास्त्र</div>
    <div class="sec-sub">
      Complete library of Kashmir Shaivism, Trika philosophy, classical texts, saints and cultural heritage
      <span class="deva">त्रिक दर्शन · काश्मीर शैव दर्शन · ग्रन्थ · संत · संस्कृति · सम्पूर्ण ग्रन्थालय</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Static data: all texts, traditions, authors ───────────────
    # Order: Saints first, then Lal Ded, then Culture, then texts
    SHASTRA_DATA = {
        "Kashmiri Saints · कश्मीरी संत": [
            {
                "title": "Lalleshwari / Lal Ded · ललद्यद (c. 1320–1392 CE)",
                "author": "Lalleshwari (born Lalla)",
                "period": "c. 1320–1392 CE — 14th century, Kashmir",
                "desc": (
                    "The mother of all Kashmiri mysticism and the first great poet of the Kashmiri language. "
                    "Born in Pandrethan village near Srinagar into a KP Brahmin family, married young into "
                    "a harsh household, she was initiated by Shaiva guru Siddha Shrikantha Swami. "
                    "She renounced home and wandered Kashmir as a naked ascetic (digambari), singing her "
                    "immortal Vakhs. Her 258+ Vakhs in Old Kashmiri are the oldest surviving literature "
                    "in the Kashmiri language. Core teaching: Shivoham — 'I am Shiva'. "
                    "Revered by Hindus as Lalla Yogeshwari and by Muslims as Lal Arifa — unique in Indian history. "
                    "Three celebrated Vakhs: "
                    "(1) 'Shiv chuy thali thali rozaan / mozan nay Hindav, na Musalmaan' — Shiva pervades everywhere; do not distinguish Hindu from Muslim. "
                    "(2) 'Lalle shiv chuy, na tyag na grev' — Shiva is in you; neither renounce nor grab. "
                    "(3) 'Pranas apanas milawath karim / Shiv Shakti akh chu, beyi nay beyi' — When prana and apana unite, Shiva and Shakti are one; there is no other, no other. "
                    "Philosophical tradition: Pratyabhijña (recognition of Self as Shiva), Spanda (divine vibration), "
                    "and elements of Hatha Yoga. Her guru Siddha Shrikantha was a master of the Trika school. "
                    "Legacy: Influenced all subsequent Kashmiri poetry — Nund Rishi, Habba Khatoon, Rupa Bhawani. "
                    "Academic works: Jayalal Kaul's 'Lal Ded' (Sahitya Akademi), Ranjit Hoskote's 'I, Lalla'."
                ),
                "tradition": "Kashmir Shaivism / Pratyabhijña / Trika",
                "link": "https://en.wikipedia.org/wiki/Lalleshwari",
                "archive": "https://archive.org/search?query=lal+ded+lalleshwari+vakhs+kashmir",
            },
            {
                "title": "Mata Sharada · माता शारदा (Saraswati of Kashmir)",
                "author": "Divine — Sharada Devi (presiding goddess of Kashmir)",
                "period": "Ancient — Vedic to present",
                "desc": (
                    "Sharada Devi is the presiding goddess of the entire Kashmir Valley — "
                    "Devi of learning, wisdom, music, arts and the sacred word. "
                    "Her principal seat: Sharada Peeth at Sharda village, Neelum Valley "
                    "(now in Pakistan-administered Kashmir). One of the 18 Maha Shakti Pithas — "
                    "Sati's right hand is said to have fallen here. "
                    "The Kashmiri script (Sharada lipi) is named after her — all KP manuscripts, "
                    "horoscopes and religious texts were written in Sharada script for centuries. "
                    "Kashmiri Pandits invoke her at all beginnings: 'Ya Sharada nilotpala-dala-shyama' "
                    "(the Sharada Stotram — she is described as blue as the blue lotus petal). "
                    "The Nilamata Purana describes her as the Vak (speech) of the valley. "
                    "Sharada Peeth held one of India's greatest ancient libraries and universities — "
                    "Adi Shankaracharya is said to have visited and debated here. "
                    "Key texts: Sharada Stotram, Saraswati Sahasranama, Devi Mahatmya (read in KP homes). "
                    "Annual virtual puja by KPs worldwide on Sharada Navami. "
                    "Campaign for restoration of access: Sharda Peeth Trust (India)."
                ),
                "tradition": "Kashmir Shakta / Saraswati / Shakti Pitha tradition",
                "link": "https://en.wikipedia.org/wiki/Sharada_Peeth",
                "archive": "https://archive.org/search?query=sharada+peeth+kashmir+saraswati",
            },
            {
                "title": "Devi Roop Bhawani · देवी रूपा भवानी (1625–1721 CE)",
                "author": "Rupa Bhawani (born Alakeshwari, daughter of Madhav Joo Dhar)",
                "period": "1625–1721 CE — 17th–18th century, Srinagar",
                "desc": (
                    "Mystic poetess, Shakti saint and living embodiment of Kashmir Shaivism. "
                    "Born in Srinagar to Pandit Madhav Joo Dhar (Dhar gotra, Vasishtha lineage). "
                    "Married Pandit Prana Koul but renounced household life for Shiva-sadhana. "
                    "Considered a Shakti incarnation — tradition holds she manifested miraculous powers. "
                    "Her shrine: Fateh Kadal, Srinagar (Rupa Bhawani Mandir) — active KP pilgrimage site. "
                    "Second shrine: Rainawari, Srinagar. "
                    "Philosophical teaching: body as temple of Shiva-Shakti, non-duality in bhakti. "
                    "Key Vakh: 'Zaan tse Aham Brahmasmi / Yeli che nab nab Suyii' — "
                    "Know thyself as Brahman; when the sky is sky, that alone is. "
                    "Works: Vakhs of Rupa Bhawani — collected oral verses in Kashmiri, "
                    "some compiled in 'Vakhs of Rupa Bhawani' (KP community publications). "
                    "Festivals: Her birth anniversary (Rupa Bhawani Jayanti) observed by KPs. "
                    "Academic reference: 'The Mystic Poetesses of Kashmir' — various scholars."
                ),
                "tradition": "Kashmir Shaivism / Shakta / Bhakti",
                "link": "https://en.wikipedia.org/wiki/Rupa_Bhawani",
                "archive": "https://archive.org/search?query=rupa+bhawani+vakhs+kashmir+shaivism",
            },
            {
                "title": "Mata Vatasta · माता वितस्ता (River Goddess Vitasta)",
                "author": "Divine — Vitasta Devi (Jhelum river goddess)",
                "period": "Ancient — Rigvedic to present",
                "desc": (
                    "Vitasta (the river Jhelum) is the sacred mother of Kashmir — "
                    "mentioned in the Rigveda (Nadistuti hymn, 10.75) as one of the great rivers of India. "
                    "The Nilamata Purana (6th–8th c.) dedicates extensive verses to her worship: "
                    "'Vitasta is the mother; she alone nourishes Kashmir.' "
                    "The valley of Kashmir was originally the lake Satisar — Vitasta drained it, "
                    "making the land habitable (Nilamata Purana mythology). "
                    "Source: Verinag spring (Anantnag district) — a beautiful octagonal Mughal-era "
                    "spring that is one of Kashmir's holiest sites. "
                    "KP rituals: Vitasta Jayanti is observed annually. Shraddha rites are performed "
                    "on the banks of the Vitasta. Water from Vitasta is used in all major KP rituals. "
                    "The Vitasta Stotram (from Nilamata Purana) is recited by KP priests. "
                    "Reference: Nilamata Purana (translated by Ved Kumari Ghai, JKAAS publication)."
                ),
                "tradition": "Kashmiri river-goddess worship / Nilamata Purana / Shakta",
                "link": "https://en.wikipedia.org/wiki/Jhelum_River",
                "archive": "https://www.wisdomlib.org/hinduism/book/nilamata-purana",
            },
            {
                "title": "Bhagwan Gopinath Ji · भगवान गोपीनाथ जी (1898–1968 CE)",
                "author": "Bhagwan Gopinath (born Gopinath Bhat)",
                "period": "1898–1968 CE — Srinagar",
                "desc": (
                    "One of the most beloved modern KP saints and a direct embodiment of Kashmir Shaivism. "
                    "Born 1898 in Rainawari, Srinagar, to a KP Brahmin family. "
                    "From childhood he entered spontaneous samadhi states — neighbours found him motionless "
                    "for hours in deep consciousness. Never accepted formal disciples; lived in complete simplicity. "
                    "Known for miraculous healings, clairvoyance, and a radiant presence that transformed all who met him. "
                    "His teaching was wordless — his very presence was the teaching (shaktipat by darshan). "
                    "Deep connection with Lal Ded's tradition — he embodied 'Pratyabhijña' as direct recognition, not philosophy. "
                    "Swami Lakshman Joo was his contemporary and they were mutually reverential. "
                    "Shrine: Rainawari, Srinagar — active pilgrimage site for KPs worldwide. "
                    "Annual: Gopinath Jayanti celebrated by KP community. "
                    "Books: 'Bhagwan Gopinath: The Divine Flame' (devotees' accounts, KP Sabha publications), "
                    "'Saintly Saga of Bhagwan Gopinath' — anecdote collections by devotees. "
                    "Website: gopinathji.com (devotee resource)."
                ),
                "tradition": "Kashmir Shaivism / Pratyabhijña / living saint tradition",
                "link": "https://en.wikipedia.org/wiki/Bhagwan_Gopinath",
                "archive": "https://archive.org/search?query=bhagwan+gopinath+kashmir+saint",
            },
            {
                "title": "Swami Merza Kak Ji · स्वामी मेर्ज़ा कक जी",
                "author": "Swami Merza Kak Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Revered Kashmiri Pandit saint from the Kak lineage (Jamadagni gotra). "
                    "A Shaiva Swami in the Trika-Pratyabhijña tradition of Kashmir Shaivism. "
                    "Known for intense tapas (austerity), mastery of Shaiva mantras and the "
                    "ability to guide lay devotees through complex ritual and philosophical questions. "
                    "The Kak family has ancient associations with Shaiva priesthood and the "
                    "Datthtreya gotra tradition. His teachings drew on the Shiva Sutras of Vasugupta, "
                    "the Spanda Karikas, and the oral Vakh tradition of Lal Ded. "
                    "Venerated locally through oral family traditions and shrine worship in Srinagar. "
                    "His memory preserved in the Kak community's spiritual oral lineage."
                ),
                "tradition": "Kashmir Shaivism / Trika",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "https://archive.org/search?query=kashmiri+pandit+saints+shaivism",
            },
            {
                "title": "Krishna Joo Razdan · कृष्ण जू रज़दन",
                "author": "Krishna Joo Razdan",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit saint and devotee from the illustrious Razdan lineage "
                    "(Gautama / Dhaumyayana gotra — see the Bhannamasis table). "
                    "The Razdan surname appears in 7 distinct gotra lineages in the KP tradition, "
                    "reflecting the antiquity and spread of this family. "
                    "Krishna Joo Razdan was known for deep bhakti toward Shiva and expertise in "
                    "the Kul Devi puja tradition (Kheer Bhawani / Ragnya Devi). "
                    "A practitioner of the Kashmir Shaiva path, he guided KP families in Srinagar "
                    "through ritual, mantra and philosophical instruction rooted in Pratyabhijña. "
                    "His teachings emphasised the unity of Shiva-consciousness in every act of daily life. "
                    "Venerated particularly by the Razdan community of old-city Srinagar."
                ),
                "tradition": "Kashmir Shaivism / KP devotional tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Laxman Joo Razdan · लक्ष्मण जू रज़दन",
                "author": "Laxman Joo Razdan",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit saint from the Razdan family — closely related in lineage to Krishna Joo Razdan, "
                    "likely from the same extended family tradition. "
                    "Note: Not to be confused with Swami Lakshmanjoo (the academic master); this is a separate "
                    "figure in the KP devotional saint tradition. "
                    "Known for austere sadhana, deep knowledge of Shaiva mantras and puja vidhi, "
                    "and oral transmission of the Lal Ded Vakh tradition within the Razdan community. "
                    "His spiritual lineage connects the Razdan family's Gautama/Dhaumyayana gotra tradition "
                    "with the living Pratyabhijña practice of Kashmir Shaivism. "
                    "Venerated for his blessings at family ceremonies — particularly Herath, Navreh and Janmashtami."
                ),
                "tradition": "Kashmir Shaivism / KP devotional tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Kash Kak Ji · काश कक जी",
                "author": "Kash Kak Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Revered saint from the Kak lineage of Kashmiri Pandits (Jamadagni gotra). "
                    "Known as a Siddha (perfected being) in the Kashmir Shaiva tradition — "
                    "his spiritual powers and compassionate guidance made him a sought-after figure "
                    "across the Srinagar KP community. "
                    "The name 'Kash' relates to the root 'Kash' (to shine) — an auspicious Kashmiri name "
                    "connected to Kashmir itself (Ka = Brahma, Shmir = to dry = the dried lake Satisar). "
                    "His sadhana path: intense Shiva-mantra japa, Kul Devi puja and the Herath Vatak ritual. "
                    "The Kak family's Datthtreya gotra tradition (from the Bhannamasis table) is one of the "
                    "most prominent in the KP priestly lineage. Memory preserved in Kak family oral traditions "
                    "and at local Srinagar shrines."
                ),
                "tradition": "Kashmir Shaivism / Siddha tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Kral Bab Ji · क्राल बाब जी",
                "author": "Kral Bab Ji",
                "period": "19th–20th century CE — Kashmir Valley",
                "desc": (
                    "Beloved KP saint known by the honorific 'Bab Ji' — a title of deep respect "
                    "given to realised masters and elder saints in Kashmir (used similarly to 'Baba'). "
                    "'Kral' in Kashmiri refers to the potter community — suggesting either artisan origins, "
                    "a village name, or metaphorical reference (the potter who shapes consciousness = Shiva). "
                    "Venerated as a Shaiva Siddha who embodied simplicity and seva (selfless service). "
                    "His teachings focused on: accessibility to all regardless of caste/standing, "
                    "direct devotion to Shiva without complex ritual, and the Lal Ded teaching that "
                    "Shiva is found within the self. "
                    "Known for miraculous deeds (healings, prophetic dreams) described in KP oral tradition. "
                    "His dargah/sthal is visited for blessings before important life events."
                ),
                "tradition": "Kashmir Shaivism / popular Siddha tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Swami Tik Kak Ji · स्वामी टिक कक जी",
                "author": "Swami Tik Kak Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit Swami-saint from the Kak (Jamadagni gotra) and Tikku (Bharadwaja gotra) "
                    "lineage — 'Tik' is the Kashmiri form of Tikku/Tickoo. "
                    "As a Swami (formal renunciate), he took vows in the Kashmir Shaiva monastic tradition. "
                    "Practiced and transmitted the Trika-Pratyabhijña path: the three means of liberation "
                    "(Shambhavopaya, Shaktopaya, Anavopaya) from the Shiva Sutras. "
                    "Known for guiding householder devotees (grihastha shishyas) in integrating "
                    "Kashmir Shaiva philosophy with daily KP ritual life — Herath, Nityakarma, Kul Devi puja. "
                    "His teachings on the Spanda doctrine (divine vibration) were particularly influential "
                    "in the Srinagar KP community. Memory preserved through disciples' families."
                ),
                "tradition": "Kashmir Shaivism / Trika / Spanda",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Swami Nand Lal Ji · स्वामी नन्द लाल जी",
                "author": "Swami Nand Lal Ji",
                "period": "19th–20th century CE — Kashmir",
                "desc": (
                    "Kashmiri Pandit renunciate and spiritual master of the Shaiva monastic tradition. "
                    "The name Nand Lal is deeply Kashmiri: Nanda (bliss / devotee) + Lal (beloved / Shiva). "
                    "As a Swami, he embodied the Trika teaching that renunciation is inner, not merely external. "
                    "Known for his exposition of the Shiva Sutras and Spanda Karikas to lay devotees — "
                    "making the deepest philosophical teachings of Kashmir Shaivism accessible to KP householders. "
                    "Particular strength: the Anavopaya path (individual means) — mantra, pranayama, "
                    "and the Nityakarma daily ritual as a form of Pratyabhijña practice. "
                    "His disciple lineage maintained the oral tradition of his teachings in Kashmir. "
                    "Context: Contemporary of Swami Lakshman Joo — both represent the final flourishing "
                    "of the living Kashmir Shaivism tradition before the 1990 exodus."
                ),
                "tradition": "Kashmir Shaivism / Trika / Spanda",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Sidh Bab · सिद्ध बाब (Siddha tradition)",
                "author": "Multiple Siddha masters — Siddha Shrikantha (Lal Ded's guru) most celebrated",
                "period": "Medieval to modern — ongoing tradition",
                "desc": (
                    "'Sidh Bab' (Siddha Baba) is the honorific given to perfected Shaiva masters in Kashmir — "
                    "saints who have achieved Siddhi (spiritual perfection) through the Trika path. "
                    "The most celebrated historical Sidh Bab: Siddha Shrikantha Swami — the guru of Lalleshwari. "
                    "He belonged to the Shaiva Siddha lineage of Kashmir and transmitted the Pratyabhijña "
                    "recognition-path to Lal Ded, catalysing her transformation. "
                    "Multiple Sidh Bab figures exist across the Kashmir Valley: each is venerated as a "
                    "Kshetrapala (field protector) of a locality. Their shrines (often a stone, tree or spring) "
                    "dot the landscape of Kashmir. "
                    "In the Trika tradition, a Siddha has mastered: Khechari mudra, Pratyabhijña, "
                    "and the 36-tattva cosmology. The 84 Siddhas (Chaurasi Siddha) tradition also "
                    "intersects with Kashmiri Shaivism. "
                    "Reference: Alexis Sanderson's papers on Kashmir Shaivism siddha traditions (Oxford)."
                ),
                "tradition": "Kashmir Shaivism / Siddha tradition",
                "link": "https://en.wikipedia.org/wiki/Siddha",
                "archive": "https://www.wisdomlib.org/definition/siddha#kashmir",
            },
            {
                "title": "Paramanand · परमानन्द",
                "author": "Paramanand (Kashmiri saint)",
                "period": "19th–20th century CE",
                "desc": (
                    "Kashmiri Pandit saint whose very name encodes the highest Shaiva teaching: "
                    "Parama (supreme) + Ananda (bliss) = the supreme bliss of Brahman / Shiva. "
                    "In the Trika tradition, Paramananda is technically a name for the state of "
                    "liberated consciousness — Anuttara (the unsurpassable), the highest of the 36 tattvas. "
                    "This saint embodied the name through his direct experience of non-dual awareness "
                    "and his transmission of that joy to all who sought him. "
                    "Venerated by KP families for spiritual guidance, especially in Kul Devi puja tradition "
                    "and the Herath ritual. His teachings emphasised that ananda (bliss) is not a state "
                    "to be achieved but recognised as one's own nature — pure Pratyabhijña. "
                    "Reference: The name Paramananda appears in the KP spiritual lineage preserved "
                    "in the Bhannamasis gotra records and community oral histories."
                ),
                "tradition": "Kashmir Shaivism / Pratyabhijña",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Madhav Das Ji · माधव दास जी",
                "author": "Madhav Das Ji",
                "period": "18th–19th century CE",
                "desc": (
                    "Kashmiri Pandit saint whose name honours Madhava — a name of Vishnu/Krishna "
                    "(Ma = Lakshmi, Dhava = lord = Lord of Lakshmi). "
                    "Significant lineage connection: Rupa Bhawani's father was Pandit Madhav Joo Dhar — "
                    "illustrating the deep connection between the Madhav devotional lineage and "
                    "the Kashmir Shaiva-Shakta tradition. "
                    "Madhav Das Ji combined Vaishnava bhakti (devotion to Madhava/Vishnu) with the "
                    "Kashmir Shaiva non-dual philosophy — reflecting the characteristic KP synthesis "
                    "of Shaiva and Vaishnava streams. "
                    "This Shaiva-Vaishnava synthesis is documented in the Svamina Bharadwaja lineage "
                    "(Bhannamasis table) where both Shiva and Vishnu worship coexist in single families. "
                    "His teachings on Madhava bhakti within the Trika framework were significant for "
                    "KP communities who maintained both Shaiva and Vaishnava household traditions."
                ),
                "tradition": "Kashmir Shaivism / Vaishnava-Shaiva synthesis",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Nand Lal Sahib Ji · नन्द लाल साहिब जी",
                "author": "Nand Lal Sahib Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Revered KP saint given the double honorific 'Sahib Ji' — a title of great reverence "
                    "used in Kashmir for both Sufi pirs and Hindu saints, reflecting the valley's syncretic tradition. "
                    "Nand Lal Sahib Ji is remembered for his extraordinary compassion, accessibility to all, "
                    "and his practice of Kashmir Shaiva sadhana through daily ritual, mantra and "
                    "the living transmission of Lal Ded's Vakh tradition. "
                    "Core teaching: 'Anuttara' — the Supreme, Shiva, is ever-present; "
                    "Pratyabhijña is available in every moment of consciousness. "
                    "Known for healing the spiritually distressed and guiding families through "
                    "the upheavals of 19th–20th century Kashmir. "
                    "Venerated at his samadhi sthal in Srinagar where devotees offer flowers and prayers. "
                    "His memory kept alive through oral traditions in multiple KP families of Srinagar."
                ),
                "tradition": "Kashmir Shaivism / popular devotion",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
            {
                "title": "Gobind Koul Ji · गोबिन्द कौल जी",
                "author": "Gobind Koul Ji",
                "period": "19th–20th century CE — Srinagar",
                "desc": (
                    "Kashmiri Pandit saint from the Koul family — one of the most widespread KP lineages "
                    "(Kashyapa and Kaushika gotras; Datthtreya Koul and Svamina Rishi Kanya Gargya lineages "
                    "from the Bhannamasis table). "
                    "The name Gobind (Sanskrit: Go = cows/senses + Vinda = finder = 'One who finds/controls the senses' = Vishnu/Krishna) "
                    "combined with the Koul lineage illustrates the Shaiva-Vaishnava synthesis of KP spirituality. "
                    "Known for mastery of Shaiva mantras, puja vidhi and oral transmission of the Trika tradition "
                    "within the Koul community of Srinagar. "
                    "Venerated for his ability to guide families through the Herath ritual, "
                    "Kul Devi puja (Kheer Bhawani / Sharika Devi), and the Nityakarma daily practice. "
                    "His teachings on Gobinda (Vishnu) as a manifestation of Shiva reflect the "
                    "non-sectarian spirit of Kashmir Shaivism."
                ),
                "tradition": "Kashmir Shaivism / KP Koul lineage tradition",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits",
                "archive": "",
            },
        ],
        "Kashmiri Saints — Extended · अन्य संत": [
            {
                "title": "Swami Lakshman Joo · स्वामी लक्ष्मण जू (1907–1991)",
                "author": "Swami Lakshman Joo (born Laxman Raina)",
                "period": "1907–1991 CE — Srinagar",
                "desc": "The last great master of the living Kashmir Shaivism tradition. Born in Srinagar into a KP family, he received shaktipat initiation at age 8 by Swami Mahatabakak Ji. Spent his entire life in Srinagar — first at Ishber (Nishat) garden, later at his Ishwara Ashram. Taught the Shiva Sutras, Vijnana Bhairava, Spanda Karikas to generations of students including western scholars. His works: Kashmir Shaivism: The Secret Supreme, Shiva Sutras commentary, Vijnana Bhairava commentary, Bhagavad Gita in light of Kashmir Shaivism. Transmitted the complete Trika-Pratyabhijña oral lineage. Regarded as a Siddha (perfected master) who embodied the recognition (pratyabhijña) he taught.",
                "tradition": "Kashmir Shaivism / Pratyabhijña / Living tradition",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+kashmir+shaivism",
            },
            {
                "title": "Abhinavagupta · अभिनवगुप्त (c. 975–1025 CE)",
                "author": "Abhinavagupta (born in Srinagar)",
                "period": "c. 975–1025 CE — Srinagar, Kashmir",
                "desc": "The greatest philosopher-saint of Kashmir Shaivism — and arguably the greatest Tantric philosopher in history. Born into a Brahmin family in Srinagar. Studied under 15+ teachers including Shambhunatha (Kula), Lakshmanagupta (Pratyabhijña), Bhutiraja (Trika). His works span philosophy, mysticism, aesthetics, and poetics. Key works: Tantraloka (37 chapters), Tantrasara, Abhinavabharati, Paramarthasara, Paratrishika Vivarana, and commentaries on the Pratyabhijña Karikas. Composed the Bhairavastava (Hymn to Bhairava) as his final act before entering the Bhairava cave at Bheravaguhya with 1200 disciples — and never returning. A Siddha of the highest order.",
                "tradition": "Trika / Pratyabhijña / Kula / Spanda",
                "link": "https://en.wikipedia.org/wiki/Abhinavagupta",
                "archive": "https://archive.org/search?query=abhinavagupta+kashmir+shaivism",
            },
            {
                "title": "Vasugupta · वसुगुप्त (c. 800–850 CE)",
                "author": "Vasugupta",
                "period": "c. 800–850 CE — Kashmir",
                "desc": "The first great systematiser of Kashmir Shaivism. Received the Shiva Sutras in a vision on Mahadeva (Shankaracharya) Hill, Srinagar — either carved on a rock or revealed in a dream. Also authored the Spanda Karikas (or inspired them — attributed to his disciple Kallata). Teacher of Kallata. His two texts — Shiva Sutras and Spanda Karikas — founded the entire Kashmir Shaivism tradition.",
                "tradition": "Pratyabhijña / Spanda",
                "link": "https://en.wikipedia.org/wiki/Vasugupta",
                "archive": "https://archive.org/search?query=vasugupta+shiva+sutras+kashmir",
            },
            {
                "title": "Utpaladeva · उत्पलदेव (c. 875–925 CE)",
                "author": "Utpaladeva",
                "period": "c. 875–925 CE — Kashmir",
                "desc": "Disciple of Somananda and teacher of Lakshmanagupta (who taught Abhinavagupta). The most philosophically rigorous thinker of the Pratyabhijña school. Works: Ishvarapratyabhijña Karikas (the masterwork), Shivadrishti Vritti (commentary on Somananda), Ajadapramatarasiddhi, Shivastotravali (20 devotional hymns). Established recognition (pratyabhijña) as the path to liberation — deeper and more thorough than both Buddhist and Advaita Vedanta schools.",
                "tradition": "Pratyabhijña",
                "link": "https://en.wikipedia.org/wiki/Utpaladeva",
                "archive": "https://archive.org/search?query=utpaladeva+pratyabhijna",
            },
            {
                "title": "Kshemaraja · क्षेमराज (c. 1000–1050 CE)",
                "author": "Kshemaraja (direct disciple of Abhinavagupta)",
                "period": "c. 1000–1050 CE — Kashmir",
                "desc": "Abhinavagupta's most prominent disciple. His works are the most widely read today: Pratyabhijnahridayam (20 sutras — gateway text), Shiva Sutra Vimarsini, Spanda Nirnaya, Svacchanda Tantra Uddyota, Netra Tantra Uddyota. Made the abstruse philosophy of his guru accessible to general students. His Pratyabhijnahridayam is still used as the first text taught in Kashmir Shaivism study.",
                "tradition": "Pratyabhijña / Trika",
                "link": "https://en.wikipedia.org/wiki/Kshemaraja",
                "archive": "https://archive.org/search?query=kshemaraja+pratyabhijna",
            },
            {
                "title": "Somananda · सोमानन्द (c. 850–925 CE)",
                "author": "Somananda",
                "period": "c. 850–925 CE — Kashmir",
                "desc": "Founder of the Pratyabhijña philosophical school and teacher of Utpaladeva. Author of the Shivadrishti — the first systematic philosophical treatise of Kashmir Shaivism establishing that all experience is Shiva's own vision (drishti). A direct disciple of Vasugupta (through Kallata). His work forms the philosophical foundation on which Utpaladeva and Abhinavagupta built.",
                "tradition": "Pratyabhijña",
                "link": "https://en.wikipedia.org/wiki/Somananda",
                "archive": "https://archive.org/search?query=somananda+shivadrishti",
            },
            {
                "title": "Kallata · कल्लट (c. 850–900 CE)",
                "author": "Kallata",
                "period": "c. 850–900 CE — Kashmir",
                "desc": "Direct disciple of Vasugupta. Either authored or systematised the Spanda Karikas. His Vritti (brief commentary on Spanda Karikas) is the earliest commentary on that text. Teacher of the Spanda school — his student lineage later merged with Somananda's Pratyabhijña lineage through Abhinavagupta.",
                "tradition": "Spanda",
                "link": "https://en.wikipedia.org/wiki/Spanda_karikas",
                "archive": "https://archive.org/search?query=kallata+spanda+karikas",
            },
        ],
        "Lal Ded & Kashmiri Poetry · ललद्यद और काव्य": [
            {
                "title": "Lal Vākhs · लल वाख — Verses of Lalleshwari",
                "author": "Lalleshwari / Lal Ded (c. 1320–1392 CE)",
                "period": "14th century CE",
                "desc": (
                    "258+ mystical verses (Vakhs = 'speech/word' in Kashmiri) — the oldest literature "
                    "in the Kashmiri language and the foundation of all later KP spiritual poetry. "
                    "Language: Old Kashmiri (14th century Koshur) — a Dardic Indo-Aryan dialect. "
                    "Themes: (1) Shivoham — I am Shiva; the atman is Brahman. "
                    "(2) Futility of external ritual — 'I searched outside, Shiva is within.' "
                    "(3) Pranayama as path — the inner fire of prana as Kundalini Shakti. "
                    "(4) Non-dual love — Shiva as the beloved, creation as his dance. "
                    "(5) Social equality — transcending caste and religion. "
                    "Three celebrated Vakhs with Kashmiri originals: "
                    "· 'Lale ous yeli gurus vachas razi' — When I, Lalla, became alert to the Guru's word... "
                    "· 'Pranas apanas milawath karim' — When prana and apana unite... "
                    "· 'Akis akis panas akis' — One, and one, and one is one... "
                    "Editions: Jayalal Kaul 'Lal Ded' (Sahitya Akademi, 1973), "
                    "Ranjit Hoskote 'I, Lalla: The Poems of Lal Ded' (Penguin, 2011), "
                    "Coleman Barks translation (Maypop Books). "
                    "Academic: Grierson & Barnett 'Lallāvākyāni' (1920, Royal Asiatic Society) — first scholarly edition."
                ),
                "tradition": "Kashmir Shaivism / Lal Ded oral tradition",
                "link": "https://en.wikipedia.org/wiki/Lalleshwari",
                "archive": "https://archive.org/search?query=lal+ded+vakhs+lalleshwari+kashmiri",
            },
            {
                "title": "Shrukhs · श्रुख — Verses of Nund Rishi (Sheikh Nuruddin)",
                "author": "Nund Rishi / Sheikh Nuruddin Noorani (1377–1440 CE)",
                "period": "15th century CE",
                "desc": (
                    "Nund Rishi (Nund = pure/silent, Rishi = sage) — patron saint of all Kashmir, "
                    "founder of the Rishi Sufi order, and the most revered saint of the valley. "
                    "Born 1377 in Kaimoh village, Kulgam. Said to have been suckled as an infant by Lal Ded herself. "
                    "His Shrukhs (poems) in Kashmiri blend Shaiva and Sufi themes so seamlessly that "
                    "both traditions claim him. His order, the Rishis, practiced vegetarianism, "
                    "celibacy and integration with nature — unique in Sufi traditions. "
                    "Shrine: Charar-i-Sharief, Budgam — Kashmir's holiest Sufi site, destroyed in 1995 conflict, rebuilt. "
                    "Key Shrukh: 'Boh chu myon mantrith kur / Bhagwan kus tim karan wanun' — "
                    "I am that enchanted bird; who can tell me what Bhagwan is? "
                    "Works: Shrukhs (collected Kashmiri poems), preserved in oral and manuscript traditions. "
                    "Book: 'The Rishi Order of Kashmir' (academic studies), "
                    "'Nund Rishi: Patron Saint of Kashmir' (various KP community publications)."
                ),
                "tradition": "Rishi Sufi order / Shaiva-Sufi synthesis",
                "link": "https://en.wikipedia.org/wiki/Nund_Rishi",
                "archive": "https://archive.org/search?query=nund+rishi+shrukhs+kashmir",
            },
            {
                "title": "Vakhs of Rupa Bhawani · रूपा भवानी वाख",
                "author": "Rupa Bhawani (1625–1721 CE)",
                "period": "17th–18th century CE",
                "desc": (
                    "The Vakhs of Rupa Bhawani are among the most philosophically rich of all Kashmiri "
                    "mystic poetry — combining intense bhakti (devotion) with the rigorous non-dual philosophy "
                    "of Kashmir Shaivism. Written in classical Kashmiri with Sanskrit elements. "
                    "Key themes: body as Shiva-Shakti union, dissolution of ego-identity, "
                    "the Guru as the Grace of Shiva, and direct recognition of supreme consciousness. "
                    "Key Vakh: 'Zaan tse Aham Brahmasmi / Yeli che nab nab Suyii' — "
                    "Know thyself as I am Brahman; when the sky is sky, that alone is. "
                    "Editions: 'Vakhs of Rupa Bhawani' — compiled by KP Sabha Jammu; "
                    "also preserved in oral family traditions across the KP diaspora. "
                    "Academic: Referenced in 'Women Saints of India' and Kashmiri Shaivism studies."
                ),
                "tradition": "Kashmir Shaivism / Shakta / Bhakti poetry",
                "link": "https://en.wikipedia.org/wiki/Rupa_Bhawani",
                "archive": "https://archive.org/search?query=rupa+bhawani+kashmir+poetry",
            },
            {
                "title": "Songs of Habba Khatoon · हब्बा खातून",
                "author": "Habba Khatoon (c. 1554–1609 CE)",
                "period": "16th century CE",
                "desc": (
                    "Called the 'Nightingale of Kashmir' (Bulbul-e-Kashmir). Born Zooni (moon-face) "
                    "in Chandahar village, married Yusuf Shah Chak (last independent sultan of Kashmir) "
                    "before Akbar annexed the valley in 1586. Her Lol (lyric songs) express the "
                    "intense viraha (love-in-separation) for her exiled husband — and at a deeper level, "
                    "for the beloved divine. The most musically beautiful voice in Kashmiri literature. "
                    "Key song: 'Rozis na biyus dilbar myon' — My beloved does not return. "
                    "Her songs are still sung at Kashmiri festivals, especially spring and Navreh. "
                    "Editions: 'Habba Khatoon: Poems' — translated by Trilokinath Raina, "
                    "Sahitya Akademi publication. "
                    "Academic: 'The Nightingale of Kashmir' — multiple literary studies. "
                    "Her memorial: Government College for Women, Srinagar bears her name."
                ),
                "tradition": "Classical Kashmiri lyric poetry",
                "link": "https://en.wikipedia.org/wiki/Habba_Khatoon",
                "archive": "https://archive.org/search?query=habba+khatoon+kashmir+poetry",
            },
            {
                "title": "Vakhs of Arnimal · अर्निमल",
                "author": "Arnimal (c. 18th century CE)",
                "period": "18th century CE",
                "desc": (
                    "Kashmiri poetess whose Vakhs uniquely blend personal anguish with spiritual longing. "
                    "Her husband remarried, and she channelled that pain into some of Kashmiri literature's "
                    "most poignant verses — the private becomes universal. "
                    "Her language bridges the mystical Vakh tradition of Lal Ded with the personal lol "
                    "(lyric) tradition of Habba Khatoon. "
                    "Considered the third great woman poet of Kashmir after Lal Ded and Habba Khatoon. "
                    "Key Vakh: 'Suy myon yar, suy myon dilbar / Suy myon chu sahib-i-jamal' — "
                    "He is my friend, he is my beloved / He is my master of beauty. "
                    "Editions: 'Arnimal: Selected Poems' — Sahitya Akademi and KP literary organisations. "
                    "Academic: Referenced in studies of Kashmiri women's literature and Bhakti traditions."
                ),
                "tradition": "Kashmiri Bhakti / lyric poetry",
                "link": "https://en.wikipedia.org/wiki/Arnimal",
                "archive": "https://archive.org/search?query=arnimal+kashmiri+poetry",
            },
            {
                "title": "Swami Lakshman Joo · स्वामी लक्ष्मण जू (1907–1991 CE)",
                "author": "Swami Lakshmanjoo (born Laxman Raina)",
                "period": "1907–1991 CE — Srinagar",
                "desc": (
                    "The last great master (acharya) of the living Kashmir Shaivism tradition. "
                    "Born 1907 in Srinagar, he spent his entire life there — never leaving Kashmir. "
                    "Disciple of Swami Mahatab Koul. Mastered the entire Kashmir Shaivism corpus: "
                    "Tantraloka, Spanda Karikas, Shiva Sutras, Pratyabhijnahridayam. "
                    "Brought the Trika tradition to global audiences through recorded lectures and writings. "
                    "His ashram: Ishber, Nishat, Srinagar (still active). "
                    "Key works: 'Kashmir Shaivism: The Secret Supreme' (Universal Shaiva Fellowship, 1988) — "
                    "the most authoritative modern English exposition of the tradition. "
                    "Also: 'Shiva Sutras: The Supreme Awakening', 'Vijnanabhairava: The Manual for Self Realization', "
                    "'Self Realization in Kashmir Shaivism' (all Universal Shaiva Fellowship). "
                    "Audio: 200+ hours of recorded lectures — available at universalshaivafelllowship.org. "
                    "Website: universalshaivafelllowship.org · lakshmanjoo.com"
                ),
                "tradition": "Kashmir Shaivism / Trika / Pratyabhijña — modern transmission",
                "link": "https://en.wikipedia.org/wiki/Swami_Lakshmanjoo",
                "archive": "https://archive.org/search?query=swami+lakshmanjoo+kashmir+shaivism",
            },
        ],
        "Kashmiri Poets & Writers · काव्य एवं साहित्य": [
            {
                "title": "Mahmud Gami · महमूद गामी (c. 1765–1855 CE)",
                "author": "Mahmud Gami (Mahmud of Gam village)",
                "period": "c. 1765–1855 CE",
                "desc": "The greatest classical poet of Kashmiri language — equivalent to Shakespeare in his mastery of Kashmiri poetic forms. A Muslim by faith but deeply steeped in Sanskrit and Kashmiri Hindu literary traditions. His Yusuf-Zulaykha (retelling of the Joseph story) is considered the finest long poem in Kashmiri. Also wrote versions of Shirin-Farhad and Banu-Nala. His poetry demonstrates the remarkable Hindu-Muslim literary synthesis of Kashmir's golden age. Editions: Sahitya Akademi publications.",
                "tradition": "Classical Kashmiri literature",
                "link": "https://en.wikipedia.org/wiki/Mahmud_Gami",
                "archive": "https://archive.org/search?query=mahmud+gami+kashmiri+poetry",
            },
            {
                "title": "Zinda Kaul (Masterji) · ज़िन्दा कौल (1884–1965 CE)",
                "author": "Zinda Kaul (pen name: Masterji)",
                "period": "1884–1965 CE — Srinagar",
                "desc": "The foremost modern KP poet in the Kashmiri language. A schoolteacher (hence Masterji) who revived and modernised Kashmiri poetry in the 20th century. His collection 'Sumran' (Remembrance) is a landmark of modern Kashmiri literature. Recipient of the Sahitya Akademi Award (1956) — first Kashmiri writer to receive it. Deeply influenced by Lal Ded's Vakh tradition and Sufi poetry.",
                "tradition": "Modern Kashmiri literature",
                "link": "https://en.wikipedia.org/wiki/Zinda_Kaul",
                "archive": "https://archive.org/search?query=zinda+kaul+kashmiri+poetry",
            },
            {
                "title": "Ghulam Ahmad Mahjoor · ग़ुलाम अहमद महजूर (1887–1952 CE)",
                "author": "Ghulam Ahmad Mahjoor",
                "period": "1887–1952 CE",
                "desc": "Called the 'Wordsworth of Kashmir' — the poet who brought the natural beauty of the Valley into Kashmiri verse. His poetry of the mountains, rivers, and seasons of Kashmir is beloved by all Kashmiris. Influenced by both Lal Ded and Persian/Sufi poetry. His collection 'Mahjoor' is a standard Kashmiri text. Works alongside Zinda Kaul to represent the two poles of modern Kashmiri literary tradition.",
                "tradition": "Modern Kashmiri literature",
                "link": "https://en.wikipedia.org/wiki/Mahjoor",
                "archive": "https://archive.org/search?query=mahjoor+kashmiri+poet",
            },
            {
                "title": "Kalhana · कल्हण (c. 1100–1150 CE)",
                "author": "Kalhana (son of Champaka, minister of King Harsha)",
                "period": "c. 1148–1150 CE",
                "desc": "Author of the Rajatarangini — Kashmir's great Sanskrit chronicle. A KP Brahmin scholar who was the first Indian historian to write a systematic historical work with critical analysis of sources. His opening statement: 'The praise-worthy poet is one who, free from passion, describes the past events like a judge.' Unique in Indian literary history for its historical consciousness. His family background: father was minister under King Harsha of Kashmir.",
                "tradition": "Sanskrit literature / History",
                "link": "https://en.wikipedia.org/wiki/Kalhana",
                "archive": "https://archive.org/search?query=kalhana+rajatarangini",
            },
            {
                "title": "Bilhana · बिल्हण (c. 1050–1100 CE)",
                "author": "Bilhana of Kashmir",
                "period": "c. 1050–1100 CE",
                "desc": "Kashmiri Sanskrit poet who left Kashmir and became court poet of King Vikramaditya VI of the Chalukya dynasty in Kalyana (Karnataka). Author of the Vikramankadevacharita (biography of his patron) and the Chaurapanchasika — 50 erotic-mystical verses about a forbidden love. The Chaurapanchasika is among the most translated Sanskrit poems; it influenced Persian and Mughal miniature painting traditions.",
                "tradition": "Sanskrit literature / Kashmir school",
                "link": "https://en.wikipedia.org/wiki/Bilhana",
                "archive": "https://archive.org/search?query=bilhana+chaurapanchasika+kashmir",
            },
            {
                "title": "Ksemendra · क्षेमेन्द्र (c. 990–1065 CE)",
                "author": "Ksemendra of Kashmir",
                "period": "c. 990–1065 CE",
                "desc": "The most prolific Kashmiri Sanskrit author — a student of Abhinavagupta. Wrote in almost every Sanskrit literary genre: satire (Desopadesa, Kalavilasa), condensed epics (Ramayana-Manjari, Mahabharata-Manjari, Brihatkatha-Manjari), political science (Niti-Kalpataru), and poetics (Kavikanthabharan). His satires on corrupt society — doctors, merchants, women — are razor-sharp and still remarkably modern.",
                "tradition": "Sanskrit literature / Kashmir school",
                "link": "https://en.wikipedia.org/wiki/Ksemendra",
                "archive": "https://archive.org/search?query=ksemendra+kashmir+sanskrit",
            },
            {
                "title": "Somadeva · सोमदेव (c. 1063–1081 CE)",
                "author": "Somadeva Bhatta",
                "period": "c. 1063–1081 CE",
                "desc": "Author of the Kathasaritsagara — 'The Ocean of the Streams of Story' — a massive collection of 18 books and 124 chapters containing 350+ stories derived from Gunadhya's Brihatkatha. The greatest story collection in Sanskrit. Composed for Queen Suryamati of Kashmir. Contains fairy tales, frame stories, philosophical parables, and erotica — the source of many stories in Arabian Nights and European folk literature.",
                "tradition": "Sanskrit literature / Kashmir",
                "link": "https://en.wikipedia.org/wiki/Somadeva",
                "archive": "https://archive.org/search?query=somadeva+kathasaritsagara",
            },
        ],
        "Kashmiri Culture & Customs · संस्कृति": [
            {
                "title": "Herath (Kashmiri Shivratri) · हेरथ",
                "author": "Living KP tradition — ancient origin",
                "period": "Phalguna Krishna Chaturdashi (Feb–Mar) — annual",
                "desc": (
                    "The most sacred Kashmiri Pandit festival — entirely distinct from mainstream Shivratri. "
                    "Etymology: 'Herath' derives from 'Hara-ratri' (night of Hara/Shiva). "
                    "3-day ritual sequence: "
                    "Day 1 (Salam, 13th night): 12 earthen pots (Vatak) filled with water are set up — "
                    "each represents one of the 12 Shiva lingas and one Rishi. Sacred walnut (Shishur) "
                    "and ritual paraphernalia arranged. The 'Salam' (salutation to Shiva) is performed. "
                    "Day 2 (Vatak Puja, 14th): All-night worship of the Vatak pots as Shiva himself. "
                    "Bhairava is worshipped as Vatuk (child form of Bhairava). Purohit recites "
                    "Shiva Sutras, Spanda Karikas and specific Herath mantras through the night. "
                    "Day 3 (15th, Purnima): Paran (breaking of fast). Sweet Harissa, Nadru dishes served. "
                    "Unique elements: The walnut (Shishur) is the sacred fruit of Herath. "
                    "The 12 Vatak pots are unique to KP Herath — not found in pan-Indian Shivratri. "
                    "Sources: Nilamata Purana (Vatak tradition), Svacchanda Tantra (Bhairava worship)."
                ),
                "tradition": "Kashmiri Pandit ritual / Nilamata Purana",
                "link": "https://en.wikipedia.org/wiki/Herath",
                "archive": "https://archive.org/search?query=herath+kashmiri+pandit+shivratri+festival",
            },
            {
                "title": "Navreh · नवरेह — Kashmiri New Year",
                "author": "Living KP tradition — Chaitra Shukla Pratipada",
                "period": "Chaitra Shukla Pratipada (Mar–Apr) — annual",
                "desc": (
                    "Navreh (Nava + Varsha = New Year in Kashmiri) is the KP New Year — "
                    "one of the most joyous festivals. Observed on Chaitra Shukla Pratipada "
                    "(first day of the bright fortnight of Chaitra, Amavasyanta reckoning). "
                    "The night before (Navreh eve): A Navreh Thali (plate) is prepared with: "
                    "· Rice (dhaan) — prosperity · Walnut (doon) — wisdom "
                    "· Salt (noon) — flavour of life · Sugar (mishri) — sweetness "
                    "· Curd (dahi) — auspiciousness · Seasonal bread (tchot/kulcha) "
                    "· Spring flowers (narcissus, iris) · Pen and inkpot (learning) "
                    "· Coins (lakshmi) · Jantri (KP almanac — the most important item). "
                    "The Jantri contains the annual panchang, festivals, muhurtas and horoscope data. "
                    "Morning ritual: First sight on waking = omen for the year — hence the Thali is "
                    "placed where it will be seen first. Temple visit, exchange of Navreh Mubarak greetings. "
                    "Foods: Modur Pulav (sweet rice), Haakh, Nadru, Shufta (dry fruit sweet). "
                    "Reference: Nilamata Purana on Chaitra Pratipada, 'KP Festivals' (KPSS publications)."
                ),
                "tradition": "Kashmiri Pandit ritual / Nilamata Purana",
                "link": "https://en.wikipedia.org/wiki/Navreh",
                "archive": "https://archive.org/search?query=navreh+kashmiri+new+year+pandit",
            },
            {
                "title": "Kheer Bhawani Mela · खीर भवानी — Zyeth Ashtami",
                "author": "Living KP tradition",
                "period": "Jyeshtha Shukla Ashtami (May–Jun) — annual",
                "desc": (
                    "Annual pilgrimage to Kheer Bhawani temple at Tullamulla (Tulmul), Ganderbal — "
                    "the single largest annual gathering of Kashmiri Pandits. "
                    "The temple contains a sacred spring of changing colour. "
                    "Tradition holds: white water = peace and prosperity; dark/black water = trouble ahead. "
                    "The goddess: Ragnya Devi (Kheer Bhawani) — one of the principal Kul Devis of KPs. "
                    "Offering: Milk and Kheer (rice pudding with saffron) poured into the spring. "
                    "History: The temple was built over an ancient sacred spring mentioned in the "
                    "Nilamata Purana. Mughal records also mention it. Last major restoration: 20th century. "
                    "For the KP diaspora after 1990: Zyeth Ashtami melas are held worldwide with proxy puja. "
                    "Also: Multiple satellite Kheer Bhawani temples established by KPs in diaspora cities. "
                    "Reference: 'Kheer Bhawani: The Spring Goddess of Kashmir' (various academic studies)."
                ),
                "tradition": "Kashmiri Pandit pilgrimage / Shakta",
                "link": "https://en.wikipedia.org/wiki/Kheer_Bhawani",
                "archive": "https://archive.org/search?query=kheer+bhawani+tulmul+kashmir+zyeth+ashtami",
            },
            {
                "title": "KP Vivāha (Wedding) · कश्मीरी पण्डित विवाह",
                "author": "Living KP tradition",
                "period": "Auspicious muhurta dates",
                "desc": (
                    "Traditional KP wedding — a multi-day ritual combining Vedic, Shaiva and uniquely Kashmiri elements. "
                    "Pre-wedding: Devgun (invoking family deities — Kul Devi, Kul Devta, Bhairava), "
                    "Lagan (purohit ties auspicious thread, sets muhurta). "
                    "Wedding day: Wanwun songs (women's group songs specific to each ritual stage — "
                    "groom's arrival, Saptapadi, vidai). Dejhour (formal gift exchange between families). "
                    "Pheran ceremony (bride dressed in traditional Pheran + Tarang headpiece). "
                    "Kanyadan (father's gift of daughter). Saptapadi (7 steps around sacred fire). "
                    "Post-wedding: Khon Batta (homecoming feast). "
                    "Music: Live Wanwun singing — elderly women are custodians of these Kashmiri songs. "
                    "Purohit: Recites in Sanskrit with Kashmiri explanations. "
                    "Gotra check: Same-gotra marriage strictly forbidden (sagotra vivaha varjya). "
                    "Reference: 'Kashmiri Pandit Wedding Rituals' (KPSS, AIKS publications), "
                    "Sahitya Akademi resources on Kashmiri folk tradition."
                ),
                "tradition": "Kashmiri Pandit ritual / Vedic-Shaiva synthesis",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Customs_and_traditions",
                "archive": "https://archive.org/search?query=kashmiri+pandit+wedding+customs",
            },
            {
                "title": "Shrāddha & Pitru Paksha · श्राद्ध",
                "author": "Living KP tradition",
                "period": "Bhadrapada Krishna Paksha (Sep–Oct)",
                "desc": (
                    "Ancestral rites in KP tradition — unique in their Shaiva-Vedic synthesis. "
                    "Matamaal Shradh: rites for the maternal lineage (observed separately from paternal) — "
                    "unique to KP tradition and not common in other regional traditions. "
                    "Tithis: Each ancestor is remembered on their death tithi. Amavasya = for all. "
                    "Pinda Daan: Offered at Gaya (Bihar), Prayag, or on the banks of Vitasta (Jhelum). "
                    "Specific KP practices: Kashmiri Shaiva mantras (Shiva Sutras invocations) alongside "
                    "standard Vedic Shraddha mantras. The Purohit uses the Kashmiri panchang (Jantri) "
                    "for precise Amavasyanta tithi calculation. "
                    "Reference: 'Shraddha in the KP Tradition' (various pandit community publications), "
                    "Nilamata Purana ancestral rite references."
                ),
                "tradition": "Kashmiri Pandit ritual / Vedic ancestral tradition",
                "link": "https://en.wikipedia.org/wiki/Pitru_Paksha",
                "archive": "https://archive.org/search?query=shraddha+kashmiri+pandit+pitru",
            },
            {
                "title": "Nityakarma · नित्यकर्म — KP Daily Practice",
                "author": "Living KP tradition",
                "period": "Daily observance",
                "desc": (
                    "The complete daily ritual routine (Nityakarma) of a traditional KP: "
                    "· Brahma Muhurta (96 min before sunrise): waking, Achaman (sipping water thrice), "
                    "recitation of Shiva's names. "
                    "· Sandhya Vandana: morning prayer facing the rising sun — unique KP version "
                    "combines Vedic Gayatri with Kashmiri Shaiva mantras. "
                    "· Home shrine puja: offerings to Shiva linga, Kul Devi image, Naga (family serpent deity), "
                    "and ancestors (pitru). Incense, flowers, diya (lamp), naivedya (food offering). "
                    "· Surya Namaskar: 12 prostrations to the sun (Martand tradition of south Kashmir). "
                    "· Mantra japa: Om Namah Shivaya (primary); Mrityunjaya; Shiva Stotras. "
                    "· Evening: Deepa Puja (lamp lighting at dusk), recitation of Shiva Stotras or Lal Ded Vakhs. "
                    "· Herath nights: extended puja including Vatak worship. "
                    "Reference: 'Nityakarma: Daily Worship of Kashmiri Pandits' (KP community guides), "
                    "Svacchanda Tantra (Kshemaraja commentary) for ritual basis."
                ),
                "tradition": "Kashmiri Pandit ritual / Shaiva-Vedic",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Religious_practices",
                "archive": "https://archive.org/search?query=kashmiri+pandit+daily+ritual+nityakarma",
            },
            {
                "title": "Kashmiri Language & Sharada Script · कोशुर / शारदा",
                "author": "Linguistic heritage",
                "period": "Ancient — Dardic branch, script from c. 8th century CE",
                "desc": (
                    "Kashmiri (Koshur) is the ancient language of Kashmir — a Dardic Indo-Aryan language "
                    "spoken by ~7 million. One of the 22 Scheduled Languages of India (8th Schedule). "
                    "Three scripts: Sharada (traditional KP — most ancient), Nastaliq/Perso-Arabic "
                    "(current official script in J&K), and Devanagari. "
                    "Sharada script: Ancestor of Gurmukhi and Takri. Used for all KP religious manuscripts, "
                    "horoscopes (janmapatri), temple inscriptions. Named after Sharada Devi (Saraswati). "
                    "~10,000 Sharada manuscripts survive in libraries (Srinagar, Pune BORI, Berlin, London). "
                    "Unicode block: U+11180–U+111DF. Now endangered — taught in only a few KP families. "
                    "Dialects: Koshuri (urban Srinagar), Kishtwari, Poguli, Siraji, Rambani. "
                    "Notable: Kashmiri is the only language in India where the verb 'to be' is "
                    "completely dropped in present tense — a linguistic feature tied to Kashmir Shaivism's "
                    "teaching that Being (Shiva) is self-evident. "
                    "Resources: Kashmiri Language Project (kashmiri.net), "
                    "Sahitya Akademi Kashmiri publications, "
                    "'A Dictionary of Kashmiri Proverbs' (Grierson, 1929, archive.org available)."
                ),
                "tradition": "Linguistic heritage / Kashmiri culture",
                "link": "https://en.wikipedia.org/wiki/Kashmiri_language",
                "archive": "https://archive.org/search?query=kashmiri+language+sharada+script+manuscripts",
            },
        ],
        "Āgama & Root Tantras · आगम तन्त्र": [
            {
                "title": "Mālinīvijayottara Tantra · मालिनीविजयोत्तर तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "Supreme root Trika Agama. Describes the 36 tattvas, three Upayas (Shambhava, Shakta, Anava), and Trika cosmology of Shiva–Shakti–Nara. Abhinavagupta treats it as the highest Agama and bases the Tantraloka on it. Contains the Trika goddess triad (Para, Parapara, Apara).",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/malini-vijayottara-tantra",
                "archive": "https://archive.org/search?query=malinivijayottara+tantra",
            },
            {
                "title": "Siddhayogeśvarīmata · सिद्धयोगेश्वरीमत",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "Second root Trika Agama. Centers on Siddhayogesvari and the 64 yoginis. Key source for Kula-Trika synthesis, yogini worship, and the transmission of Kula doctrine through Shambhunatha's lineage.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/siddhayogesvarimata",
                "archive": "",
            },
            {
                "title": "Vijñānabhairava Tantra · विज्ञानभैरव तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-9th century CE",
                "desc": "112 dharanas (meditation techniques) for directly experiencing Bhairava-consciousness — through breath, sound, space, darkness, dissolution of thought. The most practical tantric text of Kashmir Shaivism. Translated by Paul Reps ('Centering'), Jaideva Singh, and Osho. Still used in daily sadhana.",
                "tradition": "Trika / Shaiva Agama",
                "link": "https://www.wisdomlib.org/hinduism/book/vijnana-bhairava-or-divine-consciousness",
                "archive": "https://archive.org/search?query=vijnana+bhairava+tantra",
            },
            {
                "title": "Svacchanda Tantra · स्वच्छन्द तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-9th century CE",
                "desc": "18 chapters on Svacchanda Bhairava — the 'self-willed' form of Shiva. Contains the most detailed Kashmiri Shaiva cosmology, initiatory rituals (diksha), mantras, yoga, and the description of the various Shaiva initiates. Kshemaraja's Uddyota commentary is the standard reading.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/svacchanda-tantra",
                "archive": "https://archive.org/search?query=svacchanda+tantra",
            },
            {
                "title": "Netra Tantra · नेत्र तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "The 'Eye' (Netra) tantra — focused on Amriteshvara (the lord of immortality). 22 chapters covering Mrityunjaya mantra, royal protection (raksha) rituals, yoga of the eye of Shiva, and the tantric path to immortality. Important source for Kashmiri royal ritual.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/netra-tantra",
                "archive": "https://archive.org/search?query=netra+tantra+kashmir",
            },
            {
                "title": "Paratrishikā · परात्रिंशिका",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "36 verses on Para — the supreme Shakti of Trika. Deals with the nature of mantra, the phonematic cosmology (Matrika — 50 Sanskrit letters as the body of the goddess), and supreme non-dual consciousness. Abhinavagupta's Vivarana commentary is longer than the root text.",
                "tradition": "Trika / Kula",
                "link": "https://www.wisdomlib.org/definition/paratrishika",
                "archive": "https://archive.org/search?query=paratrishika+vivarana",
            },
            {
                "title": "Mṛgendra Āgama · मृगेन्द्र आगम",
                "author": "Revealed text (Shaiva Siddhanta Agama)",
                "period": "Pre-10th century CE",
                "desc": "One of the 28 Shaiva Siddhanta Agamas — the Mrigendra deals with cosmology, Shaiva yoga, initiation, and the four padas (charya, kriya, yoga, jnana). Important for understanding the Agamic basis that Kashmiri Shaivism critiques and transcends.",
                "tradition": "Shaiva Siddhanta / Agama",
                "link": "https://www.wisdomlib.org/definition/mrigendra-agama",
                "archive": "https://archive.org/search?query=mrigendra+agama+shaiva",
            },
            {
                "title": "Tantrasadbhāva · तन्त्रसद्भाव",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "Important Trika-Kula Agama that forms a bridge between the Trika and Krama traditions. Contains detailed descriptions of the Kula goddesses, their mandalas, and the Kaula practices. Frequently quoted by Abhinavagupta in the Tantraloka.",
                "tradition": "Trika / Kula",
                "link": "https://www.wisdomlib.org/definition/tantrasadbhava",
                "archive": "https://archive.org/search?query=tantrasadbhava+kashmir",
            },
            {
                "title": "Jayadrathayāmala Tantra · जयद्रथयामल तन्त्र",
                "author": "Revealed text (Āgama)",
                "period": "Pre-10th century CE",
                "desc": "One of the largest Shakta-Shaiva Agamas — four 'Satkas' (sections of 6000 verses each). The fourth Satka is the Tantric source for the Kali traditions absorbed into Kashmir Shaivism. Contains detailed descriptions of the Krama goddess cycles and the 64-Bhairava traditions. Extensively cited by Abhinavagupta.",
                "tradition": "Shakta-Shaiva / Krama",
                "link": "https://www.wisdomlib.org/definition/jayadrathayamala",
                "archive": "https://archive.org/search?query=jayadrathayamala+tantra",
            },
            {
                "title": "Trika Hṛdaya · त्रिक हृदय",
                "author": "Attributed to Abhinavagupta / Traditional",
                "period": "c. 10th–11th century CE",
                "desc": "Short manual on the Trika system — the 'Heart of Trika'. Describes the essential practices of the three-goddess Trika: Para (supreme), Parapara (middling), and Apara (lower) — worshipped as the trident (trishula) of Shiva. Used as a daily practice guide in the tradition.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/trika",
                "archive": "https://archive.org/search?query=trika+hridaya+kashmir",
            },
            {
                "title": "Kulachudāmani Tantra · कुलचूडामणि तन्त्र",
                "author": "Revealed text (Kula Āgama)",
                "period": "c. 9th–10th century CE",
                "desc": "Short but important Kula Agama dealing with the 'Crest-jewel of the Kula' — the supreme Kula doctrine of non-dual Shakta practice. Contains the essence of Kaula initiation and the nature of the Kula tradition as a lineage (santana) of masters and disciples.",
                "tradition": "Kula / Kaula",
                "link": "https://www.wisdomlib.org/definition/kulachudamani",
                "archive": "https://archive.org/search?query=kulachudamani+tantra",
            },
        ],
        "Śiva Sūtras & Spanda · शिव सूत्र एवं स्पन्द": [
            {
                "title": "Śiva Sūtras · शिव सूत्र",
                "author": "Vasugupta (c. 875 CE)",
                "period": "c. 875 CE",
                "desc": "77 aphorisms in three sections — Shambhavopaya (7 sutras: divine means), Shaktopaya (10 sutras: energetic means), Anavopaya (45 sutras: individual means). Revealed to Vasugupta on Mahadeva (Shankaracharya) Hill, Srinagar. Foundation of the entire Kashmir Shaivism tradition. Commentaries by Kshemaraja (Vimarsini), Bhaskara, and Varadaraja.",
                "tradition": "Pratyabhijña / Trika",
                "link": "https://www.wisdomlib.org/hinduism/book/the-shiva-sutras",
                "archive": "https://archive.org/search?query=shiva+sutras+vasugupta",
            },
            {
                "title": "Spanda Kārikā · स्पन्द कारिका",
                "author": "Vasugupta / Kallata (c. 875–900 CE)",
                "period": "c. 875–900 CE",
                "desc": "52 karikas in 4 sections (nihnhava, sahaja vidya, vibhuti, etc.) on Spanda — the divine pulsation or vibration that is Shiva's own nature. The Spanda doctrine holds that consciousness is not static but dynamic — eternally vibrating. Commentaries: Kallata's Vritti, Kshemaraja's Spanda Nirnaya (authoritative).",
                "tradition": "Spanda",
                "link": "https://www.wisdomlib.org/hinduism/book/spanda-karikas",
                "archive": "https://archive.org/search?query=spanda+karikas",
            },
            {
                "title": "Spanda Nirṇaya · स्पन्द निर्णय",
                "author": "Kshemaraja (c. 1000–1050 CE)",
                "period": "c. 1025 CE",
                "desc": "The most authoritative commentary on Spanda Karikas. Establishes Spanda as the dynamic creative power of Shiva-consciousness — vibration that simultaneously recognises itself as pure awareness. More philosophical and comprehensive than Kallata's Vritti.",
                "tradition": "Spanda",
                "link": "https://www.wisdomlib.org/definition/spandanirnaya",
                "archive": "https://archive.org/search?query=spanda+nirnaya+kshemaraja",
            },
            {
                "title": "Spanda Vivṛti (Kallata's Vritti) · स्पन्द विवृति",
                "author": "Kallata (c. 875–900 CE)",
                "period": "c. 900 CE",
                "desc": "The earliest commentary on the Spanda Karikas by Kallata, Vasugupta's direct disciple. More concise than Kshemaraja's Nirnaya — often read as a first commentary. Establishes the Spanda school as an independent darshana within Kashmir Shaivism.",
                "tradition": "Spanda",
                "link": "https://www.wisdomlib.org/definition/spanda-karikas",
                "archive": "https://archive.org/search?query=spanda+vritti+kallata",
            },
            {
                "title": "Śiva Sūtra Vimarśinī · शिव सूत्र विमर्शिनी",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "The standard commentary on all 77 Shiva Sutras. Illuminates each sutra with Trika philosophy — explaining the three upayas, the nature of Shiva-consciousness, and practical guidance for sadhana. The most widely studied commentary in the living tradition.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/hinduism/book/shiva-sutra-vimarsini",
                "archive": "https://archive.org/search?query=shiva+sutra+vimarsini",
            },
            {
                "title": "Śiva Sūtra Vārttika · शिव सूत्र वार्त्तिक",
                "author": "Bhaskara (c. 10th–11th century CE)",
                "period": "c. 1000 CE",
                "desc": "Another important commentary on the Shiva Sutras by Bhaskara — represents a slightly different interpretive lineage from Kshemaraja. Valuable for understanding the diversity within the Pratyabhijña tradition.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/hinduism/book/the-shiva-sutras",
                "archive": "https://archive.org/search?query=shiva+sutra+vartika+bhaskara",
            },
            {
                "title": "Stava Cintāmaṇi · स्तव चिन्तामणि",
                "author": "Bhattatrayambaka (c. 10th century CE)",
                "period": "c. 10th century CE",
                "desc": "A celebrated hymn to Shiva in the Spanda tradition — 'The Wish-Fulfilling Jewel of Praise'. Uses Spanda philosophy to express intense devotion. Studied alongside the Shivastotra texts.",
                "tradition": "Spanda / Bhakti",
                "link": "https://www.wisdomlib.org/definition/stavacintamani",
                "archive": "",
            },
        ],
        "Pratyabhijñā Darśana · प्रत्यभिज्ञा दर्शन": [
            {
                "title": "Īśvarapratyabhijñā Kārikā · ईश्वरप्रत्यभिज्ञा कारिका",
                "author": "Utpaladeva (c. 900–950 CE)",
                "period": "c. 925 CE",
                "desc": "The philosophical masterwork of Utpaladeva — 4 Adhikaras (chapters) on Jnana (knowledge), Kriya (action), Agama (tradition), and Tattva (reality). Argues that liberation is the spontaneous recognition (pratyabhijña) of one's identity as Shiva. Critiques Buddhist Vijnana-vada and establishes Shaiva idealism. Basis of Abhinavagupta's Vimarshini and Vivrittivimarshini commentaries.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/definition/ishvarapratyabhijna",
                "archive": "https://archive.org/search?query=ishvara+pratyabhijna+karikas",
            },
            {
                "title": "Pratyabhijñāhṛdayam · प्रत्यभिज्ञाहृदयम्",
                "author": "Kshemaraja (c. 1000–1050 CE)",
                "period": "c. 1025 CE",
                "desc": "20 sutras — the most accessible gateway to Kashmir Shaivism. Sutra 1: 'Chiti Shakti of her own free will is the cause of the siddhi of the universe.' Condenses the entire Pratyabhijña system for the sincere seeker. Translated by Jaideva Singh, Swami Lakshman Joo, and others. Still used in daily study and teaching worldwide.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/hinduism/book/pratyabhijnahrdayam",
                "archive": "https://archive.org/search?query=pratyabhijnahridayam+kshemaraja",
            },
            {
                "title": "Īśvarapratyabhijñā Vimarśinī · ईश्वरप्रत्यभिज्ञा विमर्शिनी",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Abhinavagupta's concise commentary on Utpaladeva's karikas. Clarifies the central arguments and introduces his own Trika framework. Companion to the longer Vivrittivimarshini — together they form the most authoritative reading of the Pratyabhijña karikas.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/definition/ishvarapratyabhijna",
                "archive": "https://archive.org/search?query=ishvarapratyabhijna+vimarsini",
            },
            {
                "title": "Īśvarapratyabhijñā Vivṛttivimarśinī · विवृत्तिविमर्शिनी",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "The longer, more detailed commentary on the Pratyabhijña karikas — Abhinavagupta's magnum opus in philosophical prose. Engages with Buddhist (Dignaga, Dharmakirti) and Shaiva Siddhanta views in detail. One of the most philosophically profound texts in Indian philosophy.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/definition/ishvarapratyabhijna",
                "archive": "https://archive.org/search?query=vivrittivimarshini+abhinavagupta",
            },
            {
                "title": "Ajadapramatarasiddhi · अजडप्रमातृसिद्धि",
                "author": "Utpaladeva (c. 925 CE)",
                "period": "c. 925 CE",
                "desc": "Short philosophical treatise proving the existence of the sentient knower (ajada pramata = non-inert recogniser = Shiva). Refutes Buddhist no-self theories. One of Utpaladeva's minor but important works alongside the Karikas.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/definition/utpaladeva",
                "archive": "https://archive.org/search?query=utpaladeva+pratyabhijna+works",
            },
            {
                "title": "Shivadrishti · शिवदृष्टि",
                "author": "Somananda (c. 875–925 CE)",
                "period": "c. 900 CE",
                "desc": "The founding text of the Pratyabhijña school — Somananda was Utpaladeva's teacher and the first to articulate the recognition (pratyabhijña) doctrine systematically. 9 chapters establishing that all existence is Shiva's own vision (Shiva-drishti). Critiques Advaita Vedanta, Buddhism, and Shaiva Siddhanta.",
                "tradition": "Pratyabhijña",
                "link": "https://www.wisdomlib.org/definition/shivadrishti",
                "archive": "https://archive.org/search?query=shivadrishti+somananda",
            },
        ],
        "Abhinavagupta · अभिनवगुप्त": [
            {
                "title": "Tantrāloka · तन्त्रालोक",
                "author": "Abhinavagupta (c. 975–1025 CE)",
                "period": "c. 1000 CE",
                "desc": "The greatest encyclopaedia of Tantric Shaivism — 37 Ahnikas (chapters), ~5800 verses. Systematically covers: Anuttara (the Absolute), the 3 Upayas, cosmology, Kula doctrines, initiation (diksha), yogic practices, Krama goddess worship, mantra, and liberation. Teachers: Shambhunatha (Kula), Lakshmanagupta (Pratyabhijña). Called 'the Tantric Mahabharata'.",
                "tradition": "Trika / Kula / Kaula",
                "link": "https://www.wisdomlib.org/hinduism/book/tantraloka",
                "archive": "https://archive.org/search?query=tantraloka+abhinavagupta",
            },
            {
                "title": "Tantrasāra · तन्त्रसार",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Prose condensation of the Tantraloka — written for students who cannot study the full text. Covers the 36 tattvas, three Upayas, nature of consciousness, mantra, yantra, and the path to liberation. The most accessible of Abhinavagupta's major works.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/tantrasara",
                "archive": "https://archive.org/search?query=tantrasara+abhinavagupta",
            },
            {
                "title": "Paramārthasāra · परमार्थसार",
                "author": "Abhinavagupta (adaptation of Adhara Shastra)",
                "period": "c. 1000 CE",
                "desc": "105 verses (adapted from the Adhara Shastra of Shesha Muni) summarising the entire Shaiva cosmology and soteriology — the 36 tattvas, the nature of bondage and liberation, grace, and the recognition of Shiva as one's own Self. One of the best introductions to Kashmir Shaivism in verse.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/paramarthasara",
                "archive": "https://archive.org/search?query=paramarthasara+abhinavagupta",
            },
            {
                "title": "Parātriṃśikā Vivaraṇa · परात्रिंशिका विवरण",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Detailed commentary on the 36-verse Paratrishika — Abhinavagupta's most esoteric work. Contains the complete phonematic cosmology (Matrika — 50 Sanskrit letters as the body of the Goddess), the nature of the supreme mantra AHAM, and the Kula transmission. Translated by Paul Eduardo Muller-Ortega.",
                "tradition": "Trika / Kula",
                "link": "https://www.wisdomlib.org/definition/paratrishika",
                "archive": "https://archive.org/search?query=paratrishika+vivarana",
            },
            {
                "title": "Abhinavabhāratī · अभिनवभारती",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Massive commentary on Bharata's Natyashastra (treatise on performance arts). Introduces the Rasa theory with Shaiva philosophical depth — aesthetic experience (rasa) is identified with Brahmananda (the bliss of Brahman). Foundation of all subsequent Indian aesthetics (Alankara Shastra). The Rasa of Shanta (tranquility) as the supreme rasa.",
                "tradition": "Aesthetics / Rasashastra",
                "link": "https://www.wisdomlib.org/definition/abhinavabharati",
                "archive": "https://archive.org/search?query=abhinavabharati+natyashastra",
            },
            {
                "title": "Bodhapañcadaśikā · बोधपञ्चदशिका",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "15 verses on Bodha (pure awareness as Shiva). A concise but profound text laying out the core Trika view — that the entire universe is an expression of Shiva's own self-luminous awareness. Used as a teaching text in the tradition.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/abhinavagupta",
                "archive": "https://archive.org/search?query=bodhapanchadasika+abhinavagupta",
            },
            {
                "title": "Mālinīślokavārttika · मालिनीश्लोकवार्त्तिक",
                "author": "Abhinavagupta (c. 1000 CE)",
                "period": "c. 1000 CE",
                "desc": "Commentary on verses of the Malinivijayottara Tantra. Presents Abhinavagupta's reading of the root Trika Agama — explaining the Anuttara (the Absolute) and the three Shaktis (Para, Parapara, Apara) of the Trika.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/abhinavagupta",
                "archive": "https://archive.org/search?query=malinislokavartika+abhinavagupta",
            },
            {
                "title": "Kramastotra · क्रमस्तोत्र",
                "author": "Attributed to Siddhanatha / traditional Krama masters",
                "period": "c. 9th–10th century CE",
                "desc": "Hymns of the Krama tradition to Kali in her sequential (krama) aspect — past, present, future as three forms of the goddess Mahakali. The Krama system is the tantric antecedent of Kashmir Shaivism, focused on the dynamic sequence of consciousness rather than its static recognition. Incorporated by Abhinavagupta into the Tantraloka.",
                "tradition": "Krama",
                "link": "https://www.wisdomlib.org/definition/krama",
                "archive": "https://archive.org/search?query=krama+tradition+kashmir",
            },
            {
                "title": "Bhogarahasyam · भोगरहस्यम्",
                "author": "Traditional Kaula / Kula",
                "period": "Medieval",
                "desc": "A text on the 'secret of enjoyment' in the Kaula tradition — the doctrine that liberation is achieved through the transformation of ordinary experience (bhoga = enjoyment) into the recognition of Shiva. Central to the Kaula teaching that the body and world are not obstacles but instruments of liberation.",
                "tradition": "Kula / Kaula",
                "link": "https://www.wisdomlib.org/definition/kaula",
                "archive": "",
            },
            {
                "title": "Tantraloka Viveka · तन्त्रालोक विवेक",
                "author": "Jayaratha (c. 1150–1200 CE)",
                "period": "c. 1200 CE",
                "desc": "The indispensable commentary on Abhinavagupta's Tantraloka by Jayaratha — without which the Tantraloka is virtually unreadable. Explains thousands of technical terms, identifies source texts quoted, and clarifies the ritual and philosophical meaning of every verse. The KSTS (Kashmir Series of Texts and Studies) published both texts together in 12 volumes.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/hinduism/book/tantraloka",
                "archive": "https://archive.org/search?query=tantraloka+jayaratha+viveka",
            },
        ],
        "Kshemaraja & Commentators · क्षेमराज": [
            {
                "title": "Svacchanda Tantra Uddyota · स्वच्छन्द तन्त्रोद्योत",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "Kshemaraja's massive commentary on the 18-chapter Svacchanda Tantra. The primary source for Kashmiri Shaiva initiatory practice, cosmology (the 36 tattvas in detail), and the daily ritual of the Shaiva initiate (dikshita). Most comprehensive Agamic commentary in the tradition.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/svacchanda-tantra",
                "archive": "https://archive.org/search?query=svacchandatantrauddyota+kshemaraja",
            },
            {
                "title": "Netra Tantra Uddyota · नेत्र तन्त्रोद्योत",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "Commentary on the Netra Tantra. Explains the Mrityunjaya ritual, protection rites, and the significance of the 'third eye' (netra) as the eye of Shiva-consciousness that transcends death.",
                "tradition": "Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/netra-tantra",
                "archive": "https://archive.org/search?query=netra+tantra+uddyota+kshemaraja",
            },
            {
                "title": "Herātrika Paddhati · हेरात्रिका पद्धति",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "Ritual manual for the Trika goddess worship — the three goddesses Para, Parapara, and Apara. Documents the KP worship of the Trika deities that connects to the Herath (Shivratri) festival traditions.",
                "tradition": "Trika / Ritual",
                "link": "https://www.wisdomlib.org/definition/kshemaraja",
                "archive": "",
            },
            {
                "title": "Stava Cintāmaṇi Ṭīkā · स्तव चिन्तामणि टीका",
                "author": "Kshemaraja (c. 1025 CE)",
                "period": "c. 1025 CE",
                "desc": "Commentary on Bhattatrayambaka's Stava Cintamani hymn. Demonstrates how devotional hymns encode Spanda and Trika philosophical truths.",
                "tradition": "Spanda / Bhakti",
                "link": "https://www.wisdomlib.org/definition/kshemaraja",
                "archive": "",
            },
            {
                "title": "Śivastotrāvalī Vivṛti · शिवस्तोत्रावली विवृति",
                "author": "Kshemaraja (commentary on Utpaladeva)",
                "period": "c. 1025 CE",
                "desc": "Commentary on Utpaladeva's 20 devotional hymns to Shiva. Shows how the most philosophical thinker of Kashmir Shaivism was also the most ardent devotee — bhakti and jnana are inseparable in this tradition.",
                "tradition": "Pratyabhijña / Bhakti",
                "link": "https://www.wisdomlib.org/definition/shivastotravali",
                "archive": "https://archive.org/search?query=shivastotravali+utpaladeva",
            },
        ],
        "Krama & Kula Darshana · क्रम और कुल": [
            {
                "title": "Mahānayaprakāśa · महानयप्रकाश",
                "author": "Shitivaraha / Arnavagupta (c. 12th century CE)",
                "period": "c. 12th century CE",
                "desc": "One of the earliest surviving texts in the Kashmiri language (with Sanskrit passages). Documents the Krama tradition — worship of Kali in her sequential (krama) manifestations of emanation, existence, and reabsorption. Critical for understanding Kashmiri Kali traditions and the link between Sanskrit and vernacular KP literature.",
                "tradition": "Krama",
                "link": "https://www.wisdomlib.org/definition/mahanayaprakasha",
                "archive": "",
            },
            {
                "title": "Kramastotra · क्रमस्तोत्र",
                "author": "Various Krama masters",
                "period": "c. 9th–11th century CE",
                "desc": "Hymns of the Krama tradition praising Kali in her sequential manifestations. The Krama system worships Kali as the power of time (krama = sequence) — past, present, future as three forms of the goddess. Distinct from Trika but absorbed into it by Abhinavagupta.",
                "tradition": "Krama",
                "link": "https://www.wisdomlib.org/definition/krama",
                "archive": "https://archive.org/search?query=krama+tradition+kashmir+shaivism",
            },
            {
                "title": "Kulārṇava Tantra · कुलार्णव तन्त्र",
                "author": "Revealed text (Kula Āgama)",
                "period": "c. 10th–12th century CE",
                "desc": "17 chapters — the most comprehensive surviving Kula Agama. Covers: the nature of Kula (the Shakta family/lineage), Kaula practices, initiation by a Kula guru, non-dual consciousness, the role of the body in liberation, and Kaula worship. Widely studied in all Shakta-Shaiva traditions.",
                "tradition": "Kula / Kaula",
                "link": "https://www.wisdomlib.org/hinduism/book/kularnava-tantra",
                "archive": "https://archive.org/search?query=kularnava+tantra",
            },
            {
                "title": "Kaulajñānanirṇaya · कौलज्ञाननिर्णय",
                "author": "Matsyendranatha (c. 9th–10th century CE)",
                "period": "c. 900 CE",
                "desc": "Attributed to Matsyendranatha — the guru of Gorakshanatha and the founder of the Natha tradition which drew heavily from Kashmiri Kaula sources. Contains the earliest surviving description of Kaulachara practices, the body as a cosmological map, and the yogini traditions.",
                "tradition": "Kula / Natha",
                "link": "https://www.wisdomlib.org/definition/kaulajnananirnaya",
                "archive": "https://archive.org/search?query=kaulajnananirnaya+matsyendranatha",
            },
            {
                "title": "Gorakshashatakam · गोरक्षशतकम्",
                "author": "Gorakshanatha (c. 10th–11th century CE)",
                "period": "c. 10th–11th century CE",
                "desc": "100 verses on Hatha Yoga by Gorakshanatha — who drew extensively from Kashmiri Kaula-Natha sources. The physical yoga described here (Hatha) is the practical embodied path of the same tradition that Abhinavagupta systematised philosophically. Demonstrates the link between Kashmir Shaivism and the Natha yoga tradition.",
                "tradition": "Natha / Kula / Hatha Yoga",
                "link": "https://www.wisdomlib.org/definition/goraksha-shataka",
                "archive": "https://archive.org/search?query=goraksha+shataka+natha",
            },
            {
                "title": "Yogavāsiṣṭha (Kashmir recension) · योगवासिष्ठ",
                "author": "Valmiki (traditional) / Kashmir recension c. 10th–12th century CE",
                "period": "Kashmir recension c. 1000–1200 CE",
                "desc": "The Yogavasistha (also called Moksopaya) is a massive philosophical text of ~32,000 verses in its longer recension. The Kashmir version (Moksopaya) is considered distinct and earlier than the pan-Indian version. It uses stories and dialogues to teach Advaita-Vedanta / Kashmir Shaivism philosophy — reality as pure consciousness. Composed in or strongly associated with Kashmir. Translated by Swami Venkatesananda.",
                "tradition": "Kashmir Advaita / Shaiva Vedanta",
                "link": "https://www.wisdomlib.org/definition/yoga-vasistha",
                "archive": "https://archive.org/search?query=yoga+vasistha+moksopaya+kashmir",
            },
            {
                "title": "Trika Sāra · त्रिक सार",
                "author": "Abhinavagupta",
                "period": "c. 1000 CE",
                "desc": "A short but dense text presenting the 'essence of Trika' — the three goddesses (Para, Parapara, Apara), their relationship to the Shiva-Shakti unity, and the nature of the Trika cosmological triangle. Used as a devotional and philosophical summary in the tradition.",
                "tradition": "Trika",
                "link": "https://www.wisdomlib.org/definition/trika",
                "archive": "https://archive.org/search?query=trika+sara+abhinavagupta",
            },
        ],
        "Devotional & Hymn Literature · स्तोत्र साहित्य": [
            {
                "title": "Śivastotrāvalī · शिवस्तोत्रावली",
                "author": "Utpaladeva (c. 925 CE)",
                "period": "c. 925 CE",
                "desc": "20 hymns (stotravalı) of intense devotion to Shiva — the most moving devotional poetry in the Kashmir Shaivism canon. Each hymn demonstrates that Utpaladeva's deep philosophy arose from direct experience. Key hymns: Shivastava (praise of Shiva), Paramarthacarca (discussion of supreme reality). Translated by Constantina Rhodes Bailly.",
                "tradition": "Pratyabhijña / Bhakti",
                "link": "https://www.wisdomlib.org/definition/shivastotravali",
                "archive": "https://archive.org/search?query=shivastotravali+utpaladeva",
            },
            {
                "title": "Mahimnastava · महिम्नस्तव",
                "author": "Pushpadanta (c. 900–950 CE)",
                "period": "c. 925 CE",
                "desc": "43 verses praising the greatness (mahimna) of Shiva — one of the most beloved hymns in all of Shaivism, composed in Kashmir. Celebrates Shiva's transcendence beyond all paths and philosophies. Recited daily in KP homes and temples.",
                "tradition": "Shaiva Bhakti",
                "link": "https://www.wisdomlib.org/hinduism/book/mahimna-stava",
                "archive": "https://archive.org/search?query=mahimnastava+pushpadanta",
            },
            {
                "title": "Sharada Stotram · शारदा स्तोत्रम्",
                "author": "Traditional KP authorship",
                "period": "Medieval",
                "desc": "The invocation of Sharada Devi — 'Ya Sharada nilotpala-dala-shyama' (She who is dark as the blue lotus petal). The primary KP hymn to Saraswati-Sharada, recited at all beginnings, on Sharada Navami, and before any scholarly work. Named after the Sharada Peeth at Sharda (PoK).",
                "tradition": "Kashmir Shakta / Saraswati tradition",
                "link": "https://en.wikipedia.org/wiki/Sharada_Peeth",
                "archive": "https://archive.org/search?query=sharada+stotram+kashmiri+pandit",
            },
            {
                "title": "Shiva Panchakshara Stotra · शिव पञ्चाक्षर स्तोत्र",
                "author": "Adi Shankaracharya (c. 788–820 CE)",
                "period": "c. 800 CE",
                "desc": "5 verses on the five-syllable mantra Na-Ma-Shi-Va-Ya — each syllable corresponding to the five cosmic functions of Shiva (creation, preservation, dissolution, concealment, grace) and the five elements. Recited during Herath (KP Shivratri) all-night vigil.",
                "tradition": "Shaiva / Pan-Hindu",
                "link": "https://www.wisdomlib.org/definition/shiva-panchakshara-stotram",
                "archive": "https://archive.org/search?query=shiva+panchakshara+stotra",
            },
            {
                "title": "Mrityunjaya Mantra & Stotra · मृत्युञ्जय",
                "author": "Rigveda (Vamadeva Rishi) / expanded by tradition",
                "period": "Vedic / Medieval",
                "desc": "The Tryambaka mantra of the Rigveda (RV 7.59.12) — 'Tryambakam yajamahe sugandhim pushtivardhanam' — as developed in the Netra Tantra and Kashmiri Shaiva tradition. Used in Kashmiri Pandit rituals for longevity, healing, and at death rites. The Mrityunjaya tradition is specifically elaborated in the Kashmiri Netra Tantra.",
                "tradition": "Vedic / Shaiva Agama",
                "link": "https://www.wisdomlib.org/definition/mahamrityunjaya",
                "archive": "https://archive.org/search?query=mrityunjaya+mantra+netra+tantra",
            },
            {
                "title": "Vakhs of Lalleshwari · लल वाख",
                "author": "Lalleshwari / Lal Ded (c. 1320–1392 CE)",
                "period": "14th century CE",
                "desc": "258+ mystic verses in Old Kashmiri — the oldest surviving Kashmiri literature. Core teaching: Shivoham (I am Shiva). Key Vakhs: 'Shiv chuy thali thali rozaan' (Shiva pervades everywhere), 'Pranas apanas milawath karim' (when prana and apana unite, Shiva-Shakti are one). The foundational text of all later KP devotional and literary tradition.",
                "tradition": "Kashmir Shaivism / Pratyabhijña / Bhakti",
                "link": "https://en.wikipedia.org/wiki/Lalleshwari",
                "archive": "https://archive.org/search?query=lal+ded+vakhs+lalleshwari+kashmiri",
            },
            {
                "title": "Shiva Tandava Stotra · शिव तान्डव स्तोत्र",
                "author": "Ravana (traditional attribution)",
                "period": "Ancient / Medieval",
                "desc": "17 verses of intense Shiva praise — arguably the most powerful hymn in all of Shaivism. Each verse a torrent of compound Sanskrit describing Shiva's cosmic dance. 'Jatatavigalajjala...' — among the most recited Sanskrit texts in KP households. Recited during Herath vigil and Shivratri worship across all KP families.",
                "tradition": "Shaiva Bhakti",
                "link": "https://www.wisdomlib.org/definition/shiva-tandava-stotra",
                "archive": "https://archive.org/search?query=shiva+tandava+stotra",
            },
            {
                "title": "Rudrashtakam · रुद्राष्टकम्",
                "author": "Tulsidas (16th century CE) / also traditional versions",
                "period": "16th century CE / traditional",
                "desc": "8 verses glorifying Rudra-Shiva. 'Namami Shamishan Nirvana Rupam...' — begins with salutation to Shiva in his supreme formless aspect (nirvana rupa) and proceeds through his many forms. Widely recited by KP families during morning puja and Herath. The Kashmiri tradition has its own variant verses in the Rudrashtakam.",
                "tradition": "Shaiva Bhakti",
                "link": "https://www.wisdomlib.org/definition/rudrashtaka",
                "archive": "https://archive.org/search?query=rudrashtakam+shiva+stotram",
            },
            {
                "title": "Lingashtakam · लिंगाष्टकम्",
                "author": "Traditional (attributed to Adi Shankaracharya)",
                "period": "Medieval",
                "desc": "8 verses on the Shiva Linga — 'Brahma Muraari Sura Archita Lingam...' Glorifies the Shiva Linga as the form worshipped by Brahma, Vishnu, and all gods. Central to KP Shiva puja — the Herath Vatak pots represent the 12 Jyotirlingas, and the Lingashtakam is recited during their installation.",
                "tradition": "Shaiva Bhakti",
                "link": "https://www.wisdomlib.org/definition/linga-ashtaka",
                "archive": "https://archive.org/search?query=lingashtakam+shiva",
            },
            {
                "title": "Devi Mahatmya (Durga Saptashati) · देवी माहात्म्य",
                "author": "Markandeya Purana / Vedavyasa (traditional)",
                "period": "c. 400–600 CE",
                "desc": "700 verses from the Markandeya Purana in three episodes — Madhu-Kaitabha, Mahishasura, and Shumbha-Nishumbha. The supreme text of Shakta tradition. Recited by KP families during all nine nights of Navratri. The Kashmiri Pandit tradition has specific recitation customs: beginning with Siddha Kunjika Stotra, daily recitation of specific chapters, ending with Kshama Prarthana.",
                "tradition": "Shakta / Devi worship",
                "link": "https://www.wisdomlib.org/hinduism/book/devi-mahatmya",
                "archive": "https://archive.org/search?query=devi+mahatmya+durga+saptashati",
            },
            {
                "title": "Lalita Sahasranama · ललिता सहस्रनाम",
                "author": "Brahmanda Purana (Hayagriva to Agastya)",
                "period": "c. 700–1000 CE",
                "desc": "1000 names of the Goddess Lalita Tripurasundari — the same goddess as Tripura Sundari of Kashmir (Kulgam) and the supreme Shakti of the Trika. Each name is a concentrated mantra. Recited by KP families on Navratri and Sharad Purnima. Philosophically, the names encode the entire Shakta cosmology of the Srikula tradition.",
                "tradition": "Shakta / Srikula / Trika",
                "link": "https://www.wisdomlib.org/hinduism/book/lalita-sahasranama",
                "archive": "https://archive.org/search?query=lalita+sahasranama",
            },
        ],
        "Nilamata & Kashmir History · नीलमत एवं इतिहास": [
            {
                "title": "Nīlamata Purāṇa · नीलमत पुराण",
                "author": "Unknown Kashmirian author",
                "period": "c. 6th–8th century CE",
                "desc": "The oldest known Kashmiri text — 2156 verses. Describes: the mythological origin of Kashmir Valley (the drying of lake Satisar by Vitasta), the geography of the valley, a complete calendar of festivals and rituals (primary source for Herath, Navreh, Nag worship), and the customs of Kashmiri people. The Vitasta Stotram within is recited by KP priests. Translated by Ved Kumari Ghai (JKAAS).",
                "tradition": "Kashmiri Puranic tradition",
                "link": "https://www.wisdomlib.org/hinduism/book/nilamata-purana",
                "archive": "https://archive.org/search?query=nilamata+purana+kashmir",
            },
            {
                "title": "Rājataraṅgiṇī · राजतरङ्गिणी",
                "author": "Kalhana (c. 1150 CE)",
                "period": "c. 1150 CE",
                "desc": "Kashmir's great chronicle — 8 Tarangas (waves/cantos), ~7826 verses in Sanskrit. History from mythological Gonanda dynasty to Kalhana's own time (1149 CE). First systematic historical work in Sanskrit. Invaluable for KP lineage, temple geography, Kashmiri kings, and cultural history. Continued by Jonaraja (1459 CE), Shrivara (1477), and Prajna Bhatta (1586). Translated by Sir M.A. Stein.",
                "tradition": "History / Itihas",
                "link": "https://www.wisdomlib.org/hinduism/book/rajatarangini",
                "archive": "https://archive.org/search?query=rajatarangini+kalhana",
            },
            {
                "title": "Jonarāja's Rājataraṅgiṇī (continuation) · जोनराज",
                "author": "Jonaraja (c. 1420–1459 CE)",
                "period": "c. 1459 CE",
                "desc": "First continuation of Kalhana's chronicle — covers Kashmir history from c. 1150 to 1459 CE. Written in the court of Sultan Zayn-ul-Abidin (Bud Shah) of Kashmir. Jonaraja was a Kashmiri Pandit scholar who continued the Sanskrit chronicle tradition through the Sultanate period.",
                "tradition": "History / Itihas",
                "link": "https://en.wikipedia.org/wiki/Jonaraja",
                "archive": "https://archive.org/search?query=jonaraja+rajatarangini+kashmir",
            },
            {
                "title": "Shrivara's Jāinarājataraṅgiṇī · श्रीवर",
                "author": "Shrivara (c. 1477 CE)",
                "period": "c. 1477 CE",
                "desc": "Second continuation of the Rajatarangini by Shrivara, also a KP scholar in the Sultani court. Covers 1459–1486 CE including the reign of Sultan Hassan Shah. Important for understanding the KP experience under Kashmir's Sultanate rulers.",
                "tradition": "History / Itihas",
                "link": "https://en.wikipedia.org/wiki/Shrivara",
                "archive": "https://archive.org/search?query=shrivara+rajatarangini",
            },
            {
                "title": "Mahānayaprakāśa · महानयप्रकाश",
                "author": "Shitivaraha / Arnavagupta (c. 12th century CE)",
                "period": "c. 12th century CE",
                "desc": "Earliest surviving substantial text in the Kashmiri language — bilingual (Old Kashmiri and Sanskrit). Documents the Krama goddess tradition. Critical bridge between Sanskrit scholarly Shaivism and vernacular Kashmiri spiritual expression. Precedes Lal Ded's Vakhs by two centuries.",
                "tradition": "Krama",
                "link": "https://www.wisdomlib.org/definition/mahanayaprakasha",
                "archive": "",
            },
            {
                "title": "Vitasta Māhātmya · वितस्ता माहात्म्य",
                "author": "Traditional (Kashmiri)",
                "period": "Medieval",
                "desc": "The glorification of the river Vitasta (Jhelum) — the sacred mother-river of Kashmir mentioned in the Rigveda (Nadistuti, 10.75). The Nilamata Purana contains the core Vitasta Stotram. The river's source at Verinag (Anantnag) is a major KP pilgrimage site. Shraddha rites performed on its banks. Water used in all KP rituals.",
                "tradition": "Kashmiri river-goddess worship",
                "link": "https://en.wikipedia.org/wiki/Jhelum_River",
                "archive": "https://www.wisdomlib.org/hinduism/book/nilamata-purana",
            },
            {
                "title": "Haracharita Cintamani · हरचरित चिन्तामणि",
                "author": "Jayadratha (c. 12th century CE)",
                "period": "c. 1150–1200 CE",
                "desc": "A Sanskrit text on the deeds of Hara (Shiva) — part of the rich tradition of Shiva hagiography in Kashmir. Compiled around the same period as Kalhana's Rajatarangini, it documents the mythology and sacred sites of Kashmir from a Shaiva perspective.",
                "tradition": "Kashmir Shaiva / History",
                "link": "https://www.wisdomlib.org/definition/hara",
                "archive": "https://archive.org/search?query=haracharita+cintamani+kashmir",
            },
            {
                "title": "Kathasaritsagara · कथासरित्सागर",
                "author": "Somadeva (c. 1063–1081 CE)",
                "period": "c. 1063–1081 CE",
                "desc": "18 books, 124 chapters, 21,388 verses — 'The Ocean of the Rivers of Story'. Written by the Kashmiri Pandit Somadeva for Queen Suryamati. Drawn from Gunadhya's lost Brihatkatha. Contains 350+ stories: frame tales, fairy tales, folk stories, philosophical parables. Source for stories in Arabian Nights, Panchatantra, and European folk literature. One of the greatest literary works of ancient India — and a KP achievement.",
                "tradition": "Sanskrit literature / Kashmir",
                "link": "https://en.wikipedia.org/wiki/Kathasaritsagara",
                "archive": "https://archive.org/search?query=kathasaritsagara+somadeva",
            },
            {
                "title": "Vikramankadevacharita · विक्रमाङ्कदेवचरित",
                "author": "Bilhana of Kashmir (c. 1050–1100 CE)",
                "period": "c. 1086 CE",
                "desc": "Sanskrit court epic by the Kashmiri poet Bilhana, celebrating his patron King Vikramaditya VI of Chalukya dynasty. 18 cantos of polished Sanskrit verse — demonstrates the high level of Sanskrit literary culture carried by KP scholars who traveled and became court poets across India. His Chaurapanchasika is equally celebrated.",
                "tradition": "Sanskrit literature / Kashmir school",
                "link": "https://en.wikipedia.org/wiki/Bilhana",
                "archive": "https://archive.org/search?query=vikramankadevacharita+bilhana",
            },
        ],
        "Swami Lakshman Joo · स्वामी लक्ष्मण जू": [
            {
                "title": "Kashmir Shaivism: The Secret Supreme",
                "author": "Swami Lakshman Joo (1907–1991 CE)",
                "period": "20th century CE (teachings recorded 1970s–80s)",
                "desc": "The most accessible introduction to Kashmir Shaivism by the last great master of the living tradition. Covers: the 36 tattvas, the three Upayas, the seven states of the percipient (pramata), and the path to liberation through recognition (pratyabhijña). Based on oral teachings given to Western and Indian students. Published by Universal Shaiva Fellowship.",
                "tradition": "Pratyabhijña / Living tradition",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+kashmir+shaivism",
            },
            {
                "title": "Shiva Sutras: The Supreme Awakening",
                "author": "Swami Lakshman Joo (teachings) / edited disciples",
                "period": "20th century CE",
                "desc": "Swami Lakshman Joo's oral commentary on all 77 Shiva Sutras — the most authoritative modern explanation of the text from within the living Kashmiri tradition. Explains the three Upayas with practical clarity. Essential companion to Kshemaraja's Vimarsini.",
                "tradition": "Pratyabhijña",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+shiva+sutras",
            },
            {
                "title": "Vijnanabhairava: The Practice of Centring Awareness",
                "author": "Swami Lakshman Joo (commentary)",
                "period": "20th century CE",
                "desc": "Swami Lakshman Joo's explanation of the 112 dharanas of the Vijnanabhairava Tantra. Gives the practical method for each dharana as used in the Kashmir Shaiva sadhana tradition. Unique because it comes from a master who personally practised these techniques.",
                "tradition": "Trika / Shaiva Agama",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+vijnana+bhairava",
            },
            {
                "title": "Bhagavad Gita: In the Light of Kashmir Shaivism",
                "author": "Swami Lakshman Joo",
                "period": "20th century CE",
                "desc": "A unique reading of the Bhagavad Gita through the lens of Kashmir Shaivism — demonstrating that the Gita's teachings align with and are illuminated by the Trika and Pratyabhijña darshana. Shows how KP tradition synthesised Shaiva and Vaishnava streams.",
                "tradition": "Pratyabhijña / Vedanta synthesis",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+bhagavad+gita",
            },
            {
                "title": "Self Realization in Kashmir Shaivism",
                "author": "Swami Lakshman Joo",
                "period": "20th century CE",
                "desc": "Oral teachings of Swami Lakshman Joo compiled by John Hughes — covers the complete path of Kashmir Shaivism from the perspective of direct experience. Includes his commentary on the recognition path, the nature of Shiva-consciousness, and the role of the guru. More personal and experiential than his academic works.",
                "tradition": "Pratyabhijña / Living tradition",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+self+realization",
            },
            {
                "title": "Vijnanabhairava: The Manual for Self Realization",
                "author": "Swami Lakshman Joo (commentary)",
                "period": "20th century CE",
                "desc": "Swami Lakshman Joo's practical commentary on the 112 dharanas of the Vijnanabhairava Tantra. Each dharana explained as a living practice — how to enter the pure awareness of Bhairava through breath, sound, void, sleep, and daily experience. Unique authority: he personally practised these techniques across 80+ years of sadhana.",
                "tradition": "Trika / Shaiva Agama",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+vijnanabhairava",
            },
            {
                "title": "Paratrishika Vivarana (Lakshman Joo's commentary)",
                "author": "Swami Lakshman Joo (oral commentary on Abhinavagupta)",
                "period": "20th century CE",
                "desc": "Recorded lectures explaining Abhinavagupta's Paratrishika Vivarana — among the most esoteric texts of Kashmir Shaivism. Swami Lakshman Joo's oral explanation makes the phonematic cosmology (Matrika), the supreme mantra AHAM, and the Kula transmission accessible to modern students.",
                "tradition": "Trika / Kula",
                "link": "https://en.wikipedia.org/wiki/Lakshman_Joo",
                "archive": "https://archive.org/search?query=lakshman+joo+paratrishika",
            },
        ],
        "Academic & Modern Scholars · आधुनिक विद्वान": [
            {
                "title": "Kashmir Shaivism (Mark Dyczkowski)",
                "author": "Mark S.G. Dyczkowski",
                "period": "20th–21st century CE",
                "desc": "The most comprehensive academic study of Kashmir Shaivism in English. Dyczkowski studied directly under Swami Lakshman Joo and is the foremost Western scholar of the tradition. Key works: 'The Doctrine of Vibration' (Spanda), 'The Canon of the Shaivagama', 'A Journey in the World of the Tantras'. His translations of the Stanzas on Vibration (Spanda Karikas) are authoritative.",
                "tradition": "Academic / Spanda / Agama",
                "link": "https://en.wikipedia.org/wiki/Mark_S.G._Dyczkowski",
                "archive": "https://archive.org/search?query=dyczkowski+kashmir+shaivism",
            },
            {
                "title": "The Triadic Heart of Shiva (Paul Muller-Ortega)",
                "author": "Paul Eduardo Muller-Ortega",
                "period": "20th century CE",
                "desc": "Authoritative study of the Paratrishika Vivarana and the Kula tradition in Kashmir Shaivism. Explores the 'heart' (hridaya) as the centre of Shiva-consciousness in Abhinavagupta's thought. One of the finest academic works on the esoteric aspects of Kashmir Shaivism.",
                "tradition": "Academic / Trika / Kula",
                "link": "https://en.wikipedia.org/wiki/Paul_Eduardo_Muller-Ortega",
                "archive": "https://archive.org/search?query=muller+ortega+triadic+heart+shiva",
            },
            {
                "title": "Abhinavagupta: An Historical and Philosophical Study (K.C. Pandey)",
                "author": "K.C. Pandey",
                "period": "1935 CE (1st ed.)",
                "desc": "The first comprehensive scholarly monograph on Abhinavagupta in English. Still essential reading — covers his life, the philosophical context, his works, and the Pratyabhijña system. The Chowkhamba Sanskrit Series edition has been widely used in universities.",
                "tradition": "Academic / Pratyabhijña",
                "link": "https://archive.org/search?query=KC+Pandey+Abhinavagupta",
                "archive": "https://archive.org/search?query=KC+Pandey+Abhinavagupta+historical+philosophical",
            },
            {
                "title": "Kashmir Shaivism: The Central Philosophy (Jaideva Singh)",
                "author": "Jaideva Singh",
                "period": "20th century CE",
                "desc": "Jaideva Singh's translations and studies are the standard academic texts on Kashmir Shaivism. His works: Pratyabhijnahridayam (translation), Shiva Sutras (translation), Spanda Karikas (translation), Vijnanabhairava (translation). Published by Motilal Banarsidass — still the most widely used translations in English.",
                "tradition": "Academic / Pratyabhijña / Spanda",
                "link": "https://archive.org/search?query=jaideva+singh+kashmir+shaivism",
                "archive": "https://archive.org/search?query=jaideva+singh+pratyabhijna+shiva+sutras",
            },
            {
                "title": "The Recognition Sutras (Christopher Wallis)",
                "author": "Christopher Wallis (Hareesh)",
                "period": "21st century CE (2017)",
                "desc": "Modern translation and commentary on Kshemaraja's Pratyabhijnahridayam — making this foundational text fully accessible to contemporary readers. Wallis studied Sanskrit at Oxford and UC Berkeley and is one of the foremost contemporary teachers of Kashmir Shaivism. His approach balances rigorous scholarship with living practice.",
                "tradition": "Pratyabhijña / Modern",
                "link": "https://en.wikipedia.org/wiki/Christopher_Wallis_(scholar)",
                "archive": "https://archive.org/search?query=christopher+wallis+recognition+sutras",
            },
            {
                "title": "The Doctrine of Vibration (Mark Dyczkowski)",
                "author": "Mark S.G. Dyczkowski",
                "period": "1987 CE",
                "desc": "Definitive academic study of the Spanda doctrine — the philosophy of divine vibration in Kashmir Shaivism. Covers: Vasugupta's Shiva Sutras, Kallata's Spanda Karikas, Kshemaraja's Spanda Nirnaya, and the Spanda school's relationship to Pratyabhijña. Essential for understanding the Spanda tradition.",
                "tradition": "Academic / Spanda",
                "link": "https://archive.org/search?query=dyczkowski+doctrine+vibration",
                "archive": "https://archive.org/search?query=dyczkowski+doctrine+vibration+spanda",
            },
            {
                "title": "Kashmir Series of Texts and Studies (KSTS)",
                "author": "Edited by Mukund Ram Shastri, Madhusudan Kaul Shastri and others",
                "period": "1911–1947 CE",
                "desc": "The monumental publication series by the Research Department, Jammu & Kashmir State — 84 volumes of critical editions of Kashmir Shaivism manuscripts. Published the complete Sanskrit texts of: Tantraloka (with Jayaratha's Viveka), Spanda Karikas, Shiva Sutras, Pratyabhijnahridayam, Svacchanda Tantra, Netra Tantra, and dozens of other texts for the first time. The foundation of all modern academic study of Kashmir Shaivism.",
                "tradition": "Academic / Editorial",
                "link": "https://archive.org/search?query=KSTS+Kashmir+Series+Texts+Studies",
                "archive": "https://archive.org/search?query=Kashmir+Series+of+Texts+and+Studies",
            },
        ],
    }

    _sh_col1, _sh_col2 = st.columns([1.4, 2])
    with _sh_col1:
        sh_sections = ["All Sections · सभी"] + list(SHASTRA_DATA.keys())
        sh_filter = st.selectbox("Category · श्रेणी", sh_sections, key="sh_filter")
    with _sh_col2:
        sh_search_term = st.text_input("Search · खोजें", key="sh_search_text",
                                        placeholder="e.g. Abhinavagupta, Tantraloka, Spanda, Lal Ded…")

    def _render_items(items):
        for item in items:
            _lparts = []
            if item.get("link"):
                _lparts.append(
                    f'<a href="{item["link"]}" target="_blank" style="'
                    f'display:inline-flex;align-items:center;gap:5px;'
                    f'font-family:Cinzel,serif;font-size:9px;letter-spacing:1px;'
                    f'color:var(--teal);text-decoration:none;'
                    f'padding:5px 12px;border:1px solid rgba(42,122,106,.35);'
                    f'border-radius:20px;background:rgba(42,122,106,.06);'
                    f'transition:all .15s;white-space:nowrap">'
                    f'&#128279; Reference</a>'
                )
            if item.get("archive"):
                _lparts.append(
                    f'<a href="{item["archive"]}" target="_blank" style="'
                    f'display:inline-flex;align-items:center;gap:5px;'
                    f'font-family:Cinzel,serif;font-size:9px;letter-spacing:1px;'
                    f'color:var(--walnut-mid);text-decoration:none;'
                    f'padding:5px 12px;border:1px solid var(--border);'
                    f'border-radius:20px;background:var(--cream2);'
                    f'transition:all .15s;white-space:nowrap">'
                    f'&#128218; Archive.org</a>'
                )
            link_html = "".join(_lparts)
            st.markdown(f"""
            <div style="background:white;border:1px solid var(--border);border-radius:10px;
                 padding:16px 20px;margin-bottom:10px;box-shadow:0 1px 6px var(--shadow)">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:6px">
                <div>
                  <span style="font-family:Cinzel,serif;font-size:13px;font-weight:500;
                        color:var(--walnut)">{item['title']}</span>
                  <span style="font-size:10px;font-family:Cinzel,serif;letter-spacing:1px;
                        color:var(--saffron);margin-left:10px;padding:2px 8px;
                        background:rgba(212,114,42,.08);border-radius:10px">{item['tradition']}</span>
                </div>
                <div style="text-align:right;font-size:11px;color:var(--muted)">
                  {item['author']} &nbsp;·&nbsp; {item['period']}
                </div>
              </div>
              <div style="font-size:13.5px;color:var(--ink);line-height:1.75;margin:8px 0 10px">
                {item['desc']}
              </div>
              <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:4px">{link_html}</div>
            </div>
            """, unsafe_allow_html=True)

    _sh_active = sh_filter != "All Sections · सभी" or bool(sh_search_term)

    if not _sh_active:
        st.markdown("""
        <div style="text-align:center;padding:40px 20px;color:var(--muted)">
          <div style="font-size:32px;margin-bottom:12px;opacity:.4"></div>
          <div style="font-family:'Cinzel',serif;font-size:11px;letter-spacing:2px;
               color:var(--walnut-mid);margin-bottom:8px">SELECT A CATEGORY · श्रेणी चुनें</div>
          <div style="font-size:13px;line-height:1.8;max-width:400px;margin:0 auto">
            Choose a category from the dropdown, or type a keyword to search across all texts.
          </div>
        </div>
        """, unsafe_allow_html=True)
    elif sh_search_term:
        term = sh_search_term.lower()
        sections_to_show = {}
        for sec, items in SHASTRA_DATA.items():
            filtered = [it for it in items if
                        term in it["title"].lower() or
                        term in it["author"].lower() or
                        term in it["desc"].lower() or
                        term in it["tradition"].lower()]
            if filtered:
                sections_to_show[sec] = filtered
        total = sum(len(v) for v in sections_to_show.values())
        if total == 0:
            st.info("No results found. Try a different search term.")
        else:
            st.markdown(f'<div style="font-size:12px;color:var(--muted);margin:4px 0 14px;font-style:italic">Showing {total} result(s)</div>', unsafe_allow_html=True)
            for sec_name, items in sections_to_show.items():
                st.markdown(f'<div class="subsec">{sec_name}</div>', unsafe_allow_html=True)
                _render_items(items)
    else:
        sections_to_show = (SHASTRA_DATA if sh_filter == "All Sections · सभी"
                            else {sh_filter: SHASTRA_DATA[sh_filter]})
        for sec_name, items in sections_to_show.items():
            st.markdown(f'<div class="subsec">{sec_name}</div>', unsafe_allow_html=True)
            _render_items(items)

    # ── AI query ──────────────────────────────────────────────────
    st.markdown('<div class="styled-div"><span>ŚĀSTRA QUERY · शास्त्र प्रश्न</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">DEEP ŚĀSTRA QUERY · गहन शास्त्र खोज</div>
      <div style="margin-top:18px;text-align:center;padding:18px 0 10px">
        <div style="font-size:28px;margin-bottom:10px"></div>
        <div style="font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
             color:#DEB85A;margin-bottom:8px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14px;color:rgba(253,248,240,.65);line-height:1.8;max-width:480px;margin:0 auto">
          Your wise Kashmiri Pandit — for deep questions on Kashmir Shaivism, Trika philosophy,
          Sanskrit texts, Abhinavagupta, Pratyabhijñā and specific commentaries —
          launching in the next release.
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
             color:rgba(222,184,90,.45);margin-top:10px">
          शास्त्र प्रश्न — शीघ्र आ रहा है
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 6 — KASHMIRI CULTURE
# ══════════════════════════════════════════════════════════════════════════════
with tabs[6]:
    st.markdown("""
    <div class="sec-head"> Kāśmīrī Saṃskṛti · कश्मीरी संस्कृति</div>
    <div class="sec-sub">
      Complete guide to Kashmiri culture — festivals, food, arts, music, dress, sacred sites, saints and living traditions
      <span class="deva">उत्सव · भोजन · कला · संगीत · वेशभूषा · तीर्थ · संत · परम्परा</span>
    </div>
    """, unsafe_allow_html=True)

    KP_CULTURE = {
        "Festivals & Puja Rituals · उत्सव और पूजा विधि": [
            {
                "name": "Herath (Kashmiri Shivratri) · हेरथ",
                "icon": "",
                "timing": "Phalguna Krishna Chaturdashi — 3-day festival (Feb–Mar)",
                "desc": (
                    "The most sacred festival of Kashmiri Pandits. 'Herath' = Hara-ratri (Night of Hara/Shiva). "
                    "Entirely distinct from mainstream Shivratri in its rituals, materials and significance.\n\n"
                    "── DAY 1: SALAM (13th evening, Trayodashi) ──\n"
                    "The household is purified with cow dung (gobar) and gangajal. "
                    "12 clay pots (Vatak) are prepared — each represents one of the 12 Shiva lingas and one cosmic month. "
                    "Pots are filled with pure water. Sacred walnut branches (Shishur = Juglans regia) are placed inside. "
                    "The 'Salam' (salutation ceremony) is performed by the eldest male of the family — "
                    "he offers namaskar to all 12 Vatak pots arranged in a row.\n\n"
                    "── DAY 2: VATAK PUJA (14th, Chaturdashi — all night) ──\n"
                    "Puja Samagri (ritual materials):\n"
                    "· 12 new clay pots (Vatak) · Pure water (ideally from sacred river/spring) "
                    "· Walnut branches with leaves (Shishur) · Sacred grass (Durva/Kusha) "
                    "· Sesame seeds (til) · Rice (akshata) · Flowers (lotus, marigold) "
                    "· Incense (dhoop/agarbatti) · Diya (earthen lamp) with mustard oil "
                    "· Panchamrit (milk, curd, ghee, honey, sugar) · Fruits · Betel leaves (paan) "
                    "· Red thread (mauli/kalawa) · Sacred ash (vibhuti) · Sandalwood paste (chandan) "
                    "· New clothes (white preferred) · Copper/brass plate for offerings.\n\n"
                    "Puja Vidhi (procedure):\n"
                    "1. Achamanam: sip water thrice, recite Shiva names. "
                    "2. Sankalpa: state the intent before Shiva. "
                    "3. Ganesh Puja: invoke Ganesha first. "
                    "4. Vatak Sthapana: install all 12 pots ceremonially, each named after a Shiva linga. "
                    "5. Abhisheka: bathe each pot with Panchamrit, then pure water. "
                    "6. Shodasopachara Puja (16-step worship): Avahana, Asana, Padya, Arghya, Achamana, "
                    "Snana, Vastra, Yagnopavita, Gandha, Pushpa, Dhupa, Dipa, Naivedya, Tambula, "
                    "Pradakshina, Namaskara. "
                    "7. Shiva Stotra recitation: Shiva Sutras, Spanda Karikas, Mrityunjaya mantra (108 times). "
                    "8. Bhairava (Vatuk) Puja: the child-form Bhairava is invoked in a separate small earthen pot. "
                    "9. All-night vigil: family stays awake, singing Shiva bhajans and reciting Vakhs of Lal Ded. "
                    "10. Naga Puja at dawn: Naga (family serpent deity) is honoured.\n\n"
                    "── DAY 3: PARAN (15th, Purnima — breaking of fast) ──\n"
                    "The fast is broken with Harissa (slow-cooked lamb/mutton porridge — the traditional Herath Paran food), "
                    "Nadru (lotus stem), and sweets. "
                    "The Vatak pots are taken to a river/stream and immersed. "
                    "Walnut branches (Shishur) are distributed to all family members — eating the walnut is auspicious.\n\n"
                    "Mantra: 'Om Namah Shivaya · ॐ नमः शिवाय' (primary) | "
                    "Mrityunjaya: 'Om Tryambakam Yajamahe Sugandhim Pushti-Vardhanam' | "
                    "Shiva Panchakshara Stotra for all-night recitation."
                ),
                "links": [
                    ("Wikipedia · Herath", "https://en.wikipedia.org/wiki/Herath"),
                    ("Kashmiri Pandits Network · Herath", "https://www.ikashmir.net/herath/"),
                    ("Nilamata Purana (Vatak source)", "https://www.wisdomlib.org/hinduism/book/nilamata-purana"),
                ],
            },
            {
                "name": "Navreh · नवरेह — Kashmiri New Year",
                "icon": "",
                "timing": "Chaitra Shukla Pratipada (Mar–Apr) — Amavasyanta reckoning",
                "desc": (
                    "Navreh (Nava + Varsha = New Year in Kashmiri) — the most joyous KP festival. "
                    "Observed on Chaitra Shukla Pratipada, the first day of the Amavasyanta new year.\n\n"
                    "── EVE OF NAVREH (Navreh Ratri) ──\n"
                    "The Navreh Thali (ceremonial plate) is prepared with precision and placed where "
                    "it will be seen first thing upon waking. Items and their significance:\n"
                    "· Dhaan (uncooked rice) — abundance and fertility\n"
                    "· Doon (walnut) — wisdom and longevity\n"
                    "· Noon (salt) — the flavour of life; also preservation\n"
                    "· Mishri (sugar crystals) — sweetness and prosperity\n"
                    "· Dahi (curd) — auspiciousness; used in all KP rituals\n"
                    "· Tchot/Kulcha (ring bread) — the circular continuity of life\n"
                    "· Flowers (narcissus/nargis, Kashmiri iris) — beauty of the new season\n"
                    "· Kalam + dawaat (pen and inkpot) — knowledge and learning (Sharada Devi's blessing)\n"
                    "· Coins (silver preferred) — Lakshmi's grace, financial prosperity\n"
                    "· Jantri (the KP almanac/panchang) — THE most important item; contains the year's "
                    "muhurtas, festivals, nakshatra calendar, and astrological data for the family\n"
                    "· Mirror — to see oneself clearly in the new year\n"
                    "· Kesar (saffron) — divine grace and the fragrance of Kashmir.\n\n"
                    "── MORNING RITUAL (Navreh day) ──\n"
                    "Puja Samagri: Flowers, incense, diya, rice, curd, fruits, paan, coconut, "
                    "red thread, sandalwood paste, Jantri.\n\n"
                    "Puja Vidhi:\n"
                    "1. Wake at Brahma Muhurta — first sight must be the Navreh Thali (not a person).\n"
                    "2. Achamanam: sip water thrice.\n"
                    "3. Sharada Devi Puja: invoke Mata Sharada (Saraswati) — she presides over Navreh "
                    "as the goddess of the new year and learning. Recite Sharada Stotram: "
                    "'Ya Sharada nilotpala-dala-shyama...' \n"
                    "4. Ganesha Puja (Vighnaharta): remove obstacles for the new year.\n"
                    "5. Kul Devi Puja: offer flowers and namaskar to the family goddess image.\n"
                    "6. Sankalpa: state the new year's resolve before Shiva.\n"
                    "7. Read the Jantri aloud — the purohit or eldest member reads the year's key dates.\n"
                    "8. Exchange Navreh Mubarak greetings.\n"
                    "9. Temple visit: Sharika Devi (Hari Parbat), Kheer Bhawani, or family temple.\n\n"
                    "── NAVREH FOODS ──\n"
                    "Modur Pulav (sweet saffron rice with dry fruits), Haakh (collard greens), "
                    "Nadru yakhni (lotus stem in yogurt sauce), Shufta (dry fruit sweet), "
                    "Kulcha with butter. "
                    "Mantra: 'Om Shreem Hreem Saraswatyai Namah' (Sharada Devi) | "
                    "'Om Gam Ganapataye Namah' (Ganesha for new beginnings)."
                ),
                "links": [
                    ("Wikipedia · Navreh", "https://en.wikipedia.org/wiki/Navreh"),
                    ("Kashmiri Pandits Network · Navreh", "https://www.ikashmir.net/navreh/"),
                ],
            },
            {
                "name": "Kheer Bhawani Mela / Zyeth Ashtami · खीर भवानी",
                "icon": "",
                "timing": "Jyeshtha Shukla Ashtami (May–Jun)",
                "desc": (
                    "Annual pilgrimage to Kheer Bhawani temple at Tulmul (Tullamulla), Ganderbal. "
                    "Thousands of KPs offer milk and kheer (rice pudding) in the sacred spring. "
                    "The spring water's colour (white = peace, dark = trouble) is held to foretell events. "
                    "Ragnya Devi (goddess of the spring) is the most widely venerated KP Kul Devi."
                ),
                "links": [
                    ("Wikipedia · Kheer Bhawani", "https://en.wikipedia.org/wiki/Kheer_Bhawani"),
                    ("iKashmir Temple Info", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "Pann · पान्न",
                "icon": "",
                "timing": "Winter solstice period (Dec–Jan)",
                "desc": (
                    "Kashmiri harvest and winter festival marking the end of the coldest period. "
                    "Community bonfires (alav), seasonal foods (haakh, nadru), songs. "
                    "Associated with the sun's return — sesame seeds (til) are central. "
                    "Corresponds broadly to Makar Sankranti."
                ),
                "links": [
                    ("Kashmiri Pandits Network", "https://www.ikashmir.net/festivals/"),
                ],
            },
            {
                "name": "Kheer Bhawani Mela · खीर भवानी — Zyeth Ashtami Puja",
                "icon": "",
                "timing": "Jyeshtha Shukla Ashtami (May–Jun) — annual pilgrimage",
                "desc": (
                    "Annual pilgrimage to Kheer Bhawani (Ragnya Devi) at Tulmul, Ganderbal.\n\n"
                    "Puja Samagri (Offerings at the spring):\n"
                    "· Fresh milk (dugdha) — the primary offering; poured directly into the sacred spring\n"
                    "· Kheer (rice pudding with saffron) — the goddess's favourite offering; 'Kheer Bhawani' = goddess of kheer\n"
                    "· Mishri (sugar crystals) · Flowers (white: lotus, jasmine, mogra)\n"
                    "· Coconut · Fruits (seasonal) · Incense · Diya (ghee lamp)\n"
                    "· Red cloth (chunri) for the goddess image\n"
                    "· Naivédya (sweet food offering) — Modur Pulav, Shufta.\n\n"
                    "Puja Vidhi:\n"
                    "1. Arrive at Tulmul at Brahma Muhurta or early morning (auspicious).\n"
                    "2. Bathe, wear clean white/yellow clothes.\n"
                    "3. Achamanam and Sankalpa at the spring.\n"
                    "4. Pour milk into the spring — observe the water colour (white = auspicious; dark = alert).\n"
                    "5. Offer kheer, mishri, flowers in the spring.\n"
                    "6. Recite the Devi Stuti: 'Om Aim Hreem Kleem Chamundayai Viche' or 'Om Ragnyai Namah'.\n"
                    "7. Circumambulate the temple (Pradakshina) 3 or 7 times.\n"
                    "8. Offer a red chunri to the goddess image.\n"
                    "9. Receive prasad and sprinkle spring water on oneself.\n\n"
                    "Significance: The spring's colour is believed to be the goddess communicating — "
                    "this tradition is unique in the world. The Zyeth Ashtami mela is the emotional "
                    "heart of KP identity, especially for the diaspora after 1990."
                ),
                "links": [
                    ("Wikipedia · Kheer Bhawani", "https://en.wikipedia.org/wiki/Kheer_Bhawani"),
                    ("iKashmir · Tulmul Temple", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "Ashtami Puja · अष्टमी पूजा — Monthly Kul Devi Worship",
                "icon": "",
                "timing": "Every Shukla Ashtami; Vaishakha, Jyeshtha & Ashwina Ashtamis most sacred",
                "desc": (
                    "KP families observe Ashtami (8th of the waxing moon) as a monthly Kul Devi puja day.\n\n"
                    "Special Ashtamis in the KP calendar:\n"
                    "· Vaishakha Ashtami: Sharika Devi (Hari Parbat) — temple visit mandatory\n"
                    "· Jyeshtha Ashtami (Zyeth Ashtami): Kheer Bhawani pilgrimage\n"
                    "· Ashwina Ashtami: Navratri Ashtami — Maha Puja of Devi\n"
                    "· Phalguna Ashtami: puja before Herath.\n\n"
                    "Puja Samagri:\n"
                    "· Red flowers (gulal/rose preferred for Devi) · Coconut · Mishri\n"
                    "· Red chunri (cloth for the goddess) · Incense · Ghee diya\n"
                    "· Panchamrit · Fruits · Sindoor (vermilion) · Betel nuts and leaves.\n\n"
                    "Puja Vidhi:\n"
                    "1. Fast till noon (upavasa) — water and fruits permitted.\n"
                    "2. Bathe and wear clean clothes (red/yellow preferred for Devi puja).\n"
                    "3. Set up Kul Devi image or yantra on a clean red cloth.\n"
                    "4. Invoke Ganesha (Om Gam Ganapataye Namah).\n"
                    "5. Shodasopachara Puja to Kul Devi: Avahana → Padya → Arghya → Achamana → "
                    "Snana → Vastra → Gandha → Pushpa → Dhupa → Dipa → Naivedya → Tambula → Pradakshina → Namaskara.\n"
                    "6. Recite Devi Kavacham or Durga Saptashati selected dohas.\n"
                    "7. Distribute prasad to family. Break fast with KP satvik meal (no onion/garlic).\n\n"
                    "Mantra: 'Om Sharikayai Namah' (for Sharika Devi) | 'Om Ragnyai Namah' (Kheer Bhawani) | "
                    "'Om Jwaladevyai Namah' (Jwala Devi, Khrew)."
                ),
                "links": [
                    ("iKashmir · KP Religion", "https://www.ikashmir.net/religion/"),
                    ("Wikipedia · Kashmiri Pandits", "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Religious_practices"),
                ],
            },
            {
                "name": "Nityakarma · नित्यकर्म — Complete Daily Ritual",
                "icon": "",
                "timing": "Every day — Brahma Muhurta to evening Deepa Puja",
                "desc": (
                    "The complete daily ritual life (Nityakarma) of a traditional Kashmiri Pandit:\n\n"
                    "── BRAHMA MUHURTA (96 min before sunrise) ──\n"
                    "Wake up, recite: 'Karagre vasate Lakshmi, karamadhye Saraswati / Karamule sthita Gouri, "
                    "prabhate kar-darshanam' (morning salutation to the hands). "
                    "Touch the earth with right foot: 'Samudra-vasane Devi, parvata-stana-mandale / "
                    "Vishnupatni namastubhyam, paadasparsham kshama swame'.\n\n"
                    "── MORNING PURIFICATION ──\n"
                    "Achamanam: sip water 3 times with Shiva names (Shivaya, Shankaraya, Mahadevaya). "
                    "Brush teeth with neem twig (traditional) or brush. "
                    "Full bath (sheetala jal preferred) — recite 'Gange Cha Yamune Chaiva' during bath.\n\n"
                    "── SANDHYA VANDANA (Morning) ──\n"
                    "Face east. Pranayama (3 cycles). "
                    "Gayatri mantra (minimum 10, ideal 108 repetitions): "
                    "'Om Bhur Bhuvaḥ Swaḥ / Tat Savitur Vareṇyam / Bhargo Devasya Dhīmahi / "
                    "Dhiyo Yo Naḥ Prachodayāt.' "
                    "KP-specific addition: Shiva Panchakshara after Gayatri.\n\n"
                    "── HOME SHRINE PUJA (Ghar ki Puja) ──\n"
                    "Puja Samagri: Shiva linga (or Shalagrama), Kul Devi image, Naga (brass serpent), "
                    "Pitru frame (ancestor photos/yantra), fresh flowers, incense, ghee diya, "
                    "panchamrit, fruits, tulsi leaves, Gangajal, kumkum, chandan, rice (akshata).\n\n"
                    "Sequence:\n"
                    "1. Invoke Ganesha first (Vakratunda Mahakaya...).\n"
                    "2. Shiva puja: Abhisheka with water/panchamrit on linga, offer flowers, bilva leaves, "
                    "dhatura (if available), incense, diya. Recite: 'Om Namah Shivaya' (108 times).\n"
                    "3. Kul Devi puja: red flowers, sindoor, coconut, mishri. "
                    "Recite family's specific Devi stotra.\n"
                    "4. Naga puja (on Mondays especially): milk offering to brass snake image.\n"
                    "5. Pitru vandana: water offering and namaskar to ancestors.\n"
                    "6. Mrityunjaya japa (minimum 11 times): "
                    "'Om Tryambakam Yajamahe Sugandhim Pushti-Vardhanam / "
                    "Urvarukamiva Bandhanan Mrityor Mukshiya Mamritat.'\n\n"
                    "── EVENING (Sandhya Dipa) ──\n"
                    "Light ghee diya at dusk. Recite Shiva Stotras or 3 Vakhs of Lal Ded. "
                    "Offer incense. Ring the bell (ghanta) to dispel negative energies.\n\n"
                    "── NIGHT ──\n"
                    "Recite Shiva Sahasranama or Vishnu Sahasranama (by family tradition) before sleep. "
                    "Last thought: 'Om Namah Shivaya.'"
                ),
                "links": [
                    ("WisdomLib · Nityakarma", "https://www.wisdomlib.org/definition/nityakarma"),
                    ("Svacchanda Tantra (ritual basis)", "https://www.wisdomlib.org/definition/svacchanda-tantra"),
                ],
            },
            {
                "name": "Shrāddha & Matamaal Shradh · श्राद्ध — Ancestral Rites",
                "icon": "",
                "timing": "Bhadrapada Krishna Paksha (Pitru Paksha, Sep–Oct) + individual death tithis",
                "desc": (
                    "Ancestral rites of the Kashmiri Pandit tradition — combining Vedic Shraddha "
                    "with specifically Kashmiri Shaiva elements.\n\n"
                    "Types of KP Shraddha:\n"
                    "1. Navaham Shraddha: 9-day rites immediately after death.\n"
                    "2. Masik Shraddha: monthly rite on the death tithi for one year.\n"
                    "3. Varshik Shraddha: annual rite on the death tithi.\n"
                    "4. Pitru Paksha Shraddha: 16-day period when all ancestors are honoured.\n"
                    "5. Matamaal Shraddha: UNIQUE to KP tradition — rites for the maternal lineage "
                    "(mother's parents, maternal uncles) performed separately from paternal rites.\n\n"
                    "Puja Samagri:\n"
                    "· Sesamum seeds (til) — essential for all Shraddha\n"
                    "· Kusha grass (Poa cynosuroides) — purifies the ritual space\n"
                    "· Pinda (balls of cooked rice mixed with sesame, milk, honey)\n"
                    "· Pure water (Gangajal preferred) · Cow's milk and curd\n"
                    "· Sacred thread (yagnopavita) · Dharbha grass\n"
                    "· Flowers (white) · Incense · Diya (sesame oil)\n"
                    "· Black sesame seeds · Barley · Honey · Ghee.\n\n"
                    "Puja Vidhi:\n"
                    "1. Purohit sets up the Shraddha space facing south (direction of ancestors).\n"
                    "2. Invoke Vishvedeva (cosmic witnesses) first.\n"
                    "3. Sankalpa: name the deceased, their gotra, death tithi.\n"
                    "4. Pindadaan: offer 3 pindas (rice balls) — one each for father/mother/grandfather.\n"
                    "5. Tarpan: pour water + sesame southward 3 times for each ancestor.\n"
                    "6. KP-specific: recite Kashmiri Shaiva mantras (Shiva Panchakshara) after standard Vedic recitations.\n"
                    "7. Brahman bhoj (feed a Brahmin) or donate food/clothes.\n"
                    "8. Matamaal Shraddha: repeat steps 3–7 for maternal lineage separately on the same day or next day.\n\n"
                    "Tirthas for Pindadaan: Gaya (Bihar) — most sacred; Prayagraj (Allahabad); "
                    "Vitasta (Jhelum) banks in Kashmir; Haridwar (Ganga). "
                    "Mantra: 'Pitrupibhyo namah / Matrumat-pitrupibhyo namah' (for Matamaal)."
                ),
                "links": [
                    ("Wikipedia · Pitru Paksha", "https://en.wikipedia.org/wiki/Pitru_Paksha"),
                    ("Wikipedia · Shraddha", "https://en.wikipedia.org/wiki/Shraddha"),
                ],
            },
            {
                "name": "Vivāha (KP Wedding) · कश्मीरी पण्डित विवाह — Full Ritual",
                "icon": "",
                "timing": "Auspicious muhurtas (avoid Bhadra, Rahu Kaal, inauspicious nakshatras)",
                "desc": (
                    "Traditional KP wedding — a multi-day ritual combining Vedic, Shaiva and uniquely "
                    "Kashmiri elements. The purohit uses the Jantri to fix the muhurta.\n\n"
                    "── PRE-WEDDING RITUALS ──\n"
                    "Devgun (1–3 days before): invoke all family deities — Kul Devi, Kul Devta, "
                    "Naga (serpent), Ganesha, and Bhairava. "
                    "Puja Samagri: flowers, incense, panchamrit, coconut, red cloth (for Devi), "
                    "sindoor, fruits, paan, akshat (coloured rice), new clothes.\n\n"
                    "Lagan Ceremony (day before): Purohit arrives and ties the Lagan thread — "
                    "a sacred red/white cord fixed in the threshold. Recites the Muhurta Sankalpa. "
                    "Wanwun songs begin: elder women sing the Devgun Wanwun (Kashmiri songs invoking deities).\n\n"
                    "── WEDDING DAY ──\n"
                    "Groom's home — Sannaj (tilak ceremony): groom's forehead marked with kumkum, "
                    "chandan, akshat by maternal uncle. "
                    "Vardakshina: gifts from bride's family to groom's family.\n\n"
                    "Bride's home — Mehndi & Wanwun: "
                    "Henna applied; women sing Wanwun songs specific to each stage. "
                    "The song catalogue is enormous — different songs for: "
                    "dressing the bride, groom's arrival, Saptapadi, Vidai.\n\n"
                    "Pheran ceremony: bride dressed in traditional Pheran (long loose robe) "
                    "with Tarang (headpiece of gold/silver flowers) and Dejhour (earrings).\n\n"
                    "Vivaha Homa (sacred fire): Ganesha puja → Navagraha puja → Vivaha fire lit. "
                    "Kanyadan: father places daughter's right hand in groom's (Panigrahan). "
                    "Saptapadi: 7 steps around fire — each step = a vow:\n"
                    "1st: food/livelihood 2nd: strength 3rd: prosperity 4th: happiness "
                    "5th: children 6th: seasons/health 7th: eternal friendship.\n\n"
                    "Dejhour Exchange: unique KP custom — ornamental earrings (Dejhour) exchanged "
                    "between families as a bond of kinship.\n\n"
                    "── POST-WEDDING ──\n"
                    "Khon Batta (homecoming feast): bride enters groom's home, "
                    "steps on rice/flowers at threshold. "
                    "Wanwun Vidai songs: the most emotionally charged songs of the entire tradition.\n\n"
                    "Gotra verification: Both families' gotras must be different — "
                    "same-gotra marriage is strictly forbidden (sagotra vivaha varjya)."
                ),
                "links": [
                    ("Wikipedia · KP Customs", "https://en.wikipedia.org/wiki/Kashmiri_Pandits#Customs_and_traditions"),
                    ("iKashmir · Marriage", "https://www.ikashmir.net/marriage/"),
                    ("Wikipedia · Wanwun", "https://en.wikipedia.org/wiki/Wanwun"),
                ],
            },
            {
                "name": "Pann · पान्न — Winter Solstice Festival",
                "icon": "",
                "timing": "Around Makar Sankranti / winter solstice (Dec–Jan)",
                "desc": (
                    "Kashmiri winter solstice festival marking the sun's return (Uttarayana). "
                    "In Kashmir, this overlaps with the coldest period (Chillai Kalan — 40 coldest days).\n\n"
                    "Rituals and customs:\n"
                    "· Community bonfires (Alav) at night — families gather around fire, "
                    "songs are sung, the fire symbolises the returning sun.\n"
                    "· Til (sesame) offerings — til is sacred on this day: til laddoos (sesame balls), "
                    "til ka halwa, til mixed with jaggery distributed to all.\n"
                    "· Surya Puja: morning sun worship especially by KP families of Anantnag "
                    "(Martand Surya tradition).\n"
                    "· Ritual bath (snan) at dawn in the Vitasta (Jhelum) river.\n\n"
                    "Puja Samagri: Sesame seeds, jaggery (gud), flowers, water, red thread, "
                    "fruits, cow dung cakes (for the bonfire), ghee.\n\n"
                    "Puja Vidhi:\n"
                    "1. Pre-dawn bath in river or home.\n"
                    "2. Surya Arghya: offer water to the rising sun 3 times from cupped hands.\n"
                    "3. Recite Surya Stotram: 'Om Suryaya Namah / Aditya Hridayam' (Aditya Hridayam from Ramayana).\n"
                    "4. Light bonfire at dusk with family.\n"
                    "5. Distribute til-gud to neighbours and relatives (sweet = warmth/friendship).\n\n"
                    "KP saying: 'Pann on Pann, Shishur on Herath' — the walnut (Shishur) is associated "
                    "with Herath as sesame (til) is associated with Pann."
                ),
                "links": [
                    ("iKashmir · Festivals", "https://www.ikashmir.net/festivals/"),
                    ("Wikipedia · Makar Sankranti", "https://en.wikipedia.org/wiki/Makar_Sankranti"),
                ],
            },
            {
                "name": "Navratri Puja · नवरात्रि — Nine Nights of Devi",
                "icon": "",
                "timing": "Ashwina Shukla 1–9 (Sep–Oct) — main; also Chaitra Navratri (Mar–Apr)",
                "desc": (
                    "Nine nights of goddess worship — KPs observe both Ashwina and Chaitra Navratri. "
                    "Ashwina Navratri is the primary one.\n\n"
                    "KP Navratri sequence:\n"
                    "· Day 1: Kalash Sthapana (sacred water pot installed), Kul Devi invoked.\n"
                    "· Days 1–9: Daily Devi puja morning and evening. Many KPs fast (no grains, "
                    "eat fruits, samak rice, kuttu atta).\n"
                    "· Ashtami (Day 8): MOST important — Maha Puja of Kul Devi. Kanya Puja "
                    "(9 young girls worshipped as Navadurga). Homa (sacred fire) performed.\n"
                    "· Navami (Day 9): Maha Navami — weapons/tools worship (Ayudha Puja).\n\n"
                    "Puja Samagri:\n"
                    "· Kalash (copper/brass pot) with mango leaves and coconut\n"
                    "· Red cloth, red flowers (rose, hibiscus) · Sindoor · Kumkum\n"
                    "· Coconut (whole with husk) · Red chunri · Durva grass\n"
                    "· Panchamrit (milk, curd, ghee, honey, sugar) · Fruits · Halwa, puri, chana (for Kanya puja)\n"
                    "· Incense, ghee diya, camphor · Marigold garland · Betel leaves and nuts.\n\n"
                    "Puja Vidhi (Ashtami — most elaborate):\n"
                    "1. Kalash puja (water pot as Devi).\n"
                    "2. Shodasopachara Puja to Kul Devi image.\n"
                    "3. Durga Saptashati path (7 chapters) — or Devi Kavacham + Argala + Kilakam.\n"
                    "4. Kanya Puja: wash feet of 9 girls, offer food (puri, halwa, chana), tie red thread.\n"
                    "5. Homa with specific Devi mantras.\n"
                    "6. Aarti: 'Jai Ambe Gauri' or KP-specific Kul Devi aarti in Kashmiri.\n\n"
                    "Mantra: 'Om Aim Hreem Kleem Chamundayai Viche' (Devi Navarna Mantra)."
                ),
                "links": [
                    ("Wikipedia · Navratri", "https://en.wikipedia.org/wiki/Navratri"),
                    ("Durga Saptashati", "https://www.wisdomlib.org/hinduism/book/devi-mahatmya"),
                ],
            },
        ],
        "Sacred Sites & Temples · तीर्थ": [
            # ── KUL DEVI TEMPLES ──────────────────────────────────
            {
                "name": "Hari Parbat — Sharika Devi (Chakreshwari) · शारिका देवी, हरि पर्वत",
                "icon": "",
                "timing": "Year-round; Vaishakha Ashtami (Apr–May) is principal festival",
                "desc": (
                    "KUL DEVI TEMPLE · The principal Kul Devi of Srinagar and old-city KP families.\n"
                    "Location: Hari Parbat Hill, Srinagar · 34.1003°N 74.8305°E\n"
                    "Google Maps: https://maps.app.goo.gl/SharikaDevi\n\n"
                    "The hill IS the goddess — she took the form of a stone to crush the demon "
                    "Jalodbhava who lived in the primordial lake Satisar. "
                    "The Sri Chakra (sacred geometry of the goddess) is embedded in the hilltop rock. "
                    "Mughal fortification walls (Akbar era, 1590s) encircle the hill. "
                    "Also houses Makhdoom Sahib Sufi shrine on the northern slope.\n\n"
                    "Deity: Sharika Devi = Chakreshwari = 18-armed goddess holding the Sri Chakra\n"
                    "Gotra connection: Kashyapa, Vasishtha, and multiple KP lineages claim Sharika as Kul Devi\n"
                    "Puja: Milk/panchamrit abhisheka on the Sharika stone, red flowers, sindoor, coconut\n"
                    "Mantra: 'Om Sharikayai Namah' | 'Om Chakreshwaryai Namah'\n"
                    "Reference: Nilamata Purana (verses on Hari Parbat), Rajatarangini (Kalhana)"
                ),
                "links": [
                    ("Wikipedia · Hari Parbat", "https://en.wikipedia.org/wiki/Hari_Parbat"),
                    ("Wikipedia · Sharika Devi", "https://en.wikipedia.org/wiki/Sharika"),
                    ("Google Maps · Hari Parbat", "https://www.google.com/maps/search/Hari+Parbat+Srinagar"),
                    ("iKashmir · Sharika Temple", "https://www.ikashmir.net/temples/"),
                ],
            },
            {
                "name": "Kheer Bhawani — Ragnya Devi · खीर भवानी, तुलमुल (गंदेरबल)",
                "icon": "",
                "timing": "Year-round; Zyeth Ashtami (May–Jun) annual mela — most sacred day",
                "desc": (
                    "KUL DEVI TEMPLE · Most widely venerated Kul Devi across all KP families.\n"
                    "Location: Tullamulla (Tulmul) village, Ganderbal district · 34.2285°N 74.8090°E\n"
                    "Google Maps: https://www.google.com/maps/search/Kheer+Bhawani+Temple+Tulmul\n\n"
                    "Sacred spring of changing colour — white (peace), dark red (trouble), "
                    "black (great danger). Offerings of milk and kheer poured into the spring. "
                    "Built over an ancient Shakti spring mentioned in the Nilamata Purana. "
                    "Last major restoration by Maharaja Pratap Singh (early 20th century). "
                    "Multiple satellite Kheer Bhawani temples now exist in Jammu, Delhi, "
                    "Mumbai and KP diaspora cities worldwide.\n\n"
                    "Deity: Ragnya Devi = Bhagavati = Maharagya\n"
                    "Puja: Milk poured into spring → kheer → white flowers → red chunri → "
                    "Pradakshina → spring water on forehead\n"
                    "Mantra: 'Om Ragnyai Namah' | 'Om Maharaghyai Namah'\n"
                    "Stotra: Ksheer Bhawani Stotra (Sanskrit) recited by purohit at the spring"
                ),
                "links": [
                    ("Wikipedia · Kheer Bhawani", "https://en.wikipedia.org/wiki/Kheer_Bhawani"),
                    ("Google Maps · Kheer Bhawani Tulmul", "https://www.google.com/maps/search/Kheer+Bhawani+Tullamulla+Ganderbal"),
                    ("iKashmir · Tulmul", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "Jwala Devi — Khrew · ज्वाला देवी, खरेव (पुलवामा)",
                "icon": "",
                "timing": "Year-round; Navratri Ashtami (Mar–Apr & Sep–Oct) principal festival",
                "desc": (
                    "KUL DEVI TEMPLE · Principal Kul Devi of Pulwama, Pampore and south Kashmir KP families.\n"
                    "Location: Khrew village, Pulwama district · 33.8799°N 74.9800°E (approx.)\n"
                    "Google Maps: https://www.google.com/maps/search/Jwala+Devi+Temple+Khrew+Pulwama\n\n"
                    "The goddess manifests as a perpetual natural flame in the sanctum — "
                    "unique in Kashmir. Combines Shakta fire-goddess tradition with Kashmir Shaivism. "
                    "Navratri Ashtami draws thousands of KP pilgrims from across the valley.\n\n"
                    "Deity: Jwala Devi = Vahni Devi = flame manifestation of Shakti\n"
                    "Puja: Ghee offered into the flame (deepa puja), red flowers, sindoor, coconut\n"
                    "Pradakshina: 7 circumambulations\n"
                    "Mantra: 'Om Jwaladevyai Namah' | 'Om Agnijwalaayai Namah'"
                ),
                "links": [
                    ("Wikipedia · Jwaladevi Temple Khrew", "https://en.wikipedia.org/wiki/Jwaladevi_Temple,_Khrew"),
                    ("Google Maps · Jwala Devi Khrew", "https://www.google.com/maps/search/Jwala+Devi+Temple+Khrew+Kashmir"),
                ],
            },
            {
                "name": "Bhadrakali Temple, Anantnag · भद्रकाली, अनन्तनाग",
                "icon": "",
                "timing": "Year-round; Navratri and Ashtamis",
                "desc": (
                    "KUL DEVI TEMPLE · Kul Devi of Anantnag, Shopian and south Kashmir KP families.\n"
                    "Location: Anantnag district, south Kashmir · 33.7311°N 75.1487°E\n"
                    "Google Maps: https://www.google.com/maps/search/Bhadrakali+Temple+Anantnag\n\n"
                    "Bhadrakali (Bhadra = auspicious + Kali = fierce goddess) is a fierce form "
                    "of Shakti combining grace and power. Her cult is ancient in south Kashmir. "
                    "Multiple Bhadrakali temples exist across Anantnag and Shopian districts — "
                    "each neighbourhood (mohalla) has its own Bhadrakali shrine.\n\n"
                    "Deity: Bhadrakali = fierce Shakti who destroys evil and protects devotees\n"
                    "Puja: Red flowers, sindoor, coconut, goat sacrifice (in some traditions) "
                    "replaced by pumpkin sacrifice in most modern KP families\n"
                    "Mantra: 'Om Bhadrakalyai Namah' | 'Om Krim Kalyai Namah'"
                ),
                "links": [
                    ("Wikipedia · Bhadrakali", "https://en.wikipedia.org/wiki/Bhadrakali"),
                    ("Google Maps · Bhadrakali Anantnag", "https://www.google.com/maps/search/Bhadrakali+Temple+Anantnag+Kashmir"),
                ],
            },
            {
                "name": "Tripura Sundari — Devsar & Kulgam · त्रिपुरा सुन्दरी",
                "icon": "",
                "timing": "Year-round; Navratri",
                "desc": (
                    "KUL DEVI TEMPLE · Kul Devi of Kulgam, D.H. Pora and deep south Kashmir KP families.\n"
                    "Location: Devsar area, Kulgam district · 33.6443°N 75.0177°E\n"
                    "Google Maps: https://www.google.com/maps/search/Tripura+Sundari+Temple+Kulgam\n\n"
                    "Tripura Sundari (Shodashi) = the most beautiful in the three worlds. "
                    "One of the Dasha Mahavidyas (10 wisdom goddesses) in the Shakta tradition. "
                    "Her Sri Yantra is the most complex and sacred yantra in Tantra. "
                    "South Kashmir KP families with Kulgam ancestry venerate her as their primary Kul Devi.\n\n"
                    "Deity: Tripura Sundari = Shodashi = Lalita = supreme Shakti\n"
                    "Mantra: 'Om Aim Hreem Shreem Tripura Sundaryai Namah'\n"
                    "Reference: Lalita Sahasranama, Soundarya Lahari (Adi Shankaracharya)"
                ),
                "links": [
                    ("Wikipedia · Tripura Sundari", "https://en.wikipedia.org/wiki/Tripura_Sundari"),
                    ("Google Maps · Kulgam temples", "https://www.google.com/maps/search/ancient+temples+Kulgam+Kashmir"),
                ],
            },
            {
                "name": "Sharada Peeth · शारदा पीठ (Sharda, PoK) — Seat of Saraswati",
                "icon": "",
                "timing": "Sharada Navami (Ashwina Shukla 9) — proxy puja worldwide",
                "desc": (
                    "KUL DEVI / SHAKTI PITHA · Most sacred lost site of all Kashmiri Pandits.\n"
                    "Location: Sharda village, Neelum Valley, Pakistan-administered Kashmir (PoK)\n"
                    "Coordinates: 34.6745°N 73.9814°E (approximate)\n"
                    "Google Maps: https://www.google.com/maps/search/Sharda+Peeth+Neelum+Valley\n\n"
                    "One of the 18 Maha Shakti Pithas — Sati's right hand fell here. "
                    "Ancient seat of learning: library rivalling Nalanda, visited by scholars across Asia. "
                    "Adi Shankaracharya is said to have won the Sarvajnapitha debate here. "
                    "The Sharada script (ancient Kashmir script, ancestor of Gurmukhi) is named after this temple. "
                    "The Devi's form here: Sharada = 16-armed Saraswati holding veena, books, akshamala, kamandalu. "
                    "Annual proxy puja by KPs worldwide on Sharada Navami — "
                    "reciting 'Ya Sharada nilotpala-dala-shyama...'\n\n"
                    "Campaign: Sharda Peeth Trust India; cross-LoC pilgrimage access demanded annually."
                ),
                "links": [
                    ("Wikipedia · Sharada Peeth", "https://en.wikipedia.org/wiki/Sharada_Peeth"),
                    ("Google Maps · Sharda Village PoK", "https://www.google.com/maps/search/Sharda+village+Neelum+Valley+Azad+Kashmir"),
                    ("Wikipedia · Sharada script", "https://en.wikipedia.org/wiki/Sharada_script"),
                ],
            },
            {
                "name": "Vaishno Devi · वैष्णो देवी, त्रिकूट पर्वत (रियासी)",
                "icon": "",
                "timing": "Year-round; Navratri most sacred — 8–10 million pilgrims annually",
                "desc": (
                    "KUL DEVI / SHAKTI PITHA · Kul Devi of many KP families from Jammu region.\n"
                    "Location: Trikuta Hills, Reasi district, Jammu · 32.9760°N 74.9525°E\n"
                    "Google Maps: https://www.google.com/maps/search/Vaishno+Devi+Temple+Katra\n\n"
                    "One of India's most visited pilgrimage sites. The goddess resides in a natural "
                    "cave as three pindis (rocks) representing Maha Kali, Maha Lakshmi and Maha Saraswati. "
                    "The cave is reached after a 14km trek from Katra base camp. "
                    "Bhairon Mandir (at Bhairo Ghati, 2.5km from cave) is mandatory for complete pilgrimage — "
                    "'Yatra is incomplete without Bhairon darshan.'\n\n"
                    "Mantra: 'Jai Mata Di' | 'Om Aim Hreem Kleem Mahalakshmyai Namah'\n"
                    "Official board: Shri Mata Vaishno Devi Shrine Board"
                ),
                "links": [
                    ("Wikipedia · Vaishno Devi", "https://en.wikipedia.org/wiki/Vaishno_Devi"),
                    ("Official Shrine Board", "https://www.maavaishnodevi.org/"),
                    ("Google Maps · Vaishno Devi", "https://www.google.com/maps/search/Vaishno+Devi+Shrine+Katra"),
                ],
            },
            # ── MAJOR SHIVA TEMPLES ──────────────────────────────
            {
                "name": "Shankaracharya Temple (Jyeshtheshwara) · ज्येष्ठेश्वर, गोपाद्रि पर्वत",
                "icon": "",
                "timing": "Year-round; Herath night vigil most sacred",
                "desc": (
                    "SHIVA TEMPLE · Presiding Shiva of Srinagar city.\n"
                    "Location: Shankaracharya Hill (Gopadri/Takht-i-Suleiman), Srinagar · 34.0888°N 74.8601°E\n"
                    "Google Maps: https://www.google.com/maps/search/Shankaracharya+Temple+Srinagar\n\n"
                    "The octagonal stone temple at 1,000m — one of the oldest temples in Kashmir. "
                    "Original structure: King Gopaditya (Kaliyuga 2526 = c. 371 BCE per Rajatarangini). "
                    "Present form: 9th–10th century CE. Deity: Jyeshtheshwara = Lord of Elders = Shiva. "
                    "Vasugupta received the Shiva Sutras near this hill. "
                    "On Herath night: thousands of KPs climb the hill for the all-night vigil — "
                    "the view of Srinagar's lights from the top is a quintessentially Kashmiri experience.\n\n"
                    "Mantra: 'Om Jyeshtheshwaraya Namah'\n"
                    "Reference: Rajatarangini (Kalhana, Book 1), Nilamata Purana"
                ),
                "links": [
                    ("Wikipedia · Shankaracharya Temple", "https://en.wikipedia.org/wiki/Shankaracharya_temple,_Srinagar"),
                    ("Google Maps · Shankaracharya Hill", "https://www.google.com/maps/search/Shankaracharya+temple+Gopadri+hill+Srinagar"),
                ],
            },
            {
                "name": "Amarnath Cave Temple · अमरनाथ (पहलगाम/बालटाल)",
                "icon": "",
                "timing": "Annual Yatra: Shravana Purnima (Jul–Aug) · 3,888m altitude",
                "desc": (
                    "SHIVA PILGRIMAGE · Most sacred Himalayan Shiva shrine.\n"
                    "Location: South Kashmir Himalayas · 34.2144°N 75.5028°E\n"
                    "Google Maps: https://www.google.com/maps/search/Amarnath+Cave+Temple+Kashmir\n\n"
                    "Natural ice Shivalinga waxes and wanes with the moon. "
                    "Two white pigeons (immortal devotees per legend) seen in the cave every year. "
                    "Routes: Pahalgam via Chandanwari → Sheshnag → Panchtarni → Cave (45km, 4 days); "
                    "Baltal → Cave (14km, steep, 1 day). "
                    "Chhari Mubarak (holy mace) procession from Dashnami Akhara, Srinagar precedes Yatra. "
                    "KPs must perform this Yatra at least once in lifetime.\n\n"
                    "Mantra: 'Om Namah Shivaya' | Mrityunjaya Japa at the cave\n"
                    "Official: Shri Amarnathji Shrine Board (shriamarnathjishrine.com)"
                ),
                "links": [
                    ("Wikipedia · Amarnath", "https://en.wikipedia.org/wiki/Amarnath_temple"),
                    ("Official Shrine Board", "https://shriamarnathjishrine.com/"),
                    ("Google Maps · Amarnath Cave", "https://www.google.com/maps/search/Amarnath+Cave+shrine+Pahalgam"),
                ],
            },
            {
                "name": "Bijbehara Shiva Temple (Vijeshvara) · विजेश्वर, बिजबेहाड़ा",
                "icon": "",
                "timing": "Year-round; Shivratri and Herath",
                "desc": (
                    "SHIVA TEMPLE · One of the most ancient Shiva temples in Kashmir.\n"
                    "Location: Bijbehara, Anantnag district · 33.9137°N 75.0120°E\n"
                    "Google Maps: https://www.google.com/maps/search/Vijeshvara+temple+Bijbehara+Anantnag\n\n"
                    "Vijeshvara (= Shiva as the Lord of Heroes) is one of the principal Shiva shrines "
                    "of Anantnag district. The temple is mentioned in early medieval Kashmir texts. "
                    "The town Bijbehara is an ancient KP settlement with a history dating back over 2000 years. "
                    "The Vitasta (Jhelum) flows near the temple.\n\n"
                    "Mantra: 'Om Vijeshvaraya Namah'\n"
                    "Reference: Nilamata Purana, Rajatarangini"
                ),
                "links": [
                    ("Wikipedia · Bijbehara", "https://en.wikipedia.org/wiki/Bijbehara"),
                    ("Google Maps · Bijbehara temple", "https://www.google.com/maps/search/ancient+temple+Bijbehara+Anantnag"),
                ],
            },
            {
                "name": "Shiva Temple — Baramulla (Varahamula) · वराहमूल शिव मन्दिर",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "SHIVA TEMPLE · Ancient Shiva shrine at Baramulla, north Kashmir.\n"
                    "Location: Baramulla town · 34.2099°N 74.3450°E\n"
                    "Google Maps: https://www.google.com/maps/search/Shiva+Temple+Baramulla+Kashmir\n\n"
                    "Baramulla = Varahamula (Varaha's snout) — where Varaha (Vishnu's boar avatar) "
                    "struck the Himalayan range to release the waters of Satisar lake, "
                    "creating the Kashmir Valley (Nilamata Purana mythology). "
                    "The Vitasta (Jhelum) exits the valley through Baramulla. "
                    "Multiple ancient Shiva and Vishnu temples historically dotted this town.\n\n"
                    "Reference: Nilamata Purana (Varahamula section), Rajatarangini"
                ),
                "links": [
                    ("Wikipedia · Baramulla", "https://en.wikipedia.org/wiki/Baramulla"),
                    ("Google Maps · Baramulla temples", "https://www.google.com/maps/search/ancient+temple+Baramulla+Kashmir"),
                ],
            },
            # ── SURYA / VISHNU TEMPLES ────────────────────────────
            {
                "name": "Martand Sun Temple · मार्तण्ड सूर्य मन्दिर, मट्टन (अनन्तनाग)",
                "icon": "",
                "timing": "Sunrise visits; Ratha Saptami (Magha Shukla 7) most sacred",
                "desc": (
                    "SURYA TEMPLE · Greatest Surya temple of ancient India.\n"
                    "Location: Mattan, Anantnag district · 33.7583°N 75.2145°E\n"
                    "Google Maps: https://www.google.com/maps/search/Martand+Sun+Temple+Mattan+Anantnag\n\n"
                    "Built by King Lalitaditya Muktapida (c. 724–760 CE) of the Karkota dynasty. "
                    "Main sanctum flanked by 84 smaller shrines. "
                    "Temple faces east — equinox sunrise illuminates the inner sanctum precisely. "
                    "Destroyed by Sultan Sikandar (Butshikan) c. 1400 CE. "
                    "Ruins are among the finest examples of Kashmiri temple architecture. "
                    "ASI protected monument.\n\n"
                    "Deity: Martanda Surya (the immortal sun)\n"
                    "Puja: Arghya to the rising sun, Aditya Hridayam recitation\n"
                    "Mantra: 'Om Suryaya Namah' | 'Om Mitraya Namah'\n"
                    "Reference: Rajatarangini (Book 4, Lalitaditya's reign)"
                ),
                "links": [
                    ("Wikipedia · Martand Sun Temple", "https://en.wikipedia.org/wiki/Martand_Sun_Temple"),
                    ("Google Maps · Martand Temple", "https://www.google.com/maps/search/Martand+Sun+Temple+Kashmir"),
                    ("ASI Kashmir", "https://asi.nic.in/"),
                ],
            },
            {
                "name": "Awantiswara & Awantishwamin · अवन्तिस्वर और अवन्तिस्वामिन (अवन्तिपोर)",
                "icon": "",
                "timing": "Year-round; Shivratri (Awantiswara) and Ekadashi (Awantishwamin)",
                "desc": (
                    "SHIVA + VISHNU TEMPLES · Twin 9th century temples — finest pre-Islamic Kashmir architecture.\n"
                    "Location: Awantipora, Pulwama district · 33.9225°N 75.0140°E\n"
                    "Google Maps: https://www.google.com/maps/search/Avantiswara+temple+Awantipora\n\n"
                    "Built by King Awantivarman (855–883 CE) of the Utpala dynasty. "
                    "Awantiswara: Shiva temple (south side of road). "
                    "Awantishwamin: Vishnu temple (north side of road). "
                    "Both temples display the mature Kashmiri temple style — "
                    "trefoil arched niches, carved friezes, peristyle colonnades. "
                    "Now in ruins but magnificent; ASI protected.\n\n"
                    "Mantra (Awantiswara): 'Om Awanteshwaraya Namah'\n"
                    "Mantra (Awantishwamin): 'Om Awantishwamine Namah' (Vishnu)\n"
                    "Reference: Rajatarangini Book 5 (Awantivarman's reign), ASI documentation"
                ),
                "links": [
                    ("Wikipedia · Avantiswara", "https://en.wikipedia.org/wiki/Avantiswara_temple"),
                    ("Google Maps · Avantiswara Awantipora", "https://www.google.com/maps/search/Avantiswara+Awantipora+Pulwama"),
                    ("ASI Kashmir circles", "https://asi.nic.in/"),
                ],
            },
            # ── NAG TEMPLES (SACRED SPRINGS) ─────────────────────
            {
                "name": "Nag Temples — Nagbal · नागबल (गंदेरबल)",
                "icon": "",
                "timing": "Nag Panchami (Shravana Shukla 5) most sacred; year-round",
                "desc": (
                    "NAG TIRTHA · Sacred Naga (serpent deity) spring — one of the most important in Kashmir.\n"
                    "Location: Nagbal area, Ganderbal district · Near Srinagar-Leh highway\n"
                    "Google Maps: https://www.google.com/maps/search/Nagbal+spring+Ganderbal+Kashmir\n\n"
                    "Kashmir has dozens of sacred Naga springs (Nagas are water deities in Nilamata Purana). "
                    "The Nilamata Purana lists 527 Naga tirthas in Kashmir! "
                    "Major Naga tirthas: Nagbal, Anantanag (the spring that gave Anantnag its name), "
                    "Nandikund, Vasukikund, Takshakakund. "
                    "KPs perform Nag Puja on Nag Panchami — offer milk to the Naga spring, "
                    "tie sacred thread, offer flowers.\n\n"
                    "Anantnag = 'Ananta-nag' = the spring of Ananta (the infinite serpent/Shiva).\n\n"
                    "Mantra: 'Om Namo Bhagavate Anantaya' | 'Om Nagaya Namah'\n"
                    "Nag Puja items: Milk, flowers, durva grass, silver Naga image\n"
                    "Reference: Nilamata Purana (Naga section — over 300 verses on Naga worship)"
                ),
                "links": [
                    ("Wikipedia · Nag Panchami", "https://en.wikipedia.org/wiki/Nag_Panchami"),
                    ("Google Maps · Nagbal", "https://www.google.com/maps/search/Nagbal+Ganderbal+Kashmir"),
                    ("Nilamata Purana · Naga tirthas", "https://www.wisdomlib.org/hinduism/book/nilamata-purana"),
                ],
            },
            {
                "name": "Anantnag Spring (Nagin / Nag Tirtha) · अनन्तनाग नाग तीर्थ",
                "icon": "",
                "timing": "Nag Panchami; year-round pilgrimage",
                "desc": (
                    "NAG TIRTHA · The ancient spring that gave Anantnag city its name.\n"
                    "Location: Anantnag town centre · 33.7311°N 75.1487°E\n"
                    "Google Maps: https://www.google.com/maps/search/Anantanag+spring+Anantnag\n\n"
                    "Anantnag = Ananta (the infinite Naga/Shiva) + Nag (spring/serpent deity). "
                    "The original spring (natural bubbling spring) was one of the most sacred "
                    "Naga tirthas in the Nilamata Purana. Multiple ancient temples surrounded the spring. "
                    "The Vitasta (Jhelum) flows nearby. "
                    "South Kashmir KP families from Anantnag consider this their ancestral sacred spring. "
                    "Nag Panchami puja: milk, flowers, silver Naga idol offered at the spring.\n\n"
                    "Reference: Nilamata Purana · Rajatarangini"
                ),
                "links": [
                    ("Wikipedia · Anantnag", "https://en.wikipedia.org/wiki/Anantnag"),
                    ("Google Maps · Anantnag city", "https://www.google.com/maps/search/Anantnag+spring+Kashmir"),
                ],
            },
            {
                "name": "Verinag Spring (Vitasta source) · वेरीनाग, वितस्ता उद्गम",
                "icon": "",
                "timing": "Vitasta Jayanti; year-round pilgrimage",
                "desc": (
                    "NAG / RIVER TIRTHA · Source spring of the river Vitasta (Jhelum) — most sacred spring in Kashmir.\n"
                    "Location: Verinag, Anantnag district · 33.5345°N 75.2590°E\n"
                    "Google Maps: https://www.google.com/maps/search/Verinag+Spring+Anantnag+Kashmir\n\n"
                    "The source spring of the Vitasta (Jhelum) — a natural octagonal spring of "
                    "crystal-clear blue water. Visible fish at the bottom. "
                    "Emperor Jahangir built a beautiful Mughal garden and octagonal masonry spring here (1620). "
                    "KPs come here to collect sacred Vitasta water for ceremonies. "
                    "Vitasta Jayanti is observed annually — puja at the spring source. "
                    "The Nilamata Purana dedicates major sections to Vitasta worship — "
                    "she is the 'mother' of Kashmir.\n\n"
                    "Mantra: 'Om Vitastayai Namah' | Vitasta Stotra (Nilamata Purana)\n"
                    "Significance: Vitasta water is used in all major KP rituals — Herath, Shraddha, Vivaha"
                ),
                "links": [
                    ("Wikipedia · Verinag", "https://en.wikipedia.org/wiki/Verinag"),
                    ("Google Maps · Verinag Spring", "https://www.google.com/maps/search/Verinag+spring+source+Jhelum"),
                    ("Nilamata Purana", "https://www.wisdomlib.org/hinduism/book/nilamata-purana"),
                ],
            },
            # ── SACRED SPRINGS & GARDENS ─────────────────────────
            {
                "name": "Achabal Spring & Gardens · अचाबल (अनन्तनाग)",
                "icon": "",
                "timing": "Year-round; spring (Vasanta) most beautiful",
                "desc": (
                    "SACRED SPRING & GARDEN · Ancient Naga tirtha and Mughal garden.\n"
                    "Location: Achabal, Anantnag district · 33.6310°N 75.2040°E\n"
                    "Google Maps: https://www.google.com/maps/search/Achabal+Spring+Garden+Anantnag\n\n"
                    "Achabal (= Achibal = Akshivahal = 'the eye of the valley') — "
                    "an ancient sacred spring mentioned in the Rajatarangini. "
                    "The spring gushes from beneath a cliff at extraordinary volume. "
                    "Mughal Empress Nur Jahan developed it into a terraced garden (early 17th century). "
                    "The spring is considered a Naga tirtha by KP tradition — "
                    "Nag Panchami puja observed here. "
                    "Natural setting: plane trees (chinar), willows, water channels (nalas).\n\n"
                    "Reference: Rajatarangini, Ain-i-Akbari (Abul Fazl's record of Mughal Kashmir)"
                ),
                "links": [
                    ("Wikipedia · Achabal", "https://en.wikipedia.org/wiki/Achabal"),
                    ("Google Maps · Achabal", "https://www.google.com/maps/search/Achabal+garden+spring+Anantnag"),
                ],
            },
            {
                "name": "Kokernag Springs · कोकरनाग (अनन्तनाग)",
                "icon": "",
                "timing": "Year-round; spring most sacred",
                "desc": (
                    "SACRED SPRINGS · Ancient Naga tirthas and most prolific spring complex in Kashmir.\n"
                    "Location: Kokernag, Anantnag district · 33.5736°N 75.2650°E\n"
                    "Google Maps: https://www.google.com/maps/search/Kokernag+Springs+Anantnag+Kashmir\n\n"
                    "Kokernag = Kakanaag = the snake of Kaka (an ancient Naga deity). "
                    "The largest natural spring complex in Kashmir Valley — 70+ springs in one area. "
                    "The water is exceptionally pure and cold — a sacred bathing tirtha. "
                    "Ancient KP tradition: ritual bath at Kokernag on auspicious occasions. "
                    "Multiple Shiva and Naga shrines surround the springs.\n\n"
                    "Reference: Rajatarangini (Kalhana mentions multiple springs), Nilamata Purana"
                ),
                "links": [
                    ("Wikipedia · Kokernag", "https://en.wikipedia.org/wiki/Kokernag"),
                    ("Google Maps · Kokernag", "https://www.google.com/maps/search/Kokernag+springs+Kashmir"),
                ],
            },
            # ── BHAIRAVA TEMPLES ─────────────────────────────────
            {
                "name": "Anandeshwara Bhairava · आनन्देश्वर भैरव (श्रीनगर — अमीरा कदल / सत्थू बर्बर शाह)",
                "icon": "",
                "timing": "Year-round; Herath night most sacred",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian of central Srinagar — Amira Kadal, Ganpatyar, Maisuma area.\n"
                    "Location: Central Srinagar (Sathu Barbar Shah / Amira Kadal area) · 34.0800°N 74.8050°E\n"
                    "Google Maps: https://www.google.com/maps/search/Anandeshwara+Bhairava+temple+Srinagar\n\n"
                    "One of the 8 Ashta Bhairavas of Kashmir — guards the North-East direction. "
                    "Anandeshwara = Lord of Bliss (Ananda = bliss + Ishwara = Lord = Shiva as Bhairava). "
                    "Patron Bhairava of central Srinagar KP families from Amira Kadal and Ganpatyar mohallas. "
                    "Worshipped on Herath night: special Vatuk (child Bhairava) puja alongside Vatak Puja. "
                    "Puja: bilva leaves, blue flowers, til, sesame, blood-red sindoor\n\n"
                    "Mantra: 'Om Hreem Anandeshwaraya Bhairavaya Namah'\n"
                    "Reference: Nilamata Purana (Ashta Bhairava section)"
                ),
                "links": [
                    ("Wikipedia · Bhairava Kashmir", "https://en.wikipedia.org/wiki/Bhairava"),
                    ("Google Maps · Srinagar Bhairava temples", "https://www.google.com/maps/search/Bhairava+temple+Srinagar+Kashmir"),
                    ("iKashmir · Bhairava temples", "https://www.ikashmir.net/temples/bhairav.html"),
                ],
            },
            {
                "name": "Tushkaraja Bhairava · तुष्करराज भैरव (हब्बा कदल / दूध गंगा)",
                "icon": "",
                "timing": "Year-round; Herath night",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian of Habba Kadal and Doodh Ganga confluence.\n"
                    "Location: Habba Kadal area, Srinagar · 34.0900°N 74.8100°E\n"
                    "Google Maps: https://www.google.com/maps/search/Habba+Kadal+Bhairava+temple+Srinagar\n\n"
                    "Also called Turushkaraja Bhairava. Guards the East direction — "
                    "one of the 8 Ashta Bhairavas. Patron of Habba Kadal mohalla KP families, "
                    "one of the most densely KP-populated areas of old Srinagar. "
                    "The Doodh Ganga (Milk Ganga) stream flows nearby — sacred to KPs.\n\n"
                    "Mantra: 'Om Hreem Tushkarajaya Bhairavaya Namah'\n"
                    "Reference: Nilamata Purana, iKashmir Bhairava documentation"
                ),
                "links": [
                    ("iKashmir · Bhairavas", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Habba Kadal", "https://www.google.com/maps/search/Habba+Kadal+bridge+Srinagar"),
                ],
            },
            {
                "name": "Mangalaraja Bhairava · मंगलराज भैरव (फ़तेह कदल / ज़ैन कदल / बोहरी कदल)",
                "icon": "",
                "timing": "Year-round; Herath night",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian of the old-city kadal (bridge) belt.\n"
                    "Location: Fateh Kadal / Zaina Kadal / Bohri Kadal area, Srinagar\n"
                    "Google Maps: https://www.google.com/maps/search/Fateh+Kadal+Srinagar+temple\n\n"
                    "Also Mangaleshwara Bhairava. Guards the South-West direction. "
                    "Patron of the Fateh Kadal, Zaina Kadal and Bohri Kadal KP families — "
                    "historically among the most prestigious KP mohallas of Srinagar. "
                    "Rupa Bhawani's shrine is at Fateh Kadal — Mangalaraja Bhairava "
                    "is the protector deity of the same area.\n\n"
                    "Mantra: 'Om Hreem Mangalarajaya Bhairavaya Namah'"
                ),
                "links": [
                    ("iKashmir · Bhairava temples", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Zaina Kadal Srinagar", "https://www.google.com/maps/search/Zaina+Kadal+Srinagar+Kashmir"),
                ],
            },
            {
                "name": "Nandikeshwara Bhairava · नन्दिकेश्वर भैरव, सुम्बल (बांदीपोर)",
                "icon": "",
                "timing": "Year-round; Shivratri and Herath",
                "desc": (
                    "BHAIRAVA / SHIVA TEMPLE · Guardian Bhairava of Bandipora and Sumbal area.\n"
                    "Location: Sumbal, Bandipora district · 34.1500°N 74.6500°E\n"
                    "Google Maps: https://www.google.com/maps/search/Nandikeshwar+temple+Sumbal+Bandipora\n\n"
                    "Nandikeshwara = Nandi (Shiva's bull) + Ishwara (Lord) — Shiva as the Lord of Nandi. "
                    "Also known as Nandkishor / Nandkeshwar Bhairava. "
                    "Principal guardian deity (Kshetrapala) of Bandipora and Sumbal KP families. "
                    "The temple is at a scenic location near the Wular Lake shore.\n\n"
                    "Mantra: 'Om Nandikeshwaraya Namah' | 'Om Nandikeshwaraya Bhairavaya Namah'\n"
                    "Reference: iKashmir local Bhairava documentation"
                ),
                "links": [
                    ("iKashmir · Bhairava temples", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Sumbal Bandipora", "https://www.google.com/maps/search/Sumbal+Bandipora+Kashmir"),
                ],
            },
            {
                "name": "Bhuteshwara Bhairava · भूतेश्वर भैरव, तुलमुल (गंदेरबल)",
                "icon": "",
                "timing": "Year-round; especially at Zyeth Ashtami mela",
                "desc": (
                    "BHAIRAVA TEMPLE · Guardian Bhairava of Tulmul and Kheer Bhawani area.\n"
                    "Location: Tullamulla, Ganderbal district · near Kheer Bhawani temple\n"
                    "Google Maps: https://www.google.com/maps/search/Bhuteshwara+Bhairava+Tulmul+Ganderbal\n\n"
                    "Bhuteshwara = Lord of Spirits (Bhuta = spirit/element + Ishwara = Lord). "
                    "Guards the Tulmul-Kheer Bhawani sacred complex. "
                    "Worshipped alongside Ragnya Devi (Kheer Bhawani) on Zyeth Ashtami. "
                    "His puja is performed before entering the Kheer Bhawani sanctum "
                    "in traditional KP practice.\n\n"
                    "Mantra: 'Om Bhuteshwaraya Namah' | 'Om Bhuteshwaraya Bhairavaya Namah'"
                ),
                "links": [
                    ("iKashmir · Bhairava documentation", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("Google Maps · Tulmul Ganderbal", "https://www.google.com/maps/search/Tullamulla+Ganderbal+Kashmir"),
                ],
            },
            {
                "name": "Batuka Bhairava · बटुक भैरव (सर्वत्र — सभी KP घरों में)",
                "icon": "",
                "timing": "Herath (principal); all Bhairava pujas; daily worship in many KP homes",
                "desc": (
                    "BHAIRAVA DEITY · Universal child-form of Bhairava — worshipped in every KP home.\n"
                    "Not a fixed temple — present in every KP household shrine and all Herath rituals.\n"
                    "Google Maps: N/A — universal household deity\n\n"
                    "Batuka = child/boy. Batuka Bhairava is the most approachable, most beloved "
                    "form of Bhairava — a child-god who protects like a fierce guardian but is "
                    "worshipped with the tenderness given to a child. "
                    "Central to the Herath (Kashmiri Shivratri) ritual: "
                    "a small clay pot (separate from the 12 Vatak pots) is installed as Batuka Bhairava "
                    "and receives first puja. The all-night Herath vigil is dedicated to Batuka.\n\n"
                    "Puja: Small clay pot + sacred water + walnut twig + tilak of sindoor\n"
                    "Mantra: 'Om Hreem Batukaya Apadudharanaya Kuru Kuru Batukaya Hreem'\n"
                    "Reference: Svacchanda Tantra (Batuka Bhairava section), Herath ritual manuals"
                ),
                "links": [
                    ("Wikipedia · Bhairava", "https://en.wikipedia.org/wiki/Bhairava"),
                    ("Wisdomlib · Batuka", "https://www.wisdomlib.org/definition/batuka"),
                ],
            },
            # ── PANDAVA SITES ─────────────────────────────────────
            {
                "name": "Pandava Temples — Pahalgam area · पाण्डव मन्दिर (पहलगाम / लिद्दर घाटी)",
                "icon": "",
                "timing": "Year-round; Amarnath Yatra season",
                "desc": (
                    "PANDAVA PILGRIMAGE SITES · Multiple sites associated with the Pandavas in Pahalgam area.\n"
                    "Location: Pahalgam, Anantnag district · 34.0158°N 75.3128°E\n"
                    "Google Maps: https://www.google.com/maps/search/Pandava+temple+Pahalgam+Kashmir\n\n"
                    "According to local tradition and the Mahabharata's Tirthayatra Parva, "
                    "the Pandavas passed through Kashmir during their pilgrimage. "
                    "Sites associated with Pandavas in the Lidder Valley (Pahalgam area):\n"
                    "· Mamleshwar temple at Pahalgam — Shiva temple said to have been "
                    "established by Bhima\n"
                    "· Sheshnag Lake (3,590m) — on Amarnath route; sacred serpent lake "
                    "believed to be the abode of Sheshnaga seen by Pandavas\n"
                    "· Panchtarni ('five rivers') — where the Pandavas are said to have camped\n"
                    "· Tulian Lake — associated with Yudhishthira's meditation\n\n"
                    "Reference: Mahabharata Tirthayatra Parva, local Rajatarangini annotations"
                ),
                "links": [
                    ("Wikipedia · Pahalgam", "https://en.wikipedia.org/wiki/Pahalgam"),
                    ("Google Maps · Pahalgam temples", "https://www.google.com/maps/search/ancient+temples+Pahalgam+Kashmir"),
                    ("Wikipedia · Sheshnag Lake", "https://en.wikipedia.org/wiki/Sheshnag_Lake"),
                ],
            },
            {
                "name": "Pandava Temples — Kishtwar · पाण्डव मन्दिर, किश्तवाड़",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "PANDAVA PILGRIMAGE SITES · Kishtwar district sites associated with Pandavas.\n"
                    "Location: Kishtwar district · 33.3130°N 75.7660°E\n"
                    "Google Maps: https://www.google.com/maps/search/Pandava+temple+Kishtwar+Jammu+Kashmir\n\n"
                    "Kishtwar (ancient Kashyapapur) has multiple sites associated with Pandava passage: "
                    "· Sarthal Devi temple — goddess temple of great antiquity; "
                    "associated with local Pandava legends\n"
                    "· Natural rock formations identified locally as 'Pandava footprints'\n"
                    "· Machail Mata temple — Chandi Mata temple in remote mountains; "
                    "annual Yatra in August draws thousands\n"
                    "KP families from Kishtwar have strong Pandava-site veneration traditions.\n\n"
                    "Reference: Local oral histories, J&K Archaeological Survey records"
                ),
                "links": [
                    ("Wikipedia · Kishtwar", "https://en.wikipedia.org/wiki/Kishtwar"),
                    ("Google Maps · Kishtwar temples", "https://www.google.com/maps/search/ancient+temple+Kishtwar+Kashmir"),
                    ("Wikipedia · Machail Mata", "https://en.wikipedia.org/wiki/Chandi_Mata_Temple,_Machail"),
                ],
            },
            # ── SAINT SHRINES ─────────────────────────────────────
            {
                "name": "Bhagwan Gopinath Shrine · भगवान गोपीनाथ समाधि, रैनावारी (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Gopinath Jayanti (annual)",
                "desc": (
                    "SAINT SHRINE · Shrine of the most beloved modern KP saint (1898–1968).\n"
                    "Location: Rainawari, Srinagar · 34.1002°N 74.8141°E\n"
                    "Google Maps: https://www.google.com/maps/search/Bhagwan+Gopinath+Shrine+Rainawari+Srinagar\n\n"
                    "Bhagwan Gopinath Ji — modern Kashmiri Shaiva saint who embodied Pratyabhijña "
                    "(recognition of Shiva in oneself). His samadhi (resting place) at Rainawari "
                    "is an active pilgrimage site visited by KPs from across the diaspora. "
                    "Devotees experience peace and blessings at the shrine. "
                    "Annual Gopinath Jayanti observed by KP community worldwide. "
                    "His teachings: silent transmission of Shiva-consciousness through darshan.\n\n"
                    "Reference: 'Bhagwan Gopinath: The Divine Flame' (KP community publications)\n"
                    "Website: gopinathji.com"
                ),
                "links": [
                    ("Wikipedia · Bhagwan Gopinath", "https://en.wikipedia.org/wiki/Bhagwan_Gopinath"),
                    ("Google Maps · Rainawari Srinagar", "https://www.google.com/maps/search/Bhagwan+Gopinath+mandir+Rainawari+Srinagar"),
                ],
            },
            {
                "name": "Rupa Bhawani Shrine · रूपा भवानी मन्दिर, फ़तेह कदल (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Rupa Bhawani Jayanti (annual)",
                "desc": (
                    "SAINT SHRINE · Shrine of Devi Rupa Bhawani (1625–1721 CE).\n"
                    "Location: Fateh Kadal, Srinagar · 34.0830°N 74.8040°E\n"
                    "Google Maps: https://www.google.com/maps/search/Rupa+Bhawani+temple+Fateh+Kadal+Srinagar\n\n"
                    "Rupa Bhawani — Kashmiri Shakti saint and mystic poetess. "
                    "Her shrine at Fateh Kadal is one of the most revered KP sites in Srinagar. "
                    "Devotees come for blessings, especially women seeking guidance and spiritual protection. "
                    "Her Vakhs are recited at the shrine. "
                    "A second shrine is at Rainawari, Srinagar. "
                    "Rupa Bhawani Jayanti draws large gatherings of KP devotees.\n\n"
                    "Mantra: 'Om Rupa Bhawanyai Namah'"
                ),
                "links": [
                    ("Wikipedia · Rupa Bhawani", "https://en.wikipedia.org/wiki/Rupa_Bhawani"),
                    ("Google Maps · Fateh Kadal Srinagar", "https://www.google.com/maps/search/Fateh+Kadal+Srinagar+temple"),
                ],
            },
            {
                "name": "Swami Lakshmanjoo Ashram · स्वामी लक्ष्मण जू आश्रम, इशबर (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Guru Purnima most significant",
                "desc": (
                    "SAINT ASHRAM · Ashram of the last great master of Kashmir Shaivism (1907–1991).\n"
                    "Location: Ishber, Nishat, Srinagar · 34.1240°N 74.8810°E\n"
                    "Google Maps: https://www.google.com/maps/search/Swami+Lakshmanjoo+Ashram+Ishber+Srinagar\n\n"
                    "Swami Lakshmanjoo spent his entire life in Srinagar — never leaving Kashmir. "
                    "His ashram at Ishber (near Nishat, Dal Lake shore) is still active. "
                    "The Universal Shaiva Fellowship maintains the ashram and Swamiji's memory. "
                    "200+ hours of his recorded lectures are available online. "
                    "Serious students of Kashmir Shaivism make pilgrimage to this ashram. "
                    "His library and manuscripts are preserved here.\n\n"
                    "Website: lakshmanjoo.com | universalshaivafelllowship.org"
                ),
                "links": [
                    ("Wikipedia · Swami Lakshmanjoo", "https://en.wikipedia.org/wiki/Swami_Lakshmanjoo"),
                    ("Universal Shaiva Fellowship", "https://www.universalshaivafelllowship.org/"),
                    ("Google Maps · Nishat Srinagar", "https://www.google.com/maps/search/Ishber+Nishat+Srinagar+Kashmir"),
                ],
            },
            # ── OTHER MAJOR ANCIENT TEMPLES ──────────────────────
            {
                "name": "Ganesh Temple — Ganpatyar · गणपत्यार (श्रीनगर)",
                "icon": "",
                "timing": "Year-round; Ganesh Chaturthi and all new beginnings",
                "desc": (
                    "GANESHA TEMPLE · Principal Ganesha temple of Srinagar.\n"
                    "Location: Ganpatyar (Ganpatiyar), Srinagar · 34.0824°N 74.7993°E\n"
                    "Google Maps: https://www.google.com/maps/search/Ganpatyar+temple+Srinagar\n\n"
                    "The mohalla of Ganpatyar is named after this Ganesha temple — "
                    "one of the principal KP residential areas of old Srinagar. "
                    "KPs visit here before all auspicious events: marriages, new businesses, "
                    "Navreh, examinations. 'Om Gam Ganapataye Namah' is the primary mantra. "
                    "Ganesha is invoked first in every KP puja.\n\n"
                    "Mantra: 'Om Gam Ganapataye Namah' | 'Vakratunda Mahakaya Suryakoti Samaprabha...'"
                ),
                "links": [
                    ("Google Maps · Ganpatyar Srinagar", "https://www.google.com/maps/search/Ganpatyar+Srinagar+Kashmir"),
                    ("Wikipedia · Ganesha", "https://en.wikipedia.org/wiki/Ganesha"),
                ],
            },
            {
                "name": "Vitasta (Jhelum) Ghats — Srinagar · वितस्ता घाट",
                "icon": "",
                "timing": "Herath, Shraddha, Navreh, Nag Panchami",
                "desc": (
                    "RIVER GHATS · Sacred ghats of the Vitasta (Jhelum) in Srinagar.\n"
                    "Location: Multiple ghats along Jhelum in Srinagar · 34.0836°N 74.7973°E\n"
                    "Google Maps: https://www.google.com/maps/search/Jhelum+river+ghats+Srinagar\n\n"
                    "The Vitasta (Jhelum) is the sacred river-goddess of Kashmir. "
                    "KPs perform all major river rituals at the Jhelum ghats: "
                    "· Shraddha tarpan (water offerings to ancestors)\n"
                    "· Herath: Vatak pots are immersed at the ghat after puja\n"
                    "· Nag Panchami: milk offerings at the river\n"
                    "· Navreh morning: ritual bath in the Vitasta\n"
                    "· Vivaha: groom's procession traditionally included a visit to the ghat\n\n"
                    "Main ghats: Zaina Kadal ghat, Habba Kadal ghat, Fateh Kadal ghat, "
                    "Rainawari ghat (near Gopinath shrine)."
                ),
                "links": [
                    ("Wikipedia · Jhelum river", "https://en.wikipedia.org/wiki/Jhelum_River"),
                    ("Google Maps · Jhelum Srinagar ghats", "https://www.google.com/maps/search/Jhelum+river+Srinagar+ghat"),
                ],
            },
            {
                "name": "Parihas Pora (Awantivarman palace ruins) · परिहासपोर (बारामुला)",
                "icon": "",
                "timing": "Year-round; historical pilgrimage",
                "desc": (
                    "ANCIENT SITE · 9th century royal city ruins with temples.\n"
                    "Location: Parihaspora, Baramulla district · 34.0934°N 74.5891°E\n"
                    "Google Maps: https://www.google.com/maps/search/Parihaspora+temple+ruins+Baramulla\n\n"
                    "Parihaspora = City of Jest/Play — built by King Lalitaditya Muktapida (8th century CE). "
                    "Once had massive temples including Muktakeshava (Vishnu) and Parihaskesvara (Shiva). "
                    "Now ruins — but among the most important archaeological sites in Kashmir. "
                    "The scale of construction rivals Martand. ASI protected.\n\n"
                    "Reference: Rajatarangini (Books 4–5), ASI Kashmir Survey"
                ),
                "links": [
                    ("Wikipedia · Parihaspora", "https://en.wikipedia.org/wiki/Parihaspora"),
                    ("Google Maps · Parihaspora", "https://www.google.com/maps/search/Parihaspora+Kashmir"),
                ],
            },
            {
                "name": "Buniyar Temples · बुनियार मन्दिर (बारामुला)",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "ANCIENT TEMPLES · Medieval temple complex, north Kashmir.\n"
                    "Location: Buniyar, Baramulla district · 34.3100°N 73.9400°E\n"
                    "Google Maps: https://www.google.com/maps/search/Buniyar+temple+Baramulla+Kashmir\n\n"
                    "Buniyar has ruins of ancient temples from the early medieval period. "
                    "The area was an important pilgrimage route to the Lolab Valley. "
                    "Stone temple remains show the characteristic Kashmiri trefoil arch style. "
                    "KP families from Baramulla and Sopore include this in regional pilgrimage.\n\n"
                    "Reference: J&K Archaeological Survey, ASI reports"
                ),
                "links": [
                    ("Google Maps · Buniyar Baramulla", "https://www.google.com/maps/search/Buniyar+village+Baramulla+Kashmir"),
                ],
            },
            {
                "name": "Tulmul — Naga tirtha & Ragnya Devi complex · तुलमुल नाग तीर्थ",
                "icon": "",
                "timing": "Nag Panchami; Zyeth Ashtami",
                "desc": (
                    "NAG TIRTHA · The Naga spring complex at Tulmul — separate from but adjacent to the Kheer Bhawani temple.\n"
                    "Location: Tullamulla, Ganderbal · 34.2285°N 74.8090°E\n"
                    "Google Maps: https://www.google.com/maps/search/Tullamulla+Naga+spring+Ganderbal\n\n"
                    "The Tulmul area has multiple sacred springs — the Kheer Bhawani is the most "
                    "famous but the surrounding springs are also Naga tirthas. "
                    "The Naga of Tulmul is Takshaka (one of the principal Nagas of the Nilamata Purana). "
                    "Nag Panchami: milk offered at all springs in the complex. "
                    "The combination of Ragnya Devi (Shakti) and Naga (Shiva's serpent) makes "
                    "this one of the most complete sacred sites in Kashmir.\n\n"
                    "Reference: Nilamata Purana (Naga tirthas section)"
                ),
                "links": [
                    ("Google Maps · Tullamulla", "https://www.google.com/maps/search/Tullamulla+Ganderbal+Kashmir+temple"),
                    ("iKashmir · Tulmul", "https://www.ikashmir.net/tulamula/"),
                ],
            },
            {
                "name": "All Major Kashmiri Pandit Temples — iKashmir Directory",
                "icon": "",
                "timing": "Reference for all KP temples across the valley",
                "desc": (
                    "COMPLETE TEMPLE REFERENCE · The iKashmir temple directory lists all major KP temples:\n\n"
                    "Srinagar area temples:\n"
                    "· Zaina Devi temple · Sharika (Hari Parbat) · Ganpatyar · Bhairon temple "
                    "(old city) · Pandrethaan temple (Pandrethan) — ancient temple near Srinagar "
                    "where Lal Ded was born\n\n"
                    "Anantnag / South Kashmir:\n"
                    "· Martand · Bijbehara Vijeshvara · Bhadrakali · Kokernag temples "
                    "· Achabal · Verinag · Mattan · Daksum Shiva temple\n\n"
                    "Pulwama / Awantipora:\n"
                    "· Jwala Devi (Khrew) · Awantiswara · Awantishwamin · "
                    "Pampore area Naga springs\n\n"
                    "Baramulla / North Kashmir:\n"
                    "· Buniyar · Parihaspora · Sopore area temples\n\n"
                    "Ganderbal:\n"
                    "· Kheer Bhawani (Tulmul) · Nagbal · Kangan area Shiva temples\n\n"
                    "Kupwara / Remote:\n"
                    "· Sharada Peeth vicinity (PoK) · Lolab Valley temples · Gurez temples\n\n"
                    "Google Maps: Search 'ancient Hindu temples Kashmir' for comprehensive map view."
                ),
                "links": [
                    ("iKashmir · Complete temple list", "https://www.ikashmir.net/temples/index.html"),
                    ("iKashmir · All Bhairavas", "https://www.ikashmir.net/temples/bhairav.html"),
                    ("iKashmir · Peethas", "https://www.ikashmir.net/temples/peetham.html"),
                    ("Google Maps · All Kashmir temples", "https://www.google.com/maps/search/ancient+temples+Kashmir+Valley"),
                    ("Wikipedia · Temples of Jammu and Kashmir", "https://en.wikipedia.org/wiki/Category:Hindu_temples_in_Jammu_and_Kashmir"),
                    ("ASI Kashmir Circle", "https://asi.nic.in/"),
                ],
            },
        ],
        "Music & Performing Arts · संगीत": [
            {
                "name": "Sufiana Kalam · सूफियाना कलाम",
                "icon": "",
                "timing": "Classical — mehfils, weddings, spiritual gatherings",
                "desc": (
                    "The classical Sufi music of Kashmir — one of the most refined musical traditions "
                    "in the Indian subcontinent. Evolved over 500+ years blending Persian, Central Asian "
                    "and Kashmiri melodic traditions.\n\n"
                    "Instruments: Santoor (100-string hammered dulcimer), Saz-i-Kashmir (long-necked lute), "
                    "Wasul (dilruba-type bowed instrument), Tumbaknari (clay pot drum), "
                    "Harmonium, Tabla.\n\n"
                    "Language & texts: Persian ghazals, Kashmiri mystic poetry (vakhs), "
                    "Sanskrit shlokas. Most performed ragas: Yaman, Bhairav, Bhairavi, Desh, Todi.\n\n"
                    "Famous compositions & songs:\n"
                    "· 'Mast Qalandar' — devotional to Lal Shahbaz Qalandar; widely performed in Kashmir\n"
                    "· 'Allah Hoo' — deep meditation chant in Sufi gatherings\n"
                    "· 'Shamas-i-Tabrizi' — Rumi's poem set in Sufiana style\n"
                    "· 'Gulzar Hain Hum' — classical Persian ghazal\n"
                    "· Kafi compositions of Shah Qattal and Shamas Faqir\n\n"
                    "Notable artists: Ustad Ghulam Mohammad Zaz, Ustad Ghulam Nabi Shiekh, "
                    "Ustad Mohammad Yaqoob Sheikh, Ustad Nasir Fatehpuri.\n\n"
                    "Status: Recognised by Sangeet Natak Akademi, India. "
                    "Documented by Sahitya Akademi as intangible heritage."
                ),
                "links": [
                    ("Wikipedia · Sufiana Kalam", "https://en.wikipedia.org/wiki/Sufiana_Kalam"),
                    ("YouTube · Sufiana Kalam collection", "https://www.youtube.com/results?search_query=sufiana+kalam+kashmir+classical"),
                    ("YouTube · Ustad Ghulam Mohammad Zaz", "https://www.youtube.com/results?search_query=ghulam+mohammad+zaz+sufiana+kalam"),
                ],
            },
            {
                "name": "Vakhs of Lal Ded · लल देद वाख",
                "icon": "",
                "timing": "Devotional — recited at Herath, Navreh, spiritual gatherings, daily puja",
                "desc": (
                    "The mystical verses (Vakhs) of Lalleshwari are the heart of Kashmiri spiritual music. "
                    "Sung, chanted and meditated upon for 700 years.\n\n"
                    "Form: Unrhymed quatrains in Old Kashmiri. Sung in a slow, meditative style. "
                    "No fixed raga — the melody varies by region and family tradition.\n\n"
                    "Most celebrated Vakhs with Kashmiri text:\n\n"
                    "1. 'Shiv chuy thali thali rozaan\n"
                    "   Moz nay Hindav na Musalmaan\n"
                    "   Trukh pan panun parzanaan\n"
                    "   Sayi chu Shaiv agam nishan'\n"
                    "   — Shiva pervades everywhere; do not distinguish Hindu from Muslim.\n\n"
                    "2. 'Lale ous yeli gurus vachas razi\n"
                    "   Teli mye panun panas disum nazar\n"
                    "   Teli mye zanaan gay bahi nay bazi\n"
                    "   Teli mye poz panun korum shumaar'\n"
                    "   — When I, Lalla, became attentive to the Guru's word, "
                    "I saw my own Self; then I recognised what is real and unreal.\n\n"
                    "3. 'Pranas apanas milawath karim\n"
                    "   Shiv Shakti akh chu beyi nay beyi\n"
                    "   Parzanawith panas karim nisharam\n"
                    "   Panas panas mye aayi suyii'\n"
                    "   — When prana and apana unite, Shiva and Shakti are one; "
                    "recognising the Self, I became still — that alone came to me.\n\n"
                    "4. 'Wopadum wuchum naav taru tari\n"
                    "   Bramh wuchum bramh wuchinam Hari\n"
                    "   Aakis aakis panas aaki\n"
                    "   Kus mye darshyov kus me dith nari'\n"
                    "   — I crossed the water; I found the raft. I saw Brahma; I saw Hari. "
                    "One and one and one — who showed me, and who showed the fire?\n\n"
                    "5. 'Yus panas nish panas maaniy\n"
                    "   Suy chu Shivas peth baaraniy'\n"
                    "   — One who recognises the Self within the Self — "
                    "that one alone is the door to Shiva.\n\n"
                    "Sung by: Pandit Bhajan Sopori (santoor + vakh), "
                    "Kailash Mehra, Vijay Dhar, numerous KP community musicians."
                ),
                "links": [
                    ("Wikipedia · Lalleshwari", "https://en.wikipedia.org/wiki/Lalleshwari"),
                    ("YouTube · Lal Ded Vakhs sung", "https://www.youtube.com/results?search_query=lal+ded+vakhs+sung+kashmiri"),
                    ("YouTube · Lalleshwari Vakhs recitation", "https://www.youtube.com/results?search_query=lalleshwari+vakhs+kashmiri+pandit"),
                    ("Archive.org · Lal Ded texts", "https://archive.org/search?query=lal+ded+vakhs"),
                ],
            },
            {
                "name": "Bhajans & Shiva Stotras · भजन और शिव स्तोत्र",
                "icon": "",
                "timing": "Daily puja, Herath night, Navreh, Ashtami — all devotional occasions",
                "desc": (
                    "Kashmiri Pandit devotional singing tradition — combining Sanskrit stotras "
                    "with Kashmiri bhajans sung at home and temple.\n\n"
                    "── SHIVA STOTRAS (Sanskrit) ──\n\n"
                    "1. Shiva Panchakshara Stotra (by Adi Shankaracharya)\n"
                    "   Full text:\n"
                    "   'Nagendra-hārāya trilochanāya\n"
                    "   Bhasmānga-rāgāya maheshvarāya\n"
                    "   Nityāya shuddhaaya digambharāya\n"
                    "   Tasmai na-kārāya namaḥ Śivāya'\n"
                    "   (Om Namah Shivaya — each of 5 verses meditates on one syllable Na Ma Shi Va Ya)\n"
                    "   Sung at: start and end of all Shiva pujas, Herath night vigil.\n\n"
                    "2. Mrityunjaya Mantra (Rigveda 7.59.12)\n"
                    "   'Om Tryambakam yajamahe\n"
                    "   Sugandhim pushtivardhanam\n"
                    "   Urvaarukamiva bandhanan\n"
                    "   Mrityor mukshiya maamritat'\n"
                    "   — We worship the three-eyed one (Shiva) who nourishes all; "
                    "may he liberate us from death as a ripe cucumber from the vine.\n"
                    "   KP practice: 108 repetitions on Herath; 11 times daily in Nityakarma.\n\n"
                    "3. Shiva Tandava Stotra (by Ravana)\n"
                    "   Opening verse:\n"
                    "   'Jatatavigalajjala-pravahapavitasthale\n"
                    "   Gale avalambya lambitaam bhujangatungamalikaam\n"
                    "   Damad-damad-damaddama-ninnadavadamarvayam\n"
                    "   Chakara chandtandavam tanotu nah shivah shivam'\n"
                    "   — Sung/chanted on Herath; powerful rhythmic recitation.\n\n"
                    "4. Sharada Stotram (KP-specific — invocation of Mata Sharada)\n"
                    "   'Ya Sharada nilotpala-dala-shyama\n"
                    "   Ya vai susukshma-paramanu-ruupaa\n"
                    "   Ya vai para brahma-svaruupa-nityaa\n"
                    "   Namas tasmai brahmane brahma-vidyaayai'\n"
                    "   — She who is dark as the blue lotus petal; recited at Navreh and Saraswati Puja.\n\n"
                    "── KASHMIRI BHAJANS ──\n\n"
                    "5. 'Shivji Bole Nandi Se' — popular Hindi Shiva bhajan sung in KP homes on Herath\n\n"
                    "6. 'Hey Shambhu Baba Mere Bhole Nath' — widely sung at Herath night vigil\n\n"
                    "7. 'Bum Bum Bhole' — festive Shiva song for Herath processions\n\n"
                    "8. 'Kashmiri Mata Sharika Bhawani' — KP-composed devotional to Sharika Devi; "
                    "sung on Vaishakha Ashtami\n\n"
                    "9. 'Jai Kheer Bhawani Mata' — devotional sung at Zyeth Ashtami mela at Tulmul\n\n"
                    "10. 'Ragnya Devi Bhawani' — Kheer Bhawani aarti in Kashmiri; "
                    "sung by KP families before Zyeth Ashtami pilgrimage\n\n"
                    "11. 'Herathas Tsalar Shivji' — Kashmiri song specifically for Herath evening; "
                    "describes the Vatak pots and the night of Shiva\n\n"
                    "12. 'Batuk Bhairav Stotra' — recited at Vatak Puja during Herath:\n"
                    "    'Om Hreem Batukaya Apadudharanaya Kuru Kuru Batukaya Hreem'\n\n"
                    "Notable KP bhajan singers: Pandit Bhajan Sopori, Vijay Dhar, "
                    "Sharda Koul, Kailash Mehra, Pushkar Bhan."
                ),
                "links": [
                    ("YouTube · Shiva Panchakshara Stotra", "https://www.youtube.com/results?search_query=shiva+panchakshara+stotra+kashmiri"),
                    ("YouTube · Mrityunjaya Mantra 108 times", "https://www.youtube.com/results?search_query=mrityunjaya+mantra+108+times"),
                    ("YouTube · Kashmiri Herath Bhajans", "https://www.youtube.com/results?search_query=kashmiri+herath+bhajan+shiva"),
                    ("YouTube · Sharika Devi Bhajan", "https://www.youtube.com/results?search_query=sharika+devi+bhajan+kashmiri"),
                    ("YouTube · Kheer Bhawani Aarti", "https://www.youtube.com/results?search_query=kheer+bhawani+aarti+kashmiri+pandit"),
                    ("Shiva Tandava text", "https://www.wisdomlib.org/definition/shiva-tandava-stotra"),
                ],
            },
            {
                "name": "Chakri · चकरी — Kashmiri Folk Music",
                "icon": "",
                "timing": "Weddings, Navreh, festivals, community gatherings",
                "desc": (
                    "Chakri is the most vibrant and popular Kashmiri folk music genre — "
                    "upbeat, joyful, celebratory. The word 'Chakri' comes from 'chakkar' (spin/circle) "
                    "— the music makes you want to move.\n\n"
                    "Instruments: Rubab (lute — Kashmir's national instrument), "
                    "Tumbaknari (clay barrel drum), Noot (metal pot struck with rings), "
                    "Tche-tche (small cymbals), Harmonium, Sarangi.\n\n"
                    "Famous Chakri songs:\n"
                    "· 'Ded Chum Bramaan' (I am wandering) — classic Chakri about spiritual seeking\n"
                    "· 'Roshan Dalaa Chum Nazaaran' — about Dal Lake beauty; performed at Navreh\n"
                    "· 'Volo Volo Kalaamas' — wedding Chakri for the groom's procession\n"
                    "· 'Pumbe Sur' — spring Chakri about blooming flowers\n"
                    "· 'Boul Boul Gindun' — light celebratory Chakri about nature\n"
                    "· 'Mye Naav Chum Bramaan' — devotional Chakri\n"
                    "· 'Chah Naar Hasa' — festive Chakri sung at homecomings\n\n"
                    "Notable artists: Mohammed Shafi Shauq, Raj Begum (first woman Chakri singer), "
                    "Ghulam Ahmed Sufi, Shamim Dev Azad, Waheed Jeelani, "
                    "Naseem Akhter, Kailash Mehra (KP Chakri tradition).\n\n"
                    "KP Chakri: Kashmiri Pandits have their own Chakri repertoire — "
                    "songs about Herath, Navreh, Kul Devi, and the Valley sung at family gatherings."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Music", "https://en.wikipedia.org/wiki/Music_of_Jammu_and_Kashmir"),
                    ("YouTube · Kashmiri Chakri songs", "https://www.youtube.com/results?search_query=kashmiri+chakri+folk+songs"),
                    ("YouTube · Raj Begum Kashmiri songs", "https://www.youtube.com/results?search_query=raj+begum+kashmiri+folk+songs"),
                    ("YouTube · KP Chakri Navreh", "https://www.youtube.com/results?search_query=kashmiri+pandit+chakri+navreh+songs"),
                ],
            },
            {
                "name": "Wanwun · वान्वुन — KP Wedding Songs",
                "icon": "",
                "timing": "Kashmiri Pandit weddings — specific songs for each ritual stage",
                "desc": (
                    "Wanwun (from Sanskrit: Vandan = salutation/praise) are the traditional "
                    "women's ritual songs of Kashmiri Pandits — sung exclusively by women "
                    "at each stage of the wedding. One of the most endangered elements of KP culture.\n\n"
                    "Song categories by wedding stage:\n\n"
                    "1. DEVGUN WANWUN (invoking family deities):\n"
                    "   · 'Ganesha Puja Wanwun' — women invoke Ganesha before the wedding begins\n"
                    "   · 'Kul Devi Vandana' — invoking Sharika/Ragnya/Jwala Devi\n\n"
                    "2. LAGAN WANWUN (auspicious thread ceremony):\n"
                    "   · 'Lagan Khasaan' — song for the tying of the Lagan thread\n"
                    "   · 'Shubh Lagan Aayo' — welcoming the auspicious moment\n\n"
                    "3. MEHNDI WANWUN (henna night):\n"
                    "   · 'Mehndi Rachao' — in Kashmiri; sung while applying henna to the bride\n"
                    "   · 'Batuk Puja Wanwun' — invoking Bhairava/Batuk for protection\n\n"
                    "4. BARAT WANWUN (groom's procession arrival):\n"
                    "   · 'Volo Volo Dulho' — 'Come, come, O groom' — welcoming song\n"
                    "   · 'Aayo Dulha' — celebratory arrival song\n\n"
                    "5. PHERAN CEREMONY WANWUN:\n"
                    "   · 'Pheran Pahenan Dulhan Ko' — as the bride is dressed in the Pheran\n\n"
                    "6. SAPTAPADI WANWUN (seven steps around the fire):\n"
                    "   · 'Saat Phere' — singing the 7 vows in Kashmiri\n"
                    "   · 'Agni Devta' — invoking the sacred fire\n\n"
                    "7. VIDAI WANWUN (bride's departure — most emotional):\n"
                    "   · 'Wuchum Wuchum Ghar Myon' — 'I looked and looked at my home'\n"
                    "   · 'Maajan Maajan Rozum' — 'I will remain as a daughter'\n"
                    "   · 'Chu Ded Myon' — most moving farewell song\n\n"
                    "8. KHON BATTA WANWUN (bride's welcome at groom's home):\n"
                    "   · 'Aayi Nai Dulhan' — welcoming the bride into the new home\n\n"
                    "Status: Critically endangered — only older KP women (70+) know the complete "
                    "repertoire. Preservation efforts by KP cultural organisations worldwide."
                ),
                "links": [
                    ("Wikipedia · Wanwun", "https://en.wikipedia.org/wiki/Wanwun"),
                    ("YouTube · Kashmiri Pandit Wanwun wedding songs", "https://www.youtube.com/results?search_query=kashmiri+pandit+wanwun+wedding+songs"),
                    ("YouTube · KP wedding Wanwun traditional", "https://www.youtube.com/results?search_query=wanwun+kashmiri+pandit+traditional+wedding"),
                    ("iKashmir · Music", "https://www.ikashmir.net/music/"),
                ],
            },
            {
                "name": "Rouf · रौफ — Women's Dance",
                "icon": "",
                "timing": "Navreh (KP New Year), Eid, spring festivals, weddings",
                "desc": (
                    "Rouf is the most graceful traditional dance of Kashmir — performed exclusively "
                    "by women. A group dance of great elegance and cultural pride.\n\n"
                    "Form: Women stand in two rows facing each other (or in a semi-circle). "
                    "Steps are synchronised — a gentle forward-backward footwork pattern. "
                    "Arms move gracefully at waist level. Performers wear traditional Pheran.\n\n"
                    "Songs sung during Rouf:\n"
                    "· 'Phul Vari Gashe' — 'The garden is in full bloom' — spring Rouf song\n"
                    "· 'Roshan Dalaa' — about Dal Lake in spring\n"
                    "· 'Laali Laali Dodiyaas Laali' — celebratory spring song\n"
                    "· 'Volo Maelis Gulshan Manz' — 'Come to the garden of flowers'\n"
                    "· 'Chu Myon Yaar Sonuy' — 'My beloved is like gold'\n"
                    "· 'Navreh Mubarak' songs — KP-specific Rouf songs for New Year\n\n"
                    "KP context: Rouf is performed by KP women at Navreh celebrations — "
                    "it is one of the most visible signs of Kashmiri cultural identity at "
                    "KP gatherings worldwide (Jammu, Delhi, Mumbai, diaspora cities).\n\n"
                    "UNESCO: Listed as intangible cultural heritage of J&K. "
                    "Sahitya Akademi has documented Rouf as a living tradition."
                ),
                "links": [
                    ("Wikipedia · Rouf", "https://en.wikipedia.org/wiki/Rouf"),
                    ("YouTube · Rouf dance Kashmiri", "https://www.youtube.com/results?search_query=rouf+dance+kashmiri+women+traditional"),
                    ("YouTube · Rouf Navreh songs Kashmir", "https://www.youtube.com/results?search_query=rouf+navreh+kashmiri+pandit+dance"),
                ],
            },
            {
                "name": "Santoor · सन्तूर — Kashmir's Soul Instrument",
                "icon": "",
                "timing": "Classical concerts, Sufiana Kalam, devotional music",
                "desc": (
                    "The Santoor is Kashmir's most iconic instrument and India's most celebrated "
                    "hammered dulcimer. 100 strings stretched over a walnut-wood trapezoidal box, "
                    "struck with light curved mallets (mezrab/mesrab).\n\n"
                    "History: Brought to Kashmir from Persia (Santur) via the Silk Route ~500 years ago. "
                    "Kashmiri Santoor is larger and deeper than the Persian santur. "
                    "Traditional use: Sufiana Kalam ensembles.\n\n"
                    "Pandit Shivkumar Sharma (1938–2022): The greatest Santoor maestro. "
                    "He single-handedly elevated the Santoor from a folk/Sufi instrument "
                    "to a full Hindustani classical concert instrument. "
                    "His recordings are essential listening.\n\n"
                    "Essential recordings & YouTube:\n"
                    "· 'Raga Bhairavi' — Pt. Shivkumar Sharma (morning raga, deeply meditative)\n"
                    "· 'Raga Yaman' — Pt. Shivkumar Sharma (evening raga, quintessential Santoor)\n"
                    "· 'Raga Desh' — Pt. Shivkumar Sharma (monsoon raga)\n"
                    "· 'Raga Bairagi' — deeply devotional Shiva raga\n"
                    "· 'Shiv-Hari' film music collaborations with Hari Prasad Chaurasia\n"
                    "· 'Call of the Valley' (1967) — Shivkumar Sharma + Hariprasad Chaurasia + "
                    "Brij Bhushan Kabra — landmark album of Indian music\n\n"
                    "Second generation: Rahul Sharma (son of Pt. Shivkumar Sharma) continues the legacy."
                ),
                "links": [
                    ("Wikipedia · Santoor", "https://en.wikipedia.org/wiki/Santoor"),
                    ("Wikipedia · Shiv Kumar Sharma", "https://en.wikipedia.org/wiki/Shiv_Kumar_Sharma"),
                    ("YouTube · Pt. Shivkumar Sharma Raga Bhairavi", "https://www.youtube.com/results?search_query=shivkumar+sharma+santoor+raga+bhairavi"),
                    ("YouTube · Call of the Valley full album", "https://www.youtube.com/results?search_query=call+of+the+valley+shivkumar+sharma+hariprasad"),
                    ("YouTube · Santoor Raga Yaman", "https://www.youtube.com/results?search_query=shivkumar+sharma+santoor+raga+yaman"),
                    ("YouTube · Rahul Sharma Santoor", "https://www.youtube.com/results?search_query=rahul+sharma+santoor+kashmiri"),
                ],
            },
            {
                "name": "Kashmiri Bhajan & Kul Devi Aarti · कुल देवी आरती",
                "icon": "",
                "timing": "Ashtami puja, Navratri, Herath, Navreh, daily evening puja",
                "desc": (
                    "Kashmiri Pandit devotional songs specific to each Kul Devi and Shiva — "
                    "sung at home pujas, temples and community gatherings.\n\n"
                    "── SHARIKA DEVI BHAJANS (Hari Parbat, Srinagar) ──\n"
                    "· 'Sharika Mata Aarti': 'Jai Sharika Mata, Jai Chakreshwari / "
                    "Hari Parbat Nivaasi, Kashmeer Kalyan Kari' — main aarti\n"
                    "· 'Hey Sharike Bhawani' — devotional in Kashmiri to Sharika Devi\n"
                    "· 'Shresti Ki Mata' — Sanskrit stotra to Chakreshwari\n\n"
                    "── KHEER BHAWANI / RAGNYA DEVI BHAJANS (Tulmul) ──\n"
                    "· 'Jai Kheer Bhawani Mata Jai' — main aarti at Tulmul temple\n"
                    "· 'Ragnya Devi Bhawani' — Kashmiri devotional; sung by KP women at Zyeth Ashtami\n"
                    "· 'Tulmul Wali Mata' — popular KP bhajan for Kheer Bhawani\n"
                    "· 'Ksheer Bhawani Stotra' in Sanskrit — recited by purohit at spring\n\n"
                    "── JWALA DEVI BHAJANS (Khrew, Pulwama) ──\n"
                    "· 'Jai Jwala Devi Mata' — Navratri aarti\n"
                    "· 'Khrew Wali Jwala Mata' — regional bhajan for south Kashmir KPs\n\n"
                    "── HERATH BHAJANS (Shiva songs for the all-night vigil) ──\n"
                    "· 'Herathas Tsalar Shivji' — KP Kashmiri song for Herath night\n"
                    "· 'Shiv Vandana Herath' — Sanskrit-Kashmiri mix sung at Vatak Puja\n"
                    "· 'Om Namah Shivaya' — sung continuously through the Herath vigil\n"
                    "· 'Har Har Mahadev' call-and-response through the night\n\n"
                    "── NAVREH SONGS ──\n"
                    "· 'Navreh Mubarak Aayi' — celebratory Kashmiri song for New Year\n"
                    "· 'Sharada Vandana' — sung at the Navreh Thali puja to Mata Sharada\n"
                    "· 'Nava Varsha Aayo' — welcome song for the Kashmiri new year\n\n"
                    "── VITASTA / NAGA BHAJANS ──\n"
                    "· 'Vitasta Stotra' (from Nilamata Purana) — recited on Vitasta Jayanti\n"
                    "· 'Nag Panchami Bhajan' — sung at Naga puja on Shravana Panchami\n"
                    "· 'Vasuki Nagaraja Stotra' — Sanskrit; sung at Nag temples"
                ),
                "links": [
                    ("YouTube · Sharika Devi Aarti", "https://www.youtube.com/results?search_query=sharika+devi+aarti+kashmiri+pandit"),
                    ("YouTube · Kheer Bhawani Aarti", "https://www.youtube.com/results?search_query=kheer+bhawani+aarti+tulmul"),
                    ("YouTube · Kashmiri Pandit Herath bhajan", "https://www.youtube.com/results?search_query=kashmiri+pandit+herath+shiva+bhajan"),
                    ("YouTube · Navreh songs KP", "https://www.youtube.com/results?search_query=navreh+kashmiri+pandit+song"),
                    ("YouTube · Jwala Devi bhajan", "https://www.youtube.com/results?search_query=jwala+devi+khrew+aarti+kashmiri"),
                    ("YouTube · Vitasta Jayanti songs", "https://www.youtube.com/results?search_query=vitasta+jayanti+kashmiri+pandit"),
                ],
            },
            {
                "name": "Hafiz Nagma & Kashmiri Gazal · हाफ़िज़ नग्मा",
                "icon": "",
                "timing": "Literary gatherings, weddings, cultural evenings",
                "desc": (
                    "Kashmiri classical poetry set to music — the refined literary-musical tradition "
                    "of the valley.\n\n"
                    "Hafiz Nagma: named after Hafiz (the Persian poet) — Persian and Kashmiri "
                    "poems from classical masters set to classical ragas. "
                    "Slower and more meditative than Chakri.\n\n"
                    "Famous Kashmiri Gazal/Nagma songs:\n"
                    "· Habba Khatoon's Lol (lyric songs) — set to traditional Kashmiri melodies:\n"
                    "  'Rozis na biyus dilbar myon' — 'My beloved does not return' (most famous)\n"
                    "  'Aakh bael' — 'One moment' — love song\n\n"
                    "· Arnimal's Vakhs set to music:\n"
                    "  'Suy myon yaar suy myon dilbar' — devotional love\n\n"
                    "· Mahmood Gami's Kashmiri poetry — 19th century master of Kashmiri poetry:\n"
                    "  'Yimav Gayi Yimav Gayi' — elegy\n\n"
                    "· Maqbool Shah Kralawari — modern Kashmiri poet:\n"
                    "  'Sahibaa' — most performed modern Kashmiri song\n\n"
                    "Notable artists: Raj Begum (greatest Kashmiri female vocalist, "
                    "'Nightingale of Kashmir' in modern era), Shamim Dev Azad, "
                    "Gulzar Ganai, Rashid Hafiz."
                ),
                "links": [
                    ("Wikipedia · Kashmiri literature", "https://en.wikipedia.org/wiki/Kashmiri_literature"),
                    ("YouTube · Habba Khatoon songs", "https://www.youtube.com/results?search_query=habba+khatoon+kashmiri+songs"),
                    ("YouTube · Raj Begum Kashmiri songs", "https://www.youtube.com/results?search_query=raj+begum+kashmiri+classic+songs"),
                    ("YouTube · Kashmiri gazal poetry", "https://www.youtube.com/results?search_query=kashmiri+gazal+nagma+classical"),
                ],
            },
            {
                "name": "Bhand Pather · भाण्ड पाथेर — Folk Theatre",
                "icon": "",
                "timing": "Festivals, fairs, village gatherings — dying tradition",
                "desc": (
                    "Ancient Kashmiri folk theatre — satirical performances by the Bhand "
                    "(jester-actor) community. One of India's oldest living theatre traditions, "
                    "tracing roots to Sanskrit Natya Shastra.\n\n"
                    "Form: Combines music, dance, mime, spoken dialogue and sharp social satire. "
                    "Performances mock royalty, corrupt officials, greedy priests — "
                    "speaking truth to power through comedy.\n\n"
                    "Instruments used in Bhand Pather: Dhol, Nagara (kettle drum), "
                    "Surnai (oboe-like wind instrument), Thalij (cymbals).\n\n"
                    "Famous Bhand Pather pieces:\n"
                    "· 'Darzi Pather' — satire on the tailor's vanity\n"
                    "· 'Watal Pather' — about the washerman; classical piece\n"
                    "· 'Bahman Pather' — about a Brahmin; socially sharp\n"
                    "· 'Gosain Pather' — about a Hindu mendicant\n"
                    "· 'Dokur Pather' — satire on a doctor\n"
                    "· 'Shikargah' — about royal hunting; political allegory\n\n"
                    "Notable family: The Bhand Pather tradition is maintained by the "
                    "Bhand community of Akingam village, Anantnag. "
                    "Master practitioners: Mohammed Shafi Bhand, Gulzar Ahmed Bhand.\n\n"
                    "Status: UNESCO Intangible Cultural Heritage candidate. "
                    "Sangeet Natak Akademi awardees include Bhand Pather performers."
                ),
                "links": [
                    ("Wikipedia · Bhand Pather", "https://en.wikipedia.org/wiki/Bhand_Pather"),
                    ("YouTube · Bhand Pather Kashmir", "https://www.youtube.com/results?search_query=bhand+pather+kashmiri+folk+theatre"),
                    ("Sangeet Natak Akademi", "https://en.wikipedia.org/wiki/Sangeet_Natak_Akademi"),
                ],
            },
            {
                "name": "Lehar & Dumhal · लहर और दुमहल — Traditional Dances",
                "icon": "",
                "timing": "Festivals, Urs (Sufi celebrations), seasonal gatherings",
                "desc": (
                    "Two distinct Kashmiri ceremonial dances:\n\n"
                    "── DUMHAL ──\n"
                    "A ceremonial dance of the Wattal community (Lolab Valley, Kupwara). "
                    "Performed at Urs of saints and special occasions. "
                    "Men carry a tall decorated banner (Dumhal pole) and dance in a circle "
                    "to the beat of drums. "
                    "One of the most visually striking and ancient dance traditions of Kashmir. "
                    "Listed in UNESCO Intangible Cultural Heritage documentation.\n\n"
                    "── LEHAR ──\n"
                    "Men's group dance accompanied by dhol and nagara drums. "
                    "Performed at spring festivals, especially in the Gurez Valley (Bandipora). "
                    "Vigorous footwork and arm movements — a warrior-folk dance tradition.\n\n"
                    "── BAND-I-PATHER (puppet theatre) ──\n"
                    "Traditional string puppet shows (marionettes) with Kashmiri folk stories. "
                    "Now extremely rare — fewer than 5 practicing families in the valley.\n\n"
                    "Songs accompanying Dumhal:\n"
                    "· Drum-based compositions (no lyrics) — pure rhythmic recitation\n"
                    "· 'Allah Hoo' Sufi chant as the banner is raised\n\n"
                    "Reference: Documented by J&K Academy of Art Culture and Languages (JKAACL)."
                ),
                "links": [
                    ("Wikipedia · Dumhal", "https://en.wikipedia.org/wiki/Dumhal"),
                    ("YouTube · Dumhal dance Kashmir", "https://www.youtube.com/results?search_query=dumhal+dance+kashmir+traditional"),
                    ("JKAACL", "https://jkaacl.net/"),
                ],
            },
            {
                "name": "Kashmiri Classical Instruments · संगीत वाद्य",
                "icon": "",
                "timing": "All musical contexts",
                "desc": (
                    "Complete guide to traditional Kashmiri musical instruments:\n\n"
                    "── STRING INSTRUMENTS ──\n"
                    "· Santoor: 100-string hammered dulcimer — Kashmir's signature instrument. "
                    "Made from walnut wood. Maestro: Pt. Shivkumar Sharma.\n"
                    "· Rubab (Robab): Long-necked plucked lute — 'father of guitar'. "
                    "The national instrument of Afghanistan and Kashmir. "
                    "Primary instrument of Chakri. Made from mulberry wood.\n"
                    "· Saz-i-Kashmir: Long-necked lute similar to Sitar but deeper. "
                    "Used in Sufiana Kalam ensembles.\n"
                    "· Sarangi: Short-necked bowed instrument — used in classical and folk music.\n"
                    "· Tanpura: Drone instrument for classical vocal music.\n\n"
                    "── PERCUSSION ──\n"
                    "· Tumbaknari: Clay barrel-shaped drum — essential Chakri instrument. "
                    "Unique to Kashmir — played with fingers.\n"
                    "· Dhol: Large two-headed drum — festivals, processions.\n"
                    "· Nagara: Kettle drum pair — Bhand Pather, royal music.\n"
                    "· Noot: Metal cooking pot struck with rings on fingers — Chakri accompaniment.\n"
                    "· Tabla: Adopted from Hindustani classical tradition.\n\n"
                    "── WIND ──\n"
                    "· Surnai (Shehnai variant): Double-reed wind instrument — "
                    "played at festivals, processions, Bhand Pather.\n"
                    "· Bansuri (flute): Used in devotional music and folk songs.\n"
                    "· Nay (reed flute): Sufi music — associated with Rumi's 'Listen to the Nay'.\n\n"
                    "── RHYTHMIC ──\n"
                    "· Tche-tche: Small cymbals struck together — Chakri, Wanwun.\n"
                    "· Thalij: Large cymbals — Bhand Pather, Dumhal.\n"
                    "· Ghanta (temple bell): Used in all puja and aarti."
                ),
                "links": [
                    ("Wikipedia · Rubab instrument", "https://en.wikipedia.org/wiki/Rubab_(instrument)"),
                    ("Wikipedia · Santoor", "https://en.wikipedia.org/wiki/Santoor"),
                    ("YouTube · Tumbaknari Kashmiri drum", "https://www.youtube.com/results?search_query=tumbaknari+kashmiri+drum+folk"),
                    ("YouTube · Rubab Kashmir music", "https://www.youtube.com/results?search_query=rubab+kashmiri+music+traditional"),
                    ("YouTube · Kashmiri instruments demonstration", "https://www.youtube.com/results?search_query=kashmiri+traditional+instruments+music"),
                ],
            },
        ],
        "Cuisine · व्यंजन": [
            {
                "name": "KP Cuisine — Overview · कश्मीरी पण्डित रसोई",
                "icon": "",
                "timing": "Daily and festive",
                "desc": (
                    "Kashmiri Pandit cuisine is strictly sattvic — NO onion, NO garlic. "
                    "The defining spice base: asafoetida (heeng/hing), dry ginger (sounth), "
                    "fennel seeds (saunf/badiyan), Kashmiri red chilli (deghi mirch — colour without heat), "
                    "turmeric (haldi), whole cardamom (elaichi), cloves (laung), "
                    "cinnamon (dalchini), black pepper, and mustard oil (sarson ka tel) or ghee.\n\n"
                    "The layering method: in KP cooking, spices are added sequentially to hot mustard oil — "
                    "first heeng blooms (5 seconds), then whole spices (30 seconds), then powdered spices "
                    "in the steam of the ingredient — never in raw oil to avoid burning.\n\n"
                    "Key vegetarian pillars: Haakh, Dum Aloo, Chaman, Nadru, Rajma, Modur Pulav, "
                    "Shufta, Al Yakhni, Nadru Yakhni, Chaman Yakhni, Mujj Gaad."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Haakh · हाख (KP Collard Greens)",
                "icon": "",
                "timing": "Daily — the soul of KP food",
                "desc": (
                    "HAAKH is the most essential KP vegetarian dish — a type of collard greens "
                    "(Brassica oleracea / kale family) unique to Kashmir. Cannot be substituted.\n\n"
                    "── INGREDIENTS (serves 4) ──\n"
                    "· 500g fresh Haakh leaves (or substitute: kale/collard greens)\n"
                    "· 3 tbsp mustard oil\n"
                    "· ¼ tsp asafoetida (heeng)\n"
                    "· 2–3 whole dried Kashmiri red chillies\n"
                    "· ½ tsp dry ginger powder (sounth)\n"
                    "· Salt to taste · Water as needed\n\n"
                    "── PROCESS ──\n"
                    "1. PREP: Wash Haakh thoroughly. Remove thick stems. Tear large leaves. Keep small leaves whole.\n"
                    "2. HEAT OIL: Heat mustard oil in a heavy-bottomed pot to smoking point (this removes the pungency). "
                    "Remove from flame, let cool 10 seconds — oil should still be very hot.\n"
                    "3. HEENG BLOOM: Return to medium heat. Add heeng — it will sizzle and bloom in 5–8 seconds. "
                    "This is the defining KP flavour step — do not skip.\n"
                    "4. CHILLI: Add whole dry red chillies — fry 20 seconds until they darken.\n"
                    "5. GREENS: Add Haakh all at once — it will splutter. Stir quickly. "
                    "Add ½ cup water immediately to prevent burning.\n"
                    "6. SPICE: Add sounth (dry ginger) and salt. Stir well.\n"
                    "7. COOK: Cover and cook on medium-low heat 15–20 minutes. "
                    "Haakh should be tender but not mushy. Water should be almost gone — "
                    "a small amount of dark green liquid (the 'stock') remains. This liquid is precious — do not drain.\n"
                    "8. FINISH: Remove lid, raise heat for 2 minutes to concentrate. Taste for salt.\n\n"
                    "SERVE: With plain boiled rice. The Haakh liquid is poured over rice first, then the greens alongside. "
                    "Eaten with finger — traditional KP style. No accompaniment needed.\n\n"
                    "RITUAL NOTE: Haakh is served at every KP meal — weddings, shraddha, Navreh. "
                    "Without Haakh there is no proper KP meal."
                ),
                "links": [
                    ("Wikipedia · Haakh", "https://en.wikipedia.org/wiki/Haakh"),
                ],
            },
            {
                "name": "Dum Aloo · दम आलू (KP Style)",
                "icon": "",
                "timing": "Festivals, weddings, daily",
                "desc": (
                    "The jewel of KP vegetarian cooking — slow-cooked baby potatoes in an aromatic "
                    "yogurt-based spice gravy. Fundamentally different from Punjabi Dum Aloo "
                    "(which uses onion-garlic). The KP version is lighter, more fragrant, and relies "
                    "entirely on the spice-yogurt technique.\n\n"
                    "── INGREDIENTS (serves 4) ──\n"
                    "· 500g baby potatoes (small, uniform)\n"
                    "· 1 cup full-fat yogurt (whisked smooth)\n"
                    "· 4 tbsp mustard oil\n"
                    "· ½ tsp asafoetida (heeng)\n"
                    "· 1 tsp Kashmiri red chilli powder (deghi mirch)\n"
                    "· 1 tsp fennel powder (saunf)\n"
                    "· ½ tsp dry ginger powder (sounth)\n"
                    "· ½ tsp turmeric\n"
                    "· 4 green cardamoms · 2 black cardamoms · 4 cloves · 1 bay leaf\n"
                    "· 1 tsp salt · ½ cup water\n\n"
                    "── PROCESS ──\n"
                    "1. POTATOES: Boil baby potatoes until just cooked (not soft). Peel. "
                    "Prick each potato all over with a fork — this allows the gravy to penetrate.\n"
                    "2. FRY POTATOES: Heat 3 tbsp mustard oil to smoking. Cool 10 seconds. "
                    "Fry the pricked potatoes on medium heat until golden-brown on all sides (8–10 min). "
                    "Remove and set aside.\n"
                    "3. MAKE GRAVY: In the same oil, heat to medium. Add heeng — bloom 5 seconds. "
                    "Add green cardamoms, black cardamoms, cloves, bay leaf — fry 30 seconds.\n"
                    "4. SPICE PASTE: Lower heat. Add Kashmiri chilli powder and turmeric — stir for 20 seconds "
                    "in the oil (do NOT add to raw oil; add when oil is warm-medium). "
                    "Add 2 tbsp water to form a paste, cook 1 minute.\n"
                    "5. YOGURT: Add whisked yogurt 1 tbsp at a time, stirring continuously on low heat "
                    "after each addition to prevent curdling. This is the critical technique — "
                    "patience here defines the quality of the dish.\n"
                    "6. BUILD GRAVY: Once all yogurt is incorporated, add fennel powder and sounth. "
                    "Add ½ cup water. Bring to gentle simmer.\n"
                    "7. DUM (SLOW COOK): Add fried potatoes. Cover with tight lid. "
                    "Cook on lowest flame 20–25 minutes (dum = steam cooking). "
                    "The potatoes absorb all the flavours. Gravy thickens to a coating consistency.\n"
                    "8. FINISH: Check salt. The oil should float on top as a red layer — this is correct. "
                    "Garnish with fresh coriander (optional — some KPs avoid it).\n\n"
                    "SERVE: With rice or Girda bread. The signature dish of any KP feast."
                ),
                "links": [
                    ("Wikipedia · Dum Aloo", "https://en.wikipedia.org/wiki/Dum_Aloo"),
                ],
            },
            {
                "name": "Chaman · छमन (Kashmiri Paneer)",
                "icon": "",
                "timing": "Festive — weddings, Navreh",
                "desc": (
                    "KP-style paneer (cottage cheese) cooked in a fragrant yogurt-fennel gravy — "
                    "one of the most beloved vegetarian dishes of the KP kitchen. "
                    "'Chaman' means 'garden' in Kashmiri — the dish is named for its fresh, green-tinged colour.\n\n"
                    "── INGREDIENTS (serves 4) ──\n"
                    "· 250g fresh paneer, cut into 1.5-inch cubes\n"
                    "· ¾ cup yogurt (whisked)\n"
                    "· 3 tbsp mustard oil\n"
                    "· ¼ tsp asafoetida\n"
                    "· 1 tsp Kashmiri chilli powder\n"
                    "· 1½ tsp fennel powder (saunf)\n"
                    "· ½ tsp dry ginger (sounth)\n"
                    "· ½ tsp turmeric\n"
                    "· 3 green cardamoms · 2 cloves\n"
                    "· ½ tsp salt · ½ cup milk or water\n\n"
                    "── PROCESS ──\n"
                    "1. FRY PANEER: Heat mustard oil to smoking, cool 10 seconds. "
                    "Fry paneer cubes on medium heat until lightly golden (2–3 min per side). "
                    "Remove. (Optional: soak fried paneer in warm salted water 10 minutes to keep soft.)\n"
                    "2. SPICE BASE: In same oil on medium-low, add heeng — bloom. "
                    "Add cardamoms and cloves — 20 seconds. "
                    "Add turmeric and chilli powder — stir 15 seconds.\n"
                    "3. YOGURT: Add whisked yogurt slowly, 1 tbsp at a time, stirring constantly. "
                    "Cook on low heat 5 minutes until oil separates.\n"
                    "4. SPICES: Add fennel powder and sounth. Add milk/water. Simmer 5 minutes.\n"
                    "5. PANEER: Add paneer cubes gently. Simmer covered 10 minutes on low. "
                    "The gravy coats each piece. Do not stir vigorously — paneer will break.\n"
                    "6. FINISH: Check salt. A few strands of saffron dissolved in warm milk "
                    "can be added at end for colour and fragrance.\n\n"
                    "SERVE: With rice. The gravy should be semi-thick, fragrant, and golden-orange."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Nadru (Lotus Stem) · नद्रु — Nadru Yakhni & Nadru Palak",
                "icon": "",
                "timing": "Year-round — harvest from Dal Lake",
                "desc": (
                    "Nadru (lotus root/stem) is unique to Kashmiri cuisine — harvested from Dal and Wular lakes. "
                    "Crunchy, starchy, with a hollow cross-section. Used in two classic KP recipes:\n\n"
                    "── NADRU YAKHNI (in yogurt gravy) ──\n"
                    "INGREDIENTS: 300g nadru (cleaned, sliced into ½-inch rounds), 1 cup yogurt (whisked), "
                    "3 tbsp mustard oil, ¼ tsp heeng, 1 tsp fennel powder, ½ tsp sounth, "
                    "3 green cardamoms, 2 cloves, salt.\n\n"
                    "PROCESS:\n"
                    "1. BLANCH: Boil nadru slices 5 minutes. Drain. This removes any rawness.\n"
                    "2. FRY: In hot mustard oil, add heeng + cardamoms + cloves. Add blanched nadru. "
                    "Fry 5 minutes on medium until lightly golden at edges.\n"
                    "3. YOGURT GRAVY: On low heat, add whisked yogurt 1 tbsp at a time, stirring continuously. "
                    "Add fennel and sounth. Add ½ cup water. Cover and simmer 15 min on low.\n"
                    "4. FINISH: The gravy should be white, fragrant with fennel. "
                    "Oil floats on top — this is correct.\n\n"
                    "── NADRU PALAK (with spinach) ──\n"
                    "PROCESS: Sauté blanched nadru + blanched spinach in mustard oil with heeng, "
                    "Kashmiri chilli, sounth, fennel. No yogurt. Dry-ish texture. "
                    "Spinach turns deep green and coats the nadru.\n\n"
                    "── NADRU CHIPS (Nadru Monje) ──\n"
                    "Slice nadru thin (3mm), coat in rice flour batter with Kashmiri chilli and fennel, "
                    "deep fry until crisp. Street food of Srinagar."
                ),
                "links": [
                    ("Wikipedia · Lotus Stem Curry", "https://en.wikipedia.org/wiki/Lotus_stem"),
                ],
            },
            {
                "name": "Al Yakhni · आल यखनी (Turnip in Yogurt)",
                "icon": "",
                "timing": "Winter — turnip season",
                "desc": (
                    "Al = turnip in Kashmiri. Yakhni = yogurt-based white gravy. "
                    "A humble but deeply flavoured winter dish — the turnip absorbs the fennel-yogurt gravy beautifully.\n\n"
                    "── INGREDIENTS (serves 4) ──\n"
                    "· 4 medium turnips, peeled and quartered\n"
                    "· 1 cup yogurt (whisked)\n"
                    "· 3 tbsp mustard oil\n"
                    "· ¼ tsp heeng · 3 green cardamoms · 2 cloves\n"
                    "· 1½ tsp fennel powder · ½ tsp sounth · Salt\n\n"
                    "── PROCESS ──\n"
                    "1. PREP TURNIPS: Peel and quarter. Boil or pressure-cook until just tender (not mushy).\n"
                    "2. FRY TURNIPS: In hot mustard oil, fry cooked turnips until golden. Remove.\n"
                    "3. YAKHNI BASE: In remaining oil, bloom heeng. Add cardamoms + cloves. "
                    "On low heat, add whisked yogurt slowly — 1 tbsp at a time, stirring constantly. "
                    "This prevents the yogurt from breaking (the most critical step in all KP yakhni cooking).\n"
                    "4. SPICE: Add fennel powder + sounth. Add ½ cup water.\n"
                    "5. TURNIPS: Add fried turnips. Cover and simmer 15 minutes on lowest flame. "
                    "The white gravy should be fragrant, lightly thickened, and coat the turnips.\n\n"
                    "SERVE: With plain rice. A classic KP winter meal."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Modur Pulav · मोदुर पुलाव (Sweet Rice)",
                "icon": "",
                "timing": "Navreh, Herath, weddings, Navreh Thali",
                "desc": (
                    "The festive sweet rice of Kashmiri Pandits — served at Navreh (New Year), "
                    "weddings, and auspicious ceremonies. 'Modur' = sweet in Kashmiri.\n\n"
                    "── INGREDIENTS (serves 6) ──\n"
                    "· 2 cups basmati rice (washed, soaked 30 min)\n"
                    "· ½ cup ghee (NOT oil — ghee is essential here)\n"
                    "· 1 cup sugar or to taste\n"
                    "· ½ cup mixed dry fruits: raisins, cashews, almonds, walnuts (broken)\n"
                    "· 8–10 saffron strands soaked in 2 tbsp warm milk\n"
                    "· 6 green cardamoms · 4 cloves · 1 cinnamon stick · 2 bay leaves\n"
                    "· 4 cups water · ½ tsp salt\n\n"
                    "── PROCESS ──\n"
                    "1. FRY DRY FRUITS: In ghee, fry cashews until golden, then almonds, then raisins "
                    "(raisins puff in 20 seconds). Remove all and set aside.\n"
                    "2. WHOLE SPICES: In same ghee, add cardamoms, cloves, cinnamon, bay leaves — "
                    "fry 30 seconds until aromatic.\n"
                    "3. RICE: Add drained rice. Stir gently in the spiced ghee for 2 minutes "
                    "until each grain is coated and slightly translucent.\n"
                    "4. WATER + SUGAR: Add 4 cups water, sugar, salt, and saffron milk. "
                    "Stir gently to dissolve sugar. Bring to boil.\n"
                    "5. DUM: Reduce to lowest flame. Cover tightly (seal with dough if possible for true dum). "
                    "Cook 20 minutes. Do NOT open lid during this time.\n"
                    "6. FINISH: Open lid. Fluff gently with fork. Scatter fried dry fruits on top.\n\n"
                    "SERVE: Warm, as a sweet dish alongside the main meal or as an offering. "
                    "The saffron gives it a golden-orange colour and exquisite fragrance. "
                    "On Navreh morning, the first sight of Modur Pulav in the Thali is auspicious."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Shufta · शुफ्ता (Dry Fruit Sweet)",
                "icon": "",
                "timing": "Navreh, Herath, weddings — sacred sweet",
                "desc": (
                    "Shufta is the most sacred KP sweet — offered at Navreh, Herath, and all auspicious ceremonies. "
                    "A rich confection of dry fruits, cottage cheese and spices in sugar syrup.\n\n"
                    "── INGREDIENTS ──\n"
                    "· ½ cup each: walnuts (broken), cashews, almonds, raisins\n"
                    "· ½ cup fresh paneer, crumbled\n"
                    "· ½ cup coconut (desiccated or fresh grated)\n"
                    "· 1 cup sugar · ½ cup water\n"
                    "· 2 tbsp ghee\n"
                    "· 6 saffron strands in 1 tbsp warm milk\n"
                    "· ½ tsp cardamom powder · ¼ tsp dry ginger powder\n"
                    "· 1 tsp rose water (optional)\n\n"
                    "── PROCESS ──\n"
                    "1. FRY DRY FRUITS: In ghee, lightly fry each dry fruit separately — "
                    "almonds (2 min), cashews (2 min), walnuts (1 min), raisins (30 sec). Set aside.\n"
                    "2. FRY PANEER: In same ghee, fry crumbled paneer until lightly golden. Set aside.\n"
                    "3. SUGAR SYRUP: In a clean pan, dissolve sugar in ½ cup water. "
                    "Cook to one-string consistency (syrup forms a single thread between fingers). "
                    "Add saffron milk, cardamom, dry ginger, rose water.\n"
                    "4. COMBINE: Add all fried dry fruits, paneer and coconut to the syrup. "
                    "Stir quickly to coat everything. Remove from heat.\n"
                    "5. SET: Pour onto a greased plate. Flatten lightly. "
                    "It will set as it cools — not hard like barfi, but moist and jewel-like.\n\n"
                    "SERVE: Cut into pieces or serve by spoonfuls. "
                    "Central to the Navreh Thali — its presence is mandatory for auspiciousness."
                ),
                "links": [
                    ("Wikipedia · Shufta", "https://en.wikipedia.org/wiki/Shufta"),
                ],
            },
            {
                "name": "Rajma · राजमा (Kashmiri Red Kidney Beans)",
                "icon": "",
                "timing": "Daily — a KP staple",
                "desc": (
                    "KP Rajma uses the small, dark Kashmiri rajma — much smaller and more flavourful "
                    "than Punjabi rajma. Cooked without onion or garlic — the flavour comes entirely "
                    "from the spice technique.\n\n"
                    "── INGREDIENTS (serves 4) ──\n"
                    "· 1 cup Kashmiri rajma (soaked overnight)\n"
                    "· 3 tbsp mustard oil\n"
                    "· ¼ tsp heeng · 2 whole dried red chillies\n"
                    "· ½ tsp turmeric · 1 tsp Kashmiri chilli powder\n"
                    "· 1 tsp fennel powder · ½ tsp sounth · Salt\n"
                    "· 1 medium tomato (pureed) — optional in KP style\n\n"
                    "── PROCESS ──\n"
                    "1. PRESSURE COOK: Drain soaked rajma. Pressure cook with fresh water, "
                    "salt and turmeric for 4–5 whistles until very soft. Reserve the cooking liquid.\n"
                    "2. TEMPER: Heat mustard oil to smoking. Cool 10 sec. "
                    "Add heeng — bloom. Add dry chillies — darken 20 sec.\n"
                    "3. SPICES: Add Kashmiri chilli powder, fennel, sounth — stir 20 sec in warm oil. "
                    "Add 2 tbsp water to form a paste.\n"
                    "4. BEANS: Add cooked rajma along with its cooking liquid. Mash a few beans "
                    "against the side of the pot to thicken the gravy.\n"
                    "5. SIMMER: Cook uncovered 15–20 minutes on medium until gravy is thick and "
                    "coats the beans. Adjust salt.\n\n"
                    "SERVE: With plain boiled rice — the classic KP rice-rajma combination "
                    "(known as 'Chawal-Rajma' or 'Bhaat te Rajma')."
                ),
                "links": [
                    ("Wikipedia · Rajma", "https://en.wikipedia.org/wiki/Rajma"),
                ],
            },
            {
                "name": "Mujj Gaad · मुज गाड (Radish Preparation)",
                "icon": "",
                "timing": "Winter — white radish season",
                "desc": (
                    "A unique KP winter preparation — mujj = white radish (mooli) in Kashmiri. "
                    "The radish is used in multiple forms: fresh (as chutney), cooked, and dried (wari).\n\n"
                    "── MUJJ CHATIN (Radish Chutney) ──\n"
                    "INGREDIENTS: 1 large white radish (grated), ½ tsp Kashmiri chilli powder, "
                    "½ tsp sounth, salt, 1 tbsp mustard oil, fresh coriander.\n"
                    "PROCESS: Mix grated radish with salt — let it sweat 10 min. Squeeze out liquid. "
                    "Mix with chilli powder, sounth, mustard oil. Garnish with coriander. "
                    "Served as a condiment — the heat of the radish is cooling in the KP system.\n\n"
                    "── MUJJ WITH HAAKH ──\n"
                    "Radish cut into chunks is added to Haakh in the last 10 minutes of cooking. "
                    "The radish softens and absorbs the mustard oil–heeng base beautifully.\n\n"
                    "── WARI (Dried Radish Dumpling) ──\n"
                    "Traditional KP winter ingredient: white radish grated, mixed with rice flour and spices, "
                    "shaped into flat rounds and sun-dried. Stored for winter months. "
                    "Rehydrated and added to Haakh or cooked as a standalone dish in mustard oil."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Kehwa · केहवा (Kashmiri Green Tea)",
                "icon": "",
                "timing": "Daily — offered to every guest",
                "desc": (
                    "Kashmir's iconic green tea — the symbol of Kashmiri hospitality.\n\n"
                    "── INGREDIENTS (serves 2) ──\n"
                    "· 2 cups water · 1 tsp Kehwa tea leaves (or ½ tsp green tea)\n"
                    "· 4–5 saffron strands · 2 green cardamoms (crushed)\n"
                    "· 1 small cinnamon stick · 2 cloves\n"
                    "· 1 tsp sugar or honey · 6–8 blanched almond slivers\n\n"
                    "── PROCESS ──\n"
                    "1. Bring water to boil in a small copper Samovar or pot.\n"
                    "2. Add cardamom, cinnamon, cloves — boil 2 minutes.\n"
                    "3. Add tea leaves — simmer 1 minute (do not over-brew — stays green, not dark).\n"
                    "4. Add saffron — it will turn the tea golden. Sweeten lightly.\n"
                    "5. Strain into small cups. Top with almond slivers.\n\n"
                    "NOTE: Traditionally brewed in a Samovar (Samavar) — a brass urn with "
                    "a central chimney filled with hot charcoal. The charcoal-brewed version has "
                    "a distinctive smoky note impossible to replicate on a gas stove.\n\n"
                    "RITUAL: In KP homes, Kehwa is served immediately to any guest before anything else. "
                    "Refusing it is considered impolite. Drunk throughout the day in winter."
                ),
                "links": [
                    ("Wikipedia · Kahwah", "https://en.wikipedia.org/wiki/Kahwah"),
                ],
            },
            {
                "name": "Noon Chai · नून चाय (Pink Salted Tea)",
                "icon": "",
                "timing": "Morning — with bread",
                "desc": (
                    "The iconic pink tea of Kashmir — unique in the world for its colour and taste.\n\n"
                    "── INGREDIENTS (serves 4) ──\n"
                    "· 4 cups water · 2 tsp Noon Chai (Kashmiri pink tea) leaves\n"
                    "· ½ tsp baking soda · 2 cups full-fat milk · Salt to taste\n"
                    "· Crushed walnuts or pistachios (optional garnish)\n\n"
                    "── PROCESS ──\n"
                    "1. BREW: Bring 4 cups water to boil. Add tea leaves and baking soda. "
                    "Boil vigorously 10–15 minutes — the water turns bright red/brown.\n"
                    "2. CHURN: Pour the tea back and forth between two vessels (or use a whisk) "
                    "to aerate — this develops the characteristic pinkish colour.\n"
                    "3. MILK: Add milk to the red tea base. Bring back to boil. "
                    "The mixture turns pink-magenta as the alkaline soda reacts with the tea.\n"
                    "4. SALT: Add salt (generous — this is the 'noon/salt' in its name). Stir.\n"
                    "5. STRAIN into cups. Garnish with crushed nuts.\n\n"
                    "SERVE: With Girda (tandoor bread), Kulcha, Lavasa, or Bakarkhani. "
                    "The saltiness and pink colour are acquired tastes — deeply loved by Kashmiris. "
                    "No Kashmiri morning is complete without Noon Chai."
                ),
                "links": [
                    ("Wikipedia · Noon Chai", "https://en.wikipedia.org/wiki/Noon_chai"),
                ],
            },
            {
                "name": "Kashmiri Breads · कश्मीरी रोटियाँ",
                "icon": "",
                "timing": "Daily — from traditional Kaan ovens",
                "desc": (
                    "Kashmir has a rich bread culture — all baked in traditional Kaan (clay tandoor ovens). "
                    "The baker (Nanbai / Kandur) is an important community figure in every KP mohalla.\n\n"
                    "── TYPES AND PROCESS ──\n\n"
                    "GIRDA (गिर्दा): Round, slightly thick tandoor bread. "
                    "Dough: flour, water, yeast, salt, tiny amount oil. "
                    "Proved 2 hours. Shaped into thick discs. Baked on Kaan walls 8–10 min. "
                    "Eaten with Haakh, Rajma, Noon Chai.\n\n"
                    "KULCHA (कुलचा): Soft, slightly sweet round bread with sesame seeds on top. "
                    "Dough: flour, milk, sugar, salt, yeast, butter. Proved 2 hours. "
                    "Topped with sesame seeds. Baked in Kaan. "
                    "Classic breakfast bread — eaten with Noon Chai.\n\n"
                    "LAVASA (लवासा): Ultra-thin crispy flatbread — paper thin. "
                    "Dough stretched very thin, baked quickly on hot Kaan. Almost like a cracker. "
                    "Broken and dunked in Noon Chai.\n\n"
                    "TCHOT (चोट): Ring-shaped bread with sesame seeds — like a large sesame bagel. "
                    "Dough similar to Kulcha but shaped into rings. Baked until golden. "
                    "Strung on strings and sold hanging in traditional bakeries.\n\n"
                    "SHEERMAL (शीरमाल): Festive saffron-milk bread. "
                    "Dough enriched with saffron milk, sugar, and ghee. "
                    "Baked soft and golden. Only made for weddings and festivals.\n\n"
                    "BAKARKHANI (बाकरखानी): Flaky, layered, slightly crispy. "
                    "Laminated dough (like rough puff pastry) with ghee folded in. "
                    "Baked until golden-brown. Can be stored for days."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Cuisine", "https://en.wikipedia.org/wiki/Kashmiri_cuisine"),
                ],
            },
            {
                "name": "Wazwan · वाज़वान (Grand KP Feast)",
                "icon": "",
                "timing": "Weddings and major celebrations",
                "desc": (
                    "The grand Kashmiri feast — a multi-course ritual meal at weddings and celebrations. "
                    "Cooked by the Waza (master chef) on wood-fire in traditional large copper vessels. "
                    "Served on a large copper plate (Traem) shared between 4 guests. "
                    "The vegetarian dishes in the Wazwan sequence:\n\n"
                    "1. MODUR PULAV — sweet saffron rice (first served, auspicious)\n"
                    "2. HAAKH — collard greens (always present)\n"
                    "3. CHAMAN — paneer in yogurt-fennel gravy\n"
                    "4. NADRU YAKHNI — lotus stem in white gravy\n"
                    "5. AL YAKHNI — turnip in yogurt gravy (winter)\n"
                    "6. SHUFTA — the dessert-sweet served last\n\n"
                    "The complete Wazwan also includes non-vegetarian courses (Rogan Josh, Yakhni, "
                    "Gushtaba) but KP families also observe purely vegetarian Wazwan variants "
                    "for ceremonies where sattvic rules apply."
                ),
                "links": [
                    ("Wikipedia · Wazwan", "https://en.wikipedia.org/wiki/Wazwan"),
                ],
            },
        ],
        "Dress & Crafts · वेशभूषा और शिल्प": [
            {
                "name": "Pheran · फेरन",
                "icon": "",
                "timing": "Traditional — especially winter",
                "desc": (
                    "The iconic long loose robe of Kashmir — worn by both men and women. "
                    "Women's Pheran is longer with intricate embroidery; men's is plainer. "
                    "Under the Pheran, a Kangri (clay firepot in a wicker basket) is held "
                    "close to the body for warmth in winter. Symbol of Kashmiri identity."
                ),
                "links": [
                    ("Wikipedia · Pheran", "https://en.wikipedia.org/wiki/Pheran"),
                ],
            },
            {
                "name": "Kashmiri Shawls (Pashmina & Kani) · शाल",
                "icon": "",
                "timing": "Traditional craft — centuries old",
                "desc": (
                    "Kashmir's most famous craft. Pashmina: woven from the ultra-fine undercoat "
                    "of Changthangi goat. Kani shawl: woven on a special loom with wooden bobbins "
                    "(kani) — one shawl can take 3 years. Shahtoosh (banned): from Tibetan antelope. "
                    "GI-tagged product. Intricate patterns: Buta, Hashia, Jama, Jamawar."
                ),
                "links": [
                    ("Wikipedia · Pashmina", "https://en.wikipedia.org/wiki/Pashmina"),
                    ("Wikipedia · Kani Shawl", "https://en.wikipedia.org/wiki/Kani_shawl"),
                ],
            },
            {
                "name": "Kashmiri Carpet Weaving · कालीन",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Hand-knotted woollen and silk carpets — among the finest in the world. "
                    "Designs: floral medallion (herati), garden (bagh), prayer (namazluq), "
                    "tree of life. Up to 2,400 knots per square inch in fine silk pieces. "
                    "GI-tagged. Villages like Kanihama specialize in specific patterns."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Carpet", "https://en.wikipedia.org/wiki/Kashmiri_carpet"),
                ],
            },
            {
                "name": "Papier-Mâché · कागज़ की कारीगरी",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Intricate hand-painted objects — boxes, trays, vases, ornaments — "
                    "made from layered paper pulp. Motifs: chinar leaves, lotus, Mughal florals. "
                    "Introduced to Kashmir by Shah Mir Swati in the 14th century. "
                    "Painted with natural pigments by master artisans (Naqash)."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Papier-Mâché", "https://en.wikipedia.org/wiki/Papier-m%C3%A2ch%C3%A9#Kashmir"),
                ],
            },
            {
                "name": "Walnut Wood Carving · अखरोट की नक्काशी",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Kashmir's walnut wood (Juglans regia) has a distinctive dark grain ideal for "
                    "fine carving. Motifs: chinar, lotus, hunting scenes, geometric patterns. "
                    "Used for furniture, screens (jali work), boxes and decorative panels. "
                    "Traditional carving families are based in Srinagar's old city."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Crafts", "https://en.wikipedia.org/wiki/Kashmiri_handicraft"),
                ],
            },
            {
                "name": "Sozni & Tilla Embroidery · सोज़नी / तिल्ला",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Sozni: needle embroidery on Pashmina shawls — fine floral patterns worked "
                    "from both sides so the reverse mirrors the front. "
                    "Tilla: gold/silver thread embroidery (zari) on velvet — used for Pherans, "
                    "caps, accessories. Both are GI-tagged crafts of Jammu & Kashmir."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Embroidery", "https://en.wikipedia.org/wiki/Kashmiri_embroidery"),
                ],
            },
            {
                "name": "Kangri · कांगड़ी (Fire Pot)",
                "icon": "",
                "timing": "Winter — Oct to Feb",
                "desc": (
                    "The Kangri is Kashmir's iconic personal fire pot — a clay pot holding glowing charcoal "
                    "in a wicker basket. Carried under the Pheran close to the body for warmth. "
                    "Each person has their own Kangri — it is a personal and intimate object. "
                    "A well-decorated Kangri with silver or copper fittings is a prized possession and gift. "
                    "Without Kangri and Pheran, a Kashmiri winter is unimaginable. "
                    "The Kangri is also mentioned in KP ritual — the fire within symbolises the inner Agni."
                ),
                "links": [
                    ("Wikipedia · Kangri", "https://en.wikipedia.org/wiki/Kangri_(firepot)"),
                ],
            },
            {
                "name": "Khatamband · खातमबंद (Wooden Ceiling Art)",
                "icon": "",
                "timing": "Traditional architecture",
                "desc": (
                    "Khatamband is the art of making geometric wooden ceilings — "
                    "interlocking pieces of walnut or deodar wood fitted together without nails "
                    "to create complex star and polygon patterns. Found in traditional KP homes, "
                    "mosques, and shrines across Kashmir. The patterns are based on Islamic geometry "
                    "but the technique and the craftsmen (Dagr) are shared across communities. "
                    "The best examples are in old city Srinagar homes and the Shah Hamdan shrine. "
                    "A Khatamband ceiling can have 6, 8, 12, or 16-pointed star patterns."
                ),
                "links": [
                    ("Wikipedia · Khatamband", "https://en.wikipedia.org/wiki/Khatamband"),
                ],
            },
            {
                "name": "Namdah & Gabba · नमदाह / गब्बा",
                "icon": "",
                "timing": "Traditional craft",
                "desc": (
                    "Namdah: pressed felt rugs — wool fibres compressed (not woven) into thick felt and "
                    "then embroidered with floral motifs in chain stitch. Lighter and less expensive than carpets. "
                    "Gabba: recycled woollen fabric cut into strips and re-woven into colourful geometric rugs. "
                    "Both are cottage industry crafts of rural Kashmir — produced in Anantnag and Budgam districts. "
                    "Exported globally and part of the traditional KP home aesthetic."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Handicraft", "https://en.wikipedia.org/wiki/Kashmiri_handicraft"),
                ],
            },
            {
                "name": "Copper & Silverware (Kral craft) · ताँबा-चाँदी शिल्प",
                "icon": "",
                "timing": "Traditional craft — KP households",
                "desc": (
                    "Kashmir has a centuries-old tradition of copper and silverware — "
                    "the craft of the Kral (potter-metalworker) community. "
                    "Key items: Samovar (brass tea urn), Traem (large copper/brass plate for Wazwan), "
                    "Saz (copper handwashing vessel), Tasht (basin), Manji (brass lamp). "
                    "KP households traditionally had complete sets of these vessels for ritual and daily use. "
                    "Silver items: ritual spoons (Karchul), betel nut containers, puja thalis. "
                    "Many antique KP copper vessels are heirlooms brought from the Valley."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Handicraft", "https://en.wikipedia.org/wiki/Kashmiri_handicraft"),
                ],
            },
        ],
        "Language & Script · भाषा": [
            {
                "name": "Kashmiri Language (Koshur) · कोशुर",
                "icon": "",
                "timing": "Living language",
                "desc": (
                    "Kashmiri (Koshur) is a Dardic Indo-Aryan language spoken by ~7 million people. "
                    "Written in three scripts: Sharada (traditional KP script), "
                    "Nastaliq/Perso-Arabic (official in J&K), and Devanagari. "
                    "Recognized as a Scheduled Language of India (8th Schedule). "
                    "UNESCO classifies it as 'Vulnerable'. Rich in Persian, Sanskrit and Apabhramsha loanwords."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Language", "https://en.wikipedia.org/wiki/Kashmiri_language"),
                    ("Ethnologue · Kashmiri", "https://www.ethnologue.com/language/kas/"),
                ],
            },
            {
                "name": "Sharada Script · शारदा लिपि",
                "icon": "",
                "timing": "c. 8th century CE — now endangered",
                "desc": (
                    "The ancient script of Kashmir — ancestor of Gurmukhi and Takri. "
                    "Used for KP religious manuscripts, horoscopes, letters and temple inscriptions. "
                    "Named after Sharada Devi (Saraswati). ~10,000 manuscripts survive in "
                    "libraries across India and abroad. Now taught only in a few KP families. "
                    "Unicode block U+11180–U+111DF."
                ),
                "links": [
                    ("Wikipedia · Sharada Script", "https://en.wikipedia.org/wiki/Sharada_script"),
                    ("Sharada Script Unicode", "https://www.unicode.org/charts/PDF/U11180.pdf"),
                ],
            },
            {
                "name": "Kashmiri Proverbs (Maqol) · मक़ोल",
                "icon": "",
                "timing": "Living oral tradition",
                "desc": (
                    "Kashmiri has a rich proverbial tradition — Maqol (proverbs) and "
                    "Zaban-i-Khas (idiomatic expressions). Examples: "
                    "'Pyov tse panan khyon, pyov tse maraan' (One who feeds you may also harm you). "
                    "Proverbs encoded in the Vakhs of Lal Ded and Nund Rishi remain in daily speech."
                ),
                "links": [
                    ("Kashmiri Proverbs Archive", "https://archive.org/search?query=kashmiri+proverbs"),
                ],
            },
            {
                "name": "Kashmiri Numbers & Counting · कश्मीरी गिनती",
                "icon": "",
                "timing": "Living language",
                "desc": (
                    "The Kashmiri number system:\n"
                    "1 = Akh · 2 = Zey · 3 = Trey · 4 = Tsur · 5 = Panch\n"
                    "6 = She / Sheh · 7 = Sath · 8 = Ath · 9 = Nav · 10 = Dah\n"
                    "11 = Kaah · 12 = Baah · 13 = Trueh · 14 = Choudah · 15 = Pandah\n"
                    "20 = Wuh · 25 = Panchawuh · 30 = Trih · 50 = Panjah · 100 = Hath\n\n"
                    "ORDINALS: First = Peeth · Second = Zan · Third = Trijem\n"
                    "The numbers 11–14 are the same Kashmiri tithi names used in the panchang: "
                    "Kaah (Ekadashi), Baah (Dwadashi), Trueh (Trayodashi), Choudah (Chaturdashi)."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Language", "https://en.wikipedia.org/wiki/Kashmiri_language"),
                ],
            },
            {
                "name": "KP Greeting Words & Daily Speech · अभिवादन",
                "icon": "",
                "timing": "Living speech",
                "desc": (
                    "Common KP Kashmiri words and greetings:\n\n"
                    "GREETINGS:\n"
                    "· Namaskar / Jai Mata Di — traditional KP greeting\n"
                    "· Navreh Mubarak — New Year greeting (Navreh)\n"
                    "· Herath Mubarak — Shivratri greeting\n\n"
                    "FAMILY TERMS:\n"
                    "· Bab — father · Maej — mother · Ded — grandmother · Bab ji — grandfather\n"
                    "· Baeyi — brother · Bebeh — sister · Kan — maternal uncle\n\n"
                    "FOOD TERMS:\n"
                    "· Bhaat — rice · Haakh — greens · Noon — salt · Dood — milk\n"
                    "· Tschay — tea · Tchanth — curd · Ghee — ghee\n\n"
                    "SPIRITUAL TERMS:\n"
                    "· Bhagwan — God · Pooja — worship · Bab Shiv — Shiva\n"
                    "· Maej Sharika — Mother Sharika Devi · Mataji — Devi\n"
                    "· Vakh — mystical verse (Lal Ded's poems) · Shrukh — poem of Nund Rishi"
                ),
                "links": [
                    ("Wikipedia · Kashmiri Language", "https://en.wikipedia.org/wiki/Kashmiri_language"),
                ],
            },
            {
                "name": "Sharada Manuscripts & Libraries · शारदा पाण्डुलिपियाँ",
                "icon": "",
                "timing": "c. 8th century CE — ongoing preservation",
                "desc": (
                    "Kashmir was a great centre of manuscript production for over a millennium. "
                    "Major collections of Kashmiri manuscripts (in Sharada and Devanagari):\n\n"
                    "1. Srinagar Research Library (SRL) — formerly Oriental Research Institute: "
                    "largest collection in Kashmir (~15,000 manuscripts).\n"
                    "2. Bhandarkar Oriental Research Institute, Pune — significant Kashmir manuscripts.\n"
                    "3. Asiatic Society of Bengal, Kolkata.\n"
                    "4. National Archives of India, New Delhi.\n"
                    "5. British Library, London — KSTS manuscripts.\n"
                    "6. Bodleian Library, Oxford — Sir Aurel Stein collection.\n\n"
                    "Subjects: Shaiva philosophy, Ayurveda, Jyotisha, literature, history.\n"
                    "Digital access: INDIRA (government manuscript project), "
                    "Muktabodha Indological Research Institute (muktabodha.org) — free online."
                ),
                "links": [
                    ("Muktabodha Digital Library", "https://muktabodha.org"),
                    ("Wikipedia · Kashmiri Manuscripts", "https://en.wikipedia.org/wiki/Sharada_script"),
                ],
            },
        ],
        "Nature & Geography · प्रकृति": [
            {
                "name": "Dal Lake · डल झील",
                "icon": "",
                "timing": "Year-round — Lotus blooms summer",
                "desc": (
                    "The heart of Srinagar — 18 sq km freshwater lake. "
                    "Famous for houseboats (Dunga), Shikara rides, floating gardens (Rad), "
                    "floating markets (Sabzi market at dawn). "
                    "Mentioned in Nilamata Purana as sacred. Dal's islands include "
                    "Char Chinar (four chenar trees on an island) — iconic image of Kashmir."
                ),
                "links": [
                    ("Wikipedia · Dal Lake", "https://en.wikipedia.org/wiki/Dal_Lake"),
                ],
            },
            {
                "name": "Chinar Tree (Platanus orientalis) · चिनार",
                "icon": "",
                "timing": "Autumn foliage — Oct–Nov",
                "desc": (
                    "The Chinar (Oriental Plane) is the defining tree of Kashmir — "
                    "planted extensively by Mughal emperors in their gardens. "
                    "Autumn colours (gold, red, amber) are central to Kashmiri aesthetic. "
                    "The chinar leaf is the motif in Kashmiri crafts, carpets and embroidery. "
                    "Some individual trees are 600+ years old."
                ),
                "links": [
                    ("Wikipedia · Chinar Kashmir", "https://en.wikipedia.org/wiki/Chinar"),
                ],
            },
            {
                "name": "Kashmir Saffron (Kesar) · केसर",
                "icon": "",
                "timing": "Harvest: Oct–Nov; Pampore region",
                "desc": (
                    "The world's finest saffron — GI-tagged Kashmiri Kesar from Pampore (Pulwama). "
                    "Only region in the Indian subcontinent where saffron grows. "
                    "Harvested by hand before sunrise. Used in Kehwa, Wazwan, Modur Pulav, "
                    "and as a sacred offering. Cultivation dates back over 2,000 years."
                ),
                "links": [
                    ("Wikipedia · Kashmiri Saffron", "https://en.wikipedia.org/wiki/Kashmiri_saffron"),
                ],
            },
            {
                "name": "Mughal Gardens · मुग़ल बाग़",
                "icon": "",
                "timing": "Spring–Summer",
                "desc": (
                    "Three great Mughal gardens on Dal Lake shore — Shalimar Bagh (1619, Jahangir), "
                    "Nishat Bagh (1633, Asaf Khan) and Chashme Shahi (1632, Shah Jahan). "
                    "Designed on the Char-bagh (4-garden) Persian model with terraces, fountains, "
                    "chinar avenues and floral beds. UNESCO World Heritage tentative list."
                ),
                "links": [
                    ("Wikipedia · Mughal Gardens Kashmir", "https://en.wikipedia.org/wiki/Mughal_gardens_of_Kashmir"),
                ],
            },
            {
                "name": "Wular Lake · वुलर झील",
                "icon": "",
                "timing": "Year-round",
                "desc": (
                    "Wular is the largest freshwater lake in India — ~189 sq km at peak. "
                    "Located in Bandipora district, fed by the Jhelum (Vitasta) river. "
                    "Mentioned in the Nilamata Purana as sacred. "
                    "Rich in fish (mahseer, trout, carp) and water chestnuts (singhara). "
                    "The surrounding areas of Sopore and Bandipora are historically significant KP settlements. "
                    "Wular is connected to the Vitasta (Jhelum) — both sacred in KP tradition."
                ),
                "links": [
                    ("Wikipedia · Wular Lake", "https://en.wikipedia.org/wiki/Wular_Lake"),
                ],
            },
            {
                "name": "Valley of Kashmir — Geography · कश्मीर घाटी",
                "icon": "",
                "timing": "Perennial",
                "desc": (
                    "The Kashmir Valley (Koshur Maej — Mother Kashmir) is a high-altitude mountain valley "
                    "at ~1,600m (5,200 ft) elevation, ~135 km long and ~32 km wide. "
                    "Bounded by: Pir Panjal range (south), Great Himalaya (north-east), Karakoram (far north). "
                    "Drained by the Vitasta (Jhelum) river — the sacred mother-river of Kashmir (Rigvedic). "
                    "According to Nilamata Purana: the valley was once a vast lake (Satisar) — "
                    "drained by Vitasta at the request of the sage Kashyapa (from whom 'Kashmir' derives). "
                    "This origin myth is geologically plausible — the valley shows lacustrine deposits. "
                    "District count: 10 Kashmir Valley districts + 2 Ladakh + 10 Jammu = 22 districts total."
                ),
                "links": [
                    ("Wikipedia · Kashmir Valley", "https://en.wikipedia.org/wiki/Kashmir_Valley"),
                ],
            },
            {
                "name": "Himalayan Flora · हिमालयी वनस्पति",
                "icon": "",
                "timing": "Spring–Summer — blooms",
                "desc": (
                    "Kashmir's flora is extraordinary — the valley is a botanical treasure:\n\n"
                    "ICONIC BLOOMS:\n"
                    "· Tulips — Indira Gandhi Tulip Garden (Asia's largest), Srinagar — April\n"
                    "· Lotus (Kamal) — Dal and Wular lakes — sacred to Sharika Devi\n"
                    "· Saffron (Crocus sativus) — Pampore fields — Oct–Nov\n"
                    "· Almond (Badam) — Badamwari garden, Srinagar — Feb (first spring bloom)\n"
                    "· Cherry (Kiur/Gulab) blossom — March–April\n"
                    "· Narcissus (Nargis) — placed in Navreh Thali as auspicious\n\n"
                    "SACRED TREES:\n"
                    "· Chinar (Oriental Plane) — symbol of Kashmir\n"
                    "· Walnut (Doon/Akhrot) — placed in Navreh Thali; wood used for Herath Shishur\n"
                    "· Deodar Cedar — used in temples and traditional architecture\n"
                    "· Apple orchards — Kashmir's modern economy (introduced 1917 by British)"
                ),
                "links": [
                    ("Wikipedia · Flora of Kashmir", "https://en.wikipedia.org/wiki/Flora_of_Kashmir"),
                ],
            },
            {
                "name": "Sacred Mountains & Passes · पर्वत और दर्रे",
                "icon": "",
                "timing": "Pilgrimage seasons",
                "desc": (
                    "KEY SACRED MOUNTAINS:\n"
                    "· Shankaracharya Hill (Takht-e-Sulaiman) — 1100m, Srinagar: Jyeshtheshwara Shiva temple; "
                    "from where Vasugupta received the Shiva Sutras. Overlooking Dal Lake.\n"
                    "· Hari Parbat — Srinagar: Sharika Devi (Chakreshwari) temple; the hill IS the goddess.\n"
                    "· Amarnath (Sheshnag area) — 3,888m: the supreme Shiva Jyotirlinga of Kashmir; "
                    "annual Amarnath Yatra (July–Aug) — the most significant KP pilgrimage.\n"
                    "· Harmukh — 5,142m, Ganderbal: 'The throne of Shiva' — glacier lake Gangabal at its base.\n"
                    "· Nanga Parbat — 8,125m: 'The Naked Mountain' — highest in the western Himalaya region.\n\n"
                    "KEY PASSES:\n"
                    "· Banihal Pass / Jawahar Tunnel — main road link between Kashmir and Jammu\n"
                    "· Zoji La — 3,528m: links Kashmir Valley to Ladakh and Kargil\n"
                    "· Banihal Pass — historic route used by all medieval Kashmiri traders and pilgrims"
                ),
                "links": [
                    ("Wikipedia · Shankaracharya Hill", "https://en.wikipedia.org/wiki/Shankaracharya_Hill"),
                    ("Wikipedia · Amarnath Temple", "https://en.wikipedia.org/wiki/Amarnath_temple"),
                ],
            },
        ],
        "KP Life Cycle Rituals · संस्कार": [
            {
                "name": "Namakarana · नामकरण (Naming Ceremony)",
                "icon": "",
                "timing": "11th day after birth",
                "desc": (
                    "The KP naming ceremony performed on the 11th day (some families: 12th) after birth. "
                    "The Jyotishi (family astrologer) prepares the horoscope (Janam Patri) based on "
                    "the exact birth time and place. The name is derived from the nakshatra pada of the Moon "
                    "at birth — the first syllable of the name corresponds to the pada's akshar (syllable). "
                    "The family priest recites the Namakarana mantras from the Grihyasutras. "
                    "The child is placed in the father's lap. The name is whispered in the child's right ear three times. "
                    "The public name may differ from the nakshatra-based name (which is the 'secret name' "
                    "used in rituals). Accompanied by feasting and distribution of sweets."
                ),
                "links": [
                    ("Wikipedia · Namakarana", "https://en.wikipedia.org/wiki/Namakarana"),
                ],
            },
            {
                "name": "Janeu (Yagnopavita) · यज्ञोपवीत (Sacred Thread)",
                "icon": "",
                "timing": "Boys aged 7–12 — auspicious muhurta",
                "desc": (
                    "The Yagnopavita (Janeu) ceremony marks the spiritual birth of a KP boy — "
                    "'Dvija' (twice-born). From this day he is entitled to recite Vedic mantras. "
                    "The ceremony includes: Mundan (head shaving), ritual bath, Havana (fire ceremony), "
                    "donning the sacred three-strand thread (Janeu) over the left shoulder. "
                    "The boy begins learning the Gayatri Mantra from his father or guru. "
                    "In KP tradition, the Janeu ceremony is particularly elaborate — "
                    "includes Kul Devi puja, family feast, and often coincides with the boy's "
                    "first learning of the Shiva Panchakshara mantra (Na-Ma-Shi-Va-Ya)."
                ),
                "links": [
                    ("Wikipedia · Yagnopavita", "https://en.wikipedia.org/wiki/Upanayana"),
                ],
            },
            {
                "name": "Vivah Samskara · विवाह (KP Marriage Rituals)",
                "icon": "",
                "timing": "Auspicious muhurtas — typically Nov–Feb",
                "desc": (
                    "KP marriage is a multi-day ceremony with distinct rituals:\n\n"
                    "DAY 1 — DEVGUN: Both families perform Kul Devi puja. Horoscope matching (Guna Milana). "
                    "Gotra check — same gotra marriage is absolutely forbidden.\n\n"
                    "DAY 2 — LAGAN PATRIKA: The auspicious date and muhurta confirmed by Jyotishi.\n\n"
                    "DAY 3 — WANWUN: Women of both families sing traditional KP wedding songs (Wanwun) "
                    "for hours through the night — an ancient tradition preserved in the diaspora.\n\n"
                    "DAY 4 — MEHENDI / DEVGUN: Henna application, final family prayers.\n\n"
                    "WEDDING DAY — Main rituals: Saptapadi (seven steps around fire), "
                    "Kanyadan (bride given by father), Mangalsutra, Sindoor. "
                    "The fire ceremony (Havana) is conducted by a KP priest reciting Sanskrit mantras. "
                    "The couple invokes Kul Devi and Kul Devta blessings.\n\n"
                    "Wazwan feast follows — the complete 36-course meal for all guests."
                ),
                "links": [
                    ("Wikipedia · Hindu Marriage", "https://en.wikipedia.org/wiki/Hindu_marriage_traditions_in_Karnataka"),
                ],
            },
            {
                "name": "Shraddha · श्राद्ध (Ancestor Rites)",
                "icon": "",
                "timing": "Pitru Paksha (Bhadrapada Krishna 1–30) + death anniversaries",
                "desc": (
                    "Shraddha is the ritual offering to deceased ancestors (Pitrus) — "
                    "one of the most important ongoing duties of a KP family. "
                    "Performed annually during Pitru Paksha (Bhadrapada Krishna fortnight) "
                    "and on the death anniversary (tithi) of each ancestor.\n\n"
                    "KP SHRADDHA PROCESS:\n"
                    "1. SANKALPA: The male heir (eldest son) takes ritual resolution.\n"
                    "2. TARPAN: Water offerings (with sesame seeds, kusha grass) to ancestors, "
                    "gods, sages — poured three times each at a river or at home.\n"
                    "3. PINDA DAAN: Rice balls (Pinda) offered on the ground — "
                    "the physical form of nourishment for ancestors.\n"
                    "4. BRAHMIN BHOJ: A Brahmin (representing the ancestor) is fed "
                    "a full sattvic meal with all 16 traditional items.\n"
                    "5. DAAN: Gifts of cloth, food, money given to the priest.\n\n"
                    "SPECIAL KP SHRADDHA: Mahalaya Amavasya (Bhadrapada Krishna 30) — "
                    "the most important Pitru Amavasya, performed at the Vitasta (Jhelum) river ghats."
                ),
                "links": [
                    ("Wikipedia · Shraddha", "https://en.wikipedia.org/wiki/Shraddha"),
                ],
            },
            {
                "name": "Puja Vidhi (Daily Worship) · नित्यकर्म पूजा",
                "icon": "",
                "timing": "Daily — morning",
                "desc": (
                    "The KP Nityakarma (daily ritual) follows the Shaiva Agamic tradition:\n\n"
                    "1. SHUDDHI: Ritual purification — bath, clean clothes.\n"
                    "2. SANDHYAVANDANA: Prayers at the three sandhyas (dawn, noon, dusk). "
                    "The dawn Sandhya includes: Achamana, Marjana, Arghya to Sun, Gayatri Japa (108 times).\n"
                    "3. PUJA: Puja of the family deity — Shivalinga or Shalagrama. "
                    "Offerings: flowers (pushpa), incense (dhupa), lamp (dipa), water (jala), "
                    "food (naivedya), betel (tambula). "
                    "Recitation: Shiva Panchakshara stotra, Rudrashtakam, family mantras.\n"
                    "4. KUL DEVI PUJA: Brief invocation of the Kul Devi (Sharika, Ragnya, etc.) "
                    "with flowers and incense.\n"
                    "5. SHARADA STUTI: Many KP families recite the Sharada Stotram "
                    "('Ya Sharada nilotpala-dala-shyama') as a daily invocation.\n\n"
                    "The complete KP puja manual is based on the Paddhati texts of the tradition — "
                    "simplified forms are used today but the structure follows the Agamic prescription."
                ),
                "links": [
                    ("Wikipedia · Hindu Puja", "https://en.wikipedia.org/wiki/Puja_(Hinduism)"),
                ],
            },
        ],
    }

    # ── Category dropdown + search ─────────────────────────────────
    culture_cats = ["All Categories · सभी"] + list(KP_CULTURE.keys())
    cult_col1, cult_col2 = st.columns([2, 3])
    with cult_col1:
        cult_cat = st.selectbox("Category · श्रेणी", culture_cats, key="cult_cat")
    with cult_col2:
        cult_search = st.text_input("Search · खोजें", key="cult_search",
                                     placeholder="e.g. Herath, Wazwan, Santoor, Lal Ded, Pashmina…")

    # Only show content when user has picked a specific category or typed a search term
    _cult_active = cult_cat != "All Categories · सभी" or bool(cult_search)

    if not _cult_active:
        st.markdown("""
        <div style="text-align:center;padding:48px 20px;color:var(--muted)">
          <div style="font-size:36px;margin-bottom:16px;opacity:.4"></div>
          <div style="font-family:'Cinzel',serif;font-size:12px;letter-spacing:2.5px;
               color:var(--walnut-mid);margin-bottom:10px">SELECT A CATEGORY · श्रेणी चुनें</div>
          <div style="font-size:13.5px;line-height:1.8;max-width:420px;margin:0 auto">
            Choose a category from the dropdown — or type a keyword to search —
            to explore Kashmiri culture, festivals, sacred sites, music, cuisine and more.
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:12px;
               color:var(--muted);margin-top:10px;opacity:.6">
            ऊपर श्रेणी चुनें या खोज करें
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if cult_search:
            term = cult_search.lower()
            cats_to_show = {}
            for cat, items in KP_CULTURE.items():
                filtered = [it for it in items
                            if term in it["name"].lower() or term in it["desc"].lower()]
                if filtered:
                    cats_to_show[cat] = filtered
        else:
            cats_to_show = {cult_cat: KP_CULTURE[cult_cat]}

        total_cult = sum(len(v) for v in cats_to_show.values())
        if total_cult == 0:
            st.info("No results found. Try a different search term.")
        else:
            st.markdown(f'<div style="font-size:12px;color:var(--muted);margin:6px 0 14px;font-style:italic">'
                        f'Showing {total_cult} entries in {len(cats_to_show)} category/categories</div>',
                        unsafe_allow_html=True)
            for cat_name, items in cats_to_show.items():
                st.markdown(f'<div class="subsec">{cat_name}</div>', unsafe_allow_html=True)
                for item in items:
                    def _link_pill(label, url):
                        is_maps = "maps.google" in url or "google.com/maps" in url or "maps.app.goo" in url
                        is_wiki = "wikipedia.org" in url
                        if is_maps:
                            icon = "📍"
                            color = "#1A73E8"
                            border = "rgba(26,115,232,.35)"
                            bg    = "rgba(26,115,232,.06)"
                        elif is_wiki:
                            icon = "📖"
                            color = "var(--walnut-mid)"
                            border = "var(--border)"
                            bg    = "var(--cream2)"
                        else:
                            icon = "🔗"
                            color = "var(--teal)"
                            border = "rgba(42,122,106,.35)"
                            bg    = "rgba(42,122,106,.06)"
                        return (
                            f'<a href="{url}" target="_blank" style="'
                            f'display:inline-flex;align-items:center;gap:5px;'
                            f'font-family:Cinzel,serif;font-size:9px;letter-spacing:1px;'
                            f'color:{color};text-decoration:none;'
                            f'padding:5px 12px;border:1px solid {border};'
                            f'border-radius:20px;background:{bg};'
                            f'white-space:nowrap">{icon} {label}</a>'
                        )
                    links_html = " ".join(
                        _link_pill(label, url)
                        for label, url in item.get("links", [])
                    )
                    st.markdown(f"""
                    <div style="background:white;border:1px solid var(--border);border-radius:10px;
                         padding:15px 20px;margin-bottom:10px;box-shadow:0 1px 6px var(--shadow)">
                      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;flex-wrap:wrap">
                        <span style="font-size:20px">{item['icon']}</span>
                        <span style="font-family:Cinzel,serif;font-size:13px;font-weight:500;
                              color:var(--walnut)">{item['name']}</span>
                        <span style="font-size:10px;color:var(--muted);margin-left:auto;
                              font-style:italic">{item['timing']}</span>
                      </div>
                      <div style="font-size:13.5px;color:var(--ink);line-height:1.8;margin-bottom:10px">
                        {item['desc']}
                      </div>
                      <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:4px">{links_html}</div>
                    </div>
                    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 8 — KOSHURPEDIA
# ══════════════════════════════════════════════════════════════════════════════
with tabs[8]:
    st.markdown("""
    <div class="sec-head"> Koshurpedia · कोशुरपीडिया</div>
    <div class="sec-sub">
      Your wise Kashmiri Pandit — rituals, panchang, muhurats, mantras, traditions
      <span class="deva">पंचांग · अनुष्ठान · मुहूर्त · मंत्र · परंपरा · कश्मीरी संस्कृति</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ai-box">
      <div class="ai-lbl">KOSHURPEDIA · कोशुर पण्डित</div>
      <div style="margin-top:22px;text-align:center;padding:22px 0 14px">
        <div style="font-size:36px;margin-bottom:12px"></div>
        <div style="font-family:'Cinzel Decorative',serif;font-size:14px;letter-spacing:3px;
             color:#DEB85A;margin-bottom:12px">COMING IN NEXT UPDATE</div>
        <div style="font-size:14.5px;color:rgba(253,248,240,.7);line-height:2;
             max-width:520px;margin:0 auto">
          Your wise Kashmiri Pandit — deeply versed in Vedic Pañcāṅga, Kashmiri rituals,
          Herath · Navreh · Kheer Bhawani traditions, Kashmir Shaivism, Mantras,
          Kul Devī puja, saints and the Vakhs of Lalleshwari — is being prepared.
          <br><br>
          <span style="color:#DEB85A;font-family:'Cinzel',serif;font-size:12px;
                letter-spacing:1.5px">Rolling out in the next update.</span>
        </div>
        <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
             color:rgba(222,184,90,.5);margin-top:14px;line-height:1.8">
          कोशुर ज्योतिषी — पंचांग · अनुष्ठान · मंत्र · परम्परा · काश्मीर शैव दर्शन
          <br>शीघ्र ही उपलब्ध होंगे — अगले अपडेट में
        </div>
        <div style="margin-top:18px;font-size:11px;color:rgba(253,248,240,.25);
             font-family:'Cinzel',serif;letter-spacing:2px">
           &nbsp; OM NAMAH SHIVAYA &nbsp; 
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="styled-div"><span>CULTURAL HIGHLIGHTS</span></div>', unsafe_allow_html=True)
    oh1, oh2, oh3 = st.columns(3)
    oh1.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">KASHMIR SHAIVISM</div>
      <div class="ic-body">The Trika philosophy of Abhinavagupta — Pratyabhijna (recognition), 
      Spanda (vibration), and Krama. The universe as Shiva's own manifestation 
      through Shakti (Vimarsha).</div>
      <div class="ic-accent">त्रिक दर्शन · अभिनवगुप्त</div>
    </div>""", unsafe_allow_html=True)
    oh2.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">KASHMIRI RITUALS</div>
      <div class="ic-body">Herath · Navreh · Zyeth Ashtami · Kheer Bhawani Mela · 
      Pann · Shivratri Vatak Puja · Kul Devi Puja — the sacred calendar of 
      Kashmiri Pandits throughout the year.</div>
      <div class="ic-accent">कश्मीरी पण्डित परम्परा</div>
    </div>""", unsafe_allow_html=True)
    oh3.markdown("""<div class="info-card">
      <div class="ic-icon"></div>
      <div class="ic-title">SAINTS & VAKHS</div>
      <div class="ic-body">Lal Ded · Nund Rishi · Habba Khatoon · Rupa Bhawani — 
      the mystic voices of Kashmir who sang of love, liberation, and the 
      ineffable nature of Shiva.</div>
      <div class="ic-accent">वाख · मिस्टिक पोएट्री</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 7 — FEEDBACK / SUJHAV
# ══════════════════════════════════════════════════════════════════════════════
with tabs[7]:
    st.markdown("""
    <div class="sec-head">Sujhav · सुझाव</div>
    <div class="sec-sub">
      Feedback, suggestions &amp; contributions · प्रतिक्रिया, सुझाव और योगदान
      <span class="deva">आपके सुझाव इस पोर्टल को बेहतर बनाते हैं</span>
    </div>
    """, unsafe_allow_html=True)

    fb_l, fb_r = st.columns([1, 1.8])

    with fb_l:
        st.markdown(f"""
        <div style="background:white;border:1px solid var(--border);border-radius:14px;
             padding:20px 24px;box-shadow:0 2px 10px var(--shadow);margin-bottom:16px">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2px;
               color:var(--walnut-mid);margin-bottom:14px">HOW TO REACH US · कैसे संपर्क करें</div>
          <div style="display:flex;align-items:center;gap:14px;padding:12px 16px;
               background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));border-radius:10px;border:1px solid rgba(212,114,42,.2);
               margin-bottom:10px">
            <div style="font-size:22px">✉</div>
            <div>
              <div style="font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:1.5px;
                   color:var(--saffron);margin-bottom:3px">EMAIL · ईमेल</div>
              <a href="mailto:ancientkashmiri@gmail.com"
                 style="font-family:'Cinzel',serif;font-size:14px;font-weight:500;
                        color:var(--walnut);text-decoration:none;letter-spacing:1px">
                ancientkashmiri@gmail.com
              </a>
            </div>
          </div>
          <div style="display:flex;align-items:center;gap:14px;padding:12px 16px;
               background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));border-radius:10px;border:1px solid rgba(212,114,42,.2);
               margin-bottom:14px">
            <div style="font-size:22px">✉</div>
            <div>
              <div style="font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:1.5px;
                   color:var(--saffron);margin-bottom:3px">EMAIL · ईमेल</div>
              <a href="mailto:avinashbhat1401@gmail.com"
                 style="font-family:'Cinzel',serif;font-size:14px;font-weight:500;
                        color:var(--walnut);text-decoration:none;letter-spacing:1px">
                avinashbhat1401@gmail.com
              </a>
            </div>
          </div>
          <div style="font-size:12px;color:var(--muted);line-height:1.8">
            Write to us in English, Hindi or Kashmiri. We read every message.
            <br>
            <span style="font-family:'Noto Serif Devanagari',serif;font-size:12px">
              अंग्रेज़ी, हिंदी या कश्मीरी में लिखें — हम हर संदेश पढ़ते हैं।
            </span>
          </div>
        </div>

        <div style="background:linear-gradient(135deg,#3A2010,#4E2210);border-radius:14px;
             padding:28px 24px;text-align:center;box-shadow:0 4px 20px rgba(58,32,16,.3);
             border:1px solid rgba(184,134,42,.2);margin-bottom:16px">
          <div style="font-family:'Cinzel',serif;font-size:8px;letter-spacing:3px;
               color:rgba(222,184,90,.5);margin-bottom:6px">VIKRAMA SAṂVAT</div>
          <div style="font-family:'Cinzel Decorative',serif;font-size:36px;
               color:rgba(222,184,90,.9);line-height:1">{samvat_now}</div>
          <div style="font-size:11px;color:rgba(253,248,240,.4);margin-top:6px;
               margin-bottom:18px">
            {today.strftime('%A')}, {today.day} {today.strftime('%B %Y')}
          </div>
          <div style="border-top:1px solid rgba(222,184,90,.12);padding-top:16px;
               display:flex;flex-direction:column;gap:10px;text-align:left">
            <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:10px 14px">
              <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                   color:rgba(212,114,42,.7);margin-bottom:3px">AYANĀṂŚA · अयनांश</div>
              <div style="font-size:13px;color:#FDF8F0;font-weight:500">Lahiri (Chitrapaksha)</div>
              <div style="font-size:10px;color:rgba(253,248,240,.4);margin-top:1px">
                Government of India · 1955 · Rashtriya Panchang</div>
            </div>
            <div style="background:rgba(253,248,240,.06);border-radius:8px;padding:10px 14px">
              <div style="font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;
                   color:rgba(212,114,42,.7);margin-bottom:3px">MĀSA SYSTEM · मास पद्धति</div>
              <div style="font-size:13px;color:#FDF8F0;font-weight:500">Amāvasyānta</div>
              <div style="font-size:10px;color:rgba(253,248,240,.4);margin-top:1px">
                Month ends at Amāvasyā · KP tradition</div>
            </div>
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:14px;
               color:rgba(222,184,90,.4);margin-top:18px">ॐ नमः शिवाय</div>
        </div>
        """, unsafe_allow_html=True)

    with fb_r:
        st.markdown("""
        <div style="background:linear-gradient(135deg,var(--saffron-pale),var(--gold-pale));
             border:1px solid rgba(212,114,42,.2);border-radius:14px;padding:24px 28px;
             margin-bottom:18px">
          <div style="font-family:'Cinzel',serif;font-size:9px;letter-spacing:2.5px;
               color:var(--saffron);margin-bottom:8px">YOUR VOICE MATTERS · आपकी आवाज़ मायने रखती है</div>
          <div style="font-size:14px;color:var(--walnut);line-height:2;margin-bottom:14px">
            This portal is a living project — built for the Kashmiri Pandit community
            and all those connected to Kashmir's heritage. Your feedback, corrections
            and suggestions are what make it grow.
          </div>
          <div style="font-family:'Noto Serif Devanagari',serif;font-size:13px;
               color:var(--muted);line-height:1.9;margin-bottom:16px">
            यह पोर्टल एक जीवित परियोजना है — जो कश्मीरी पण्डित समुदाय के लिए
            बनाई गई है। आपकी प्रतिक्रिया और सुझाव इसे और बेहतर बनाते हैं।
          </div>
          <div style="font-size:13px;color:var(--ink);line-height:2">
            We welcome:
            <ul style="margin:8px 0 0 16px;color:var(--muted)">
              <li>Corrections to gotra or surname data</li>
              <li>Missing festivals, rituals or cultural information</li>
              <li>Panchang accuracy feedback for your region</li>
              <li>Suggestions for new features or sections</li>
              <li>Photographs, manuscripts or family records to add</li>
              <li>Stories of saints, Bhairava mandirs or Kul Devis</li>
              <li>Any knowledge that should not be lost</li>
            </ul>
          </div>
        </div>

        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="site-footer">
  ANCIENT KASHMIRI ; प्राचीन कश्मीर &nbsp;·&nbsp; PRĀCĪNA KASHMĪRA
  &nbsp;·&nbsp; VIKRAMA SAṂVAT {samvat_now} &nbsp;·&nbsp; LAHIRI AYANĀṂŚA · AMĀVASYĀNTA
</div>
""", unsafe_allow_html=True)
  # ॐ नमः शिवाय &nbsp;·&nbsp; प्राचीन कश्मीर &nbsp;·&nbsp; PRĀCĪNA KASHMĪRA
  # &nbsp;·&nbsp; VIKRAMA SAṂVAT {samvat_now} &nbsp;·&nbsp; LAHIRI AYANĀṂŚA · PŪRṆIMĀNTA
