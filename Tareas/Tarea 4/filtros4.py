import numpy as np
import cv2 as cv
#import imgkit

class filtros():
    """
    Clase de filtros ascii para imagenes

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

        Returns
        imagen original
        """
        return self.img

    def marca_agua(self, img, marca, x, y, color, tamanio, transparencia):

        for i in range(0, self.filas):
            for j in range(0, self.columnas):

                if i == x and j == y:
                    for k in range(0, len(marca)):
                        tam = k * tamanio
                        img[i,j][2] = img[(i+tam),j][2]
                        img[i,j][1] = img[(i+tam),j][1]
                        img[i,j][0] = img[(i+tam),j][0]
                        red = (transparencia * color) + (1 - transparencia) * red
                        green = (transparencia * color) + (1 - transparencia) * green
                        blue = (transparencia * color) + (1 - transparencia) * blue
        return img



    def quitar_marca_agua(self, img):
        red_w = 185
        green_w = 175
        blue_w = 235
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                red = img[i,j][2]
                green = img[i,j][1]
                blue = img[i,j][0]
                if red > (green + 15) and red > (blue + 15):
                    rest_r = red_w - red
                    rest_g = green_w - green
                    rest_b = blue_w - blue
                    prom = (rest_r + rest_g + rest_b) // 3
                    if prom < 25:
                        red = 255
                        green = 255
                        blue = 255
                    elif prom > 103:
                        red = 0
                        green = 0
                        blue = 0
                    else:
                        red = (img[i,j][2] + img[i,j][1] + img[i,j][0]) // 3
                        green = (img[i,j][2] + img[i,j][1] + img[i,j][0]) // 3
                        blue = (img[i,j][2] + img[i,j][1] + img[i,j][0]) // 3
                img[i,j][2] = red
                img[i,j][1] = green
                img[i,j][0] = blue
        return img

    def rgb_to_hex(self, r, g, b):
        """
        Convierte un color RGB a Hexadecimal

        Params
        r - color rojo
        g - color verde
        b - color azul

        Returns
        RGB convertido a Hexadecimal
        """
        return ("#{:02x}{:02x}{:02x}").format(r, g, b)

c = "WhatsApp Image 2022-03-18 at 8.50.57 AM.jpeg"
cp = filtros(c)
im = cp.obtener_imagen()
a = cp.quitar_marca_agua(im)
cv.imshow("result", a)
cv.waitKey() 
