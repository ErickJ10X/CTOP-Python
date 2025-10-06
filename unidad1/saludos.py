import sys

def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Hasta luegui, {nombre}!"


if __name__ == "__main__":
    print('no me ejecutes, !solo soy un modulo¡')
    print(__name__)
    sys.exit(1)
else:
    print(__name__)