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

        height, width, _ = frame.shape
        cx, cy = width // 2, height // 2

        r, g, b = frame[cy, cx]
        color = utils.get_color_name(int(r), int(g), int(b))
        print(color)
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    init_color_recognition()
