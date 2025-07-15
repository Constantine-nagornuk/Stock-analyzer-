import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

Conf = None 
Prediction = None

def CNN_predict():
    print("test")
    model = load_model("trend_classifier_model.h5")
    model.compile(
        optimizer=Adam(learning_rate=0.0003),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    # Load your own image
    img_path = "Current/current.png"
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    # Predict
    pred = model.predict(img_array)[0][0]
    label = "🟢 Bullish" if pred > 0.5 else "🔴 Bearish"
    print(f"Prediction: {label} (confidence: {pred:.2f})")
    global Conf
    global Prediction
    Conf = pred
    print(pred)
    Prediction = label
    print("test2")
# need way more bearish data to make it better, lot more confident with bullish data    
