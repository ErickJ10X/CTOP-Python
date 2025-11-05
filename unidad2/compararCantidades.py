def compararNumeros(num1, num2):
    if num1 > num2:
        return f"{num1} es mayor que {num2}"
    elif num1 < num2:
        return f"{num1} es menor que {num2}"
    else:
        return f"{num1} es igual a {num2}"


try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    print(compararNumeros(numero1, numero2))
except ValueError:
    print("Error: No has introducido un valor de tipo numerico.")
finally:
    print("Fin del programa.")
