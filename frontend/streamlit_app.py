
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pathlib
# Simulate a backend delay
import random
import time

# Inject external CSS
def load_local_css(file_path="static/style.css"):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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