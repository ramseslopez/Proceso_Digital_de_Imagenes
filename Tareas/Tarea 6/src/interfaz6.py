from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from filtros5 import filtros

"""
interfaz grafica

author - Ramses Antonio López Soto
date - febrero 2022
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
    global entry
    new_w = Toplevel(root)

    lb = Label(new_w, text = "Coloca el mensaje que deseas cifrar")
    lb.pack()

    entry = Entry(new_w)
    entry.pack()

    bn = Button(new_w, text= "Cifrar", width=25, command=lambda:[detec_enc(), new_w.destroy(), msg()])
    bn.pack()

def msg():
    www = Tk()

    lbo = Label(www, text = "Mensaje cifrado")
    lbo.pack()

    #bno = Button(www, text= "Cerrar", width=25, command=www.destroy())
    #bno.pack()

def d_msg():
    www2 = Tk()

    www2.geometry("250x170")


    T = Text(www2, height = 5, width = 52)
    l = Label(www2, text = "Mensaje secreto")
    l.config(font =("Courier", 14))

    b1 = Button(www2, text = "Guardar", command=lambda:[descargar_text(msg), cerrar()])
    b2 = Button(www2, text = "Cerrar", command = www2.destroy)

    l.pack()
    T.pack()
    b1.pack()
    b2.pack()

    T.insert(END, msg)

    www2.mainloop()

def detec_enc():
    global image
    global path_image
    global fil

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.cifrar(img, str(entry.get()))
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "encrypted"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_dec():
    global image
    global path_image
    global fil
    global msg

    if fil == None:
        error_img()

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    msg = fil.descrifrar(img)
    imageToShowOutput = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)


def descargar_imagen(img, filter):
    cv2.imwrite("./output/result_" + str(filter) + ".png", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def descargar_text(msg):
    with open('./output/msg_decrypted.txt', 'w') as f:
        f.write(str(msg))


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
root.title("Tarea 2")

# se muestra la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0,row=2)

# se muestra la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column = 1, row = 1, rowspan=20)

lblInfo2 = Label(root, text= "¿Que deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)


fil_btn_1 = Button(root, text= "Cifrar mensaje", width=25, command=nueva_ventana)
fil_btn_2 = Button(root, text= "Descifrar mensaje", width=25, command=lambda:[detec_dec(), d_msg()])
entry_txt = Entry()

fil_btn_1.grid(column=0, row=4, padx=5,pady=5)
fil_btn_2.grid(column=0, row=5, padx=5,pady=5)

# boton para elegir la imagen
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5,pady=5)



root.mainloop()
