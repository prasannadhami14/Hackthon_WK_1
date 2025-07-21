# build  your api
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import pickle
import io
import os
import sys
from pathlib import Path
from pydantic import BaseModel

# Add the project root to Python path
project_root = Path(__file__).parent.parent
data_dir = Path(__file__).parent.parent / 'model' /'trained_model.pkl' # Absolute path

sys.path.append(str(project_root))

from model.train_model import load_data

# -----------------------------------------------
# Initialize FastAPI application
# -----------------------------------------------
app = FastAPI(title=" Food Freshness Detector API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionResponse(BaseModel):
    prediction: str
    accuracy: float
# predict api
@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        # Read the image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Preprocess the image
        image = image.resize((100, 100))
        image = np.array(image.convert('L')).flatten().reshape(1, -1)  # Convert to grayscale and flatten
        
        # Load the model and accuracy together
        with open(data_dir, "rb") as f:
            data = pickle.load(f)
            model = data["model"]
            model_accuracy = data["accuracy"]
        
        # Make prediction
        prediction = model.predict(image)
        
        # Map prediction to label
        labels = {0: 'fresh', 1: 'spoiled'}
        result = labels.get(prediction[0], "unknown")
        
        return {"prediction": result, "accuracy": model_accuracy}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})