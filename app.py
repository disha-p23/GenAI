#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from streamlit_option_menu import option_menu
from main import run_pipeline

import tempfile
import pandas as pd


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Emotion AI Narrator",
    page_icon="🎙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,300;1,600&family=Syne:wght@400;700;800&family=IBM+Plex+Mono:wght@300;400&display=swap');

/* ── ROOT TOKENS ── */
:root {
    --ink:       #0a0a0e;
    --surface:   #111118;
    --raised:    #181820;
    --border:    #2a2a38;
    --border-hi: #3d3d55;
    --gold:      #c8973a;
    --gold-hi:   #e8b85a;
    --gold-dim:  #7a5520;
    --muted:     #6a6a84;
    --text:      #dddae8;
    --text-dim:  #9a97b0;
    --joy:       #e8a83a;
    --sadness:   #4a8fc8;
    --fear:      #8a58c8;
    --anger:     #c84848;
    --love:      #c85888;
    --neutral:   #5a5a78;
}

/* ── GLOBAL RESET ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif !important;
    color: var(--text) !important;
}

.stApp {
    background: var(--ink) !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 10% 0%, #1a0f2e44 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 90% 100%, #1a120522 0%, transparent 55%),
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 59px,
            #ffffff03 60px
        ),
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 59px,
            #ffffff03 60px
        ) !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"]::before {
    content: '';
    display: block;
    height: 3px;
    background: linear-gradient(90deg, var(--gold-dim), var(--gold), var(--gold-dim));
    margin-bottom: 2rem;
}

/* sidebar nav labels */
[data-testid="stSidebar"] .nav-link {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
}

[data-testid="stSidebar"] .nav-link:hover,
[data-testid="stSidebar"] .nav-link-selected {
    background: #1e1e2e !important;
    color: var(--gold) !important;
}

[data-testid="stSidebar"] .nav-link-selected {
    border-left: 2px solid var(--gold) !important;
}

/* ── TITLES ── */
.big-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(42px, 7vw, 72px) !important;
    font-weight: 300 !important;
    color: var(--text) !important;
    text-align: center !important;
    letter-spacing: -0.01em !important;
    line-height: 1.05 !important;
    margin: 0 0 0.5rem !important;
    padding-top: 1.5rem !important;
}

.big-title em {
    font-style: italic !important;
    color: var(--gold) !important;
}

.subtitle {
    text-align: center !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    margin-bottom: 3rem !important;
}

/* ── SECTION HEADERS (st.subheader / st.header) ── */
h2, h3 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: var(--text-dim) !important;
    border-bottom: 1px solid var(--border) !important;
    padding-bottom: 8px !important;
    margin-bottom: 1rem !important;
}

h2::before, h3::before {
    content: '— ';
    color: var(--gold-dim);
}

/* ── CARDS ── */
.card {
    background: var(--raised) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 1.75rem !important;
    margin-bottom: 1.25rem !important;
    position: relative !important;
    overflow: hidden !important;
    transition: border-color 0.3s !important;
}

.card:hover {
    border-color: var(--border-hi) !important;
}

.card::before {
    content: '' !important;
    position: absolute !important;
    top: 0; left: 0; right: 0 !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, var(--gold-dim), transparent) !important;
}

/* ── BODY TEXT ── */
p, li, .stMarkdown p {
    font-family: 'Syne', sans-serif !important;
    font-size: 14px !important;
    font-weight: 400 !important;
    color: var(--text-dim) !important;
    line-height: 1.75 !important;
}

/* ── BUTTONS ── */
.stButton > button {
    width: 100% !important;
    border-radius: 10px !important;
    height: 52px !important;
    background: transparent !important;
    border: 1px solid var(--gold-dim) !important;
    color: var(--gold) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    letter-spacing: 0.16em !important;
    text-transform: uppercase !important;
    transition: all 0.2s ease !important;
    position: relative !important;
    overflow: hidden !important;
}

