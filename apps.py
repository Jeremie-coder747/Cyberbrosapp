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
    /* 1. FORCE THE GRADIENT ON EVERY LAYER */
    .stApp, .stMain, .stHeader, .stAppViewContainer, .stMainBlockContainer {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }

    /* 2. MAKE ALL HEADERS EXTRA BOLD & CYAN */
    h1, h2, h3 {
        font-weight: 900 !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        color: #00f2ff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 3. CLEAN UP THE TEXT */
    p, li, span {
        font-weight: 500;
        color: #e6edf3 !important;
    }

    /* 4. HIDE THE STREAMLIT TOP BAR SHADOW */
    header {background: transparent !important;}
    footer {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# --- LOAD LOTTIE ASSETS ---
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return None

file_path = os.path.join(os.path.dirname(__file__), "robot.json")
lottie_robot = load_lottiefile(file_path)

# --- 1. NAVIGATION BAR ---
selected = option_menu(
    menu_title=None, 
    options=["Home", "News", "Contact"], 
    icons=["house", "newspaper", "envelope"], 
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

# --- 2. PAGE LOGIC ---
if selected == "Home":
    st.subheader("Cyberbros2013 Tech site 🤖")
    st.title("ROBOTIC PROJECTS & TUTORIALS")
    st.write("Welcome! Here we share our builds, code, and documents to help you innovate.")

    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write(
            """
            Cyberbros2013 is a robotics-focused platform. We:
            - **Design** and build real-world robotic systems.
            - **Explore** Python and Arduino programming.
            - **Create** tutorials to inspire new engineers.
            """
        )
        st.write("[Visit Youtube Channel >](https://www.youtube.com/@cyberbros2013)")

    with right_column:
        if lottie_robot:
            st_lottie(lottie_robot, height=350, key="robot")

    st.write("---")
    st.header("Project Gallery")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/download.jpeg", caption="Robotics Lab", use_container_width=True)
    with col2:
        st.image("images/images.jpeg", caption="Software Tutorials", use_container_width=True)

elif selected == "News":
    st.header("Latest News & Updates 📰")
    st.write("---")
    col_news1, col_news2 = st.columns(2)
    with col_news1:
        st.subheader("🚀 New Robot Build")
        st.write("We just finished the prototype for our new autonomous rover.")
        st.caption("Posted: March 2026")
    with col_news2:
        st.subheader("📺 YouTube Milestone")
        st.write("Check out our latest tutorial on Ubuntu system customization.")
        st.caption("Posted: February 2026")

elif selected == "Contact":
    st.header("Get In Touch! 📩")
    st.write("---")
    contact_form = f"""
    <form action="https://formsubmit.co/your-email@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 12px; margin-bottom: 12px; border-radius: 8px; border: none; background: #161b22; color: white;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 12px; margin-bottom: 12px; border-radius: 8px; border: none; background: #161b22; color: white;">
        <textarea name="message" placeholder="Your message here..." required style="width: 100%; padding: 12px; margin-bottom: 12px; border-radius: 8px; border: none; background: #161b22; color: white;"></textarea>
        <button type="submit" style="background-color: #00f2ff; color: #0a0b10; padding: 12px 24px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
