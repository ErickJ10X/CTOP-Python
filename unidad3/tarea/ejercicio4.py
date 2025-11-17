# Autor: Erick Quispe
# Fecha: 14/11/2025
# Descripcion: Solicitar la base y la altura de un rectangulo y mostrar su area.

# Funcion para calcular el area del rectangulo
def area_rectangulo(base, altura):
    area = base * altura
    return area
# Solicitar la base y la altura al usuario
try:
    base = int(input('Introduce la base: '))
    altura = int(input('Introduce la altura: '))
# Manejo de excepcion en caso de que el usuario ingrese un valor no entero
except ValueError:
    print('Error: Debe ingresar numeros enteros.')
    exit()
# Calcular el area del rectangulo
else:
    area = area_rectangulo(base, altura)
    print('El area es: ', area)