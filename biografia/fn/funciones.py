from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
def Nventana():
    rootN = Tk()
    rootN.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootN.geometry("400x400")
    mensaje =  """Bueno, yo nací en San Vicente
de Cañete,un 24 de febrero del 2007,
nací bajo el lecho de una familia
muy amorosoa que a pesar de los
errores fluye el amor con normalidad,
con respecto a mi ciudad natal, era
muy hermosa una ciudad pacífica
queccon el paso de tiempo se fue
corrompiendo política y socialmente. 
Pero no dejemos que eso arruine la
experiencia, ¿vale?"""
    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\x2.png').resize((120,150)),
     master=rootN)
    imagen2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\x1.jpg').resize((120,120)),
     master=rootN)
    labl = Label(rootN, image=imagen)
    labl.place(x=280, y=0, width=120, height=200)
    labl2 = Label(rootN, image=imagen2)
    labl2.place(x=280, y=160, width=120, height=200)
    texto = Text(rootN, font=("Arial", 13 ))
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensaje)
    texto.configure(state='disabled')
    botonsalida = Button(rootN, text="quit", command = rootN.destroy, relief="groove")
    botonsalida.place(x=120, y=320, width=160, height=80)
    rootN.mainloop()
def Cventana():
    rootC = Tk()
    rootC.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootC.geometry("300x300")
    botonsalida = Button(rootC, text="quit", command = rootC.destroy, relief="groove")
    botonsalida.pack()
    rootC.mainloop()
def Eventana():
    rootE = Tk()
    rootE.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootE.geometry("300x300")
    botonsalida = Button(rootE, text="quit", command = rootE.destroy, relief="groove")
    botonsalida.pack()
    rootE.mainloop()
def Aventana():
    rootA = Tk()
    rootA.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootA.geometry("300x300")
    botonsalida = Button(rootA, text="quit", command = rootA.destroy, relief="groove")
    botonsalida.pack()
    rootA.mainloop()
def Hventana():
    rootH = Tk()
    rootH.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootH.geometry("300x300")
    botonsalida = Button(rootH, text="quit", command = rootH.destroy, relief="groove")
    botonsalida.pack()
    rootH.mainloop()
def Gventana():
    rootG = Tk()
    rootG.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootG.geometry("300x300")
    botonsalida = Button(rootG, text="quit", command = rootG.destroy, relief="groove")
    botonsalida.pack()
    rootG.mainloop()
