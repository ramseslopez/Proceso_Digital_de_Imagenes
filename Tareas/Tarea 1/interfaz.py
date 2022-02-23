from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from filtros import filtros



def elegir_imagen():
    global path_image

    path_image = filedialog.askopenfilename(filetypes =  [
                                                ("image", ".jpg"),
                                                ("image", ".jpeg"),
                                                ("image", ".png")
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

        lblOutputImage.image = ""

def detec_gris():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.gris(img, 3)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_rojo():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.rojo(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_verde():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.verde(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_azul():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.azul(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_contraste():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.alto_contraste(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_inverso():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.inverso(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_brillo():
    global image
    global path_image
    global fil

    #fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.brillo(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #imageToShowOutput = imagen
    im = Image.fromarray(imagen)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)



image = None
path_image = None
fil = None

# ventana principal
root = Tk()
root.title("Tarea 1")

# se muestra la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0,row=2)

# se muestra la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column = 1, row = 1, rowspan=20)

lblInfo2 = Label(root, text= "¿Que filtro deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)

# botones de filtros
fil_btn_1 = Button(root, text= "Gris", width=25, command=detec_gris)
fil_btn_2 = Button(root, text= "Rojo", width=25, command=detec_rojo)
fil_btn_3 = Button(root, text= "Verde", width=25, command=detec_verde)
fil_btn_4 = Button(root, text= "Azul", width=25, command=detec_azul)
fil_btn_5 = Button(root, text= "Mosaico", width=25)
fil_btn_6 = Button(root, text= "Contraste", width=25, command=detec_contraste)
fil_btn_7 = Button(root, text= "Inverso", width=25, command=detec_inverso)
fil_btn_8 = Button(root, text= "Brillo", width=25, command=detec_brillo)
fil_btn_1.grid(column=0, row=4, padx=5,pady=5)
fil_btn_2.grid(column=0, row=5, padx=5,pady=5)
fil_btn_3.grid(column=0, row=6, padx=5,pady=5)
fil_btn_4.grid(column=0, row=7, padx=5,pady=5)
fil_btn_5.grid(column=0, row=8, padx=5,pady=5)
fil_btn_6.grid(column=0, row=9, padx=5,pady=5)
fil_btn_7.grid(column=0, row=10, padx=5,pady=5)
fil_btn_8.grid(column=0, row=11, padx=5,pady=5)

# boton para elegir la imagen
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5,pady=5)

root.mainloop()
