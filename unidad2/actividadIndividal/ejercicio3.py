numero = int(input("Introduce un numero: "))

def cuentaAtras(numero):
    while numero != 0:
        print(numero)
        numero -= 1

cuentaAtras(numero)