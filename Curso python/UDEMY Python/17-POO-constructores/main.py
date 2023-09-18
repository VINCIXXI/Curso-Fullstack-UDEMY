from coche import coche
carro1=coche("Amarillo", "Renault", "clio",150,200, 4)
carro2=coche("Rojo", "Lambo", "aventa",150,200, 4)
carro3=coche("verde", "seat", "panda",150,200, 4)

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#detectar el tipado
if type(carro3)==coche:
    print("es un objeto")
else:
    print("NO es un objeto")

# visibilidad
print(carro1.soy_publico)
#print(carro1.__soy_privado) #muestra error
print(carro1.getPrivado())