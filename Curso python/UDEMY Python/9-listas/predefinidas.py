
#ordenar una lista
numeros=[1,2,5,7,3,6]

print(numeros)
numeros.sort()
print(numeros)

#agregar
cantantes=["fasfasf","sfasfasf"]
cantantes.append("assaf")
cantantes.insert(1,"safsf") #se le pasa el indice a agregar

#buscar dentro de una lista
print("hgfs" in cantantes)

#unir listas
cantantes.extend(numeros)
print(cantantes)