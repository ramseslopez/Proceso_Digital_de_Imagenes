import numpy as np
import cv2 as cv
import random
import math

class filtros():
    """
    Clase de filtros básicos para imagenes

    author - Ramses López
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
        Aplica una sexta version un filtro gris a la imagen

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
        n - base del mosaico
        m - altura del mosaico

        Returns
        img - imagen con filtro
        """
        img_w = self.columnas
        img_h = self.filas
        limit_w = img_w // x
        limit_h = img_h // y
        rojos_prom = 0
        verdes_prom = 0
        azules_prom = 0
        #rojos = []
        #verdes = []
        #azules = []
        for z in range(0, limit_h):
            for w in range(0, limit_w):
                rojos = []
                verdes = []
                azules = []
                for i in range(x * w, x * (w + 1)):
                    for j in range(y * z, y * (z + 1)):
                        pixel = img[j][i]
                        rojos.append(pixel[2])
                        verdes.append(pixel[1])
                        azules.append(pixel[0])
                        rojos_prom = self.promedioRGB(rojos)
                        verdes_prom = self.promedioRGB(verdes)
                        azules_prom = self.promedioRGB(azules)
                img = self.rgb_prom(img, x * w, x * (w + 1), y * z,y * (z + 1), rojos_prom, verdes_prom, azules_prom)
        if img_w % x != 0:
            for w in range(0, img_h):
                rojos = []
                verdes = []
                azules = []
                for j in range(x * limit_w, img_w):
                    for i in range(y * w, y * (w + 1)):
                        pixel = img[i][j]
                        rojos.append(pixel[2])
                        verdes.append(pixel[1])
                        azules.append(pixel[0])
                        rojos_prom = self.promedioRGB(rojos)
                        verdes_prom = self.promedioRGB(verdes)
                        azules_prom = self.promedioRGB(azules)
                img = self.rgb_prom(img, x * limit_w, img_w, y * w,y * (w + 1), rojos_prom, verdes_prom, azules_prom)
        if img_h % y != 0:
            for w in range(0, limit_w):
                rojos = []
                verdes = []
                azules = []
                for i in range(x * w, x * (w + 1)):
                    for j in range(y * limit_h, img_h):
                        pixel = img[j][i]
                        rojos.append(pixel[2])
                        verdes.append(pixel[1])
                        azules.append(pixel[0])
                        rojos_prom = self.promedioRGB(rojos)
                        verdes_prom = self.promedioRGB(verdes)
                        azules_prom = self.promedioRGB(azules)
                img = self.rgb_prom(img, x * w, x * (w + 1), y * limit_h, img_h, rojos_prom, verdes_prom, azules_prom)
            rojos = []
            verdes = []
            azules = []
            for i in range(x * limitW, img_w):
                for j in range(y * limit_h, img_h):
                    pixel = img[j][i]
                    rojos.append(pixel[2])
                    verdes.append(pixel[1])
                    azules.append(pixel[0])
                    rojos_prom = self.promedioRGB(rojos)
                    verdes_prom = self.promedioRGB(verdes)
                    azules_prom = self.promedioRGB(azules)
            img = self.rgb_prom(img, x * limit_w, imageW, y * limit_h, img_h, rojos_prom, verdes_prom, azules_prom)
        return img



    def promedioRGB(self, list):
        promedio = 0
        for p in list:
            promedio += p
        return (promedio // len(list))

    def rgb_prom(self, img, ii, fi, ij, fj, r, g, b):
        for i in range(ii, fj):
            for j in range(ij, fj):
                pixel = img[i][j]
                pixel[0] = b
                pixel[1] = g
                pixel[2] = r
        return img

    def mosaico2(self, img, ancho, altura):
        """
        Aplica filtro de mosaico a una imagen

        Params
        n - base del mosaico
        m - altura del mosaico
        """
        x = ancho
        y = altura
        if x != 1 or y != 1:
            for i in range(x, self.columnas, x):
                for j in range(y, self.filas, y):
                    img = self.m(img, i - x, j - y, x, y)
            if (i - x) < self.columnas:
                for k in range(0, self.filas, y):
                    img = self.m(img, k, i - x, self.columnas - (i - x), y)
            if (j - y) < self.columnas:
                for k in range(0, self.columnas, x):
                    img = self.m(img, k, j - y, x, self.filas - (j - y))

        return img

    def m(self, img, ini, fin, w, h):
        rojos = []
        verdes = []
        azules = []
        prom_rojos = 0
        prom_verdes = 0
        prom_azules = 0
        pixeles = self.columnas * self.filas
        for k in range(0, self.filas):
            for h in range(0, self.columnas):
                pixel = img[k][h]
                rojos.append(pixel[0])
                verdes.append(pixel[1])
                azules.append(pixel[2])
        prom_rojos = self. promedioRGB(rojos)
        prom_verdes = self.promedioRGB(verdes)
        prom_azules = self.promedioRGB(azules)
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                pixel= img[i][j]
                pixel[2] = prom_rojos
                pixel[1] = prom_verdes
                pixel[0] = prom_azules
        return img


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
                elif (pixel[0] + brillo < 0):
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
#a = im.brillo(img, -255)
#cv.imshow("result", a)
#cv.waitKey()
