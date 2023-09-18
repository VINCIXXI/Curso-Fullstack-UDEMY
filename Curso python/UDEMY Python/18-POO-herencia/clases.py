# Herencia: es la posibilidad de compartir atributos y metodos entre clases
class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getAltura(self):
        return self.altura
    def getEdad(self):
        return self.edad
    
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self,apellidos):
        self.apellidos=apellidos
    def setAltura(self,altura):
        self.altura=altura
    def setEdad(self,edad):
        self.edad=edad

    def hablar(self):
        return "estoy hablando"
    
    def caminar(self):
        return "estoy caminando"
    
    def dormir(self):
        return "estoy durmiendo"
    
class Informatico(Persona): #hereda de la clase persona
    """
    lenguajes
    experiencia
    """

    def __init__(self):#constructor exclusivo de cada clase
        self.lenguajes="HTML, CSS, HS"
        self.experiencia=5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self,lenguajes):
        self.lenguajes=lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def reparar(self):
        return "he reparado tu ordenador"
    
    class TecnidoRedes(Informatico): #hereda de la clase Informatico
        def __init__(self):
            super().__init__() #para que herede de la clase padre
            self.auditarRedes="experto"
            self.expRedes=15
