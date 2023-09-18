#para instalar el plugin de sql en python se coloca en cmd
# pip install mysql-connector-python

import mysql.connector

#conexion
database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# ¿la conexion es correcta?
"""
print(database)
"""

#cursor 
cursor=database.cursor()
"""
#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#para mostrar DB
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
"""

#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id INT(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2),
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#mostrar tablas
"""
cursor.execute("SHOW TABLES")
for tabla in cursor:
    print(tabla)
"""
    
#insertar datos
"""
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel','Astra',18500)")
"""

#insertar datos masivos
"""
coches=[
    ('Renault','clio',5000),
    ('Seat','ibiza',15000),
    ('mercedes','a300',20000)
]
cursor.executemany("INSERT INTO vehiculos VALUES(null, %s,%s,%s)",coches)
database.commit()
"""

#visualizar elemtnos
"""
cursor.execute("SELECT * FROM vehiculos") #se puede usar WHERE para ver con condicional
result=cursor.fetchall()
#------------.fetchone() para sacar la primera fila

print("-----Todos los coches--------")
for coche in result:
    print(coche)
"""
#borrar   
"""
cursor.execute("DELETE FROM vehiculos WHERE marca='Renault' ")
database.commit()
"""

#actualizar
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat' ")
database.commit()