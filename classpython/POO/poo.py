class Persona: #Clase persona
    __altura=1.77 #Encapsulamiento
    #Constructor
    def __init__(self, nombre, edad):
        self.name=nombre
        self.years=edad
    #Setters de una clase
    def setEdad(self, edad):
        self.years=edad
    #getters devuelven los valores
    def getEdad(self):
        return self.years

    #metodos son funciones
    def caminar(self):
        print("Estoy caminando")


#instancias
persona1 = Persona("Wilder", 20) #CONSTRUCTOR
print(persona1.name)
print(persona1.years)
persona1.caminar()

#Con