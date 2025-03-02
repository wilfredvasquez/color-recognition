import cv2
import numpy as np

rangos_colores = {
    "rojo": ((0, 80, 80), (10, 255, 255)),  # Ejemplo de rango para rojo
    "naranja": ((10, 80, 80), (30, 255, 255)),
    "amarillo": ((50, 80, 80), (70, 255, 255)),
    "verde": ((100, 80, 80), (140, 255, 255)),
    "azul": ((220, 80, 80), (260, 255, 255)),
    "morado": ((270, 60, 60), (300, 255, 255)),
    "marron": ((20, 50, 30), (40, 80, 60)),
    "negro": ((0, 0, 0), (360, 10, 20)),
    "blanco": ((0, 0, 90), (360, 20, 100)),
    "gris": ((0, 0, 50), (360, 20, 70)),
    "rosa": ((330, 40, 80), (350, 80, 100)),
    "verde claro": ((80, 40, 80), (120, 80, 100)),
    "azul claro": ((190, 40, 80), (230, 80, 100)),
    "amarillo claro": ((50, 20, 90), (70, 60, 100)),
    "naranja claro": ((20, 40, 90), (40, 70, 100)),
    "morado claro": ((280, 30, 90), (310, 70, 100)),
}


def detectar_color(pixel_hsv):
    for nombre_color, rangos_hsv in rangos_colores.items():
        inferior, superior = rangos_hsv
        if np.all(pixel_hsv >= inferior) and np.all(pixel_hsv <= superior):
            return nombre_color

    return "desconocido"


cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar el frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx, cy = width // 2, height // 2

    pixel_center = hsv_frame[cy, cx]
    color = detectar_color(pixel_center)
    print(color)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
