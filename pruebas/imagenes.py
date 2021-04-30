from tkinter import *
from PIL import Image
from tkinter import ttk

rootN = Tk()
rootN.title("Nacimiento")
rootN.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
rootN.geometry("700x700")
rootN.configure(bg="red")
imgx = Image.open('inicio.png', 'r')
img = PhotoImage(imgx)
lbl = Label(rootN, imagen = img).pack()
lbl.imagen = img
rootN.mainloop()