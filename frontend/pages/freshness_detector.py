import streamlit as st
from PIL import Image
from io import BytesIO
from pathlib import Path

# Inject external CSS
def load_local_css():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    # Construct the full path to the CSS file
    css_path = script_dir / "../static" / "style.css"
    
    try:
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found at: {css_path}")

# Call this before rendering your layout
load_local_css()

st.set_page_config(page_title="Prediction Result", layout="centered")

st.title("Prediction Result")

if 'result' in st.session_state and 'image_bytes' in st.session_state:
    
    prediction = st.session_state['result']
    st.subheader(f"The model predicts: {prediction}")
    image_data = st.session_state['image_bytes']
    image = Image.open(BytesIO(image_data))
    st.image(image, caption="Preview", width=300)  # Set width to match product card
    st.page_link("streamlit_app.py", label="Go back to detector")
    
else:
    st.warning("No prediction found. Please upload an image first.")
    st.page_link("streamlit_app.py", label="Go back to detector")