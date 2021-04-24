from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
def Gventana():
    rootG = Tk()
    rootG.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootG.geometry("300x300")
    botonsalida = Button(rootG, text="quit", command = rootG.destroy, relief="groove")
    botonsalida.pack()
    rootG.mainloop()
def Hventana():
    rootH = Tk()
    rootH.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootH.geometry("300x300")
    botonsalida = Button(rootH, text="quit", command = rootH.destroy, relief="groove")
    botonsalida.pack()
    rootH.mainloop()
def Aventana():
    rootA = Tk()
    rootA.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootA.geometry("300x300")
    botonsalida = Button(rootA, text="quit", command = rootA.destroy, relief="groove")
    botonsalida.pack()
    rootA.mainloop()
def Eventana():
    rootE = Tk()
    rootE.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootE.geometry("300x300")
    botonsalida = Button(rootE, text="quit", command = rootE.destroy, relief="groove")
    botonsalida.pack()
    rootE.mainloop()
def Cventana():
    rootC = Tk()
    rootC.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootC.geometry("300x300")
    botonsalida = Button(rootC, text="quit", command = rootC.destroy, relief="groove")
    botonsalida.pack()
    rootC.mainloop()
def Nventana():
    rootN = Tk()
    rootN.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootN.geometry("300x300")
    botonsalida = Button(rootN, text="quit", command = rootN.destroy, relief="groove")
    botonsalida.pack()
    rootN.mainloop()

ventana = Tk()
ventana.title("Mi autobiografía")
ventana.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
ventana.configure(bg="pale turquoise")
ventana.geometry("560x600")

labelt = Label(ventana, text="¿qué quieres\nconocer de mi?", bg = "pale turquoise", font=("Cooper Black", 20 ), anchor="center")
labelt.place(x=0, y=0, width=560, height=120)

botonNacimiento = Button(ventana, text="Mi nacimiento", command=Nventana, relief="groove")
botonNacimiento.place(x=40, y=120, width=200, height=120)

botonCrecimiento = Button(ventana, text="Crecimiento", command=Cventana, relief="groove")
botonCrecimiento.place(x=40, y=280, width=200, height=120)

botonEscuela = Button(ventana, text="Escuela", command=Eventana, relief="groove")
botonEscuela.place(x=40, y=440, width=200, height=120)

botonAspiraciones = Button(ventana, text="Aspiraciones", command=Aventana, relief="groove")
botonAspiraciones.place(x=320, y=120, width=200, height=120)

botonHabilidades = Button(ventana, text="Habiliades", command=Hventana, relief="groove")
botonHabilidades.place(x=320, y=280, width=200, height=120)

botonGustos = Button(ventana, text="Crecimiento", command=Gventana, relief="groove")
botonGustos.place(x=320, y=440, width=200, height=120)

ventana.mainloop()