#1.Definir una clase de tipo coche
class coche:
    #atributos o propiedades
    color="Rojo"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    plazas=2

    soy_publico="Hola, soy un atributo publico"
    __soy_privado="Hola, soy un atributo privado"

    def __init__(self,color, marca, modelo, velocidad, caballaje, plazas): #definicion de constructor
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

    #metodos del coche
    def getPrivado(self):
        return self.__soy_privado
    
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
    
    def setMarca(self, marca):
        self.marca=marca
    def getMarca(self):    
        return self.marca
    
    def getInfo(self):
        info="---Informacion completa"
        info+="\n Color: "+self.getColor()
        info+="\n Marca: "+self.getMarca()
        info+="\n Modelo: "+self.getModelo()
        info+="\n Velocidad: "+str(self.getVelocidad())

        return info