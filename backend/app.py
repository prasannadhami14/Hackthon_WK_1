# build  your api
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import pickle
import io
import os

# -----------------------------------------------
# Initialize FastAPI application
# -----------------------------------------------
app = FastAPI(title=" Food Freshness Detector API")

@app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def run_model(image_bytes):
    # Load the model
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Preprocess the image
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 224, 224, 3)

    # Predict
    prediction = model.predict(image_array)
    return prediction[0]