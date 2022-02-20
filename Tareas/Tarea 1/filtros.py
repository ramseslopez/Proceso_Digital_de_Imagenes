import numpy as np
import cv2 as cv



# Se carga la imagen
ruta_imagen = "image.jpg"

#Se lee la imagen
img = cv.imread(ruta_imagen, 1)

cv.imshow("real", img)
cv.waitKey()

#Parametros de la imagen
filas, columnas = img.shape[:2]


for i in range(0, filas):
    for j in range(0, columnas):
        img[i][j][1] = 0
        img[i][j][2] = 0
cv.imshow("rojo", img)
cv.waitKey()
