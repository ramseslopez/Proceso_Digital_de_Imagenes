import os
import numpy as np
import cv2 as cv
import random
import time
from tqdm import tqdm

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
        """
        return self.img

    def contraste(self, img):
        """
        Aplica un contrate a una imagen en tonos de gris
        """
        g_img = self.gris(img.copy())
        grises = dict()

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris = g_img[i, j][2]

                if gris in grises:
                    grises[gris] += 1
                else:
                    grises[gris] = 1

        freq_grises = list(grises.values())

        print(freq_grises)

        freq_grises.sort()

        print(freq_grises)

        max = freq_grises[-1]
        min = freq_grises[0]

        valor = abs(max - min)

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris_ = g_img[i, j][2]

                n_pixel = (gris_ - min // valor) * 255

                g_img[i, j][2] = n_pixel
                g_img[i, j][1] = n_pixel
                g_img[i, j][0] = n_pixel

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
a = im.contraste(img)
cv.imshow("result", a)
cv.waitKey(0)
