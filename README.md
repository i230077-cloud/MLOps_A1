# Student ML API (`student-ml-api`)

**Student Name**: Muhammad Saad  
**Roll Number**: i230077  
**Course**: Advanced MLOps  
**Framework**: FastAPI  

---

## 📌 Project Overview

`student-ml-api` is a production-grade machine learning inference microservice designed following strict MLOps standards. The repository features a complete automated CI/CD pipeline, containerized delivery with Docker, multi-tag image releases on GitHub Container Registry (GHCR), reproducible artifact management, zero-rebuild rollback capabilities, and strict Git branch protection policies.

---

## 📁 Repository Structure

```
student-ml-api/
├── app.py                     # FastAPI application endpoints (/health & /predict)
├── requirements.txt           # Python dependencies (fastapi, uvicorn, pydantic, pytest, httpx)
├── Dockerfile                 # Production-oriented Dockerfile with layer optimization & OCI labels
├── .dockerignore              # Docker build exclusion rules
├── .gitignore                 # Git repository exclusion rules
├── VERSION                    # Application version tracking file (1.1.0)
├── tests/
│   └── test_app.py            # Automated pytest test suite
└── .github/
    └── workflows/
        ├── ci.yml             # PR verification & test build CI workflow
        └── release.yml        # Semantic version tag release & GHCR deployment workflow
```

---

## 🚀 Quick Start Guide

### 1. Local Python Environment Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run automated tests
pytest -v

# Start application server locally
python app.py
```

API will be accessible at: `http://localhost:5000`

---

## 🐳 Docker Usage

### Build Docker Image
```bash
docker build -t student-ml-api:1.1.0 .
```

### Run Docker Container
```bash
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.1.0
```

### Test API Endpoints

#### Health Check Endpoint
```bash
curl http://localhost:5000/health
```

**Expected Response (v1.1.0)**:
```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

#### Prediction Endpoint
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"value\": 10}"
```

**Expected Response**:
```json
{
  "input": 10.0,
  "prediction": 20.0
}
```

---

## 🔄 CI/CD & MLOps Development Workflow

1. **Feature Development**: Developers create feature branches (e.g., `feature/prediction-api`).
2. **Pull Request**: Changes are submitted via Pull Request targeting `main`.
3. **Automated CI (`ci.yml`)**: GitHub Actions runs `pytest` and validates `docker build`.
4. **Code Review & Merge**: PR is reviewed and merged into `main` using Merge Commits.
5. **Release Tagging**: Pushing a semantic git tag (e.g., `git tag v1.1.0 && git push origin v1.1.0`).
6. **Automated Release (`release.yml`)**: Builds image, attaches OCI metadata, tags as `1.1.0`, `latest`, and `<commit-sha>`, then publishes to GHCR.

---

## 📄 Documentation & Reports
For full details on the 26 assignment parts, deliberate failure evidence, container inspection, layer cache analysis, failure analysis, and Viva question answers, please consult [`ASSIGNMENT_REPORT.md`](file:///c:/Users/Saad/OneDrive/Desktop/MLOps_A1/ASSIGNMENT_REPORT.md).
