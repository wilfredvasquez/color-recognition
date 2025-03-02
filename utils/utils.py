import numpy as np
from . import const


def detectar_color(pixel_hsv):
    for nombre_color, rangos_hsv in const.RANGO_COLORES.items():
        inferior, superior = rangos_hsv
        if (
            inferior[0] <= pixel_hsv[0] <= superior[0]
            and inferior[1] <= pixel_hsv[1] <= superior[1]
            and inferior[2] <= pixel_hsv[2] <= superior[2]
        ):
            return nombre_color

    return "desconocido"


def detectar_color2(pixel_hsv):
    """
    Detecta el color de un píxel en formato HSV comparándolo con los rangos definidos.

    Parámetros:
        pixel_hsv (tuple): Un píxel en formato HSV (H, S, V).

    Retorna:
        str: El nombre del color detectado o "desconocido" si no coincide con ningún rango.
    """
    for nombre_color, rangos_hsv in const.RANGO_COLORES2.items():
        if (
            nombre_color.endswith("claro")
            or nombre_color.endswith("oscuro")
            or nombre_color.endswith("pastel")
        ):
            # Colores claros, oscuros o pastel tienen un solo rango
            lower = np.array(rangos_hsv[0])
            upper = np.array(rangos_hsv[1])
            if np.all(pixel_hsv >= lower) and np.all(pixel_hsv <= upper):
                return nombre_color
        elif nombre_color == "rojo":
            # El rojo tiene dos rangos en HSV
            lower1 = np.array(rangos_hsv[0])
            upper1 = np.array(rangos_hsv[1])
            lower2 = np.array(rangos_hsv[2])
            upper2 = np.array(rangos_hsv[3])
            if (np.all(pixel_hsv >= lower1) and np.all(pixel_hsv <= upper1)) or (
                np.all(pixel_hsv >= lower2) and np.all(pixel_hsv <= upper2)
            ):
                return nombre_color
        else:
            # Otros colores tienen un solo rango
            lower = np.array(rangos_hsv[0])
            upper = np.array(rangos_hsv[1])
            if np.all(pixel_hsv >= lower) and np.all(pixel_hsv <= upper):
                return nombre_color

    return "desconocido"
