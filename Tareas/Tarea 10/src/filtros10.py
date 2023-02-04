import os
import numpy as np
import cv2 as cv
import random
import math
import glob

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
        """
        Realiza el fotomosaico de la imagen

        Params
        img - imagen a manipular
        x - base del mosaico
        y - altura del mosaico

        Returns
        imagen modificada
        """
        f_img = img.copy()
        cx = 0
        cy = 0

        for i in range(0, f_img.shape[0], y):
            for j in range(0, f_img.shape[1], x):
                reds = []
                greens = []
                blues = []
                for h in range(i, x + i):
                    if h >= f_img.shape[0]:
                        break
                    for k in range(j, y + j):
                        if k >= f_img.shape[1]:
                            break
                        reds.append(f_img[h,k][2])
                        greens.append(f_img[h,k][1])
                        blues.append(f_img[h,k][0])

                prom_red = sum(reds) // len(reds)
                prom_green = sum(greens) //  len(greens)
                prom_blue = sum(blues) // len(blues)

                reds.clear()
                greens.clear()
                blues.clear()

                print("PRED",prom_red)
                print("PGREEN", prom_green)
                print("PBLUE",prom_blue)

                s_img = self.elegir_imagen(self.obtener_imagenes(), prom_red, prom_green, prom_blue)
                s_img = cv.resize(s_img, (y,x), interpolation = cv.INTER_AREA)
                if cx != cy:
                    break
                f_img[cx : s_img.shape[1] + cx, cy : s_img.shape[0] + cy] = s_img

                cy += y
            cx += x
            cy = 0
        cx = 0
        #print("TERMINE FM")
        return f_img

    def euclidiana(self, r1, g1, b1, r2, g2, b2):
        """
        Calculata la euclidiana de dos pixeles

        Params
        r1 - color rojo
        r2 - color rojo
        g1 - color verde
        g2 - color verde
        b1 - color azul
        b2 - color azul

        Returns
        valor de la euclidiana
        """
        re = (r1 - r2) ** 2
        ge = (g1 - g2) ** 2
        be = (b1 - b2) ** 2
        ec = re + ge + be
        return math.sqrt(ec)

    def obtener_imagenes(self):
        """
        Metodo que se encarga de recopilar
        las imagenes

        Returns
        Lista de imagenes
        """
        cv_img = []
        input_images_path = "img2"
        files_names = os.listdir(input_images_path)
        for file_name in files_names:
            image_path = input_images_path + "/" + file_name
            image = cv.imread(image_path)
            if image is None:
                continue
            cv_img.append(image)
        return cv_img

    def prom_imagen(self, imgg):
        """
        Se encarga de obtener el color promedio
        de una region

        Params
        imgg - imagen 

        Return
        Lista con el color promedio
        """
        reds = []
        greens = []
        blues = []
        for i in range(0, imgg.shape[0]):
            for j in range(0, imgg.shape[1]):
                red = imgg[i,j][2]
                green = imgg[i,j][1]
                blue = imgg[i,j][0]
                reds.append(red)
                blues.append(green)
                greens.append(blue)

        prom_red = sum(reds) // len(reds)
        prom_green = sum(greens) //  len(greens)
        prom_blue = sum(blues) // len(blues)
        #print("RED", prom_red)
        #print("BLUE", prom_blue)
        #print("GREEN", prom_green)
        reds.clear()
        greens.clear()
        blues.clear()

        return [prom_blue, prom_green, prom_red]


    def elegir_imagen(self, lst, r, g, b):
        """
        Metodo que se encarga de elegir
        una imagen parecida al color rgb

        Params
        lst - lista de imagenes
        r - color rojo promedio
        g - color verde promedio
        b - color azul promedio
        """
        n = None
        imagen = None
        #d2 = self.euclidiana(prom[2], prom[1], prom[0], r, g, b)
        for i in lst:
            prom = self.prom_imagen(i)
            relem = prom[2]
            gelem = prom[1]
            belem = prom[2]
            dis = self.euclidiana(r,g,b,relem,gelem,belem)
            if(n == None):
                n = dis
                imagen = i
            if(dis < n):
                n = dis
                imagen = i
        print("ELEGI IMAGEN")
        return imagen


#cp = filtros("image.jpg")
#img = cp.obtener_imagen()
#a = cp.fotomosaico(img, 100, 100)
#a = cp.elegir_imagen(cp.obtener_imagenes(), 47, 126, 204)
#cv.imshow("result", a)
#cv.waitKey(0)
#print(cp.elegir_imagen()
#print(cp.prom_imagen(img))
