class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, cantidad):
        if cantidad >= 0:
            self.__saldo = cantidad
        else:
            print("El saldo no puede ser negativo")

c = Cuenta(100)

print(c.saldo)
c.saldo = -1
print(c.saldo)