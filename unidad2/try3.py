numero = input("Ingrese un numero: ")

try:
    numero = int(numero)
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
else:
    print(numero)
finally:
    print("Ejecución finalizada.")