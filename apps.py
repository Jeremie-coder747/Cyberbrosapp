import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import os

# --- 1. PAGE CONFIG (Must be the very first Streamlit command) ---
st.set_page_config(page_title="Cyberbros2013 Tech site", page_icon="🤖", layout="wide")

# --- 2. ATOMIC CSS: FORCE GRADIENT & BOLD TEXT ---
# This overrides Streamlit's default theme directly from the code.
st.markdown("""
    <style>
    /* Force the background gradient on the entire app */
    .stApp {
        background: linear-gradient(135deg, #0a0b10 0%, #1a0b2e 50%, #001a2e 100%) !important;
        background-attachment: fixed !important;
    }

    /* Make the main containers transparent so the gradient shows through */
    .stMain, .stAppViewContainer, .stHeader, .stMainBlockContainer {
        background-color: transparent !important;
    }

    /* Extra Bold Cyber-Cyan Headers */
    h1, h2, h3 {
        font-weight: 900 !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        color: #00f2ff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    /* Clean white/grey text for readability */
    p, li, span, label {
        font-weight: 500;
        color: #e6edf3 !important;
    }

    /* Clean up UI elements */
    header {background: transparent !important;}
    footer {display: none !important;}
    
    /* Custom Styling for the Contact Form inputs */
    input, textarea {
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #00f2ff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD ASSETS WITH SAFETY CHECKS ---
def load_lottiefile(filepath: str):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except Exception:
            return None
    return None

lottie_robot = load_lottiefile("robot.json")

# --- 4. NAVIGATION BAR ---
selected = option_menu(
    menu_title=None, 
    options=["Home", "News", "YouTube", "Contact"], 
    icons=["house", "newspaper", "play-btn", "envelope"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#161b22"},
        "icon": {"color": "#00f2ff", "font-size": "20px"}, 
        "nav-link": {"font-size": "18px", "font-weight": "bold", "text-align": "center", "color": "#e6edf3"},
        "nav-link-selected": {"background-color": "#00f2ff", "color": "#0a0b10"},
    }
)

# --- 5. PAGE LOGIC ---

# HOME PAGE
if selected == "Home":
    st.subheader("Cyberbros2013 Tech site 🤖")
    st.title("ROBOTIC PROJECTS & TUTORIALS")
    st.write("Welcome! We share our builds and code to help you innovate.")

    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write(
            """
            Cyberbros2013 is a robotics-focused platform. We:
            - **Design** and build real-world robotic systems.
            - **Explore** Python and Arduino programming.
            - **Create** tutorials for the next generation of engineers.
            """
        )
        st.write("[Visit Youtube Channel >](https://www.youtube.com/@cyberbros2013)")

    with right_column:
        if lottie_robot:
            st_lottie(lottie_robot, height=350, key="robot")
        else:
            st.info("Robot animation loading... (Check if robot.json is on GitHub)")

    # PROJECT GALLERY WITH CRASH PROTECTION
    st.write("---")
    st.header("Project Gallery")
    col1, col2 = st.columns(2)
    
    with col1:
        if os.path.exists("images/download.jpeg"):
            st.image("images/download.jpeg", caption="Robotics Lab", use_container_width=True)
        else:
            st.error("Missing file: images/download.jpeg")

    with col2:
        if os.path.exists("images/images.jpeg"):
            st.image("images/images.jpeg", caption="Software Tutorials", use_container_width=True)
        else:
            st.error("Missing file: images/images.jpeg")

# NEWS PAGE
elif selected == "News":
    st.header("LATEST UPDATES 📰")
    st.write("---")
    st.info("🚀 **Project Rover:** The chassis assembly is complete. Software integration starting soon!")
    st.success("✅ **YouTube Update:** Our latest Ubuntu customization guide is now live.")

# YOUTUBE PAGE
elif selected == "YouTube":
    st.header("OUR VIDEOS 📺")
    st.write("---")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with your link
    st.write("### Featured Tutorial: Setting up your environment")

# CONTACT PAGE
elif selected == "Contact":
    st.header("GET IN TOUCH 📩")
    st.write("---")
    
    # Simple HTML Contact Form
    contact_form = """
    <form action="https://formsubmit.co/your-email@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px;">
        <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; height: 150px;"></textarea>
        <button type="submit" style="background-color: #00f2ff; color: #0a0b10; padding: 10px 20px; border: none; border-radius: 5px; margin-top: 10px; font-weight: bold;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
