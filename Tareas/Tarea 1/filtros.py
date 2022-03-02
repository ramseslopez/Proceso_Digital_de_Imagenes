import numpy as np
import cv2 as cv
import random
import math

class filtros():
    """
    Clase de filtros básicos para imagenes

    author - Ramses Antonio López Soto
                  315319974
    date - febrero 2022
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

    ##### EJERCICIO 1 #####

    def gris(self, img, version):
        """
        Aplica distintas versiones de escala de grises

        Params
        img - imagen
        version - version del filtro
        """
        if version == 1:
            return self.gris_v1(img)
        elif version == 2:
            return self.gris_v2(img)
        elif version == 3:
            return self.gris_v3(img)
        elif version == 4:
            return self.gris_v4(img)
        elif version == 5:
            return self.gris_v5(img)
        elif version == 6:
            return self.gris_v6(img)
        elif version == 7:
            return self.gris_v7(img)
        elif version == 8:
            return self.gris_v8(img)
        elif version == 9:
            return self.gris_v9(img)
        elif version == 10:
            return self.gris_v10(img)
        else:
            print("Numero no valido")
            exit(0)

    def gris_v1(self, img):
        """
        Aplica una primera version del filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = (pixel[0] + pixel[1] + pixel[2]) // 3
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v2(self, img):
        """
        Aplica una segunda version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = ((pixel[0] * 0.3) + (pixel[1] * 0.59) + (pixel[2] * 0.11))
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v3(self, img):
        """
        Aplica una tercera version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = ((pixel[0] * 0.2126) + (pixel[1] * 0.7152) + (pixel[2] * 0.0722))
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v4(self, img):
        """
        Aplica una cuarta version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = ((pixel[0] * 0.299) + (pixel[1] * 0.587) + (pixel[2] * 0.114))
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v5(self, img):
        """
        Aplica una quinta version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = ((max([pixel[0], pixel[1], pixel[2]])) + (min([pixel[0], pixel[1], pixel[2]]))) / 2
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v6(self, img):
        """
        Aplica una sexta version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = max([pixel[0], pixel[1], pixel[2]])
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v7(self, img):
        """
        Aplica una septima version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                count = min([pixel[0], pixel[1], pixel[2]])
                pixel[0] = count
                pixel[1] = count
                pixel[2] = count
        return img

    def gris_v8(self, img):
        """
        Aplica una octava version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[0] = pixel[2]
                pixel[1] = pixel[2]
                pixel[2] = pixel[2]
        return img

    def gris_v9(self, img):
        """
        Aplica una novena version un filtro gris a la imagen

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

    def gris_v10(self, img):
        """
        Aplica una decima version un filtro gris a la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[0] = pixel[0]
                pixel[1] = pixel[0]
                pixel[2] = pixel[0]
        return img

##### EJERCICIO 2 #####

    def rojo_verde_azul(self, img, type):
        """
        Aplica un filtro rojo, verde, azul según sea el caso

        Params
        img - imagen
        type - tipo de filtro
        """
        if type == 1:
            self.rojo(img)
        elif type == 2:
            self.verde(img)
        elif type == 3:
            self.azul(img)
        else:
            print("Numero no valido")
            exit(0)

    def azul(self, img):
        """
        Aplica un filtro azul a cada pixel

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[1] = 0
                pixel[2] = 0

        return img

    def rojo(self, img):
        """
        Aplica un filtro rojo a cada pixel

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[0] = 0
                pixel[1] = 0
        return img

    def verde(self, img):
        """
        Aplica un filtro rojo a cada pixel

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                pixel[0] = 0
                pixel[2] = 0
        return img

##### EJERCICIO 3 #####

    def mosaico(self, img, x, y):
        """
        Aplica filtro de mosaico a una imagen

        Params
        img -imagen
        x - base del mosaico
        y - altura del mosaico

        Returns
        img - imagen con filtro
        """
        rojos_prom = 0
        verdes_prom = 0
        azules_prom = 0
        rojos = []
        verdes = []
        azules = []
        for i in range(0, self.filas, x):
            for j in range(0, self.columnas, y):
                pixel = img[i][j]
                rojos.append(pixel[2])
                verdes.append(pixel[1])
                azules.append(pixel[0])
        rojos_prom = self.promedioRGB(rojos)
        verdes_prom = self.promedioRGB(verdes)
        azules_prom = self.promedioRGB(azules)
        for i in range(0, self.filas, x):
            for j in range(0, self.columnas, y):
                pixel = img[i][j]
                pixel[2] = rojos_prom
                pixel[1] = verdes_prom
                pixel[0] = azules_prom
        return img

    def promedioRGB(self, list):
        """
        Obtiene el promedio de una lista de números

        Params
        list - lista de numeros

        Returns
        promedio
        """
        promedio = 0
        for p in list:
            promedio += p
        return (promedio / len(list))

##### EJERCICIO 4 #####

    def alto_contraste(self, img):
        """
        Aumenta el contraste de una imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                num_pixel = (pixel[2] << 16) + (pixel[1] << 8) + pixel[0]
                if (num_pixel < 8000000):
                    pixel[0] = 0
                    pixel[1] = 0
                    pixel[2] = 0
                else:
                    pixel[0] = 255
                    pixel[1] = 255
                    pixel[2] = 255
        return img

    def inverso(self, img):
        """
        Invierte los colores de una imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                num_pixel = (pixel[2] << 16) + (pixel[1] << 8) + pixel[0]
                if (num_pixel > 8000000):
                    pixel[0] = 0
                    pixel[1] = 0
                    pixel[2] = 0
                else:
                    pixel[0] = 255
                    pixel[1] = 255
                    pixel[2] = 255
        return img

##### EJERCICIO 5 #####

    def brillo(self, img, brillo):
        """
        Aumenta el brillo de la imagen

        Params
        img - imagen

        Returns
        img - imagen con filtro
        """
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel = img[i][j]
                if (pixel[0] + brillo) > 255:
                    pixel[0] = 255
                elif (pixel[0] + brillo) < 0:
                    pixel[0] = 0
                else:
                    pixel[0] += brillo
                if (pixel[1] + brillo) > 255:
                    pixel[1] = 255
                elif (pixel[1] + brillo < 0):
                    pixel[1] = 0
                else:
                    pixel[1] += brillo
                if (pixel[2] + brillo) > 255:
                    pixel[2] = 255
                elif (pixel[2] + brillo < 0):
                    pixel[2] = 0
                else:
                    pixel[2] += brillo
        return img


#cp = "image.jpg"
#im = filtros(cp)
#img = im.obtener_imagen()
#a = im.mosaico(img, 5, 5)
#cv.imshow("result", a)
#cv.waitKey()
