import numpy as np
import cv2 as cv

class filtros():

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

    def mostrar_imagen(self):
        """
        Muestra la imagen
        """
        cv.imshow("Original", self.img)
        cv.waitKey()
        #return self.img

    ##### EJERCICIO 1 #####

    def gris(self, version):
        if version == 1:
            self.gris_v1()
        elif version == 2:
            self.gris_v2()
        elif version == 3:
            self.gris_v3()
        elif version == 4:
            self.gris_v4()
        elif version == 4:
            self.gris_v4()
        elif version == 5:
            self.gris_v5()
        elif version == 6:
            self.gris_v6()
        elif version == 7:
            self.gris_v7()
        else:
            return

    def gris_v1(self):
        """
        Aplica una primera version del filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = (pixel[0] + pixel[1] + pixel[2]) // 3
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v1", self.img)
        cv.waitKey()
        #return self.img

    def gris_v2(self):
        """
        Aplica una segunda version un filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = ((pixel[0] * 0.3) + (pixel[1] * 0.59) + (pixel[2] * 0.11))
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v2", self.img)
        cv.waitKey()
        #return self.img

    def gris_v3(self):
        """
        Aplica una tercera version un filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = ((pixel[0] * 0.2126) + (pixel[1] * 0.7152) + (pixel[2] * 0.0722))
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v3", self.img)
        cv.waitKey()
        #return self.img

    def gris_v4(self):
        """
        Aplica una cuarta version un filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = ((pixel[0] * 0.299) + (pixel[1] * 0.587) + (pixel[2] * 0.114))
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v4", self.img)
        cv.waitKey()
        #return self.img

    def gris_v5(self):
        """
        Aplica una quinta version un filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = ((max([pixel[0], pixel[1], pixel[2]])) + (min([pixel[0], pixel[1], pixel[2]]))) / 2
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v5", self.img)
        cv.waitKey()
        #return self.img

    def gris_v6(self):
        """
        Aplica una sexta version un filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = max([pixel[0], pixel[1], pixel[2]])
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v6", self.img)
        cv.waitKey()
        #return self.img

    def gris_v7(self):
        """
        Aplica una sexta version un filtro gris a la imagen
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                count = min([pixel[0], pixel[1], pixel[2]])
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        cv.imshow("Gris v7", self.img)
        cv.waitKey()
        #return self.img

##### EJERCICIO 2 #####

    def rojo_verde_azul(self, type):
        if type == 1:
            self.rojo()
        elif type == 2:
            self.verde()
        elif type == 3:
            self.azul()
        else:
            return

    def azul(self):
        """
        Aplica un filtro azul a cada pixel
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                pixel[1] = 0
                pixel[2] = 0
        cv.imshow("Azul", self.img)
        cv.waitKey()
        #return self.img

    def rojo(self):
        """
        Aplica un filtro rojo a cada pixel
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                pixel[0] = 0
                pixel[1] = 0
        cv.imshow("Rojo", self.img)
        cv.waitKey()
        #return self.img

    def verde(self):
        """
        Aplica un filtro rojo a cada pixel
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                pixel[0] = 0
                pixel[2] = 0
        cv.imshow("Verde", self.img)
        cv.waitKey()
        #return self.img

##### EJERCICIO 3 #####


##### EJERCICIO 4 #####

    def inverso(self):
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                num_pixel = (pixel[0] * 255) + (pixel[1] * 16) + (pixel[2])
                if (pixel > 8000000):
                    pixel[0] = 0
                    pixel[1] = 0
                    pixel[2] = 0
                else:
                    pixel[0] = 255
                    pixel[1] = 255
                    pixel[2] = 255
        cv.imshow("Inverso", self.img)
        cv.waitKey()
        #return self.img

##### EJERCICIO 5 #####

    def brillo(self):
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = self.img[i][j]
                pixel[0] += 25
                pixel[1] += 25
                pixel[2] += 25
        cv.imshow("Brillo", self.img)
        cv.waitKey()
        #return self.img






cp = "image.jpg"
im = filtros(cp)
im.inverso()
