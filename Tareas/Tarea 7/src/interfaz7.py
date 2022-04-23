from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from filtros7 import filtros

"""
interfaz grafica

author - Ramses Antonio López Soto
date - abril 2022
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



def nueva_ventana():
    global entry1
    new_w = Toplevel(root)

    lb1 = Label(new_w, text="Tamaño")
    lb1.pack()
    entry1 = Entry(new_w, text="radio")
    entry1.pack()
    bc1 = Button(new_w, text='Procesar', command=lambda:[detec_pintura_gris(), new_w.destroy()])
    bc1.pack()



def nueva_ventana_2():
    global entry2
    new_ww = Toplevel(root)

    lb2 = Label(new_ww, text="Tamaño")
    lb2.pack()
    entry2 = Entry(new_ww, text="radio")
    entry2.pack()
    bc2 = Button(new_ww, text='Procesar', command=lambda:[detec_pintura_color(), new_ww.destroy()])
    bc2.pack()


def detec_pintura_gris():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.oleo_gris(img, int(entry1.get()))

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "oil_gray"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)


def detec_pintura_color():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()


    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.oleo(img, int(entry2.get()))

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "oil_color"), cerrar()])
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
root.title("Tarea 7")

# se muestra la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0,row=2)

# se muestra la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column = 1, row = 1, rowspan=20)

lblInfo2 = Label(root, text= "¿Que filtro deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)


fil_btn_1 = Button(root, text= "Pintura Gris", width=25, command=nueva_ventana)
fil_btn_2 = Button(root, text= "Pintura Color", width=25, command=nueva_ventana_2)

fil_btn_1.grid(column=0, row=4, padx=5,pady=5)
fil_btn_2.grid(column=0, row=5, padx=5,pady=5)

# boton para elegir la imagen
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5,pady=5)



root.mainloop()
