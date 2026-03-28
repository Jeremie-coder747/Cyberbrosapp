import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cyberbros2013 Tech site", page_icon="🤖", layout="wide")


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
        "container": {"padding": "0!important", "background-color": "#262730"},
        "icon": {"color": "#00acee", "font-size": "20px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#333"},
        "nav-link-selected": {"background-color": "#00acee"},
    }
)

# --- 2. PAGE LOGIC ---

if selected == "Home":
    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Cyberbros2013 Tech site 🤖")
        st.title("Robotic Projects and Tutorials for the Future")
        st.write("Welcome! Here we share our builds, code, and documents to help you innovate.")

    # ---- ABOUT & ANIMATION ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What we do")
            st.write("##")
            st.write(
                """
                Cyberbros2013 is a robotics-focused platform. We:
                - Design and build real-world robotic systems.
                - Explore Python and Arduino programming.
                - Create tutorials to inspire new engineers.
                """
            )
            st.write("[Visit Youtube Channel >](https://www.youtube.com/@cyberbros2013)")

        with right_column:
            if lottie_robot:
                st_lottie(lottie_robot, height=300, key="robot")
            else:
                st.write("🤖 (Robot Animation Loading...)")

    # ---- PROJECT GALLERY ----
    st.write("---")
    st.header("Project Gallery")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/download.jpeg", caption="Robotics Lab", use_container_width=True)
    with col2:
        st.image("images/images.jpeg", caption="Software Tutorials", use_container_width=True)

elif selected == "News":
    with st.container():
        st.header("Latest News & Updates 📰")
        st.write("---")

        col_news1, col_news2 = st.columns(2)
        with col_news1:
            st.subheader("🚀 New Robot Build")
            st.write("We just finished the prototype for our new autonomous rover. Stay tuned for the reveal!")
            st.caption("Posted: March 2026")

        with col_news2:
            st.subheader("📺 YouTube Milestone")
            st.write("Check out our latest tutorial on Ubuntu system customization for developers.")
            st.caption("Posted: February 2026")

elif selected == "Contact":
    with st.container():
        st.header("Get In Touch! 📩")
        st.write("---")
        st.write("Have a question about a project? Send us a message below!")

        # --- CONTACT FORM (Using FormSubmit) ---
        # Replace 'your-email@gmail.com' with your actual email
        contact_form = """
        <form action="https://formsubmit.co/your-email@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; color: black;">
            <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; color: black;">
            <textarea name="message" placeholder="Your message here..." required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; color: black;"></textarea>
            <button type="submit" style="background-color: #00acee; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
        </form>
        """

        form_left, form_right = st.columns(2)
        with form_left:
            st.markdown(contact_form, unsafe_allow_html=True)
        with form_right:
            st.info("We usually respond within 24-48 hours. Make sure to check your spam folder!")