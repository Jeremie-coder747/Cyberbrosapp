import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import os

# --- 1. PAGE CONFIG (Must be first) ---
st.set_page_config(page_title="Cyberbros2013 Tech", page_icon="🤖", layout="wide")

# --- 2. FORCE THE CYBER GRADIENT (Replaces config.toml) ---
st.markdown("""
    <style>
    /* Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }
    
    /* Make headers Bold and Cyan */
    h1, h2, h3 {
        font-weight: 900 !important;
        color: #00f2ff !important;
        text-transform: uppercase;
        text-shadow: 2px 2px 10px rgba(0,242,255,0.2);
    }

    /* Clean text colors */
    p, li, span, label {
        color: #e6edf3 !important;
        font-weight: 500;
    }

    /* Hide default Streamlit clutter */
    header {background: transparent !important;}
    footer {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. ASSET LOADERS ---
def load_lottie(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

lottie_robot = load_lottie("robot.json")

# --- 4. NAVIGATION ---
selected = option_menu(
    menu_title=None, 
    options=["Home", "News", "YouTube", "Contact"], 
    icons=["house", "newspaper", "play-btn", "envelope"], 
    orientation="horizontal",
    styles={
        "container": {"background-color": "#161b22", "border": "1px solid #00f2ff"},
        "nav-link-selected": {"background-color": "#00f2ff", "color": "#0a0b10"},
    }
)

# --- 5. PAGE CONTENT ---

if selected == "Home":
    st.title("ROBOTIC PROJECTS & TUTORIALS")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.header("Innovation in Motion")
        st.write("Welcome to Cyberbros2013. We build the future with Python, Linux, and Robotics.")
        st.write("[Visit YouTube Channel >](https://www.youtube.com/@cyberbros2013)")
    with col_r:
        if lottie_robot:
            st_lottie(lottie_robot, height=300)

    st.write("---")
    st.header("Project Gallery")
    c1, c2 = st.columns(2)

    # IMAGE 1: THE "NO-CRASH" CHECK
    with c1:
        img_path1 = "images/download.jpeg"
        if os.path.exists(img_path1):
            st.image(img_path1, caption="Robotics Lab", use_container_width=True)
        else:
            st.warning(f"⚠️ {img_path1} missing on GitHub. Site stays online!")

    # IMAGE 2: THE "NO-CRASH" CHECK
    with c2:
        img_path2 = "images/images.jpeg"
        if os.path.exists(img_path2):
            st.image(img_path2, caption="Software Tutorials", use_container_width=True)
        else:
            st.warning(f"⚠️ {img_path2} missing on GitHub. Site stays online!")

elif selected == "News":
    st.header("LATEST UPDATES 📰")
    st.info("🚀 **Project Rover:** Chassis assembly is complete. Testing now in Sharjah.")
    st.success("💻 **Ubuntu 25.04:** New macOS-style 'ricing' guide coming soon!")

elif selected == "YouTube":
    st.header("OUR VIDEOS 📺")
    # Replace the link with your actual video
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

elif selected == "Contact":
    st.header("GET IN TOUCH 📩")
    st.write("Connect with Jeremie for collaborations!")
    contact_form = """
    <form action="https://formsubmit.co/your-email@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width:100%; margin-bottom:10px;">
        <input type="email" name="email" placeholder="Your Email" required style="width:100%; margin-bottom:10px;">
        <textarea name="message" placeholder="Message" style="width:100%; height:100px;"></textarea>
        <button type="submit" style="background:#00f2ff; color:#0a0b10; border:none; padding:10px 20px; font-weight:bold; cursor:pointer;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
