import numpy as np
import cv2 as cv

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
        """
        return self.img

    def letras(self, img):
        """
        Convierte la imagen a un ascii

        Params
        img - imagen

        Returns
        imagen en formato de texto
        """
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        for i in range(0, self.filas):
            letra +="<br>"
            for j in range(0, self.columnas):
                gris = ((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11))
                if (gris >= 0 and gris <= 15):
                    letra += "<font color = #000000>" + 'M'
                if (gris > 15 and gris <= 31):
                    letra += "<font color = #000000>" + 'N'
                if (gris > 31 and gris <= 47):
                    letra += "<font color = #000000>" + 'H'
                if (gris > 47 and gris <= 63):
                    letra += "<font color = #000000>" + '#'
                if (gris > 63 and gris <= 79):
                    letra += "<font color = #000000>" + 'Q'
                if (gris > 79 and gris <= 95):
                    letra += "<font color = #000000>" + 'U'
                if (gris > 95 and gris <= 111):
                    letra += "<font color = #000000>" + 'A'
                if (gris > 111 and gris <= 127):
                    letra += "<font color = #000000>" + 'D'
                if (gris > 127 and gris <= 143):
                    letra += "<font color = #000000>" + '0'
                if (gris > 143 and gris <= 159):
                    letra += "<font color = #000000>" + 'Y'
                if (gris > 159 and gris <= 175):
                    letra += "<font color = #000000>" + '2'
                if (gris > 175 and gris <= 191):
                    letra += "<font color = #000000>" + '$'
                if (gris > 191 and gris <= 209):
                    letra += "<font color = #000000>" + '%'
                if (gris > 209 and gris <= 225):
                    letra += "<font color = #000000>" + '+'
                if (gris > 225 and gris <= 239):
                    letra += "<font color = #000000>" + '.'
                if (gris > 239 and gris <= 255):
                    letra += "<font color = #000000>" + ' '
        return letra

    def letras_color(self, img):
        """
        Convierte la imagen a un ascii respetando los colores

        Params
        img - imagen

        Returns
        imagen en formato de texto
        """
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        for i in range(0, self.filas):
            letra +="<br>"
            for j in range(self.columnas):
                letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'M'
        return letra

    def letras_gris(self, img):
        """
        Convierte la imagen a un ascii en escala de grises

        Params
        img - imagen

        Returns
        imagen en formato de texto
        """
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        for i in range(0, self.filas):
            letra +="<br>"
            for j in range(self.columnas):
                gris = int(((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11)))
                letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'M'
        return letra

    def rgb_to_hex(self, r,g,b):
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


#cp = "descarga.jpg"
cp="awacatito.jpg"
im = filtros(cp)
img = im.obtener_imagen()

a = im.letras_gris(img)
with open("output.html", mode="w") as f:
    f.write(a)
#a = im.rgb_to_hex(127, 54, 203)
#print(a)
