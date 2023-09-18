# Tkinter es un modulo para crear interfaces graficas de usuario

from tkinter import *  #importamos todos los metodos de tkinter
import os.path

class Programa:
    def __init__(self):
        self.title="Master en python y tkinter"
        self.icon="./img/minecraft_logo_icon_168974.ico"
        self.icon_alt="./21-tkinter/img/minecraft_logo_icon_168974.ico"
        self.size="770x470"
        self.resizable=False

    def cargar(self):
        #crear la ventana raiz
        ventana=Tk()
        self.ventana=ventana

        #titulo de la ventana
        ventana.title(self.title)

        #comprobar si existe un archivo
        ruta_icono=os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono=os.path.abspath(self.icon_alt)

        #icono de la ventana
        ventana.iconbitmap(ruta_icono)

        #mostrar texto en el programa
        texto=Label(ventana,text=ruta_icono)
        texto.pack()

        #cambiar tamaño ventana
        ventana.geometry(self.size)

        #bloquear tamaño ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
    
    def addTexto(self,dato):
        texto=Label(self.ventana,text=dato)
        texto.pack()

    def mostrar(self):
        #arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#instancia el programa
programa=Programa()
programa.cargar()
programa.addTexto("Hola")
programa.addTexto("ahsasdas")
programa.mostrar()

#NOTA:
#para ejecutar el programa con doble click sin abrir una ventana de python alterna se cambia la extension por .pyw