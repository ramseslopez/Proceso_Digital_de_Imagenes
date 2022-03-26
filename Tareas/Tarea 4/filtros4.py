import numpy as np
import cv2 as cv
#import imgkit

class filtros():
    """
    Clase de filtros de marca de agua para imagenes

    author - Ramses Antonio López Soto
                  315319974
    date - marzo 2022
    """

    def __init__(self, ruta_imagen):
        """
        Inicializa las variables
        a utilizar

        Params
        ruta_imagen - localizacion de la imagen
        """
        self.ruta_imagen = ruta_imagen
        self.img = cv.imread(ruta_imagen)
        self.filas = len(self.img)
        self.columnas = len(self.img[0])

    def obtener_imagen(self):
        """
        Devuelve la imagen

        Returns
        imagen original
        """
        return self.img

    def quitar_marca_agua(self, img):
        """
        Elimina la marca de agua de una imagen
        en escala de grises

        Params
        img - imagen

        Returns
        imagen sin marca de agua
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                red = img[i,j][2]
                green = img[i,j][1]
                blue = img[i,j][0]
                if red > (green + 15) and red > (blue + 15):
                    rest_r = 185 - red
                    rest_g = 175 - green
                    rest_b = 235 - blue
                    prom = (rest_r + rest_g + rest_b) // 3
                    if prom < 25:
                        red = 255
                        green = 255
                        blue = 255
                    elif prom > 103:
                        red = 0
                        green = 0
                        blue = 0
                    else:
                        div = (img[i,j][2] + img[i,j][1] + img[i,j][0]) // 3
                        red = div
                        green = div
                        blue = div
                img[i,j][2] = red
                img[i,j][1] = green
                img[i,j][0] = blue
        return img
