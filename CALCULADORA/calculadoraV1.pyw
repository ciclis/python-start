from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import right   

raiz=Tk()
raiz.title("CALCULADORA EN PYTHON")
raiz.resizable(0,0)
raiz.geometry("480x265")
raiz.config(bg="grey")

boton7 = ttk.Button(text="7")
boton7.place(x=50, y=85)
boton8 = ttk.Button(text="8")
boton8.place(x=150, y=85)
boton9 = ttk.Button(text="9")
boton9.place(x=250, y=85)
botonx = ttk.Button(text="x")
botonx.place(x=350, y=85)
boton4 = ttk.Button(text="4")
boton4.place(x=50, y=135)
boton5 = ttk.Button(text="5")
boton5.place(x=150, y=135)
boton6 = ttk.Button(text="6")
boton6.place(x=250, y=135)
botonResta = ttk.Button(text="-")
botonResta.place(x=350, y=135)
boton1 = ttk.Button(text="1")
boton1.place(x=50, y=185)
boton2 = ttk.Button(text="2")
boton2.place(x=150, y=185)
boton3 = ttk.Button(text="3")
boton3.place(x=250, y=185)
botonSuma = ttk.Button(text="+")
botonSuma.place(x=350, y=185)
boton0 = ttk.Button(text="0")
boton0.place(x=150, y=185)
botonDivision= ttk.Button(text="/")
botonDivision.place(x=350, y=185)
botonIgual= ttk.Button(text="=")
botonIgual.place(x=250, y=235)
botonBorrar= ttk.Button(text="DELETE")
botonBorrar.place(x=350, y=235)
Salida=Entry(raiz,font=('arial',20,"bold"),width=22,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=45,y=0)
raiz.mainloop()
