from tkinter import *
#se instala el modulo de Pillow para python
from PIL import Image,ImageTk

ventana=Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy David").pack()

imagen=Image.open("./Curso python/UDEMY Python/21-tkinter/img/Afiche.png")
render=ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()