"""
Cyberpunk Theme CSS Module

This module contains the CSS styling for the CyberNexus Streamlit application,
providing a cyberpunk visual theme.

For this DEMO, it includes a comprehensive set of CSS rules to style
various Streamlit elements.

Future enhancements:
- Create a more modular and configurable theming system (e.g., using YAML or JSON config).
- Add animations and visual effects to further enhance the cyberpunk aesthetic.
- Potentially allow users to customize theme elements (colors, fonts, etc.).
"""

import streamlit as st

def apply_theme():
    """Applies the Cyberpunk CSS theme to the Streamlit app."""
    st.markdown(
        """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');

        body {
            font-family: 'Orbitron', sans-serif;
            color: #00ffc8;
            background-color: #111111;
        }

        .stApp {
            background-color: #050505;
            background-image: url("https://i.imgur.com/530DGSL.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        .title {
            font-size: 64px;
            color: #ff00de;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #ff00de;
        }

        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            color: #00ffc8;
            background-color: #222222;
            border: 1px solid #00ffc8;
            border-radius: 5px;
            padding: 10px;
            font-family: 'Roboto Mono', monospace;
        }

        .stButton>button {
            font-family: 'Orbitron', sans-serif;
            color: #000000;
            background-color: #00ffc8;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #00b38a;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #ff6f00;
            text-shadow: 0 0 5px #ff6f00;
        }

        p, div, span, li, a {
            color: #00ffc8;
            font-family: 'Roboto Mono', monospace;
        }

        .sidebar .st-emotion-cache-r421ms {
            background-color: #1a1a1a;
            color: #00ffc8;
        }

        .st-emotion-cache-16txtl3 .stSelectbox div[data-baseweb="select"] > div {
            background-color: #222222;
            color: #00ffc8;
            border: 1px solid #00ffc8;
        }
        .st-emotion-cache-16txtl3 .stSelectbox div[data-baseweb="select"] > div:focus {
            border-color: #00b38a;
            box-shadow: 0 0 0.25rem #00b38a;
        }
        .st-emotion-cache-16txtl3 .stSelectbox div[data-baseweb="select"] > div > div {
            color: #00ffc8;
        }

        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
            overflow-wrap: break-word;
        }

        .stChatMessage.user {
            background-color: #333333;
            color: #ccff00;
        }

        .stChatMessage.assistant {
            background-color: #1a1a1a;
            color: #00ffff;
        }

        .stChatMessage .stMarkdown {
            font-family: 'Roboto Mono', monospace;
        }

    </style>
    """,
        unsafe_allow_html=True,
    )
