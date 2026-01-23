class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self._edad = edad
        self.__dni = dni

    def getEdad(self):
        return self._edad

p = Persona("Ariel", 22, "000000000Z")

print(p.nombre)     # Acceso permitido (atributo público)
print(p.getEdad())        # Acceso permitido (convención de un solo guion bajo)
print(p._Persona__dni)      # Acceso denegado (atributo privado)