"""
Proyecto python y MySQL:
-Abrir asistente
-Login o registro
-Si registro, creara un usuario en la BBDD
-Si login, identifica al usuario
-Crear nota, mostrar notas y borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
      -Registro
      -login
""")

hazEl=acciones.Acciones() #instanciar la clase

accion=input("¿Que quieres hacer?")

if accion=="Registro":
    hazEl.registro()

elif accion=="login":
    hazEl.login()
