from pygame import mixer 
from tkinter import *
mixer.init()

def create_reproducctor():
    def play():
        mixer.music.load(r'C:\Users\Usuario\Documents\GitHub\CalculadoraVr.1.0\biografia\fn\Smooth_criminal.mp3')
        mixer.music.play()
    def continued():
        mixer.music.unpause()
        Bpause.configure(text="Pausa", command=pause)
    def pause():
        mixer.music.pause()
        Bpause.configure(text="Continuar", command=continued)

    def salir():
        mixer.music.stop()
        rpd.destroy()
    
    rpd = Tk()
    rpd.geometry("400x80")
    rpd.title("Mini reproductor")
    rpd.configure(bg="yellow")
    Bplay = Button(rpd, command=play, text="Play", relief="groove", font=("Cooper Black", 13), fg="red")
    Bplay.place(x=120, y=0, width=160, height=80)
    Bpause = Button(rpd, command=pause, text="Pause", relief="groove", font=("Cooper Black", 13), fg="red")
    Bpause.place(x=0, y=0, width=120, height=80)
    Bquit = Button(rpd, command=salir, text="Quit", relief="groove", font=("Cooper Black", 13), fg="red")
    Bquit.place(x=280, y=0, width=120, height=80)
    rpd.mainloop()