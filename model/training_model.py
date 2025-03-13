import os
import tensorflow as tf
import tensorflowjs as tfjs
import pandas as pd
from keras import Sequential, losses, optimizers
from keras.layers import Normalization
from keras import layers, regularizers

os.environ["TF_USE_LEGACY_KERAS"] = "1"


# Leer los datasets de entrenamiento y prueba
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv")
y_test = pd.read_csv("y_test.csv")

# Configuración de la red neuronal
model = tf.keras.Sequential(
    [
        layers.Dense(
            3,
            kernel_regularizer=regularizers.l2(0.001),
            activation="relu",
            input_shape=[len(X_train.keys())],
        ),  # inputshape=[3]
        layers.Dense(24, kernel_regularizer=regularizers.l2(0.001), activation="relu"),
        layers.Dense(11),
    ]
)

# Compilación del modelo
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_function = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
model.compile(loss=loss_function, optimizer=optimizer, metrics=["accuracy"])

# Entrenamiento del modelo
model.fit(
    x=X_train,
    y=y_train,
    validation_split=0.3,
    epochs=1001,
    batch_size=48,
    # verbose=0,
    shuffle=True,
)

# Guardar modelo para versión desktop
model.save("colors_model.keras")

# Guardar modelo para ser convertido en Tensorflow.js
tf.saved_model.save(model, "tf_model")

print("Modelo entrenado y guardado como 'colors_model.keras'.")
