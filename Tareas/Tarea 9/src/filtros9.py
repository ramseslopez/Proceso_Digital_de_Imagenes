import os
import numpy as np
import cv2 as cv
import random
import math

class filtros():
    """
    Clase de filtros de convolucion para imagenes

    author - Ramses Antonio López Soto
                  315319974
    date - abril 2022
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
        imagen
        """
        return self.img

    def dithering(self, img, version):
        g_img = self.gris(img.copy())
        if version == 1:
            m = [   [8, 3, 4],
                       [6, 1, 3],
                       [7, 5, 9]   ]
        if version == 2:
            m = [   [1, 7, 4],
                       [5, 8, 3],
                       [6, 2, 9]   ]

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                v1 = img[i, j][0] / 255
                v2 = (m[i % 3][j % 3]) / 9
                if v1 < v2:
                    g_img[i,j][2] = 0
                    g_img[i,j][1] = 0
                    g_img[i,j][0] = 0
                else:
                    g_img[i,j][2] = 255
                    g_img[i,j][1] = 255
                    g_img[i,j][0] = 255

        return g_img

    def gris(self, img):
        """
        Aplica un filtro gris a la imagen

        Params
        img - imagen

        Returns
        imagen con filtro aplicado
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[0] = pixel[0]
                pixel[1] = pixel[0]
                pixel[2] = pixel[0]
        return img

cp = "image3.png"
im = filtros(cp)
img = im.obtener_imagen()
a = im.dithering(img, 2)
cv.imshow("result", a)
cv.waitKey(0)
cv.imwrite("result.png", a)
