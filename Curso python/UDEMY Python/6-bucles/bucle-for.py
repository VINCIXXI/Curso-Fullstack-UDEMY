contador=0
for contador in range(0,5):
    print("Voy por el "+str(contador))


numero_usuario=int(input("De que numero quieres la tabla?: "))
if numero_usuario<1:
    numero_usuario=1

for numero_tabla in range(1,11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finaliza") 