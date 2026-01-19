class Saiyan:
    planta = "Sadala"
    def __init__(self, nombre):
        self.nombre = nombre

class Goku(Saiyan):
    pass

class Vegeta(Saiyan):
    pass

personaje1 = Goku("Goku")
personaje2 = Vegeta("Vegeta")
print(f"personaje 1:  {personaje1.nombre}")
print(f"personaje 2:  {personaje2.nombre}")