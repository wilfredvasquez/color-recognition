import numpy as np
import pandas as pd
from . import const

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)


def detectar_color(pixel_hsv):
    for nombre_color, rangos_hsv in const.RANGO_COLORES.items():
        inferior, superior = rangos_hsv
        if np.all(pixel_hsv >= inferior) and np.all(pixel_hsv <= superior):
            return nombre_color

    return "desconocido"


def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = (
            abs(R - int(csv.loc[i, "R"]))
            + abs(G - int(csv.loc[i, "G"]))
            + abs(B - int(csv.loc[i, "B"]))
        )
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname
