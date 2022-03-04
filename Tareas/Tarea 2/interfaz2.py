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
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "blur"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)



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
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "mblur"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

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
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "edges"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def nueva_ventana_3():
    global selected_3
    new_w = Toplevel(root)

    selected_3 = IntVar()
    rad1 = Radiobutton(new_w, text='Sharpen Agudo', width=25,value=1, variable=selected_3, command=detec_sharpen)
    rad2 = Radiobutton(new_w, text='Sharpen Sutil',width=25, value=2, variable=selected_3, command=detec_sharpen)
    rad3 = Radiobutton(new_w, text='Sharpen Exagerado',width=25, value=3, variable=selected_3, command=detec_sharpen)
    rad1.grid(column=0, row=4)
    rad2.grid(column=0, row=5)
    rad3.grid(column=0, row=6)

def detec_emboss():
    global image
    global path_image
    global fil

    if selected_4.get() == 1:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 4)
    if selected_4.get() == 2:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 4)
        imagen = fil.gris(imagen)
    if selected_4.get() == 3:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 5)

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "emboss"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_sharpen():
    global image
    global path_image
    global fil

    if selected_3.get() == 1:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 6)
    if selected_3.get() == 2:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 7)
    if selected_3.get() == 3:
        fil = filtros(path_image)
        img = fil.obtener_imagen()
        imagen = fil.convolucion(img, 8)

    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "sharpen"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)


def detec_promedio():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.convolucion(img, 13)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "mean"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_mediana():
    global image
    global path_image
    global fil

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.median(img)
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "median"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)

def detec_mica_rgb():
    global image
    global path_image
    global fil
    global imageToShowOutput

    fil = filtros(path_image)
    img = fil.obtener_imagen()

    imagen = fil.mica_RGB(img, scale1.get(), scale2.get(), scale3.get())
    imageToShowOutput = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    lblInfo3 = Label(root, text = "Modificada")
    lblInfo3.grid(column=1, row=0, padx=5,pady=5)
    dw_btn = Button(root, text="Descargar", command=lambda:[descargar_imagen(imageToShowOutput, "micaRGB"), cerrar()])
    dw_btn.grid(column=2, row=0, padx=5, pady=5)


def barra_rgb():
    global image
    global path_image
    global fil
    global scale1
    global scale2
    global scale3

    b_window = Toplevel(root)

    scale1 = Scale(b_window, from_=0, to=255, orient=HORIZONTAL, length=500,  troughcolor="red")

    scale1.pack()
    scale1.set (0)

    scale2 = Scale(b_window, from_=0, to=255, orient=HORIZONTAL, length=500, troughcolor="green")

    scale2.pack()
    scale2.set (1)

    scale3 = Scale(b_window, from_=0, to=255, orient=HORIZONTAL, length=500, troughcolor="blue")

    scale3.pack()
    scale3.set (2)

    btn_brillo= Button(b_window, text="Aplicar", command=detec_mica_rgb)
    btn_brillo.pack()

def nueva_ventana_4():
    global selected_4
    new_w = Toplevel(root)

    selected_4 = IntVar()
    rad1 = Radiobutton(new_w, text='Emboss 45°', width=25,value=1, variable=selected_4, command=detec_emboss)
    rad2 = Radiobutton(new_w, text='Emboss Gray',width=25, value=2, variable=selected_4, command=detec_emboss)
    rad3 = Radiobutton(new_w, text='Emboss Exagerado',width=25, value=3, variable=selected_4, command=detec_emboss)
    rad1.grid(column=0, row=4)
    rad2.grid(column=0, row=5)
    rad3.grid(column=0, row=6)

def descargar_imagen(img, filter):
    cv2.imwrite("result_" + str(filter) + ".png", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def cerrar():
    dw = Tk()
    dw.geometry('50x50')
    lb = Label(dw, text="Descarga exitosa")
    lb.grid(column=0, row=0)
    btw = Button(dw, text="Cerrar", command=dw.destroy)
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

lblInfo2 = Label(root, text= "¿Que filtro deseas probar?")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)


fil_btn_1 = Button(root, text= "Blur", width=25, command=nueva_ventana)
fil_btn_2 = Button(root, text= "Motion Blur", width=25, command=detec_motion_blur)
fil_btn_3 = Button(root, text= "Find Edges", width=25, command=nueva_ventana_2)
fil_btn_4 = Button(root, text= "Sharpen", width=25, command=nueva_ventana_3)
fil_btn_5 = Button(root, text= "Emboss", width=25, command=nueva_ventana_4)
fil_btn_6 = Button(root, text= "Promedio", width=25, command=detec_promedio)
fil_btn_7 = Button(root, text= "Mediana", width=25, command=detec_mediana)
fil_btn_8 = Button(root, text= "Mica RGB", width=25, command=barra_rgb)

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
