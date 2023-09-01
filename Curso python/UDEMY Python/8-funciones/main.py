"""
es un conjunto de instrucciones 
que se llama cuantas veces sea necesario
"""

def muestraNombre():
    print("fsfasfs")
    print("dgsdgsdg")

muestraNombre()

def mostrarNombre(nombre):
    print(f"fasfafa {nombre}")
muestraNombre("afasfas")
muestraNombre("iihth")

# Parametros opcionales
def getEmpleado(nombre, dni=None): #se coloca un =
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni!=None:
        print(f"DNI: {dni}")
getEmpleado("Victor robles")

#return
def saludame(nombre):
    saludo=print(f"Hola {nombre}")
    return saludo
saludame("David")

# funciones Lambda
dime_el_year=lambda year: print(f"el año es: {year}")
dime_el_year(2024) #se define en una sola linea



