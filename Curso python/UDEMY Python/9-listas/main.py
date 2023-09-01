"""
Listas(arrays)
"""
 
peliculas=["eeeeee","aaaaa","fffff"]
cantantes=list(('dsdas','ffsdf','ghghh')) #es una tupla y no se puede modificar
years=list(range(2020,2050))

print(peliculas[1])
print(peliculas[-2]) #empieza de atrás 
print(peliculas[1:3]) #saca un rango
print(peliculas[1:]) #saca datos a partir de...

#añadir elemento a lista
cantantes.append("Kase")

#recorrer lista
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)}.{pelicula}")

#Listas multidimensionales
contactos=[
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'sara',
        'sara@gmail.com'
    ]
]

contactos([1][1])