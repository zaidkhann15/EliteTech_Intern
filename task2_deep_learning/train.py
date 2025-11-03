# train.py — Reproducible training script (no notebook UI)
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os

def build_simple_cnn(input_shape=(32,32,3), num_classes=10):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(128, (3,3), activation='relu'),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def main():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train, x_test = x_train.astype("float32") / 255.0, x_test.astype("float32") / 255.0

    model = build_simple_cnn()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.1)

    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
    print(f"Test accuracy: {test_acc*100:.2f}%")

    model.save("cifar10_cnn_model.h5")
    print("Saved model to cifar10_cnn_model.h5")

if __name__ == "__main__":
    main()