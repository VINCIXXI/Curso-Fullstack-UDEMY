"""
Crear un programa que tenga:
-una ventana
-tamaño fijo y sin redimensionar
-un menu(inicio, añadir, informacion, salir)
-diferente pantallas
-formulario de añadir productos
-guardar datos temporalmente
-mostrar datos listados en home
-opcion de salir
"""

from tkinter import *
from tkinter import ttk

#Definir ventana
ventana=Tk()
#ventana.geometry("500x500") se reemplaza con minsize
ventana.minsize(500,500)
ventana.title("Proyecto tkinter master en python")
ventana.resizable(0,0)

#Pantallas
def home():
    #montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=80,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=2)
    """
    #listar productos
    for product in products:
        if len (product)==3:
            product.append("added")
            Label(products_box,text=product[0]).grid()
            Label(products_box,text=product[1]).grid()
            Label(products_box,text=product[2]).grid()
            Label(products_box,text="------------").grid()
    """
    #insert lista en tabla
    for product in products:
        if len (product)==3:
            product.append("added")
            products_box.insert("",0,text=product[0],values=(product[1]))

    #ocultar demas pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=120,
        pady=20
    )
    add_label.grid(row=0, column=0,columnspan=10)
    #ubicacion Campos del formulario añadir
    add_frame.grid(row=1)

    add_name_label.grid(row=1,column=0, padx=5,pady=5,sticky=E)
    add_name_entry.grid(row=1,column=1, padx=5,pady=5,sticky=W)

    add_price_label.grid(row=2,column=0, padx=5,pady=5,sticky=E)
    add_price_entry.grid(row=2,column=1, padx=5,pady=5,sticky=W)

    add_descripcion_label.grid(row=3,column=0, padx=5,pady=5,sticky=NW)
    add_descripcion_entry.grid(row=3,column=1, padx=5,pady=5,sticky=W)
    add_descripcion_entry.config(
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )

    add_separador.grid(row=4)

    boton.grid(row=5,column=0,sticky=SE)
    boton.config(
        padx=15,
        bg="black",
        fg="white"
    )

    #ocultar demas pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=80,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    #ocultar demas pantallas
    home_label.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()
    products_box.grid_remove()

def add_product():
    products.append([
        name_data.get(),
        price.get(),
        add_descripcion_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price.set("")
    add_descripcion_entry.delete("1.0",END)

    home()#lleva a la home page


#variables importantes
products=[]
name_data=StringVar()
price=StringVar()

#definir campor de pantallas
home_label=Label(ventana,text="Inicio")
#products_box=Frame(ventana,width=250)

Label(ventana).grid(row=1)
products_box=ttk.Treeview(height=12,columns=2)
products_box.grid(row=1,column=0,columnspan=2)
products_box.heading("#0",text='Producto',anchor=W)
products_box.heading("#1",text="Precio",anchor=W)

add_label=Label(ventana,text="Añadir producto")
info_label=Label(ventana,text="Información")
data_label=Label(ventana,text="Creador por DR-2023")

#campos del formulario añadir
add_frame=Frame(ventana)

add_name_label=Label(add_frame,text="Nombre: ")
add_name_entry=Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame,text="Precio: ")
add_price_entry=Entry(add_frame, textvariable=price)

add_descripcion_label=Label(add_frame,text="Descripcion: ")
add_descripcion_entry=Text(add_frame)

add_separador=Label(add_frame)

boton=Button(add_frame,text="Guardar",command=add_product)

#cargar pantalla inicio
home()

#menu superior
menu_superior=Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información",command=info)
menu_superior.add_command(label="Salir",command=ventana.quit)

#Cargar menu
ventana.config(menu=menu_superior)

#cargar ventana
ventana.mainloop()