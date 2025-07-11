import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os


IMAGE_DIR = "TrainingSets"  
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10
MODEL_OUTPUT = "trend_classifier_model.h5"


datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    IMAGE_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training',
    shuffle=True
)

val_data = datagen.flow_from_directory(
    IMAGE_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

# ✅ CNN Architecture
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')  # Binary: 0 = bearish, 1 = bullish
])

model.compile(
    optimizer=Adam(learning_rate=0.0003),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ✅ Train
print("\n📈 Training model...\n")
history = model.fit(
    train_data,
    epochs=EPOCHS,
    validation_data=val_data
)

# ✅ Save model
model.save(MODEL_OUTPUT)
print(f"\n✅ Model saved to {MODEL_OUTPUT}")





# Load the trained model
model = load_model("trend_classifier_model.h5")

# Load your own image
img_path = "TrainingSets/Bearish/22.png"
img = image.load_img(img_path, target_size=(224, 224))
img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

# Predict
pred = model.predict(img_array)[0][0]
label = "🟢 Bullish" if pred > 0.5 else "🔴 Bearish"
print(f"Prediction: {label} (confidence: {pred:.2f})")
