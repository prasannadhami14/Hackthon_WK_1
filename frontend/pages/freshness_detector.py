import streamlit as st
from PIL import Image
from io import BytesIO
import pathlib

# Inject external CSS
def load_local_css(file_path="static/style.css"):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call this before rendering your layout
load_local_css()

st.set_page_config(page_title="Prediction Result", layout="centered")

st.title("Prediction Result")

if 'result' in st.session_state and 'image_bytes' in st.session_state:
    
    prediction = st.session_state['result']
    st.subheader(f"The model predicts: {prediction}")
    image_data = st.session_state['image_bytes']
    image = Image.open(BytesIO(image_data))

    st.image(image, caption="Analyzed Image", use_container_width=True)
    st.page_link("streamlit_app.py", label="Go back to detector")
    
else:
    st.warning("No prediction found. Please upload an image first.")
    st.page_link("streamlit_app.py", label="Go back to detector")