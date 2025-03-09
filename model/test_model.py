import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

# Cargar el modelo entrenado
model = load_model("colors_model.keras")

# Leer los datasets de entrenamiento y prueba
data_to_test = np.array(
    [
        [255, 0, 0],  # Rojo
        [0, 255, 0],  # Verde
        [0, 0, 255],  # Azul
        [255, 255, 0],  # Amarillo
        [0, 255, 255],  # Cian o Azul claro
        [255, 0, 255],  # Magenta o Rosa
        [128, 0, 128],  # Púrpura
        [165, 42, 42],  # Marrón
        [128, 128, 128],  # Gris
        [255, 255, 255],  # Blanco
        [0, 0, 0],  # Negro
    ]
)

# Predicción de la data de entrenamiento
train_predictions = model.predict(data_to_test)

categories = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Orange",
    "Pink",
    "Purple",
    "Brown",
    "Grey",
    "Black",
    "White",
]
for i, prediction in enumerate(train_predictions):
    color_index = np.argmax(prediction)
    color_name = categories[color_index]
    print(f"Color {i+1}: {color_name}")
