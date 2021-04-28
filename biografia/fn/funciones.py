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
    rootA.title("Aspiraciones")
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
    rootH.geometry("500x400")
    rootH.title("Habilidades")
    rootH.configure(bg="red")
    mensaje =  """Ok, ahora entramos al terreno de mis
habilidades, aunque ustedes piensen
que solo programo tambien me gusta
escribir además de usar la
computadora de manera eficiente, a
por cierto soy bueno apra las
matemáticas, asi que si tienen
dudas, fuera de la hoar de clase,
solo me avisan con gusto les echo
una mano."""
    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\programación.png').resize((220,110)),
     master=rootH)
    labl = Label(rootH, image=imagen, bg="red")
    texto = Text(rootH, font=("Arial", 13 ), bg="yellow")
    labl.place(x=280, y=80, width=220, height=200)
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensaje)
    texto.configure(state='disabled')
    botonsalida = Button(rootH, text="quit", command = rootH.destroy,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsalida.place(x=120, y=320, width=160, height=80)
    rootH.mainloop()
def Gventana():
    def retroceder():
        texto.configure(state='normal')
        texto.delete("1.0","end")
        texto.insert(tk.END, mensajes[0])
    def completar():
        texto.configure(state='normal')
        texto.delete("1.0","end")
        texto.insert(tk.END, mensajes[1])
        texto.configure(state='disabled')
        botonXP = Button(rootG, text="<=", command=retroceder,
        relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
        botonXP.place(x=0, y=320, width=160, height=80)

    rootG = Tk()
    rootG.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
    rootG.geometry("400x400")
    rootG.title("Gustos")
    rootG.configure(bg="red")
    mensaje =  """Bueno ahora hablemos de mis gustos
personales, en lo básico me gusta las
computadoras creo que desde cumplí
12, fue algo repentino; pero
dejando de lado eso,tambien me
gusta leer,de echo ahí me
entretengo más que en otras
cosas,además hace pocos meses me
empezó a gustar pintar(OJO: pintar
no es lo mismo que dibujar) por si
me olvidaba tambien me gusta
escribir, lo considero un
pasatiempo reflexivo y puro.
Bueno no tengo otra cosa más quye
decir. Bueno creo que eso es todo."""
    mensaje2 = """Gracias por tu tiempo. Bye :-)"""
    mensajes = [mensaje, mensaje2]
    imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\libros.jpg').resize((120,110)),
     master=rootG)
    labl = Label(rootG, image=imagen, bg="red")
    labl.place(x=280, y=0, width=120, height=200)
    imagen2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\compu.jpg').resize((120,110)),
     master=rootG)
    labl2 = Label(rootG, image=imagen2, bg="red")
    labl2.place(x=280, y=160, width=120, height=200)
    texto = Text(rootG, font=("Arial", 13 ), bg="yellow")
    texto.place(x=0, y=0, width=280, height=320)
    texto.insert(tk.END, mensajes[0])
    texto.configure(state='disabled')
    botonsalida = Button(rootG, text="quit", command = rootG.destroy,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsalida.place(x=120, y=320, width=160, height=80)
    botonsiguiente = Button(rootG, text="=>", command = completar,
    relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
    botonsiguiente.place(x=280, y=320, width=120, height=80)
    rootG.mainloop()
