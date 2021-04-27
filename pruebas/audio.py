from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from pygame import mixer 
mixer.init()

def pause():
    mixer.music.pause()

def continued():
    mixer.music.unpause()

def play():
    mixer.music.load(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\pruebas\Michael Jackson - Billie Jean (Official Video) (192 kbps).mp3')
    mixer.music.play()
rootN = Tk()
rootN.title("Nacimiento")
rootN.iconbitmap(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\icono.ico')
rootN.geometry("400x400")
rootN.configure(bg="red")

botonsalida = Button(rootN, text="quit", command = play,
relief="groove", font=("Cooper Black", 15), bg="tan", fg="red")
botonsalida.place(x=120, y=320, width=160, height=80)
botonpausa = Button(rootN, text="pause", command = pause)
botonpausa.pack()
botonxd = Button(rootN, text="unpause", command = continued)
botonxd.pack()
rootN.mainloop()