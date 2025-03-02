import numpy as np
from . import const


def detectar_color(pixel_hsv):
    for nombre_color, rangos_hsv in const.RANGO_COLORES.items():
        inferior, superior = rangos_hsv
        if np.all(pixel_hsv >= inferior) and np.all(pixel_hsv <= superior):
            return nombre_color

    return "desconocido"
