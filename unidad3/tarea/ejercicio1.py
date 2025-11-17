# Autor: Erick Quispe
# Fecha: 14/11/2025
# Descripcion: Solicitar tres numeros enteros y mostrar el mayor de ellos.

# Solicitar tres numeros enteros al usuario
try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    num3 = int(input("Ingrese otro numero: "))
# Manejo de excepcion en caso de que el usuario ingrese un valor no entero
except ValueError:
    print("Error: Debe ingresar numeros enteros.")
    exit()

# Determinar el mayor de los tres numeros
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostrar el mayor numero
print("El numero mayor es:", mayor)