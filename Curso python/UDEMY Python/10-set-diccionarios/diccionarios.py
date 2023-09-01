"""
un tipo de dato que almacena un conjunto de datos
en formato clave>valor
parecido a un array asociativo o json
"""

persona={
    "nombre":"david",
    "apellido":"rod",
}

print(persona["nombre"])

#lista con diccionarios
contactos=[
    {
        "nombre":"asdasd",
        "apellido":"asdasf"
    },
    {
        "nombre":"khkhj",
        "apellido":"ytryr"
    }
]
contactos[0]['nombre']="Davicito"
print(contactos[0]['nombre'])

