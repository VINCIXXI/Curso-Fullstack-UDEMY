# POO

#1.Definir una clase de tipo coche
class coche:
    #atributos o propiedades
    color="Rojo"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    plazas=2

    #metodos del coche
    def acelerar(self): #palabra reservada para acceder a las propiedades
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1

    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color=color #se asignará el color que queramos
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    

#crear objetos o instanciar clase
carro=coche()

coche.setColor("Trnasparente")

print(coche.marca, coche.getModelo,coche.getColor)
print("Velocidad actual: ",coche.getVelocidad())
print("!-----------------------------!")

# crear más objetos
carro2=coche()
carro2.setColor("Verde")
carro2.setModelo("Lykan")
print(carro2.getColor, carro2.getModelo)
