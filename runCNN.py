import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os



def CNN_predict():
    model = load_model("trend_classifier_model.h5")
    model.compile(
        optimizer=Adam(learning_rate=0.0003),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

 
    img_path = "Current/current.png"
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    pred = model.predict(img_array)[0][0]
    label = "Bullish" if pred > 0.5 else "Bearish"
    Label_Output = f"Prediction: {label} (confidence: {pred:.2f})"
    return Label_Output
# need way more bearish data to make it better, lot more confident with bullish data    
