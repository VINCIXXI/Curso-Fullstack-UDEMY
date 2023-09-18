from tkinter import *

ventana=Tk()
ventana.geometry("700x500")

texto=Label(ventana,text="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="black",
            padx=20,
            font=("Arial",30),
            justify=RIGHT,
            cursor="circle"
)
texto.pack()

texto=Label(ventana,text="Soy David")
texto.config(
            fg="black",
            bg="yellow",
            padx=20,
            font=("Arial",30),
            justify=RIGHT,
            width=200,
            cursor="circle"
)
texto.pack(side="top", fill=X, expand=YES)

def pruebas(nombre, apellidos, pais):
    return f"Hola, {nombre} {apellidos} veo que eres de {pais}"

texto=Label(ventana,text="Basico")
texto.pack(anchor=E)

ventana.mainloop()