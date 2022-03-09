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

    def letras_color_v2(self, img):
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        for i in range(0, self.filas):
            letra +="<br>"
            for j in range(self.columnas):
                num_RGB = ((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11))
                if (num_RGB >= 0 and num_RGB <= 15):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'M'
                if (num_RGB > 15 and num_RGB <= 31):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'N'
                if (num_RGB > 31 and num_RGB <= 47):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'H'
                if (num_RGB > 47 and num_RGB <= 63):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '#'
                if (num_RGB > 63 and num_RGB <= 79):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'Q'
                if (num_RGB > 79 and num_RGB <= 95):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'U'
                if (num_RGB > 95 and num_RGB <= 111):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'A'
                if (num_RGB > 111 and num_RGB <= 127):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'D'
                if (num_RGB > 127 and num_RGB <= 143):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '0'
                if (num_RGB > 143 and num_RGB <= 159):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + 'Y'
                if (num_RGB > 159 and num_RGB <= 175):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '2'
                if (num_RGB > 175 and num_RGB <= 191):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '$'
                if (num_RGB > 191 and num_RGB <= 209):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '%'
                if (num_RGB > 209 and num_RGB <= 225):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '+'
                if (num_RGB > 225 and num_RGB <= 239):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + '.'
                if (num_RGB > 239 and num_RGB <= 255):
                    letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + ' '
        return letra

    def letras_gris_v2(self, img):
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        for i in range(0, self.filas):
            letra +="<br>"
            for j in range(self.columnas):
                gris = int(((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11)))
                if (gris >= 0 and gris <= 15):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'M'
                if (gris > 15 and gris <= 31):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'N'
                if (gris > 31 and gris <= 47):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'H'
                if (gris > 47 and gris <= 63):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '#'
                if (gris > 63 and gris <= 79):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'Q'
                if (gris > 79 and gris <= 95):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'U'
                if (gris > 95 and gris <= 111):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'A'
                if (gris > 111 and gris <= 127):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'D'
                if (gris > 127 and gris <= 143):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '0'
                if (gris > 143 and gris <= 159):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + 'Y'
                if (gris > 159 and gris <= 175):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '2'
                if (gris > 175 and gris <= 191):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '$'
                if (gris > 191 and gris <= 209):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '%'
                if (gris > 209 and gris <= 225):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '+'
                if (gris > 225 and gris <= 239):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + '.'
                if (gris > 239 and gris <= 255):
                    letra += "<font color = " + self.rgb_to_hex(gris , gris , gris) + ">" + ' '
        return letra

    def letras_color_text(self, img, text):
        """
        Convierte la imagen a un ascii respetando los colores

        Params
        img - imagen

        Returns
        imagen en formato de texto
        """
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        c = 0
        for i in range(0, self.filas):
            letra +="<br>"
            for j in range(self.columnas):
                if c == len(text):
                    c = 0
                letra += "<font color = " + self.rgb_to_hex(img[i, j][2], img[i, j][1], img[i, j][0]) + ">" + text[c]
                c += 1
        return letra

    def cartas(self, img):
        letra = ""
        for i in range(0, self.filas):
            letra += "\n"
            for j in range(0, self.columnas):
                gris = ((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11))
                if (gris >= 0 and gris <= 23):
                    letra += 'K'
                if (gris > 23 and gris <= 46):
                    letra += 'J'
                if (gris > 46 and gris <= 69):
                    letra += 'I'
                if (gris > 69 and gris <= 92):
                    letra += 'H'
                if (gris > 92 and gris <= 115):
                    letra += 'G'
                if (gris > 115 and gris <= 140):
                    letra += 'F'
                if (gris > 140 and gris <= 163):
                    letra += 'E'
                if (gris > 163 and gris <= 186):
                    letra += 'D'
                if (gris > 186 and gris <= 209):
                    letra += 'C'
                if (gris > 209 and gris <= 232):
                    letra += 'B'
                if (gris > 232 and gris <= 255):
                    letra += 'A'
        return letra

    def cartas_html(self, img):
        letra = "<FONT SIZE = 1 COLOR  = #000008> <pre> <title> Output Image </title>"
        for i in range(0, self.filas):
            letra += "<br>"
            for j in range(0, self.columnas):
                gris = ((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11))
                if (gris >= 0 and gris <= 23):
                    letra += "<font face = 'PlayingCards'>" + 'K'
                if (gris > 23 and gris <= 46):
                    letra += "<font face = 'PlayingCards'>" + 'J'
                if (gris > 46 and gris <= 69):
                    letra += "<font face = 'PlayingCards'>" + 'I'
                if (gris > 69 and gris <= 92):
                    letra += "<font face = 'PlayingCards'>" + 'H'
                if (gris > 92 and gris <= 115):
                    letra += "<font face = 'PlayingCards'>" + 'G'
                if (gris > 115 and gris <= 140):
                    letra += "<font face = 'PlayingCards'>" + 'F'
                if (gris > 140 and gris <= 163):
                    letra += "<font face = 'PlayingCards'>" + 'E'
                if (gris > 163 and gris <= 186):
                    letra += "<font face = 'PlayingCards'>" + 'D'
                if (gris > 186 and gris <= 209):
                    letra += "<font face = 'PlayingCards'>" + 'C'
                if (gris > 209 and gris <= 232):
                    letra += "<font face = 'PlayingCards'>" + 'B'
                if (gris > 232 and gris <= 255):
                    letra += "<font face = 'PlayingCards'>" + 'A'
        return letra

    def dominos(self, img):
        letra = ""
        letra_1 = ""
        letra_2 = ""
        for i in range(0, self.filas):
            letra = "\n"
            for j in range(0, self.columnas):
                gris = ((img[i, j][0] * 0.3) + (img[i, j][1] * 0.59) + (img[i, j][2] * 0.11))
                if (gris >= 0 and gris <= 36):
                    letra_1 = '6'
                    letra_2 = '^'
                    letra += letra_1 + letra_2
                if (gris >=37 and gris <= 72):
                    letra_1 = '5'
                    letra_2 = '%'
                    letra += letra_1 + letra_2
                if (gris >= 73 and gris <= 108):
                    letra_1 = '4'
                    letra_2 = '$'
                    letra += letra_1 + letra_2
                if (gris >= 109 and gris <= 144):
                    letra_1 = '3'
                    letra_2 = '#'
                    letra += letra_1 + letra_2
                if (gris >= 145 and gris <= 180):
                    letra_1 = '2'
                    letra_2 = '@'
                    letra += letra_1 + letra_2
                if (gris >= 181 and gris <= 216):
                    letra_1 = '1'
                    letra_2 = '!'
                    letra += letra_1 + letra_2
                if (gris >= 217 and gris <= 255):
                    letra_1 = '0'
                    letra_2 = ')'
                    letra += letra_1 + letra_2
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
cp="image444.jpg"
im = filtros(cp)
img = im.obtener_imagen()

#a = im.letras_color_text(img, "awacate")
#with open("output.html", mode="w") as f:
#    f.write(a)
#a = im.rgb_to_hex(127, 54, 203)
#print(a)
a = im.cartas(img)
with open("output.html", mode="w") as f:
    f.write(a)
