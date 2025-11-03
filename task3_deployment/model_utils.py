# # model_utils.py
# import numpy as np
# from tensorflow.keras.models import load_model

# CLASS_NAMES = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

# def load_trained_model(path="cifar10_cnn_model.h5"):
#     return load_model(path)

# def predict_image(model, img_array):
#     # img_array should be normalized (0-1) and shape (H,W,3)
#     arr = np.expand_dims(img_array, axis=0)
#     preds = model.predict(arr)
#     return np.argmax(preds, axis=1)[0]



import tensorflow as tf
import numpy as np

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def load_model(path="cifar10_cnn_model.h5"):
    model = tf.keras.models.load_model(path)
    return model

def predict_image(model, img_array):
    img_array = np.expand_dims(img_array, axis=0)   # (1, 32, 32, 3)
    predictions = model.predict(img_array)
    return CLASS_NAMES[np.argmax(predictions)]