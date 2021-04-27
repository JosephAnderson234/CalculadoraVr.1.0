from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
def Nventana():
    rootN = Tk()
    rootN.title("Nacimiento")
    rootN.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootN.geometry("400x400")
    rootN.configure(bg="red")
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
    labl = Label(rootN, image=imagen, bg="red")
    labl.place(x=280, y=0, width=120, height=200)
    labl2 = Label(rootN, image=imagen2, bg="red")
    labl2.place(x=280, y=160, width=120, height=200)
    texto = Text(rootN, font=("Arial", 13 ), bg="yellow")
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensaje)
    texto.configure(state='disabled')
    botonsalida = Button(rootN, text="quit", command = rootN.destroy,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsalida.place(x=120, y=320, width=160, height=80)
    rootN.mainloop()
def Cventana():
    rootC = Tk()
    rootC.title("Nacimiento")
    rootC.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootC.geometry("400x400")
    rootC.configure(bg="red")
    mensaje =  """Bueno, en esta parte de mi vida se
presentaron 2 razones por la que fui 
victima de bullying, mi baja de 
estatura y mi supuesto sobrepeso, ya 
que ni yo me veia gordo, pero a
pesar de todo eso me desarrolle más
en mis partes cognitivas. Por lo
demás me empeze a preocupar a los
11, porque ahí empeze a jugar en el
pequeño estadio de mi barrio. Por
eso te digo que tuve un crecimiento
muy buena. :-)"""
    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\crecimientoT.jpg').resize((120,200)),
     master=rootC)
    imagen2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\AF.jpg').resize((120,120)),
     master=rootC)
    labl = Label(rootC, image=imagen, bg="red")
    labl.place(x=280, y=0, width=120, height=200)
    labl2 = Label(rootC, image=imagen2, bg="red")
    labl2.place(x=280, y=160, width=120, height=200)
    texto = Text(rootC, font=("Arial", 13 ), bg="yellow")
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensaje)
    texto.configure(state='disabled')
    botonsalida = Button(rootC, text="quit", command = rootC.destroy,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsalida.place(x=120, y=320, width=160, height=80)
    rootC.mainloop()
def Eventana():
    rootE = Tk()
    rootE.title("Escuela")
    rootE.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootE.geometry("400x400")
    rootE.configure(bg="red")
    mensaje =  """Esto se esta poniendo cada vez mas
bueno XD, en lo que concierne a mi
educación, en mi etapa de la
infacia no recuerdo mucho, a lo
mucho puedo recordar el nombre de
ese colegio \'Niño Jesus De
Praga\', en mi educación primaria,
estudie en el \'Centro de Varones\'
y aqui fue donde poco a poco me fui
formando como un excelente
estudiante, pero en mis inicios de
la secundaria fue despertando poco
a poco mis gustos actuales. En
serio estar en la secundaria
me cambio la vida"""
    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\Colegio_mayor_coar_logo.png').resize((120,120)),
     master=rootE)
    imagen2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\descarga.jpg').resize((120,200)),
     master=rootE)
    labl = Label(rootE, image=imagen, bg="red")
    labl.place(x=280, y=0, width=120, height=200)
    labl2 = Label(rootE, image=imagen2, bg="red")
    labl2.place(x=280, y=160, width=120, height=200)
    texto = Text(rootE, font=("Arial", 13 ), bg="yellow")
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensaje)
    texto.configure(state='disabled')
    botonsalida = Button(rootE, text="quit", command = rootE.destroy,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsalida.place(x=120, y=320, width=160, height=80)
    rootE.mainloop()
def Aventana():
    rootA = Tk()
    rootA.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootA.geometry("500x400")
    rootA.configure(bg="red")
    mensaje =  """Bueno llegamos a la parte donde
hablamos de mis metas a futuro,
bueno en mi caso(creo que ya lo
saben xD) quiero ser un Ingeniero
de Sistemos Computacional, porque,
como ya saben, soy bueno para las
metmáticas y más cosas(lo voy a
mencionar más adelante) la cosa
esque todo eso me ayudo a  marcar
mi futuro. A parte, sueño con formar
una familia muy humilde llena de
valores y profundo cariño, ya que
del fruto del trabajo lo utilizare
para el futuro de mi descendencia."""
    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\inicio.jpg').resize((220,110)),
     master=rootA)
    labl = Label(rootA, image=imagen, bg="red")
    labl.place(x=280, y=80, width=220, height=200)
    texto = Text(rootA, font=("Arial", 13 ), bg="yellow")
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensaje)
    texto.configure(state='disabled')
    botonsalida = Button(rootA, text="quit", command = rootA.destroy,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsalida.place(x=120, y=320, width=160, height=80)
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
