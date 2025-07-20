# UI  code

import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from pathlib import Path
# Simulate a backend delay
import random
import time

<<<<<<< HEAD
# Inject external CSS
=======
>>>>>>> b92db61919f3c3f852be1b295cd6f7a380b48881
def load_local_css():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    # Construct the full path to the CSS file
    css_path = script_dir / "static" / "style.css"
    
    try:
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found at: {css_path}")
<<<<<<< HEAD

=======
>>>>>>> b92db61919f3c3f852be1b295cd6f7a380b48881
# Call this before rendering your layout
load_local_css()

st.set_page_config(page_title="Food Freshness Detector", layout="centered")

st.title("Food Freshness Detector")
st.write("Upload a fruit or vegetable image to check if it's fresh or spoiled.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Preview", use_container_width=True)

    if st.button("Detect Freshness"):
        with st.spinner("Analyzing..."):
            # try:
            #     response = requests.post(
            #         "http://localhost:5000/predict",
            #         files={"image": uploaded_file.getvalue()}
            #     )
            #     if response.status_code == 200:
            #         result = response.json().get("prediction", "Unknown")

            #         st.session_state['result'] = result
            #         st.session_state['image_bytes'] = uploaded_file.getvalue()
            #         st.switch_page("freshness_detector.py")
            #     else:
            #         st.error("API returned an error.")
            # except Exception as e:
            #     st.error(f"Could not connect to backend: {e}")

            # fake simulation
            time.sleep(1.5)  # simulate processing time

            # Simulate a random prediction
            fake_predictions = ["Fresh!!", "Spoiled!!", "Not Sure!!"]
            result = random.choice(fake_predictions)

            st.session_state['result'] = result
            st.session_state['image_bytes'] = uploaded_file.getvalue()
            st.switch_page("pages/freshness_detector.py")
