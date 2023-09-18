"""
modulos son funcionalidades hechas para reutilizar.
Hay muchos modulos por defecto y se pueden consultar aqui:
https://docs.python.org/es/3/tutorial/modules.html
 tambien podemos crear modulos.
"""

#importar el modulo creado
import mimodulo

# from mimodulo import holaMundo
#asi se llama a una sola funcion de un modulo

#from mimodulo import *
#importa todas las funciones del modulo y no hay necesidad de fx.(metodo)

print(mimodulo.holaMundo("David R"))

#modulo fechas
import datetime

print(datetime.date.today())

fecha_completa=datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)

# modulo matemáticas
import math

print("Raiz cuadrada de 10:",math.sqrt(10))

# Modulo random
import random

print("Numero aleatorio entre 15 y 67: ",random.randint(15,67))
