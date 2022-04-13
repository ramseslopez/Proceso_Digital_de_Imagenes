import numpy as np
import cv2 as cv
import random
import math
import statistics as st

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

    def cifrar(self, img, str):
        """
        Cifra un mensaje en una imagen

        Params
        img - imagen
        str - mensaje a cifrar

        Returns
        imagen con cifrado
        """

        str += "#####"
        count = 0

        bin_str = self.str_to_bin(str)

        str_len = len(bin_str)
        for values in img:
            for pixels in values:
                r, g, b = self.str_to_bin(pixels)
                if count < str_len:
                    pixels[0] = int(r[:-1] + bin_str[count], 2)
                    count += 1
                if count < str_len:
                    pixels[1] = int(g[:-1] + bin_str[count], 2)
                    count += 1
                if count < str_len:
                    pixels[2] = int(b[:-1] + bin_str[count], 2)
                    count += 1
                if count >= str_len:
                    break
        return img

    def descrifrar(self, img):
        """
        Decifra el mensaje escondido en una imagen

        Params
        img - imagen cifrada

        Returns
        mensaje descrifrado
        """
        bin_str = ""
        for values in img:
            for pixels in values:
                r, g, b = self.str_to_bin(pixels)
                bin_str += r[-1]
                bin_str += g[-1]
                bin_str += b[-1]
        str_bytes = [bin_str[i: i + 8] for i in range(0, len(bin_str), 8)]
        str = ""
        for bytes in str_bytes:
            str += chr(int(bytes, 2))
            if str[-5:] == "#####":
                break
        return str[:-5]

    def str_to_bin(self, msg):
        """
        Transforma un cadena a su
        representacion binaria

        Params
        msg - cadena

        Returns
        cadena en binario
        """
        if type(msg) == str:
            return ''.join([format(ord(i), "08b") for i in msg])
        elif type(msg) == bytes or type(msg) == np.ndarray:
            return [format(i, "08b") for i in msg]
        elif type(msg) == int or type(msg) == np.uint8:
            return format(msg, "08b")


#cp = "image3.png"
#cp = "cifrado.png"
#im = filtros(cp)
#img = im.obtener_imagen()
#c = im.cifrar(img, "sabor a mi")
#d = im.descrifrar(img)
#print(d)
#cv.imwrite("cifrado.png", c)
