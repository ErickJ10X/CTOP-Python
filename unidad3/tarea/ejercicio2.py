# Autor: Erick Quispe
# Fecha: 14/11/2025
# Descripcion: Solicitar un numero entero y mostrar todos los numeros desde 0 hasta ese numero.

# Solicitar un numero entero al usuario
try:
    num = int(input("Ingrese un número entero: "))

# Manejo de excepcion en caso de que el usuario ingrese un valor no entero
except ValueError:
    print("Error: Debe ingresar un número entero.")
    exit()

# Mostrar todos los numeros desde 0 hasta el numero ingresado
for i in range(num + 1):
    print(i)