.stButton > button::before {
    content: '' !important;
    position: absolute !important;
    inset: 0 !important;
    background: linear-gradient(90deg, transparent, #c8973a15, transparent) !important;
    transform: translateX(-100%) !important;
    transition: transform 0.4s ease !important;
}

.stButton > button:hover::before {
    transform: translateX(100%) !important;
}

.stButton > button:hover {
    background: #c8973a12 !important;
    border-color: var(--gold) !important;
    color: var(--gold-hi) !important;
    box-shadow: 0 0 24px #c8973a20 !important;
}

.stButton > button:active {
    transform: scale(0.98) !important;
}

/* download button variant */
.stDownloadButton > button {
    background: var(--gold-dim) !important;
    border: none !important;
    color: #fff !important;
    border-radius: 8px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
}

.stDownloadButton > button:hover {
    background: var(--gold) !important;
}

/* ── INPUTS ── */
.stTextArea textarea,
.stTextInput input {
    background: var(--ink) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 13px !important;
    line-height: 1.7 !important;
    padding: 14px !important;
    transition: border-color 0.2s !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: var(--gold-dim) !important;
    box-shadow: 0 0 0 2px #c8973a18 !important;
}

.stTextArea textarea::placeholder {
    color: var(--muted) !important;
    font-style: italic !important;
}

/* ── FILE UPLOADER ── */
[data-testid="stFileUploader"] {
    background: var(--ink) !important;
    border: 1.5px dashed var(--border-hi) !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
    text-align: center !important;
    transition: border-color 0.2s, background 0.2s !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: var(--gold-dim) !important;
    background: #c8973a06 !important;
}

[data-testid="stFileUploader"] label {
    color: var(--muted) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.08em !important;
}

/* ── SELECTBOX ── */
.stSelectbox [data-baseweb="select"] {
    background: var(--ink) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}

.stSelectbox [data-baseweb="select"] > div {
    background: var(--ink) !important;
    color: var(--text) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
}

/* ── SLIDER ── */
.stSlider [data-baseweb="slider"] {
    padding: 0.5rem 0 !important;
}

.stSlider [data-testid="stThumbValue"] {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 11px !important;
    color: var(--gold) !important;
    background: var(--raised) !important;
    border: 1px solid var(--gold-dim) !important;
    border-radius: 4px !important;
    padding: 2px 6px !important;
}

/* slider track */
[data-testid="stSlider"] div[role="slider"] {
    background: var(--gold) !important;
    border: 2px solid var(--gold-hi) !important;
    box-shadow: 0 0 8px #c8973a50 !important;
}

/* ── METRICS ── */
[data-testid="metric-container"] {
    background: var(--raised) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 1.25rem 1.5rem !important;
    transition: border-color 0.2s !important;
}

[data-testid="metric-container"]:hover {
    border-color: var(--gold-dim) !important;
}

[data-testid="metric-container"] label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 36px !important;
    font-weight: 600 !important;
    color: var(--gold) !important;
    line-height: 1.1 !important;
}

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    background: var(--raised) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

[data-testid="stDataFrame"] th {
    background: var(--surface) !important;
    color: var(--muted) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid var(--border) !important;
    padding: 10px 14px !important;
}

[data-testid="stDataFrame"] td {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    color: var(--text-dim) !important;
    border-bottom: 1px solid #1a1a28 !important;
    padding: 9px 14px !important;
}

/* ── BAR CHART ── */
[data-testid="stArrowVegaLiteChart"] canvas,
[data-testid="stVegaLiteChart"] {
    border-radius: 10px !important;
}

/* ── ALERTS / WARNING / SUCCESS ── */
.stAlert {
    background: var(--raised) !important;
    border-radius: 10px !important;
    border: 1px solid var(--border) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
}

[data-testid="stAlert"][data-type="warning"] {
    border-color: #6a4a18 !important;
}

[data-testid="stAlert"][data-type="success"] {
    border-color: #1a4a2a !important;
}

/* ── SPINNER ── */
.stSpinner > div {
    border-top-color: var(--gold) !important;
}

/* ── AUDIO PLAYER ── */
audio {
    width: 100% !important;
    border-radius: 8px !important;
    filter: invert(1) hue-rotate(180deg) !important;
    opacity: 0.85 !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--ink); }
::-webkit-scrollbar-thumb { background: var(--border-hi); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold-dim); }

/* ── OPTION MENU OVERRIDE ── */
#MainMenu, footer, header { visibility: hidden !important; }

/* top gold rule */
.block-container {
    padding-top: 1rem !important;
}

.block-container::before {
    content: '';
    display: block;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold-dim) 30%, var(--gold) 50%, var(--gold-dim) 70%, transparent);
    margin-bottom: 1.5rem;
}

/* ── HOME PAGE FEATURE ITEMS ── */
.stMarkdown ul {
    list-style: none !important;
    padding-left: 0 !important;
}

.stMarkdown ul li {
    padding: 5px 0 5px 1.4rem !important;
    position: relative !important;
    font-size: 14px !important;
    color: var(--text-dim) !important;
    border-bottom: 1px solid #1a1a28 !important;
}

.stMarkdown ul li:last-child {
    border-bottom: none !important;
}

.stMarkdown ul li::before {
    content: '›' !important;
    position: absolute !important;
    left: 0 !important;
    color: var(--gold) !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    line-height: 1.6 !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Emotion Analysis",
            "Narration"
        ],
        icons=[
            "house",
            "emoji-smile",
            "music-note-beamed"
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "0",
                "background-color": "transparent"
            },
            "menu-title": {
                "font-family": "'IBM Plex Mono', monospace",
                "font-size": "10px",
                "letter-spacing": "0.2em",
                "text-transform": "uppercase",
                "color": "#4a4a62",
                "padding": "0 0 1rem 0",
                "border-bottom": "1px solid #2a2a38",
                "margin-bottom": "0.5rem"
            },
            "nav-link": {
                "font-family": "'IBM Plex Mono', monospace",
                "font-size": "12px",
                "letter-spacing": "0.08em",
                "text-transform": "uppercase",
                "color": "#6a6a84",
                "padding": "10px 14px",
                "border-radius": "8px",
                "margin-bottom": "4px"
            },
            "nav-link-selected": {
                "background-color": "#1e1e2e",
                "color": "#c8973a",
                "border-left": "2px solid #c8973a",
                "font-weight": "700"
            },
            "icon": {
                "color": "#c8973a",
                "font-size": "14px"
            }
        }
    )

