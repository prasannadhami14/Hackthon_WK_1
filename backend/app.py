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
