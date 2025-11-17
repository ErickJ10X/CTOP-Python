# Autor: Erick Quispe
# Fecha: 14/11/2025
# Descripcion: Solicitar dos numeros y una operacion (+,-,*,/) y mostrar el resultado de la operacion.

# Solicitar dos numeros al usuario
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
# Manejo de excepcion en caso de que el usuario ingrese un valor no numerico
except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos.")
    exit()

# Solicitar la operacion a realizar
try:
    operacion = input("Seleccione la operación a realizar (+,-,*,/):")
    if operacion not in ['+', '-', '*', '/']:
        raise ValueError("Operación no válida.")
except ValueError:
    print("Error: Operación no válida.")
    exit()

# Realizar la operacion y mostrar el resultado
if operacion == '+':
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == '-':
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == '*':
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")