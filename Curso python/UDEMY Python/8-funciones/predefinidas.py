nombre="dasdas"
#funciones generales
print(nombre)

#comprobar el tipo
print(type(nombre))
comprobar=isinstance(nombre,str)
if comprobar==True:
    print("Es string")
else:
    print("No es string")

#Limpiar espacios
frase="     dsaadasda   "
print(frase)
print(frase.strip)

#Eliminar variables
year=2032
print(year)
del year

#comprobar caracteres
texto="  dasd"
if len(texto)<=0:
    print("esta vacio")
else:
    print("tiene: ",len(texto))

"""
importante tener en cuenta que siempre es mejor
que las funciones retornen datos y no print
Es por eso que se coloca el print afuera de la fx
"""