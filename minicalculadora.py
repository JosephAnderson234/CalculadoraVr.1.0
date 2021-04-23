from tkinter import *
from tkinter import messagebox

class calculadora(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=500, height=480)
        self.master = master
        self.pack()
        self.create_widget()

    def botonN1(self):
        Nu1 = 1
        self.muestra.insert('end', Nu1)
    def botonN2(self):
        Nu2 = 2
        self.muestra.insert('end',Nu2)
    def botonN3(self):
        Nu3 = 3
        self.muestra.insert('end', Nu3)
    def botonN4(self):
        Nu4 = 4
        self.muestra.insert('end', Nu4)
    def botonN5(self):
        Nu5 = 5
        self.muestra.insert('end', Nu5)
    def botonN6(self):
        Nu6 = 6
        self.muestra.insert('end', Nu6)
    def botonN7(self):
        Nu7 = 7
        self.muestra.insert('end', Nu7)
    def botonN8(self):
        Nu8 = 8
        self.muestra.insert('end', Nu8)
    def botonN9(self):
        Nu9 = 9
        self.muestra.insert('end', Nu9)
    #def botonNcoma(self):
        #Nucoma = ','
        #self.muestra.insert('end', Nucoma)
    def botonN0(self):
        Nu0 = 0
        self.muestra.insert('end', Nu0)
    def botonsuma(self):
        v1 = self.muestra.get() 
        v2 = self.muestra2.get()
        Vresultado = float(v1) + float(v2)
        self.muestraResultado.delete(0,'end')
        self.muestraResultado.insert('end', Vresultado)

    def botonresta(self):
        v1 = self.muestra.get() 
        v2 = self.muestra2.get()
        Vresultado = float(v1) - float(v2)
        self.muestraResultado.delete(0,'end')
        self.muestraResultado.insert('end', Vresultado)
    
    def botonmultiplication(self):
        v1 = self.muestra.get() 
        v2 = self.muestra2.get()
        Vresultado = float(v1) * float(v2)
        self.muestraResultado.delete(0,'end')
        self.muestraResultado.insert('end', Vresultado)
    def botondivision(self):
        v1 = self.muestra.get() 
        v2 = self.muestra2.get()
        Vresultado = float(v1) / float(v2)
        self.muestraResultado.delete(0,'end')
        self.muestraResultado.insert('end', Vresultado)
    def boton_eliminar(self):
        self.muestra.delete(0,'end')
        self.muestra2.delete(0,'end')
        self.muestraResultado.delete(0,'end')
    def boton_info(self):
        messagebox.showinfo('Información','Esta parte es ta en desarrollo xD')

    #-----------------------------comandos de la tabla 2--------------------------------
    def botonN1_1(self):
        Nu1 = 1
        self.muestra2.insert('end', Nu1)
    def botonN2_1(self):
        Nu2 = 2
        self.muestra2.insert('end',Nu2)
    def botonN3_1(self):
        Nu3 = 3
        self.muestra2.insert('end', Nu3)
    def botonN4_1(self):
        Nu4 = 4
        self.muestra2.insert('end', Nu4)
    def botonN5_1(self):
        Nu5 = 5
        self.muestra2.insert('end', Nu5)
    def botonN6_1(self):
        Nu6 = 6
        self.muestra2.insert('end', Nu6)
    def botonN7_1(self):
        Nu7 = 7
        self.muestra2.insert('end', Nu7)
    def botonN8_1(self):
        Nu8 = 8
        self.muestra2.insert('end', Nu8)
    def botonN9_1(self):
        Nu9 = 9
        self.muestra2.insert('end', Nu9)
    #def botonNcoma_1(self):
        #Nucoma = ','
        #self.muestra2.insert('end', Nucoma)
    def botonN0_1(self):
        Nu0 = 0
        self.muestra2.insert('end', Nu0)

    def create_widget(self):
        self.label1 = Label(self, text="Primer numero(solo aqui funciona el teclado 1)", bg="yellow"
        , font=("Arial", 7))
        self.label1.place(x=20, y=0, width=200, height=20)

        self.label2 = Label(self, text="Segundo número, aqui funciona el teclado 2", bg="yellow"
        , font=("Arial", 7))
        self.label2.place(x=280, y=0, width=200, height=20)

        self.label3 = Label(self, text="Resultado", bg="yellow")
        self.label3.place(x=120, y=80, width=260, height=20)

        self.labelcensura = Label(self, text="Soon", bg="medium spring green", fg="yellow"
        , font=("Arial", 20))
        self.labelcensura.place(x=320, y=160, width=160, height=60)

        self.muestra = Entry(self, bg="red")
        self.muestra.place(x=20, y=20, width=200, height=40)   

        self.muestra2 = Entry(self, bg="red")
        self.muestra2.place(x=280, y=20, width=200, height=40)

        self.muestraResultado = Entry(self, bg="red")
        self.muestraResultado.place(x=120, y=100, width=260, height=40) 

        self.botonN1 = Button(self, text="1", command=self.botonN1)
        self.botonN1.place(x=20, y=240, width=40, height=40) 

        self.botonN2 = Button(self, text="2", command=self.botonN2)
        self.botonN2.place(x=80, y=240, width=40, height=40)

        self.botonN3 = Button(self, text="3", command=self.botonN3)
        self.botonN3.place(x=140, y=240, width=40, height=40)

        self.botonN4 = Button(self, text="4", command=self.botonN4)
        self.botonN4.place(x=20, y=300, width=40, height=40)

        self.botonN5 = Button(self, text="5", command=self.botonN5)
        self.botonN5.place(x=80, y=300, width=40, height=40)

        self.botonN6 = Button(self, text="6", command=self.botonN6)
        self.botonN6.place(x=140, y=300, width=40, height=40)

        self.botonN7 = Button(self, text="7", command=self.botonN7)
        self.botonN7.place(x=20, y=360, width=40, height=40)

        self.botonN8 = Button(self, text="8", command=self.botonN8)
        self.botonN8.place(x=80, y=360, width=40, height=40)

        self.botonN9 = Button(self, text="9", command=self.botonN9)
        self.botonN9.place(x=140, y=360, width=40, height=40)

        #self.botoncoma = Button(self, text=",", command=self.botonNcoma)
        #self.botoncoma.place(x=20, y=420, width=40, height=40)

        self.botonN0 = Button(self, text="0", command=self.botonN0)
        self.botonN0.place(x=80, y=420, width=40, height=40)

        #self.botondelete12 = Button(self, text="=", command=self.botonresultado)
        #self.botondelete12.place(x=140, y=420, width=40, height=40)

        self.botonmas = Button(self, text="+", command=self.botonsuma)
        self.botonmas.place(x=20, y=160, width=60, height=60)

        self.botonmenos = Button(self, text="-", command=self.botonresta)
        self.botonmenos.place(x=120, y=160, width=60, height=60)

        self.botoneinfo = Button(self, text="Info.", command=self.boton_info)
        self.botoneinfo.place(x=220, y=160, width=60, height=60)

        self.botonpor = Button(self, text="X", command=self.botonmultiplication)
        self.botonpor.place(x=220, y=240, width=60, height=60)

        self.botonentre = Button(self, text="/", command=self.botondivision)
        self.botonentre.place(x=220, y=320, width=60, height=60)

        self.botondelete = Button(self, text="CE",command=self.boton_eliminar)
        self.botondelete.place(x=220, y=400, width=60, height=60)

        #-----------------------consola 2--------------------------------
        self.botonN1_1 = Button(self, text="1", command=self.botonN1_1)
        self.botonN1_1.place(x=320, y=240, width=40, height=40) 

        self.botonN2_1 = Button(self, text="2", command=self.botonN2_1)
        self.botonN2_1.place(x=380, y=240, width=40, height=40)

        self.botonN3_1 = Button(self, text="3", command=self.botonN3_1)
        self.botonN3_1.place(x=440, y=240, width=40, height=40)

        self.botonN4_1 = Button(self, text="4", command=self.botonN4_1)
        self.botonN4_1.place(x=320, y=300, width=40, height=40)

        self.botonN5_1 = Button(self, text="5", command=self.botonN5_1)
        self.botonN5_1.place(x=380, y=300, width=40, height=40)

        self.botonN6_1 = Button(self, text="6", command=self.botonN6_1)
        self.botonN6_1.place(x=440, y=300, width=40, height=40)

        self.botonN7_1 = Button(self, text="7", command=self.botonN7_1)
        self.botonN7_1.place(x=320, y=360, width=40, height=40)

        self.botonN8_1 = Button(self, text="8", command=self.botonN8_1)
        self.botonN8_1.place(x=380, y=360, width=40, height=40)

        self.botonN9_1 = Button(self, text="9", command=self.botonN9_1)
        self.botonN9_1.place(x=440, y=360, width=40, height=40)

        #self.botoncoma_1 = Button(self, text=",", command=self.botonNcoma_1)
        #self.botoncoma_1.place(x=320, y=420, width=40, height=40)

        self.botonN0_1 = Button(self, text="0", command=self.botonN0_1)
        self.botonN0_1.place(x=380, y=420, width=40, height=40)

ventana = Tk()
ventana.wm_geometry("500x480")
ventana.wm_title("xD")
ventana.wm_resizable(0,0)
app = calculadora(ventana)
app.mainloop()