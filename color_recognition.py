import cv2
import numpy as np
from utils import utils
from tensorflow.keras.models import load_model

# Cargar el modelo entrenado
model = load_model("model/colors_model.keras")

NOMBRE_COLORES = [
    "Rojo",
    "Verde",
    "Azul",
    "Amarillo",
    "Naranja",
    "Rosado",
    "Púrpura",
    "Marrón",
    "Gris",
    "Negro",
    "Blanco",
]


def detenting_color(pixel_rgb):
    data_to_test = np.array([[pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]]])
    train_predictions = model.predict(data_to_test)

    color_index = np.argmax(train_predictions[0])
    return NOMBRE_COLORES[color_index]


def detectar_indice_camara():
    index = None
    for i in range(10):
        cap = cv2.VideoCapture(i, cv2.CAP_V4L2)
        if cap.isOpened():
            print(f"Camera index {i} is available.")
            cap.release()
            index = i
        else:
            print(f"Camera index {i} is not available.")

    return index


def init_color_recognition():
    index = detectar_indice_camara()
    if index is None:
        print("Cámara no habilitada")

    cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el frame")
            break

        # hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape
        cx, cy = width // 2, height // 2

        pixel_center = frame[cy, cx]
        # color = utils.detectar_color(pixel_center)
        # color = utils.detectar_color2(pixel_center)
        color = detenting_color(pixel_center)
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

        # Texto para indicar al usuario que coloque el objeto en el centro
        texto_instruccion = "Coloque el objeto en el punto medio"
        cv2.putText(
            frame,
            texto_instruccion,
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        # Texto para mostrar el color detectado
        texto_color = f"Color detectado: {color.title()}"
        cv2.putText(
            frame,
            texto_color,
            (50, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        # Texto salida
        texto_salida = "Presione ESC para salir"
        cv2.putText(
            frame,
            texto_salida,
            (50, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    init_color_recognition()
