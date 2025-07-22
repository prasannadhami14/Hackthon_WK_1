# Food Freshness Detector

A full-stack application to detect the freshness of fruits and vegetables from images using a machine learning model. The project features a FastAPI backend for prediction and a Streamlit frontend for user interaction.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model](#model)
- [Backend API](#backend-api)
- [Frontend (UI)](#frontend-ui)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
This project predicts whether a fruit or vegetable is **fresh** or **spoiled** from an uploaded image. It uses a Random Forest classifier trained on a custom dataset of labeled images. The backend exposes a REST API for predictions, while the frontend provides a user-friendly interface for image upload and result display.

## Features
- Upload images of fruits/vegetables to check freshness
- Real-time prediction with accuracy score
- FastAPI backend for scalable API
- Streamlit frontend for interactive UI
- Custom dataset and model training pipeline

## Project Structure
```
Hackthon_WK_1/
├── backend/           # FastAPI backend
│   └── app.py         # API implementation
├── frontend/          # Streamlit frontend
│   ├── streamlit_app.py
│   ├── pages/
│   │   └── freshness_detector.py
│   ├── components/
│   │   ├── sidebar.py
│   │   └── upload.py
│   └── static/
│       ├── images/
│       │   └── PushImage.png
│       └── style.css
├── model/             # Model training and storage
│   ├── train_model.py
│   └── trained_model.pkl
├── Dataset/           # Image dataset
│   ├── fresh/
│   └── spoiled/
├── requirements.txt   # Python dependencies
└── README.md
```

## Dataset
- **Location:** `Dataset/`
- **Structure:**
  - `fresh/` — Images of fresh fruits
  - `spoiled/` — Images of spoiled fruits
- **Format:** Standard image files (e.g., PNG, JPG)

## Model
- **Script:** `model/train_model.py`
- **Algorithm:** Random Forest Classifier
- **Input:** Grayscale, resized (100x100) images, flattened
- **Output:**
  - `trained_model.pkl` — Pickle file containing the trained model and accuracy
- **Training:**
  - Loads images from `Dataset/`, preprocesses, splits into train/test, trains, and saves the model

## Backend API
- **Framework:** FastAPI
- **Entry Point:** `backend/app.py`
- **Endpoint:**
  - `POST /predict` — Accepts an image file, returns prediction (`fresh`/`spoiled`) and model accuracy
- **CORS:** Enabled for all origins
- **Error Handling:** Returns error message on failure

## Frontend (UI)
- **Framework:** Streamlit
- **Entry Point:** `frontend/streamlit_app.py`
- **Pages:**
  - Main upload and prediction page
  - Result display page (`pages/freshness_detector.py`)
- **Features:**
  - Upload image, preview, and trigger prediction
  - Displays prediction and image
  - Custom CSS for a clean look (see `static/style.css`)

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/prasannadhami14/Hackthon_WK_1.git
cd Hackthon_WK_1
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Unix/Mac:
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model (if not already trained)
```bash
python model/train_model.py
```

### 5. Run the Backend API
```bash
uvicorn backend.app:app --reload
```

### 6. Run the Frontend
```bash
cd frontend
streamlit run streamlit_app.py
```

## Usage
1. Start both the backend and frontend servers.
2. Open the Streamlit app in your browser (usually at `http://localhost:8501`).
3. Upload an image of a fruit or vegetable.
4. Click "Detect Freshness" to get the prediction.
5. View the result and model accuracy.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License
This project is for educational purposes. Please check with the authors for commercial use.
