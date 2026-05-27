import numpy as np
from pydantic import BaseModel
from joblib import load
from fastapi import FastAPI, HTTPException
from src.core.config import settings
from contextlib import asynccontextmanager

# Define the model like gloabal variable
model = None

# Define the class for the request
class PredictionRequest(BaseModel):
    features : list[float]

# Define the class for the response
class PredictionResponse(BaseModel):
    drought_level : int
    confidence : float

# Load the model at the startup of the API
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Take the global model variable
    global model
    
    # Check if the model file exists
    if not settings.model_path.exists():
        raise RuntimeError("Model file not found. Run 'python -m src.model.train' first.")
    
    # Load the model
    model = load(settings.model_path)
    
    # Yield to start the API
    yield

# Define the details of the API
app = FastAPI(title="Drought Predictor API", description="API for predicting drought conditions", version="0.1.0",lifespan=lifespan)

# Define the endpont for the health check
@app.get("/health")
def health_check():
    return {"Status": "OK"}

# Define the endpoint for the prediction
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Check if the model is loaded
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Run 'python -m src.model.train' first.")
    
    # Convert the features to a numpy array
    X = np.array(request.features).reshape(1,-1)
    
    # Make the prediction
    drought_level = model.predict(X)[0]
    
    # Get the confidence of the prediction
    confidence = model.predict_proba(X)[0]
    
    # Get the max confidence
    confidence = float(max(confidence))
    
    # Return the prediction
    return PredictionResponse(drought_level=int(drought_level), confidence=confidence)
    
    