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
        """
        return self.img

    def contraste(self, img):
        """
        Aplica un contrate a una imagen en tonos de gris
        """
        g_img = self.gris(img)
        grises = dict()

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris = g_img[i, j][2]

                if gris in grises:
                    grises[gris] += 1
                else:
                    grises[gris] = 1

        freq_grises = list(grises.values())

        mx = max(freq_grises)
        mn = min(freq_grises)

        max_t = list(grises.keys())[list(grises.values()).index(mx)]
        min_t = list(grises.keys())[list(grises.values()).index(mn)]

        valor = abs(float(max_t) - float(min_t))

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris = g_img[i, j][2]

                n_pixel = (gris / valor) * 255

                if n_pixel > 255:
                    n_pixel = 255
                if n_pixel < 0:
                    n_pixel = 0

                g_img[i, j][2] = n_pixel
                g_img[i, j][1] = n_pixel
                g_img[i, j][0] = n_pixel


        return g_img


    def ecualizar(self, img):
        g_img = self.gris(img)
        grises = dict()

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris = g_img[i, j][2]

                if gris in grises:
                    grises[gris] += 1
                else:
                    grises[gris] = 1

        freq_grises = list(grises.values())

        cdf_l = self.cdf(freq_grises)

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris = g_img[i,j][2]

                n_pixel = round(((cdf_l[gris] - 1) / cdf_l[255]) * 255)

                g_img[i,j][2] = n_pixel
                g_img[i,j][1] = n_pixel
                g_img[i,j][0] = n_pixel

        return g_img


    def cdf(self, list):
        list_cdf = [0] * 256
        list_cdf[0] = list[0]
        for i in range(1, len(list)):
            suma = list_cdf[i-1] + list[i]
            list_cdf[i] = suma
        return list_cdf


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

cp = "Einstein.jpg"
im = filtros(cp)
img = im.obtener_imagen()
a = im.ecualizar(img)
#print(a)
cv.imshow("result", a)
cv.waitKey(0)
cv.imwrite("result.png", a)
