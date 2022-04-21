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

    def oleo(self, img):
        return img

    def img_recursiva(self, img, x, y):
        g_img = self.gris(img.copy())
        cx = 0
        cy = 0
        grays = 0
        reg = 0

        gen_imgs = self.genera_imgs(img)

        for i in range(0, self.filas, x):
            for j in range(0, self.columnas, y):
                for h in range(i, x + i):
                    for k in range(j,  y + j):
                        red = g_img[h,k][2]
                        green = g_img[h,k][1]
                        blue = g_img[h,k][0]
                        grays += blue
                        reg += 1

                pr = grays // reg
                grays = 0
                reg = 0


                if pr >= 0 and pr <= 8:
                    img_r = gen_imgs[0]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 8 and pr <= 16:
                    img_r = gen_imgs[1]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cy : cy + img_r.shape[0], cx : cx +img_r.shape[1]] = img_r
                elif pr > 16 and pr <= 24:
                    img_r = gen_imgs[2]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 24 and pr <= 32:
                    img_r = gen_imgs[3]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 32 and pr <= 40:
                    img_r = gen_imgs[4]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 40 and pr <= 48:
                    img_r = gen_imgs[5]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 48 and pr <= 56:
                    img_r = gen_imgs[6]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 56 and pr <= 64:
                    img_r = gen_imgs[7]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 64 and pr <= 72:
                    img_r = gen_imgs[8]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 72 and pr <= 80:
                    img_r = gen_imgs[9]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 80 and pr <= 88:
                    img_r = gen_imgs[10]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 88 and pr <= 96:
                    img_r = gen_imgs[11]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 96 and pr <= 104:
                    img_r = gen_imgs[12]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 104 and pr <= 112:
                    img_r = gen_imgs[13]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 112 and pr <= 120:
                    img_r = gen_imgs[14]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 120 and pr <= 128:
                    img_r = gen_imgs[15]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 128 and pr <= 136:
                    img_r = gen_imgs[16]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 136 and pr <= 144:
                    img_r = gen_imgs[17]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 144 and pr <= 152:
                    img_r = gen_imgs[18]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 152 and pr <= 160:
                    img_r = gen_imgs[19]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 160 and pr <= 168:
                    img_r = gen_imgs[20]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 168 and pr <= 176:
                    img_r = gen_imgs[21]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 176 and pr <= 184:
                    img_r = gen_imgs[22]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 184 and pr <= 192:
                    img_r = gen_imgs[23]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 192 and pr <= 200:
                    img_r = gen_imgs[24]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 200 and pr <= 208:
                    img_r = gen_imgs[25]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 208 and pr <= 216:
                    img_r = gen_imgs[26]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 216 and pr <= 224:
                    img_r = gen_imgs[27]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 224 and pr <= 232:
                    img_r = gen_imgs[28]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 232 and pr <= 240:
                    img_r = gen_imgs[29]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 240 and pr <= 248:
                    img_r = gen_imgs[30]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r
                elif pr > 248 and pr < 256:
                    img_r = gen_imgs[31]
                    img_r = cv.resize(img_r, (x,y), interpolation = cv.INTER_AREA)
                    g_img[cx : cx + img_r.shape[1], cy : cy + img_r.shape[0]] = img_r

                cy += y
            cx += x
            cy = 0
        cx = 0

        return g_img

    def img_recursiva_color(self, img, x, y):
        c_img = img.copy()
        cx = 0
        cy = 0
        reds = 0
        greens = 0
        blues = 0
        reg = 0

        for i in range(0, self.filas, x):
            for j in range(0, self.columnas, y):
                for h in range(i, x + i):
                    for k in range(j, y + j):
                        red = c_img[h, k][2]
                        green = c_img[h, k][1]
                        blue = c_img[h, k][0]
                        reds += red
                        greens += green
                        blues += blue
                        reg += 1

                prom_red = reds // reg
                prom_green = greens //  reg
                prom_blue = blues // reg

                reds = 0
                greens = 0
                blues = 0
                reg = 0

                s_img = self.mica_RGB(c_img.copy(), prom_red, prom_green, prom_blue)
                s_img = cv.resize(s_img, (x,y), interpolation = cv.INTER_AREA)
                c_img[cx : cx + s_img.shape[1], cy : cy + s_img.shape[0]] = s_img

                cy += y
            cx += x
            cy = 0
        cx = 0

        return c_img





    def genera_imgs(self, img):
        g_img = self.gris(img)
        cont = 0
        gen_imgs = []

        bf = -127
        bt = 127

        print("Generando imágenes ...")
        while bf <= bt:
            b_img = self.brillo(img.copy(), bf)
            gen_imgs.append(b_img)
            cont += 1
            bf += 8
        print("Imágenes generadas")

        return gen_imgs



    def brillo(self, img, brillo):
        """
        Aumenta o disminuye el brillo de la imagen

        Params
        img - imagen

        Returns
        imagen con filtro aplicado
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

cp = "image3.png"
im = filtros(cp)
img = im.obtener_imagen()
a = im.img_recursiva(img, 5, 5)
cv.imshow("result", a)
cv.waitKey()
cv.imwrite("result.png", a)
#x = 0
#y = 0
#g_img = im.gris(img)
#img_r = cv.imread("./g_imgs/g_img1.png")
#mg_r = cv.resize(img_r, (50,50), interpolation = cv.INTER_AREA)
#g_img[y : y + img_r.shape[0], x : x + img_r.shape[1]] = img_r
#cv.imshow("result", g_img)
#cv.waitKey()
#cv.imwrite("result.png", g_img)
