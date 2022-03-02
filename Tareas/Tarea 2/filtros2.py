import numpy as np
import cv2 as cv
import random
import math

class filtros():
    """
    Clase de filtros básicos para imagenes

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
        """
        return self.img

    def mica_RGB(self, img, red, green, blue):
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                m = max([pixel[0], pixel[1], pixel[2]])
                if pixel[2] + red < m:
                    pixel[2] = 0

                if pixel[1] + green < m:
                    pixel[1] = 0

                if pixel[0] + blue < m:
                    pixel[0] = 0
        return img

    def mica_RGB2(self, img, red, green, blue):
        r = red
        g = green
        b = blue
        value = (b * 255) + (g * 16) + r
        val = hex(value)
        v = int(val, base=16)
        for i in range(self.filas):
            for j in range(self.columnas):
                pixel = img[i][j]

                pixel[0] = b and v
                pixel[1] = g and v
                pixel[2] = r and v
        return img

    def convolucion(self, img, option):
        if option == 1: # blur
            m = [
                        [0.0, 0.2,  0.0],
                        [0.2, 0.2,  0.2],
                        [0.0, 0.2,  0.0]
                    ]
            factor = 1.0
            bias = 0.0
        if option == 2:
            m = [
                        [1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1]
                    ]
            factor = 1.0 / 9.0
            bias = 0.0

        w = self.filas
        h = self.columnas

        filter_w = len(m)
        filter_h = len(m[0])

        for x in range(0, w):
            for y in range(0, h):
                red = 0.0
                green = 0.0
                blue = 0.0
                for filter_y in range(0, filter_h):
                    for filter_x in range(0, filter_w):
                        img_x = (x - filter_w // 2 + filter_x + w) % w
                        img_y = (y - filter_h // 2 + filter_y + h) % h
                        red += img[img_x][img_y][2] * m[filter_y][filter_x]
                        green += img[img_x][img_y][1] * m[filter_y][filter_x]
                        blue += img[img_x][img_y][0] * m[filter_y][filter_x]
                img[x][y][2] = min([max([int(factor * red + bias), 0]), 255])
                img[x][y][1] = min([max([int(factor * green + bias), 0]), 255])
                img[x][y][0] = min([max([int(factor * blue + bias), 0]), 255])
        return img


cp = "photo.png"
im = filtros(cp)
img = im.obtener_imagen()
#cv.imshow("a", img)
a = im.convolucion(img, 2)
cv.imshow("result", a)
cv.waitKey()
