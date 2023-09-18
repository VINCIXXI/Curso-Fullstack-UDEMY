from tkinter import *

ventana=Tk()

ventana.title("Marcos en python")
ventana.geometry("700x400")

marco=Frame(ventana,width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief="solid"
)
marco.pack(side="right", anchor=SE)

marco=Frame(ventana,width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief="solid"
)
marco.pack(side="right", anchor=SE)
marco.pack_propagate(False)

texto=Label(marco, text="Primer marco")
texto.config(
    bg="green",
    fg="white",
    font=("Arial",20)
)
texto.pack(anchor=CENTER,fill=Y,expand=YES)

ventana.mainloop()