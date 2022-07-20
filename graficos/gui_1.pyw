#ayuda tkinter https://acortar.link/uPZSIH


import tkinter
from this import s
from tkinter import *
from turtle import right                                                                            # la extension .pyw es para que al abrir la ventana no salga la consola

raiz=Tk()     

raiz.title("Francisco Franco Bahamonde")  #cambiar TITULO PESTAÑA

#raiz.resizable(1,1)   # escalar ANCHO,ALTO

raiz.iconbitmap("img = franco1.ico")  #icono de la izquierda

raiz.geometry("1280x720")  #tamaño por defecto de la ventana

raiz.config(bg="red")  #color fondo

miFrame=Frame()

#miFrame.pack(side="bottom", anchor=E)    #hayque ponerlo si o si, lo de dentro del parentesis es para donde quermos que este el FRAME

miFrame.pack()  #(fill="y" , expand=1)

miFrame.config(bg="blue")

raiz.config(bd=30)

raiz.config(relief="groove")                 

raiz.config(cursor="spider")

miFrame.config(width="650" , height="350")

miFrame.config(bd=20)

miFrame.config(relief="groove")                  #groove es el tipo de nombre que tkinter asigna , hay mas

miFrame.config(cursor="spider")

raiz.mainloop()