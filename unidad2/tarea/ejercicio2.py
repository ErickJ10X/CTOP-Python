try:
    num = int(input("Ingrese un número entero: "))
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
else:
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
