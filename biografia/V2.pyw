from tkinter import *
#from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
def Nventana():
    global root
    root = Tk()
    root.geometry("300x300")
    botonsalida = Button(root, text="quit", command = root.destroy)
    botonsalida.pack()
    root.mainloop()

ventana = Tk()
ventana.title("Mi autobiografía")
ventana.configure(bg="pale turquoise")
ventana.geometry("400x400")

labelt = Label(ventana, text="¿qué quieres conocer de mi?", bg = "pale turquoise", font=("Cooper Black", 20 ))
labelt.place(x=0, y=0, width=400, height=40)

botonNacimiento = Button(ventana, text="Mi nacimiento", command=Nventana)
botonNacimiento.place(x=20, y=100, width=150, height=40)

ventana.mainloop()