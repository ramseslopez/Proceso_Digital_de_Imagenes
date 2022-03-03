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
        for i in range(self.filas):
            for j in range(self.columnas):
                #pixel = img[i][j]
                img[i][j][0] = b and img[i][j][0]
                img[i][j][1] = g and img[i][j][1]
                img[i][j][2] = r and img[i][j][2]
        return img

    def convolucion(self, img, option):
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
        if option == 4: #emboss
            m = [
                        [-1, -1, -1, -1, 0],
                        [-1, -1, -1, 0, 1],
                        [-1, -1, 0, 1, 1],
                        [-1, 0, 1, 1, 1],
                        [0, 1, 1, 1, 1]
                    ]
            factor = 1.0
            bias = 128.0
        if option == 5: # sharpen
            m = [
                        [1,  1,  1],
                        [1, -7,  1],
                        [1,  1,  1]
                   ]
            factor = 1.0
            bias = 0.0
        if option == 6: # sharpen horizontal
            m = [
                         [0,  0, -1,  0,  0],
                         [0,  0, -1,  0,  0],
                         [0,  0,  2,  0,  0],
                         [0,  0,  0,  0,  0],
                         [0,  0,  0,  0,  0]
                  ]
            factor = 1.0
            bias = 0.0
        if option == 7: #sharpen vertical
            m =[
                        [0,  0, -1,  0,  0],
                        [0,  0, -1,  0,  0],
                        [0,  0,  4,  0,  0],
                        [0,  0, -1,  0,  0],
                        [0,  0, -1,  0,  0]
                  ]
            factor = 1.0
            bias = 0.0
        if option == 8: # sharpen 45°
            m =[
                        [-1,  0,  0,  0,  0],
                        [0, -2,  0,  0,  0],
                        [0,  0,  6,  0,  0],
                        [0,  0,  0, -2,  0],
                        [0,  0,  0,  0, -1]
                  ]
            factor = 1.0
            bias = 0.0
        if option == 9: # sharpen todas direcciones
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
#Find edge (encuentra bordes)
#    *vertical
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
a = im.convolucion(img, 7)
cv.imshow("result", a)
cv.waitKey()
