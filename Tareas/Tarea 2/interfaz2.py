from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from filtros2 import filtros

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

def detec_blur():
    global image
    global path_image
    global fil

    if selected.get() == 1:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 1)
    if selected.get() == 2:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 2)

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)



def nueva_ventana():
    global selected
    new_w = Toplevel(root)

    selected = IntVar()
    rad1 = Radiobutton(new_w, text='Blur v1', width=25,value=1, variable=selected, command=detec_blur)
    rad2 = Radiobutton(new_w, text='Blur v2',width=25, value=2, variable=selected, command=detec_blur)
    rad1.grid(column=0, row=4)
    rad2.grid(column=0, row=5)


def detec_motion_blur():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.convolucion(img, 3)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def nueva_ventana_2():
    global selected_2
    new_w = Toplevel(root)

    selected_2 = IntVar()
    rad1 = Radiobutton(new_w, text='FE Horizontal', width=25,value=1, variable=selected_2, command=detec_find_edges)
    rad2 = Radiobutton(new_w, text='FE Vertical',width=25, value=2, variable=selected_2, command=detec_find_edges)
    rad3 = Radiobutton(new_w, text='FE 45°',width=25, value=3, variable=selected_2, command=detec_find_edges)
    rad4 = Radiobutton(new_w, text='FE Todos',width=25, value=4, variable=selected_2, command=detec_find_edges)
    rad1.grid(column=0, row=4)
    rad2.grid(column=0, row=5)
    rad3.grid(column=0, row=6)
    rad4.grid(column=0, row=7)

def detec_find_edges():
    global image
    global path_image
    global fil

    if selected_2.get() == 1:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 9)
    if selected_2.get() == 2:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 10)
    if selected_2.get() == 3:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 11)
    if selected_2.get() == 4:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 12)

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_azul():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.azul(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_contraste():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.alto_contraste(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_inverso():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.inverso(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)

def detec_brillo():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.brillo(img, scale1.get())
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")


def barra_brillo():
    global image
    global path_image
    global fil
    global scale1

    b_window = Toplevel(root)

    scale1 = Scale(b_window, from_=-255, to=255, orient=HORIZONTAL, tickinterval=1, length=500)

    scale1.pack()
    scale1.set (0)

    btn_brillo= Button(b_window, text="Aplicar", command=detec_brillo)
    btn_brillo.pack()

def m_ventana():
    global image
    global path_image
    global fil
    global entry1
    global entry2

    m_window = Toplevel(root)
    m_label1 = Label(m_window, text="ancho")
    m_label1.pack()
    entry1 = Entry(m_window)
    entry1.pack()
    m_label2 = Label(m_window, text="alto")
    m_label2.pack()
    entry2 = Entry(m_window)
    entry2.pack()
    btn_m = Button(m_window, text="Aplicar", command=detec_mosaico)
    btn_m.pack()

def detec_mosaico():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.mosaico(img, int(entry1.get()), int(entry2.get()))
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    pass


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


fil_btn_1 = Button(root, text= "Blur", width=25, command=nueva_ventana)
fil_btn_2 = Button(root, text= "Motion Blur", width=25, command=detec_motion_blur)
fil_btn_3 = Button(root, text= "Find Edges", width=25, command=nueva_ventana_2)
fil_btn_4 = Button(root, text= "Sharpen", width=25, command=detec_azul)
fil_btn_5 = Button(root, text= "Emboss", width=25, command=m_ventana)
fil_btn_6 = Button(root, text= "Promedio", width=25, command=detec_contraste)
fil_btn_7 = Button(root, text= "Mediana", width=25, command=detec_inverso)
fil_btn_8 = Button(root, text= "Mica RGB", width=25, command=barra_brillo)

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
