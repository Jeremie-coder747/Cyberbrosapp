import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cyberbros2013 Tech site", page_icon="🤖", layout="wide")

# --- CUSTOM CSS FOR GRADIENT & BOLD TEXT ---
st.markdown("""
    <style>
    .stApp, .stMain, .stHeader, .stAppViewContainer, .stMainBlockContainer {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }
    h1, h2, h3 {
        font-weight: 900 !important;
        font-family: 'Inter', sans-serif;
        color: #00f2ff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    p, li, span {
        font-weight: 500;
        color: #e6edf3 !important;
    }
    header {background: transparent !important;}
    footer {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# --- LOAD LOTTIE ASSETS ---
def load_lottiefile(filepath: str):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except:
            return None
    return None

file_path = os.path.join(os.path.dirname(__file__), "robot.json")
lottie_robot = load_lottiefile(file_path)

# --- NAVIGATION BAR ---
selected = option_menu(
    menu_title=None, 
    options=["Home", "News", "YouTube", "Contact"], # Added YouTube tab
    icons=["house", "newspaper", "play-btn", "envelope"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#161b22"},
        "icon": {"color": "#00f2ff", "font-size": "20px"}, 
        "nav-link": {"font-size": "18px", "font-weight": "bold", "text-align": "center", "margin":"0px", "--hover-color": "#262730"},
        "nav-link-selected": {"background-color": "#00f2ff", "color": "#0a0b10"},
    }
)

# --- PAGE LOGIC ---
if selected == "Home":
    st.subheader("Cyberbros2013 Tech site 🤖")
    st.title("ROBOTIC PROJECTS & TUTORIALS")
    
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What we do")
        st.write("Cyberbros2013 is a robotics-focused platform. We design, build, and innovate.")
    with right_col:
        if lottie_robot:
            st_lottie(lottie_robot, height=300, key="robot")

    # --- SAFETY IMAGE GALLERY ---
    st.write("---")
    st.header("Project Gallery")
    img_col1, img_col2 = st.columns(2)
    
    with img_col1:
        if os.path.exists("images/download.jpeg"):
            st.image("images/download.jpeg", caption="Robotics Lab")
        else:
            st.warning("Image 'images/download.jpeg' not found on GitHub.")

    with img_col2:
        if os.path.exists("images/images.jpeg"):
            st.image("images/images.jpeg", caption="Software Tutorials")
        else:
            st.warning("Image 'images/images.jpeg' not found on GitHub.")

elif selected == "YouTube":
    st.header("Our Latest Tutorials 📺")
    st.write("---")
    # Replace with your actual video URL
    st.video("https://www.youtube.com/watch?v=your_video_id")
    st.write("Subscribe to Cyberbros2013 for more robotic content!")

elif selected == "News":
    st.header("Latest News & Updates 📰")
    st.write("Check back here for rover launch updates!")

elif selected == "Contact":
    st.header("Get In Touch! 📩")
    # Contact form code here...
