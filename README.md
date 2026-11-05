# Diabetes Prediction using SVM Classifier

A full-stack, containerized machine learning application for clinical diabetes risk prediction using a Support Vector Machine (SVM) model.

## Tech Stack

- **Backend:** FastAPI, Scikit-Learn, Pandas, NumPy, Uvicorn
- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
- **DevOps:** Docker, Docker Compose, Nginx Reverse Proxy

## Project Structure

\\\	ext
+-- backend/
¦   +-- app.py               # FastAPI REST service
¦   +-- train.py             # SVM training & serialization pipeline
¦   +-- diabetes.csv         # Pima Indians Diabetes dataset
¦   +-- diabetes_model.pkl   # Serialized SVM model artifact
¦   +-- scaler.pkl           # StandardScaler artifact
¦   +-- requirements.txt     # Python dependencies
¦   +-- Dockerfile           # Backend container image
+-- frontend/
¦   +-- index.html           # Interactive assessment UI
¦   +-- nginx.conf           # Reverse proxy configuration
¦   +-- Dockerfile           # Frontend container image
+-- docker-compose.yml       # Multi-container orchestration
+-- .gitignore
\\\

## Quick Start (Docker)

Run both services with Docker Compose:

\\\ash
docker compose up -d --build
\\\

- **Frontend App:** http://localhost
- **Swagger API Docs:** http://localhost:8000/docs
- **API Health Check:** http://localhost:8000/health

## Local Development

### 1. Backend
\\\ash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python train.py
python app.py
\\\

### 2. Frontend
Open \rontend/index.html\ directly in any web browser.
