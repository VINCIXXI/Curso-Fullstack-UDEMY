import clases

persona1=clases.Persona()
persona1.setNombre("David")
persona1.setApellido("Rodriguez")
persona1.setAltura("181cm")
persona1.setEdad("20 años")

print(f"la persona es: {persona1.getNombre()} {persona1.getApellidos()}{persona1.getEdad}")
print(persona1.hablar())
print("-----------------------")


ingeniero=clases.Informatico()
ingeniero.setNombre("Rudolph")
ingeniero.setApellido("Santa")
print(f"el ingeniero de sistemas es: {ingeniero.getNombre()} {ingeniero.getApellidos()}")
print(ingeniero.lenguajes)