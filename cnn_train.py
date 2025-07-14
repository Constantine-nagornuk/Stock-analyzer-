import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
import os


IMAGE_DIR = "TrainingSets"  
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10
MODEL_OUTPUT = "trend_classifier_model.h5"

datagen = ImageDataGenerator(
    rescale=1./255,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=False,
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

# ✅ Print summary of loaded images
print("\n📊 Image Counts:")
print(f"Train: {train_data.samples} images")
print(f"Validation: {val_data.samples} images")
print(f"Class Indices: {train_data.class_indices}")

# ✅ Count raw images from folders
def print_image_counts(path):
    print("\n📁 Folder Image Counts:")
    for class_name in os.listdir(path):
        class_path = os.path.join(path, class_name)
        if os.path.isdir(class_path):
            count = len([
                f for f in os.listdir(class_path)
                if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            ])
            print(f"{class_name}: {count} images")

print_image_counts(IMAGE_DIR)

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

early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

history = model.fit(
    train_data,
    epochs=10,
    validation_data=val_data,
    callbacks=[early_stop]
)

# ✅ Save model
model.save(MODEL_OUTPUT)  
print(f"\n✅ Model saved to {MODEL_OUTPUT}")

# Load the trained model
model = load_model("trend_classifier_model.h5")
model.compile(
    optimizer=Adam(learning_rate=0.0003),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Load your own image
img_path = "TrainingSets/Bullish/4.png"
img = image.load_img(img_path, target_size=(224, 224))
img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

# Predict
pred = model.predict(img_array)[0][0]
label = "🟢 Bullish" if pred > 0.5 else "🔴 Bearish"
print(f"Prediction: {label} (confidence: {pred:.2f})")

# need way more bearish data to make it better, lot more confident with bullish data