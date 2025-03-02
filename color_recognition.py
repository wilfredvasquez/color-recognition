import cv2
from utils import utils


def init_color_recognition():
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
        # color = utils.detectar_color(pixel_center)
        color = utils.detectar_color2(pixel_center)
        print(color)
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

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    init_color_recognition()
