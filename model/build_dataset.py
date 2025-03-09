from sklearn.model_selection import train_test_split
import pandas as pd

# Construir Dataset
# ------------------

# Cargar el dataset
colors_df = pd.read_csv("colors_dataset.csv")

dataset = pd.get_dummies(colors_df, columns=["label"])
dataset = dataset[
    [
        "red",
        "green",
        "blue",
        "label_Red",
        "label_Green",
        "label_Blue",
        "label_Yellow",
        "label_Orange",
        "label_Pink",
        "label_Purple",
        "label_Brown",
        "label_Grey",
        "label_Black",
        "label_White",
    ]
]

# Dividir el dataset en conjuntos de entrenamiento y prueba
# 80% de los datos para entrenamiento y 20% para prueba
train_dataset = dataset.sample(frac=0.8, random_state=9)
test_dataset = dataset.drop(train_dataset.index)

"""## Split features: `red`, `green`, `blue` and labels"""
# Data set de entrenamiento
train_labels = pd.DataFrame(
    [
        train_dataset.pop(x)
        for x in [
            "label_Red",
            "label_Green",
            "label_Blue",
            "label_Yellow",
            "label_Orange",
            "label_Pink",
            "label_Purple",
            "label_Brown",
            "label_Grey",
            "label_Black",
            "label_White",
        ]
    ]
).T


# Dataset de prueba
test_labels = pd.DataFrame(
    [
        test_dataset.pop(x)
        for x in [
            "label_Red",
            "label_Green",
            "label_Blue",
            "label_Yellow",
            "label_Orange",
            "label_Pink",
            "label_Purple",
            "label_Brown",
            "label_Grey",
            "label_Black",
            "label_White",
        ]
    ]
).T

# Guardar los conjuntos de entrenamiento y prueba en archivos CSV
train_dataset.to_csv("X_train.csv", index=False)
train_labels.to_csv("y_train.csv", index=False)
test_dataset.to_csv("X_test.csv", index=False)
test_labels.to_csv("y_test.csv", index=False)

"""
# Convertir la columna 'label' a formato one-hot
one_hot_enc_df = pd.get_dummies(colors_df, columns=["label"], dtype="int")

# Separar las características (valores RGB) y las etiquetas (one-hot encoded labels)
X = one_hot_enc_df[["red", "green", "blue"]]
y = one_hot_enc_df.drop(columns=["red", "green", "blue"])

# Dividir el dataset en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Guardar los conjuntos de entrenamiento y prueba en archivos CSV
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Dataset de entrenamiento y prueba creados y guardados en archivos CSV.")
"""
