# ✅ Task 3 – End-to-End Data Science Project (API + Web App Deployment)

This is the **third task of the EliteTech Internship**, where a complete Data Science workflow is implemented — from data processing to model deployment using both **API (FastAPI)** and **Web App (Streamlit)**.

---

## 📌 Project Highlights

✔ Data loading and preprocessing  
✔ Model training on CIFAR-10 dataset using CNN  
✔ Model saved as `.h5` file  
✔ FastAPI-based backend API for predictions  
✔ Streamlit-based Web App for user-friendly prediction interface  
✔ Modular and scalable project structure

---

## 📁 Folder Structure

task3_deployment/
│
├── model/
│ └── cifar10_cnn_model.h5 # Trained model
│
├── api/
│ └── app.py # FastAPI backend
│
├── web_app/
│ └── app_streamlit.py # Streamlit frontend
│
├── utils/
│ └── predict.py # Image preprocessing + prediction logic
│
├── requirements.txt # Python libraries
└── README.md # Project documentation


---

## ⚙️ Setup & Installation

### ✅ 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt


Run the FastAPI Backend (API)

uvicorn app:app --reload
Then open in browser:
API Root: http://127.0.0.1:8000
API Docs (Swagger UI): http://127.0.0.1:8000/docs

Run the Streamlit Web App

streamlit run web_app/app_streamlit.py
Upload an image
The model predicts the class (e.g., airplane, cat, ship, dog)


Model Information

Dataset: CIFAR-10 (60,000 images, 10 classes)
Algorithm: Convolutional Neural Network (CNN)
Framework: TensorFlow / Keras
Output: Class label with confidence score


Developed By:
Zaid Khan
EliteTech Internship – Task 3: End-to-End Data Science Project