\# Diabetes Prediction using SVM Classifier



A full-stack, containerized machine learning application for clinical diabetes risk prediction using a Support Vector Machine (SVM) model.



\## Tech Stack

\- \*\*Backend:\*\* FastAPI, Scikit-Learn, Pandas, NumPy, Uvicorn

\- \*\*Frontend:\*\* HTML5, Tailwind CSS, Vanilla JavaScript

\- \*\*DevOps:\*\* Docker, Docker Compose, Nginx Reverse Proxy



\## Project Structure

```text

├── backend/

│   ├── app.py               # FastAPI REST service

│   ├── train.py             # SVM training \& serialization pipeline

│   ├── diabetes.csv         # Pima Indians Diabetes dataset

│   ├── diabetes\_model.pkl   # Serialized SVM model artifact

│   ├── scaler.pkl           # StandardScaler artifact

│   ├── requirements.txt     # Python dependencies

│   └── Dockerfile           # Backend container image

├── frontend/

│   ├── index.html           # Interactive assessment UI

│   ├── nginx.conf           # Reverse proxy configuration

│   └── Dockerfile           # Frontend container image

├── docker-compose.yml       # Multi-container orchestration

└── .gitignore

