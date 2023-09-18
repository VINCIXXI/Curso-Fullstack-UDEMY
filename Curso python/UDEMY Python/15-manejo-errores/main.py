# capturar excepciones y manejar errores en código
try:#se ejecuta en el pedazo que puede ser el error
    nombre=input("Cual es tu nombre?")
    if len(nombre)>1: #longitud minima de 1
        nombre_usuario="El nombre es: "+nombre

    print(nombre_usuario)

except: #se ejecuta cuando se encuentra un error
    print("Ha ocurrido un error, ingresa el nombre correcto")
else:
    print("Todo esta correcto")
finally:
    print("Fin del ciclo")


# manejar multiples errores
try:
    numero=int(input("numero para elevar al cuadrado: "))
    print("el numero es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error: ",type(e).__name__) #nombre del error


# excepciones personalizadas
nombre=input("Ingrese su nombre: ")
edad=int(input("ingresa edad: "))
try:
    if edad<5 or edad>110:
        raise ValueError("La edad introducida no es real")  #genera un error
    elif len(nombre)<=1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"bienvenido {nombre}")
except ValueError:
    print("introduce los datos correctamente")
except Exception as e: #errores mas concretos
    print("Existe un error: ",e)
