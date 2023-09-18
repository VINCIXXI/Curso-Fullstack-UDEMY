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
            width=400,
            cursor="circle"
)
texto.pack()

texto=Label(ventana,text="Soy David")
texto.pack(anchor=E)

def pruebas(nombre, apellidos, pais):
    return f"Hola, {nombre} {apellidos} veo que eres de {pais}"

texto=Label(ventana,text=pruebas("Victor","Robles", "España"))
texto.pack()

ventana.mainloop()