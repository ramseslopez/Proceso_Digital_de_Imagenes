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

    def contraste(self, img):
        """
        Aplica un contraste a una imagen en tonos de gris

        Params
        img - imagen

        Returns
        imagen modificada
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
        """
        Aplica una ecualización a una imagen en tonos de gris

        Params
        img - imagen

        Returns
        imagen modificada
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

        cdf_l = [0] * 256
        cdf_l[0] = freq_grises[0]
        for f in range(1, len(freq_grises)):
            suma = cdf_l[f - 1] + freq_grises[f]
            cdf_l[f] = suma

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                gris = g_img[i,j][2]

                n_pixel = round(((cdf_l[gris] - 1) / cdf_l[255]) * 255)

                g_img[i,j][2] = n_pixel
                g_img[i,j][1] = n_pixel
                g_img[i,j][0] = n_pixel

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
