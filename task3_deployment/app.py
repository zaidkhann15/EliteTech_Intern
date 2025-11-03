# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import HTMLResponse
# import numpy as np
# from PIL import Image
# import tensorflow as tf

# app = FastAPI()

# # Load the trained model
# model = tf.keras.models.load_model("../task2_deep_learning/cifar10_cnn_model.h5")

# # Class names from CIFAR-10
# CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
#                'dog', 'frog', 'horse', 'ship', 'truck']

# @app.get("/")
# def home():
#     return {"message": "CIFAR10 Image Classification API is Running!"}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     # Read image file
#     img = Image.open(file.file).convert('RGB')
#     img = img.resize((32, 32))  # CIFAR10 size
#     img_array = np.array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     predictions = model.predict(img_array)
#     predicted_class = CLASS_NAMES[np.argmax(predictions)]

#     return {"prediction": predicted_class}



import streamlit as st
import numpy as np
from PIL import Image
from model_utils import load_model, predict_image

st.title("CIFAR-10 Image Classifier")
st.write("Upload an image and the model will try to identify it!")

model = load_model("cifar10_cnn_model.h5")

uploaded_img = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_img is not None:
    image = Image.open(uploaded_img).convert("RGB")
    resized_img = image.resize((32, 32))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(resized_img) / 255.0

    if st.button("Predict"):
        prediction = predict_image(model, img_array)
        st.success(f"Predicted Class: **{prediction}**")