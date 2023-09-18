#importar modulo 
import sqlite3

#conexion sqlite
conexion=sqlite3.connect('pruebas.db')

#crear cursor
cursor=conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+ 
"precio INT(255)"+              
")")

#guardar cambios
conexion.commit()

#insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'DEscripcion de mi producto',550)")
conexion.commit()
"""

#borrar registros
"""cursor.execute("DELEte FROM productos")"""

#insertar muchos datos de golpe
productos=[
    ("Ordenador portatil", "Buen PC", 700), #esto se reemplaza en los ?
    ("telefono", "Buen movil", 140),
    ("placa base", "Buen placa", 80),
    ("tablet", "Bueno", 250),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos) #signos se reemplazan por los datos arriba
conexion.commit()

#update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >=250;")
productos=cursor.fetchall()
#print(productos) #es una opcion mas desorganizada
for producto in productos:
    print("ID:",producto[0])
    print("Titulo:",producto[1])
    print("Desripcion:",producto[2])
    print("Precio:",producto[3])
    print("\n")

#cerrar conexion para guardar cambios
conexion.close()