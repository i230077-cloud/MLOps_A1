import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="student-ml-api",
    description="ML Inference API for MLOps Assignment",
    version="1.0.0"
)

def read_version():
    version_path = os.path.join(os.path.dirname(__file__), "VERSION")
    if os.path.exists(version_path):
        with open(version_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "1.0.0"

class PredictRequest(BaseModel):
    value: float

class PredictResponse(BaseModel):
    input: float
    prediction: float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": read_version()
    }

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    # Simple mathematical prediction algorithm (value * 2)
    result = request.value * 2.0
    return {
        "input": request.value,
        "prediction": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
