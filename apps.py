import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import os

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Cyberbros2013", page_icon="🤖", layout="wide")

# --- 2. THE BACKGROUND & STYLE (REPLACES CONFIG.TOML) ---
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }
    
    /* Transparent Containers */
    .stMain, .stHeader, .stAppViewContainer, .stMainBlockContainer {
        background-color: transparent !important;
    }

    /* Bold Electric Headers */
    h1, h2, h3 {
        font-weight: 900 !important;
        color: #00f2ff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    /* Text Color */
    p, li, span, label {
        font-weight: 500;
        color: #e6edf3 !important;
    }

    /* Hide Streamlit elements */
    header {background: transparent !important;}
    footer {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. ASSET LOADING ---
def load_lottie(path):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return None
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
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.header("Innovation in Motion")
        st.write("Cyberbros2013 is building the future. From Ubuntu ricing to autonomous robotics, we explore it all.")
        st.write("[Visit Youtube Channel >](https://www.youtube.com/@cyberbros2013)")
    
    with col_right:
        if lottie_robot:
            st_lottie(lottie_robot, height=300)

    st.write("---")
    st.header("Project Gallery")
    c1, c2 = st.columns(2)
    
    # --- IMAGE 1 WITH CRASH PROTECTION ---
    with c1:
        img1 = "images/download.jpeg"
        if os.path.exists(img1):
            st.image(img1, caption="Robotics Lab", use_container_width=True)
        else:
            st.error(f"⚠️ {img1} not found on GitHub. Check folder/name!")

    # --- IMAGE 2 WITH CRASH PROTECTION ---
    with c2:
        img2 = "images/images.jpeg"
        if os.path.exists(img2):
            st.image(img2, caption="Software Tutorials", use_container_width=True)
        else:
            st.error(f"⚠️ {img2} not found on GitHub. Check folder/name!")

elif selected == "News":
    st.header("LATEST UPDATES 📰")
    st.info("🚀 **Project Rover:** Chassis assembly is complete. Testing now in Sharjah.")
    st.success("💻 **Ubuntu Ricing:** New macOS-style transformation guide coming soon.")

elif selected == "YouTube":
    st.header("CYBERBROS2013 VIDEOS 📺")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Rickroll for now, replace later!

elif selected == "Contact":
    st.header("GET IN TOUCH 📩")
    st.write("Connect with Jeremie for collaborations!")
    contact_form = """
    <form action="https://formsubmit.co/your-email@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width:100%; margin-bottom:10px; background:#161b22; color:white; border:1px solid #00f2ff;">
        <input type="email" name="email" placeholder="Your Email" required style="width:100%; margin-bottom:10px; background:#161b22; color:white; border:1px solid #00f2ff;">
        <textarea name="message" placeholder="Message" style="width:100%; height:100px; background:#161b22; color:white; border:1px solid #00f2ff;"></textarea>
        <button type="submit" style="background:#00f2ff; color:#0a0b10; border:none; padding:10px 20px; font-weight:bold; cursor:pointer;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
