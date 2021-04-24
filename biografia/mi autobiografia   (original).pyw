from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk

#ventana
ventana = Tk()
ventana.title("mi autobiografia")
ventana.geometry("500x450")
ventana.resizable(1,1)
ventana.iconbitmap('Colegio_mayor_coar_logo.ico')

#diviciones
tab_control = ttk.Notebook(ventana)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Presentacion')
tab_control.add(tab2, text='nacimiento y crecimiento')
tab_control.add(tab3, text='escuela')
tab_control.add(tab4, text='gustos')

#El contenido del tab1
#la barrita de desplazamiento del scroll bar y texto
scroll = tk.Scrollbar(tab1)
texto = tk.Text(tab1, height=8, width=30, bg="yellow", fg="red", font=("Arial", 12))
scroll.pack(side=tk.RIGHT, fill=tk.Y)
texto.pack(side=tk.LEFT, fill=tk.Y)
scroll.config(command=texto.yview)
texto.config(yscrollcommand=scroll.set)
mensaje = """Soy un niño cualquiera que\n aspira cosas grandes, desde\n pequeño me gusta la logica y los \nnumeros,
pero todo tiene un incio y un final y he\naqui te cuento\nla mia, una muy grande :-).\nPorque aqui se guarda tesoros
que pocos conosen y ahora tú, que\nlees esto los conozcas el esfuerzo de\nun inicio que no tendra final.Te lo\npuedo asegurar"""
texto.insert(tk.END, mensaje)
texto.configure(state='disabled')
#imagenes
imagen = ImageTk.PhotoImage(Image.open('download.jpg'))
lbl = Label(tab1, image=imagen)
lbl.pack()

#Ahora el tab2
#barrita y texto
scroll2 = tk.Scrollbar(tab2)
texto2 = tk.Text(tab2, height=8, width=30, bg="yellow", fg="red", font=("Arial", 12))
scroll2.pack(side=tk.RIGHT, fill=tk.Y)
texto2.pack(side=tk.LEFT, fill=tk.Y)
scroll2.config(command=texto2.yview)
texto2.config(yscrollcommand=scroll2.set)
mensaje2 = """Bueno esto es un si es una historia\nmuy larga, pero común, todo comienza un 24 de Febrero del 2007(En San\nVicente, Cañete, Lima en el H. rezola),
nace Joseph Anderson Cose Rojas,\nno tengo mucho conocimiento de\ncomo fue ese día; pero de lo que te\naseguro es que sufri desnutricion unos meses(que ha decir verdad creo que
esa fue la causa de mi falta de\nestatura), me desarrolle como todo\nniño normal, hasta en el momento que escribo esto tengo 14, y si, ¿un
adolescente programando?, pues si 
soy un adolescente que busca crecer y madurar.Por cierto hoy recibi una\nnoticia muy importante para mi."""
texto2.insert(tk.END, mensaje2)
texto2.configure(state='disabled')
#Imagen
imagen2 = ImageTk.PhotoImage(Image.open('x2.png').resize((170, 220)))
lbl2 = Label(tab2, image=imagen2)
lbl2.pack()
imagen21 = ImageTk.PhotoImage(Image.open('x1.jpg').resize((220, 200)))
lbl21 = Label(tab2, image=imagen21)
lbl21.pack()

#Y el tab3
#barrita y texto
scroll3 = tk.Scrollbar(tab3)
texto3 = tk.Text(tab3, height=8, width=30, bg="yellow", fg="red", font=("Arial", 12))
scroll3.pack(side=tk.RIGHT, fill=tk.Y)
texto3.pack(side=tk.LEFT, fill=tk.Y)
scroll3.config(command=texto3.yview)
texto3.config(yscrollcommand=scroll3.set)
mensaje3 = """Inicie primero en el jardin n°023
(Actuelmente conocido como \'Jardin
Niño Jesus de Praga\'), pase unos
lindosaños allí, con una promoción 
inolvedable, pero crecí y mis papas
me matricularon en el Colegio 
N°20874(Centro de Varones),fue aqui 
donde pase toda mi primaria y
posteriormente parte de mi
secundaría; y es aqui donde viene mi
noticia ingreso al coar donde pasaré
mi parte restante de mi secundaria a
la universidad. Como verás tuve una
vida educativa muy estable y me
siento feliz de eso."""
texto3.insert(tk.END, mensaje3)
texto3.configure(state='disabled')
#Imagen
imagen3 = ImageTk.PhotoImage(Image.open('Colegio_mayor_coar_logo.png').resize((160, 160)))
lbl3 = Label(tab3, image=imagen3)
lbl3.pack()
imagen31 = ImageTk.PhotoImage(Image.open('descarga.jpg'))
lbl31 = Label(tab3, image=imagen31)
lbl31.pack()

#Conten. tab4
#Barrrita, texto
scroll4 = tk.Scrollbar(tab4)
texto4 = tk.Text(tab4, height=8, width=30, bg="yellow", fg="red", font=("Arial", 12))
scroll4.pack(side=tk.RIGHT, fill=tk.Y)
texto4.pack(side=tk.LEFT, fill=tk.Y)
scroll4.config(command=texto4.yview)
texto4.config(yscrollcommand=scroll4.set)
mensaje4 = """"""
texto4.insert(tk.END, mensaje4)
texto4.configure(state='disabled')
#Imagen


#"el mainloop del tab"
tab_control.pack(expand=1, fill='both')
ventana.mainloop()