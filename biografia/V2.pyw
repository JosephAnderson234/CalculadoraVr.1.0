from tkinter import *
from fn.funciones import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
ventana = Tk()
ventana.title("Mi autobiografía")
ventana.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
ventana.configure(bg="pale turquoise")
ventana.geometry("560x600")

labelt = Label(ventana, text="¿qué quieres\nconocer de mi?", bg = "pale turquoise", font=("Cooper Black", 20 ), anchor="center")
labelt.place(x=0, y=0, width=560, height=120)

botonNacimiento = Button(ventana, text="Mi nacimiento", command=Nventana, relief="groove",
font=("Cooper Black", 15), bg="green yellow", fg="firebrick")
botonNacimiento.place(x=40, y=120, width=200, height=120)

botonCrecimiento = Button(ventana, text="Crecimiento", command=Cventana, relief="groove",
font=("Cooper Black", 15), bg="green yellow", fg="firebrick")
botonCrecimiento.place(x=40, y=280, width=200, height=120)

botonEscuela = Button(ventana, text="Escuela", command=Eventana, relief="groove",
font=("Cooper Black", 15), bg="green yellow", fg="firebrick")
botonEscuela.place(x=40, y=440, width=200, height=120)

botonAspiraciones = Button(ventana, text="Aspiraciones", command=Aventana, relief="groove",
font=("Cooper Black", 15), bg="green yellow", fg="firebrick")
botonAspiraciones.place(x=320, y=120, width=200, height=120)

botonHabilidades = Button(ventana, text="Habiliades", command=Hventana, relief="groove",
font=("Cooper Black", 15), bg="green yellow", fg="firebrick")
botonHabilidades.place(x=320, y=280, width=200, height=120)

botonGustos = Button(ventana, text="Crecimiento", command=Gventana, relief="groove",
font=("Cooper Black", 15), bg="green yellow", fg="firebrick")
botonGustos.place(x=320, y=440, width=200, height=120)

ventana.mainloop()