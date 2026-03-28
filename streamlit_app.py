import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import os

# --- 1. PAGE CONFIG (Must be the very first command) ---
st.set_page_config(page_title="Cyberbros2013 Tech", page_icon="🤖", layout="wide")

# --- 2. ATOMIC CSS: FORCE GRADIENT & BOLD TEXT ---
st.markdown("""
    <style>
    /* Force the background gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }

    /* Transparent containers so the gradient shines through */
    .stMain, .stHeader, .stAppViewContainer, .stMainBlockContainer {
        background-color: transparent !important;
    }

    /* Extra Bold Cyber-Cyan Headers */
    h1, h2, h3 {
        font-weight: 900 !important;
        font-family: 'Inter', sans-serif;
        color: #00f2ff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    /* Soft white text for readability */
    p, li, span, label {
        font-weight: 500;
        color: #e6edf3 !important;
    }

    /* UI Cleanup */
    header {background: transparent !important;}
    footer {display: none !important;}
    
    /* Input styling for Contact Form */
    input, textarea {
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #00f2ff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ASSET LOADERS ---
def load_lottie(path):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception:
            return None
    return None

lottie_robot = load_lottie("robot.json")

# --- 4. NAVIGATION BAR ---
selected = option_menu(
    menu_title=None, 
    options=["Home", "News", "YouTube", "Contact"], 
    icons=["house", "newspaper", "play-btn", "envelope"], 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#161b22", "border": "1px solid #00f2ff"},
        "icon": {"color": "#00f2ff", "font-size": "20px"}, 
        "nav-link": {"font-size": "18px", "font-weight": "bold", "text-align": "center", "color": "#e6edf3"},
        "nav-link-selected": {"background-color": "#00f2ff", "color": "#0a0b10"},
    }
)

# --- 5. PAGE LOGIC ---

if selected == "Home":
    st.title("ROBOTIC PROJECTS & TUTORIALS")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.header("Innovation in Motion")
        st.write("Welcome to Cyberbros2013. We build the future with Python and Robotics.")
        st.write("[Visit Youtube Channel >](https://www.youtube.com/@cyberbros2013)")

    with col_r:
        if lottie_robot:
            st_lottie(lottie_robot, height=300, key="robot_anim")
        else:
            st.info("Robot animation placeholder (Check robot.json on GitHub)")

    st.write("---")
    st.header("Project Gallery")
    c1, c2 = st.columns(2)
    
    # Image 1 Check
    with c1:
        if os.path.exists("images/download.jpeg"):
            st.image("images/download.jpeg", caption="Robotics Lab", width=None) # width=None lets it be responsive
        else:
            st.warning("⚠️ images/download.jpeg not found.")

    # Image 2 Check
    with c2:
        if os.path.exists("images/images.jpeg"):
            st.image("images/images.jpeg", caption="Software Tutorials", width=None)
        else:
            st.warning("⚠️ images/images.jpeg not found.")

elif selected == "News":
    st.header("LATEST UPDATES 📰")
    st.info("🚀 **Project Rover:** The chassis is ready for testing in Sharjah!")
    st.success("✅ **Ubuntu Ricing:** New macOS-theme guide for HP EliteBook is coming.")

elif selected == "YouTube":
    st.header("OUR VIDEOS 📺")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with your link
    st.write("### Newest Upload: Robotics 101")

elif selected == "Contact":
    st.header("GET IN TOUCH 📩")
    contact_form = """
    <form action="https://formsubmit.co/your-email@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-top: 10px;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-top: 10px;">
        <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-top: 10px; height: 100px;"></textarea>
        <button type="submit" style="background-color: #00f2ff; color: #0a0b10; padding: 10px 20px; border: none; margin-top: 10px; font-weight: bold; cursor: pointer;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
