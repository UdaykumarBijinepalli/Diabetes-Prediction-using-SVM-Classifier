🩺 Diabetes Prediction using SVM Classifier

This project is a Flask web application that predicts whether a person is diabetic or not based on medical input parameters. The prediction is powered by a Support Vector Machine (SVM) Classifier trained on the Pima Indians Diabetes dataset.

📌 Features

User-friendly web interface for inputting medical details.

Predicts whether the person is Diabetic or Not Diabetic.

Displays model accuracy on test data.

Built with Flask (Python backend) and styled with CSS frontend.

📊 Dataset

The project uses the Pima Indians Diabetes Dataset, which includes the following features:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI (Body Mass Index)

Diabetes Pedigree Function

Age

Outcome (Target: 1 → Diabetic, 0 → Not Diabetic)

🛠️ Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS (style.css)

ML Model: Support Vector Machine (SVM) with linear kernel

Libraries:

numpy

pandas

scikit-learn

flask

🚀 Installation & Setup

Clone the repository

git clone https://github.com/your-username/diabetes-prediction-svm.git
cd diabetes-prediction-svm


Create and activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt


Add the dataset
Place the diabetes.xlsx file inside a data/ folder.

project-folder/
├── app.py
├── style.css
├── templates/
│   └── prg12.html
└── data/
    └── diabetes.xlsx


Run the Flask app

python app.py


Open the app in your browser

http://127.0.0.1:5000/

🖥️ Usage

Enter the required medical values in the web form.

Click Predict to check if the person is diabetic.

Check Model Accuracy by accessing:

http://127.0.0.1:5000/accuracy

📷 Screenshots

(You can add screenshots of your web interface here for better presentation.)

📈 Model Performance

Classifier: SVM (Support Vector Machine)

Kernel: Linear

Evaluation Metric: Accuracy (on test dataset)

📂 Project Structure
diabetes-prediction-svm/
│── app.py              # Main Flask application
│── style.css           # CSS file for styling
│── templates/
│    └── prg12.html     # HTML frontend
│── data/
│    └── diabetes.xlsx  # Dataset
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

✅ Future Improvements

Deploy the app using Heroku / AWS / Azure.

Add additional ML models for comparison (Logistic Regression, Random Forest, etc.).

Improve UI with Bootstrap or React frontend.

Include detailed metrics like Precision, Recall, F1-score.

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit pull requests.
