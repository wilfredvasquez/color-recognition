import tensorflow as tf
import pandas as pd
from keras import Sequential, losses, optimizers
from keras.layers import Normalization
from keras import layers, regularizers

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

model.save("colors_model.keras")
print("Modelo entrenado y guardado como 'colors_model.keras'.")


"""
# Convertir las etiquetas a formato one-hot (ya están en formato one-hot en los archivos CSV)
# y_train = pd.get_dummies(y_train)
# y_test = pd.get_dummies(y_test)

# Convertir DataFrame objects a Tensor objects
train_input_tensor = tf.convert_to_tensor(X_train, dtype=tf.float32)
train_output_tensor = tf.convert_to_tensor(y_train, dtype=tf.float32)
test_input_tensor = tf.convert_to_tensor(X_test, dtype=tf.float32)
test_output_tensor = tf.convert_to_tensor(y_test, dtype=tf.float32)

# Normalizer layer
input_normalizer = Normalization(axis=-1)

# Compute the mean and variance of values in a dataset.
input_normalizer.adapt(train_input_tensor)

# Creación del modelo ANN
ann_model = tf.keras.Sequential(
    [
        input_normalizer,
        tf.keras.layers.Dense(64, activation=tf.nn.relu),
        tf.keras.layers.Dense(64, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax),  # para clasificacion
    ]
)

ann_model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Entrenar el modelo
ann_model.fit(
    x=train_input_tensor,
    y=train_output_tensor,
    validation_split=0.2,
    batch_size=32,
    epochs=100,
    shuffle=True,
)

# Guardar el modelo entrenado
ann_model.save("colors_model.keras")

print("Modelo entrenado y guardado como 'colors_model.keras'.")
"""
