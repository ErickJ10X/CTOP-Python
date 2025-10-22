num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

def esMayor(num1, num2):
    if num1 > num2:
        return f"El número {num1} es mayor que {num2}."
    if num2 > num1:
        return f"El número {num2} es mayor que {num1}."
    return "Ambos números son iguales."

print(esMayor(num1, num2))