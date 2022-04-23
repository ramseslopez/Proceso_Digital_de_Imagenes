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

    def oleo(self, img, rad):
        """
        Difumina la imagen simulando
        una pintura

        Params
        img - imagen
        rad - radio

        Returns
        imagen procesada
        """

        print("Procesando imagen")

        o_img = img.copy()

        prom_red = dict()
        prom_green = dict()
        prom_blue = dict()

        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                max_r = -1
                max_g = -1
                max_b = -1
                for h in range(i, i+rad):
                    if h >= self.filas:
                        break
                    for k in range(j,j+rad):
                        if k >= self.columnas:
                            break
                        red = o_img[h,k][2]
                        green = o_img[h,k][1]
                        blue = o_img[h,k][0]

                        if max_r == -1:
                            max_r = red
                            max_g = green
                            max_b = blue

                        if red in prom_red:
                            prom_red[red] += 1
                            if prom_red[max_r] > prom_red[red]:
                                max_r = max_r
                            else:
                                max_r = red
                        else:
                            prom_red[red] = 1

                        if green in prom_green:
                            prom_green[green] += 1
                            if prom_green[max_g] > prom_green[green]:
                                max_g = max_g
                            else:
                                max_g = green
                        else:
                            prom_green[green] = 1

                        if blue in prom_blue:
                            prom_blue[blue] += 1
                            if prom_blue[max_b] > prom_blue[blue]:
                                max_b = max_b
                            else:
                                max_b = blue
                        else:
                            prom_blue[blue] = 1

                o_img[i,j][2] = max_r
                o_img[i,j][1] = max_g
                o_img[i,j][0] = max_b

                prom_red.clear()
                prom_blue.clear()
                prom_green.clear()

        print("Imagen procesada")

        return o_img

    def oleo_gris(self, img, rad):
        """
        Difumina la imagen simulando
        una pintura en escala de grises

        Params
        img - imagen
        rad - radio

        Returns
        imagen procesada
        """
        return self.gris(self.oleo(img,rad))


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
