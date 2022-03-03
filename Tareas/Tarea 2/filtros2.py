import numpy as np
import cv2 as cv
import random
import math
from PIL import ImageTk, Image

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
        """
        for i in range(self.filas):
            for j in range(self.columnas):
                pixel = img[i][j]
                r = pixel[2]
                g = pixel[1]
                b = pixel[0]
                pixel[0] = blue & b
                pixel[1] = green & g
                pixel[2] = red & r
                img[i][j][0] = pixel[0]
                img[i][j][1] = pixel[1]
                img[i][j][2] = pixel[2]
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

        w = self.filas
        h = self.columnas

        filter_w = len(m)
        filter_h = len(m[0])

        imgCopy = img.copy()

        for x in range(0, w):
            for y in range(0, h):
                red = 0.0
                green = 0.0
                blue = 0.0
                for filter_y in range(0, filter_h):
                    for filter_x in range(0, filter_w):
                        img_x = int((x - (filter_w / 2) + filter_y + w) % w)
                        img_y = int((y - (filter_h / 2) + filter_x + h) % h)

                        red += imgCopy[img_x][img_y][2] * m[filter_y][filter_x]
                        green += imgCopy[img_x][img_y][1] * m[filter_y][filter_x]
                        blue += imgCopy[img_x][img_y][0] * m[filter_y][filter_x]
                img[x][y][2] = int(min(max(int(factor * red + bias), 0), 255))
                img[x][y][1] = int(min(max(int(factor * green + bias), 0), 255))
                img[x][y][0] = int(min(max(int(factor * blue + bias), 0), 255))
        return img

#Blur (difumina una imagen - la hace borrosa) ===
#Motion blur (efecto de foto movida) ===
#Find edge (encuentra bordes) ===
#    *vertical ===
#    *horizontal ===
#    *45° ===
#    *bordes en todas direcciones ===
#Sharpen (la imagen es más precisa) ===
#Emboss (encuentra bordes y los pone en relieve 3D) ===
#Promedio (mean)
#Mediano
# micaRGB

cp = "photo.png"
im = filtros(cp)
img = im.obtener_imagen()
#cv.imshow("a", img)
a = im.mica_RGB(img, 155, 44, 98)
cv.imshow("result", a)
cv.waitKey()
