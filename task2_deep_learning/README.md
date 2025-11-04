# 🧠 Task 2 — CIFAR-10 Image Classification

## 📌 Overview
This project uses **Convolutional Neural Networks (CNN)** to classify images from the **CIFAR-10 dataset** into 10 categories such as airplane, car, bird, cat, etc. The model is trained using **TensorFlow/Keras**.

---

## 📁 Project Structure

task2_deep_learning/
│
├── cifar10_cnn.ipynb # Main Jupyter Notebook
├── train.py # Python script (optional)
├── models/
│ └── cifar10_cnn_model.h5 # Saved trained model
├── requirements.txt # Required dependencies
└── README.md # Project documentation

---

## ⚙️ How to Run the Project

### Step 1: Create Virtual Environment
```bash
cd task2_deep_learning
python -m venv venv
venv\Scripts\activate     # For Windows

### Step 2: Install Required Libraries
pip install -r requirements.txt

### Step 3: Train the Model
Option A: Using Jupyter Notebook
Open cifar10_cnn.ipynb
Run all cells

Option B: Using Python Script
python train.py


### Model Saving
After training, the model is saved automatically at: cifar10_cnn_model.h5
You can load it later by:
from tensorflow.keras.models import load_model
model = load_model("cifar10_cnn_model.h5")



Developed By:
Zaid Khan
EliteTech Internship – Task 2: CIFAR-10 Image Classification