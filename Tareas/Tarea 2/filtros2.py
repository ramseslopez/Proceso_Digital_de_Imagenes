import numpy as np
import cv2 as cv
import random
import math
import statistics as st

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
        """
        Coloca una mica sobre la imagen

        Params
        img - imagen
        red - componente rojo
        green - componente verde
        blue - componente azul

        Returns
        imagen modificada
        """
        for i in range(self.filas):
            for j in range(self.columnas):
                pixel = img[i][j]
                pixel[0] = blue & pixel[0]
                pixel[1] = green & pixel[1]
                pixel[2] = red & pixel[2]
        return img

    def convolucion(self, img, option):
        """
        Realiza distintos filtros de convolucion

        Params
        img - imagen de entrada
        option - tipo de filtro de convolucion

        Returns
        imagen modificada
        """
         # ========= BLUR =========
        if option == 1: # blur v1
            m = [
                        [0.0, 0.2,  0.0],
                        [0.2, 0.2,  0.2],
                        [0.0, 0.2,  0.0]
                    ]
            factor = 1.0
            bias = 0.0

        if option == 2: #blur v2
            m = [
                        [0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 0],
                        [1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 1, 0, 0]
                   ]
            factor = 1.0 / 13.0
            bias = 0.0

            # ========= MOTION BLUR =========
        if option == 3: #motion blur
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

            # ========= EMBOSS =========
        if option == 4: #emboss 45°
            m = [
                        [-1, -1, 0],
                        [-1, 0, 1],
                        [0, 1, 1]
                    ]
            factor = 1.0
            bias = 128.0

        if option == 5: #emboss exagerado
            m = [
                        [-1, -1, -1, -1, 0],
                        [-1, -1, -1, 0, 1],
                        [-1, -1, 0, 1, 1],
                        [-1, 0, 1, 1, 1],
                        [0, 1, 1, 1, 1]
                    ]
            factor = 1.0
            bias = 128.0

            # ========= SHARPEN =========
        if option == 6: # sharpen agudo
            m = [
                         [-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]
                   ]
            factor = 1.0
            bias = 0.0

        if option == 7: # sharpen sutil
            m = [
                          [-1, -1, -1, -1, -1],
                          [-1, 2, 2, 2, -1],
                          [-1, 2, 8, 2, -1],
                          [-1, 2, 2, 2, -1],
                          [-1, -1, -1, -1, -1]
                   ]
            factor = 1.0 / 8.0
            bias = 0.0

        if option == 8: # sharpen exagerado
            m = [
                        [1,  1,  1],
                        [1, -7,  1],
                        [1,  1,  1]
                   ]
            factor = 1.0
            bias = 0.0

            # ========= FIND EDGES =========
        if option == 9: # find edges horizontal
            m = [
                         [0,  0, -1,  0,  0],
                         [0,  0, -1,  0,  0],
                         [0,  0,  2,  0,  0],
                         [0,  0,  0,  0,  0],
                         [0,  0,  0,  0,  0]
                  ]
            factor = 1.0
            bias = 0.0

        if option == 10: # find edges vertical
            m =[
                        [0,  0,  0,  0,  0],
                        [0,  0,  0,  0,  0],
                        [-1,  -1,  4,  -1,  -1],
                        [0,  0, 0,  0,  0],
                        [0,  0, 0,  0,  0]
                  ]
            factor = 1.0
            bias = 0.0

        if option == 11: # find edges 45°
            m =[
                        [-1,  0,  0,  0,  0],
                        [0, -2,  0,  0,  0],
                        [0,  0,  6,  0,  0],
                        [0,  0,  0, -2,  0],
                        [0,  0,  0,  0, -1]
                  ]
            factor = 1.0
            bias = 0.0

        if option == 12: # find edges todas direcciones
            m =[
                        [-1,  0,  0,  0,  0],
                        [0, -2,  0,  0,  0],
                        [0,  0,  6,  0,  0],
                        [0,  0,  0, -2,  0],
                        [0,  0,  0,  0, -1]
                  ]
            factor = 1.0
            bias = 0.0

            # ========= MEAN =========
        if option == 13: # mean
            m =[
                        [1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]
                  ]
            factor = 1.0 / 9.0
            bias = 0.0

        w = self.filas
        h = self.columnas

        filter_w = len(m)
        filter_h = len(m[0])

        img_copy = img.copy()

        for x in range(0, w):
            for y in range(0, h):
                red = 0.0
                green = 0.0
                blue = 0.0
                for filter_y in range(0, filter_h):
                    for filter_x in range(0, filter_w):
                        img_x = int((x - (filter_w / 2) + filter_y + w) % w)
                        img_y = int((y - (filter_h / 2) + filter_x + h) % h)
                        red += img_copy[img_x][img_y][2] * m[filter_y][filter_x]
                        green += img_copy[img_x][img_y][1] * m[filter_y][filter_x]
                        blue += img_copy[img_x][img_y][0] * m[filter_y][filter_x]
                img[x][y][2] = int(min(max(int(factor * red + bias), 0), 255))
                img[x][y][1] = int(min(max(int(factor * green + bias), 0), 255))
                img[x][y][0] = int(min(max(int(factor * blue + bias), 0), 255))
        return img

    def median(self, img):

        m = [
                    [22, 24, 27],
                    [31, 98, 29],
                    [27, 22, 23],
               ]

        w = self.filas
        h = self.columnas

        filter_w = len(m)
        filter_h = len(m[0])

        img_copy = img.copy()

        for x in range(0,w):
            for y in range(0, h):
                red = []
                green = []
                blue = []
                for filter_y in range(0, filter_h):
                    for filter_x in range(0, filter_w):
                        img_x = int((x - (filter_w / 2) + filter_y + w) % w)
                        img_y = int((x - (filter_w / 2) + filter_x + y) % w)
                        red.append(img_copy[img_x][img_y][2])
                        green.append(img_copy[img_x][img_y][1])
                        blue.append(img_copy[img_x][img_y][0])

                red.sort()
                green.sort()
                blue.sort()

                img[x][y][2] = self.media(red)
                img[x][y][1] = self.media(green)
                img[x][y][0] = self.media(blue)


        return img

    def media(self, list):
        m = float(len(list)) / 2
        if m % 2 != 0:
            return list[int(m - .5)]
        else:
            return (list[int(m)], list[int(m - 1)])


    def gris(self, img):
        """
        Aplica un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[0] = pixel[1]
                pixel[1] = pixel[1]
                pixel[2] = pixel[1]
        return img


#cp = "noise.png"
#im = filtros(cp)
#img = im.obtener_imagen()
#cv.imshow("a", img)
#a = im.median(img)
#a= im.gris(a)
#cv.imshow("result", a)
#cv.waitKey()
