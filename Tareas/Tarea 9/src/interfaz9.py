from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import os
import errno
from filtros9 import filtros

"""
interfaz grafica

author - Ramses Antonio López Soto
date - mayo 2022
"""

def elegir_imagen():
    global path_image

    path_image = filedialog.askopenfilename(filetypes = [
                                                        ("image", "*.png"),
                                                        ("image", "*.gif"),
                                                        ("image", "*.jpg"),
                                                        ("image", "*.jpeg")
                                                        ])

    if len(path_image) > 0:
        global image
        global fil

        # se crea el objeto
        fil = filtros(path_image)

        # se lee la imagen de entrada
        image = fil.obtener_imagen()
        image = imutils.resize(image, height=380)

        imageToShow = imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        # se muestra la imagen original
        lblInfo1 = Label(root, text="Original")
        lblInfo1.grid(column=0,row=1, padx=5, pady=5)


def detec_ditering_ord():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.ord_dithering(img)

    imageToShowOutput_1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput_1)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput_1, "dit_ord"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_ditering_rnd():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.random_dithering(img)

    imageToShowOutput_1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput_1)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput_1, "dit_rnd"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_ditering_disp_3x3():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.disp_dithering_3x3(img)

    imageToShowOutput_1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput_1)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput_1, "dit_disp_3x3"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_ditering_disp_2x2():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.disp_dithering_2x2(img)

    imageToShowOutput_1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput_1)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput_1, "dit_disp_2x2"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_ditering_disp_4x4():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.disp_dithering_4x4(img)

    imageToShowOutput_1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput_1)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput_1, "dit_disp_4x4"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)


def descargar_imagen(img, filter):
    cv2.imwrite("./output/result_" + str(filter) + ".png", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def cerrar():
    dw = Tk()
    dw.geometry('50x50')
    lb = Label(dw, text="Descarga exitosa")
    lb.grid(column=0, row=0)
    btw = Button(dw, text="Cerrar", command=dw.destroy)
    btw.grid(column=0, row=1)

def error_img():
    dww = Tk()
    #dw.geometry('50x50')
    lb = Label(dww, text="ERROR \nEliga una imagen")
    lb.grid(column=0, row=0)
    btw = Button(dww, text="Cerrar", command=dww.destroy)
    btw.grid(column=0, row=1)

image = None
path_image = None
fil = None

# ventana principal
root = Tk()
root.title("Tarea 9")

# se muestra la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0,row=2)

# se muestra la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column = 1, row = 1, rowspan=20)

lblInfo2 = Label(root, text= "¿Que filtro deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)


fil_btn_1 = Button(root, text= "Dithering Random", width=25, command=detec_ditering_rnd)
fil_btn_2 = Button(root, text= "Dithering Ordenada", width=25, command=detec_ditering_ord)
fil_btn_3 = Button(root, text= "Dithering Disperso 3x3", width=25, command=detec_ditering_disp_3x3)
fil_btn_4 = Button(root, text= "Dithering Disperso 2x2", width=25, command=detec_ditering_disp_2x2)
fil_btn_5 = Button(root, text= "Dithering Disperso 4x4", width=25, command=detec_ditering_disp_4x4)

fil_btn_1.grid(column=0, row=4, padx=5,pady=5)
fil_btn_2.grid(column=0, row=5, padx=5,pady=5)
fil_btn_3.grid(column=0, row=6, padx=5,pady=5)
fil_btn_4.grid(column=0, row=7, padx=5,pady=5)
fil_btn_5.grid(column=0, row=8, padx=5,pady=5)

# boton para elegir la imagen
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5,pady=5)


try:
    os.mkdir('dir1')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
root.mainloop()