# =====================================================
# HOME PAGE
# =====================================================

if selected == "Home":

    st.markdown(
        "<div class='big-title'>Emotion-Aware<br><em>AI Narration</em></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>&#9656;&ensp;Emotionally adaptive storytelling &amp; voice synthesis&ensp;&#9656;</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("What This Project Does")

        st.write("""
        This AI system analyzes emotional context in text and generates expressive narration dynamically.

        The pipeline:
        - Reads PDF / DOCX / TXT files
        - Detects sentence-level emotions
        - Generates emotional voice profiles
        - Produces adaptive audiobook-style output
        """)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Supported Formats")

        st.write("""
        - PDF Documents
        - DOCX Files
        - TXT Files
        - Manual Text Input
        """)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# EMOTION ANALYSIS PAGE
# =====================================================

elif selected == "Emotion Analysis":

    st.markdown(
        "<div class='big-title'>Emotion<br><em>Analysis</em></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>&#9656;&ensp;Analyze emotional flow across narration&ensp;&#9656;</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Upload Document")

        uploaded_file = st.file_uploader(
            "Upload PDF / DOCX / TXT",
            type=["pdf", "docx", "txt"]
        )

        text_input = st.text_area(
            "OR Paste Your Text Here",
            height=250,
            placeholder="Enter your story or narration text..."
        )

        analyze = st.button(
            "⟶  Run Emotion Analysis"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Settings")

        voice_style = st.selectbox(
            "Voice Style",
            [
                "Neutral",
                "Emotional",
                "Dramatic"
            ]
        )

        narration_speed = st.slider(
            "Narration Speed",
            0.5,
            2.0,
            1.0
        )

        st.markdown("</div>", unsafe_allow_html=True)

    if analyze:

        if uploaded_file is None and not text_input.strip():

            st.warning(
                "Please upload a file or paste text."
            )

        else:

            with st.spinner(
                "Processing Emotion AI Pipeline..."
            ):

                if text_input.strip():

                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=".txt",
                        mode="w",
                        encoding="utf-8"
                    ) as tmp_file:

                        tmp_file.write(text_input)

                        temp_path = tmp_file.name

                else:

                    suffix = uploaded_file.name.split(".")[-1]

                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=f".{suffix}"
                    ) as tmp_file:

                        tmp_file.write(
                            uploaded_file.read()
                        )

                        temp_path = tmp_file.name

                result = run_pipeline(temp_path)

                st.session_state["result"] = result

                states = result["states"]

                emotion_df = pd.DataFrame({

                    "Sentence": [
                        state["text"]
                        for state in states
                    ],

                    "Emotion": [
                        state["emotion"]
                        for state in states
                    ],

                    "Intensity": [
                        state["intensity"]
                        for state in states
                    ],

                    "Voice Style": [
                        state["voice"]["style"]
                        for state in states
                    ]
                })

                emotions = emotion_df[
                    "Emotion"
                ].tolist()

                dominant_emotion = max(
                    set(emotions),
                    key=emotions.count
                )

                st.markdown("## Emotion Results")

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Dominant Emotion",
                    dominant_emotion
                )

                c2.metric(
                    "Total Sentences",
                    len(states)
                )

                c3.metric(
                    "Emotion Types",
                    len(set(emotions))
                )

                st.subheader("Emotion Distribution")

                st.bar_chart(emotion_df["Emotion"].value_counts())

                st.subheader("Sentence Emotion Analysis")

                st.dataframe(
                    emotion_df,
                    use_container_width=True
                )

# =====================================================
# NARRATION PAGE
# =====================================================

elif selected == "Narration":

    st.markdown(
        "<div class='big-title'>AI<br><em>Narration</em></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>&#9656;&ensp;Generated emotional narration output&ensp;&#9656;</div>",
        unsafe_allow_html=True
    )

    if "result" not in st.session_state:

        st.warning(
            "Please run Emotion Analysis first."
        )

    else:

        result = st.session_state["result"]

        final_audio = result["final_audio"]

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Generated Narration")

        st.audio(final_audio)

        with open(
            final_audio,
            "rb"
        ) as audio_file:

            st.download_button(
                label="⬇  Download Narration",
                data=audio_file,
                file_name="final_narration.mp3",
                mime="audio/mp3"
            )

        st.success(
            "Narration generated successfully."
        )

        st.markdown("</div>", unsafe_allow_html=True)

