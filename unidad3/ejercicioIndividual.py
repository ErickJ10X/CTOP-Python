# ejercicio 1

alumno = {'nombre': 'Erick', 'edad': 24, 'estudiante': True}
alumno2 = {'nombre': 'Juan', 'edad': 21, 'estudiante': True}
alumno3 = {'nombre': 'Alejandro', 'edad': 21, 'estudiante': True}


def esMayorDeEdad(alumno):
    if alumno['edad'] < 18:
        return 'Eres menor de edad'
    elif 18 <= alumno['edad'] <= 25:
        return 'Eres muy joven'
    elif 26 <= alumno['edad'] <= 40:
        return 'Eres Joven'
    else:
        return 'Ya no eres joven'


print(esMayorDeEdad(alumno))
print(esMayorDeEdad(alumno2))
print(esMayorDeEdad(alumno3))


# ejercicio 2

def crearTablaMultiplicar(n):
    tabla = []
    for i in range(1, 11):
        tabla.append(f"{n} x {i} = {n * i}")
    return tabla


try:
    num = int(input("Ingrese un número del 5 al 12: "))
    if num < 5 or num > 12:
        raise ValueError
except ValueError:
    print("Error: Por favor, ingrese un número entero válido que este entre el 5 y el 12.")
else:
    tabla = crearTablaMultiplicar(num)
    for linea in tabla:
        print(linea)


# ejercicio 3

def mediaAritmetica():
    num1=0
    num2=0
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")
    else:
        media = (num1 + num2) / 2
        print(f"La media aritmética de {num1} y {num2} es {media}")


mediaAritmetica()


def mediaAritmeticaLista(lista):
    try:
        numeros = [float(x) for x in lista]
    except ValueError:
        print("Error: Por favor, ingrese una lista de números válidos.")
    else:
        media = sum(numeros) / len(numeros)
        print(f"La media aritmética de la lista es {media}")

mediaAritmeticaLista([10, 20, 30, 40, 50])
# ejercicio 4
from unidad3.operaciones import sumar, restar

print(sumar(10,20))
print(restar(30,15))




