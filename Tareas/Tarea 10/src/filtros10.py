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
    date - mayo 2022
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

    def fotomosaico(self, img, x, y):
        f_img = img.copy()
        cx = 0
        cy = 0

        for i in range(0, self.filas, x):
            for j in range(0, self.columnas, y):
                reds = []
                greens = []
                blues = []
                for h in range(i, x + i):
                    for k in range(j, y + j):
                        reds.append(f_img[h, k][2])
                        greens.append(f_img[h, k][1])
                        blues.append(f_img[h, k][0])

                prom_red = sum(reds) // len(reds)
                prom_green = sum(greens) //  len(greens)
                prom_blue = sum(blues) // len(blues)

                reds.clear()
                greens.clear()
                blues.clear()

                cy += y
            cx += x
            cy = 0
        cx = 0

        return f_img

    def euclidiana(self, r1, r2, g1, g2, b1, b2):
        return math.sqrt(pow((r1 - r2), 2) + pow((g1 - g2), 2) + pow((b1 - b2), 2))

    def obtener_imagenes(self):
        contenido = os.listdir("img")
        imagenes = []
        for fichero in contenido:
            if os.path.isfile(os.path.join("img", fichero)) and fichero.endswith(".JPG"):
                imagenes.append(fichero)
        return imagenes

    def prom_imagen(self, img):
        reds = []
        greens = []
        blues = []
        for h in range(0, self.filas):
            for k in range(0, self.columnas):
                reds.append(f_img[h, k][2])
                greens.append(f_img[h, k][1])
                blues.append(f_img[h, k][0])

        prom_red = sum(reds) // len(reds)
        prom_green = sum(greens) //  len(greens)
        prom_blue = sum(blues) // len(blues)

        reds.clear()
        greens.clear()
        blues.clear()

        return [prom_blue, prom_green, prom_red]


cp = filtros("image.jpg")
img = cp.obtener_imagen()
#a = cp.fotomosaico(img, 5, 5)
#cv.imshow("result", a)
#cv.waitKey(0)
cp.obtener_imagenes()
