import streamlit as st
import os

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Cyberbros2013", layout="wide")

# --- 2. THE BACKGROUND (FORCED) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }
    h1, h2, h3 { font-weight: 900 !important; color: #00f2ff !important; }
    p, li { color: #e6edf3 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("CYBERBROS2013 TECH")

# --- 3. THE IMAGE CHECK (This prevents the crash in your log) ---
st.header("Project Gallery")
col1, col2 = st.columns(2)

with col1:
    if os.path.exists("images/download.jpeg"):
        # The log asked to use width="stretch" instead of use_container_width
        st.image("images/download.jpeg", caption="Robotics Lab", width="stretch")
    else:
        st.warning("Found the code, but images/download.jpeg is missing from GitHub!")

with col2:
    if os.path.exists("images/images.jpeg"):
        st.image("images/images.jpeg", caption="Software Tutorials", width="stretch")
    else:
        st.warning("images/images.jpeg not found.")
