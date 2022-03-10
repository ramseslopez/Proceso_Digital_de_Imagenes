from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from filtros3 import filtros

"""
interfaz grafica

author - Ramses Antonio López Soto
date - marzo 2022
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
        image = imutils.resize(image, height=760)

        imageToShow = imutils.resize(image, width=360)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        # se muestra la imagen original
        lblInfo1 = Label(root, text="Original")
        lblInfo1.grid(column=1,row=0, padx=5, pady=5)

def detec_colores():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.letras_color(img)

    with open("./output/result_colores.html", mode="w") as f:
        f.write(imagen)

def detec_grises():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.letras_gris(img)

    with open("./output/result_grises.html", mode="w") as f:
        f.write(imagen)

def detec_bn():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.letras(img)

    with open("./output/result_bn.html", mode="w") as f:
        f.write(imagen)

def detec_colores_v2():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.letras_color_v2(img)

    with open("./output/result_colores_v2.html", mode="w") as f:
        f.write(imagen)

def detec_grises_v2():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.letras_gris_v2(img)

    with open("./output/result_grises_v2.html", mode="w") as f:
        f.write(imagen)

def detec_colores_text():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.letras_color_text(img, entry.get())

    with open("./output/result_colores_text.html", mode="w") as f:
        f.write(imagen)

def detec_cartas_html():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.cartas_html(img)

    with open("./output/result_cartas.html", mode="w") as f:
        f.write(imagen)

def detec_cartas():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.cartas(img)

    with open("./output/result_cartas.txt", mode="w") as f:
        f.write(imagen)

def detec_dominos_html():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.dominos_html(img)

    with open("./output/result_dominos.html", mode="w") as f:
        f.write(imagen)

def detec_dominos():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.dominos(img)

    with open("./output/result_dominos.txt", mode="w") as f:
        f.write(imagen)

def detec_dominos_black_html():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.dominos_black_html(img)

    with open("./output/result_dominos_black.html", mode="w") as f:
        f.write(imagen)

def detec_dominos_black():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.dominos_black(img)

    with open("./output/result_dominos_black.txt", mode="w") as f:
        f.write(imagen)

def cerrar():
    dw = Tk()
    dw.geometry('50x50')
    lb = Label(dw, text="Archivo generado")
    lb.grid(column=0, row=0)
    btw = Button(dw, text="Cerrar", command=dw.destroy)
    btw.grid(column=0, row=1)

def txt():
    global entry

    dow = Toplevel(root)
    lbl = Label(dow, text="Coloca un texto")
    lbl.pack()

    entry = Entry(dow)
    entry.pack()

    btn_n = Button(dow, text="Aplicar", command=lambda:[detec_colores_text(), cerrar(), dow.destroy()])
    btn_n.pack()

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
root.title("Tarea 3")

# se muestra la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column = 1, row = 1, rowspan=20)

lblInfo2 = Label(root, text= "¿Que filtro deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)

fil_btn_1 = Button(root, text= "Colores", width=25, command=lambda:[detec_colores(), cerrar()])
fil_btn_2 = Button(root, text= "Escala de Grises", width=25, command=lambda:[detec_grises(), cerrar()])
fil_btn_3 = Button(root, text= "Blanco y Negro", width=25, command=lambda:[detec_bn(), cerrar()])
fil_btn_4 = Button(root, text= "Colores, Blanco y Negro", width=25, command=lambda:[detec_colores_v2(), cerrar()])
fil_btn_5 = Button(root, text= "Grises, Blanco y Negro", width=25, command=lambda:[detec_grises_v2(), cerrar()])
fil_btn_6 = Button(root, text= "Texto en imagen", width=25, command=txt)
fil_btn_7 = Button(root, text= "Cartas", width=25, command=lambda:[detec_cartas(), detec_cartas_html(), cerrar()])
fil_btn_8 = Button(root, text= "Dominó", width=25, command=lambda:[detec_dominos(), detec_dominos_html(), cerrar()])
fil_btn_9 = Button(root, text= "Dominó Negro", width=25, command=lambda:[detec_dominos_black(), detec_dominos_black_html(), cerrar()])

fil_btn_1.grid(column=0, row=4, padx=5,pady=5)
fil_btn_2.grid(column=0, row=5, padx=5,pady=5)
fil_btn_3.grid(column=0, row=6, padx=5,pady=5)
fil_btn_4.grid(column=0, row=7, padx=5,pady=5)
fil_btn_5.grid(column=0, row=8, padx=5,pady=5)
fil_btn_6.grid(column=0, row=9, padx=5,pady=5)
fil_btn_7.grid(column=0, row=10, padx=5,pady=5)
fil_btn_8.grid(column=0, row=11, padx=5,pady=5)
fil_btn_9.grid(column=0, row=12, padx=5,pady=5)

# boton para elegir la imagen
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5,pady=5)

root.mainloop()
