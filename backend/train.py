import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('diabetes.csv')

# Split features & labels
X = df.drop(columns=['Outcome'])
Y = df['Outcome']

# Scale features
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

# Train/test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, Y, test_size=0.2, stratify=Y, random_state=2
)

# Train linear SVM
classifier = svm.SVC(kernel='linear', probability=True)
classifier.fit(X_train, Y_train)

# Evaluate accuracy
train_acc = accuracy_score(Y_train, classifier.predict(X_train))
test_acc = accuracy_score(Y_test, classifier.predict(X_test))
print(f"[*] Train Accuracy: {train_acc * 100:.2f}%")
print(f"[*] Test Accuracy:  {test_acc * 100:.2f}%")

# Save model and scaler artifacts
joblib.dump(classifier, 'diabetes_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("[+] Exported diabetes_model.pkl and scaler.pkl successfully!")