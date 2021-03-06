from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from filtros6 import filtros

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

def new_w_1():
    global entry1_g
    global entry2_g

    new_w = Toplevel(root)

    lb1g = Label(new_w, text="Ancho")
    lb1g.pack()
    entry1_g = Entry(new_w)
    entry1_g.pack()

    lb2g = Label(new_w, text="Alto")
    lb2g.pack()
    entry2_g = Entry(new_w)
    entry2_g.pack()

    btng = Button(new_w, text="Procesar", command=lambda:[detec_rec_gray(), new_w.destroy()])
    btng.pack()

def new_w_2():
    global entry1_c
    global entry2_c

    new_ww = Toplevel(root)

    lb1c = Label(new_ww, text="Ancho")
    lb1c.pack()
    entry1_c = Entry(new_ww)
    entry1_c.pack()

    lb2c = Label(new_ww, text="Alto")
    lb2c.pack()
    entry2_c = Entry(new_ww)
    entry2_c.pack()

    btnc = Button(new_ww, text="Procesar", command=lambda:[detec_rec_color(), new_ww.destroy()])
    btnc.pack()

def detec_rec_gray():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.img_recursiva_gris(img, int(entry1_g.get()), int(entry2_g.get()))

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "rec_gray"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)


def detec_rec_color():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()
    imagen = fil.img_recursiva_color(img, int(entry1_c.get()), int(entry2_c.get()))

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "rec_color"), cerrar()])
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
root.title("Tarea 6")

# se muestra la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0,row=2)

# se muestra la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column = 1, row = 1, rowspan=20)

lblInfo2 = Label(root, text= "¿Que filtro deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)


fil_btn_1 = Button(root, text= "Recursiva Gris",  width=25, command=new_w_1)
fil_btn_2 = Button(root, text= "Recursiva Color",  width=25, command=new_w_2)

fil_btn_1.grid(column=0, row=4, padx=5,pady=5)
fil_btn_2.grid(column=0, row=5, padx=5,pady=5)

# boton para elegir la imagen
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5,pady=5)



root.mainloop()
