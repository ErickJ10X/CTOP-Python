"""
EJERCICIO 1 – Listas
-------------------
Crea una lista con 5 números enteros:

numeros = [1, 2, 3, 4, 5]

Añade un número al final
Elimina el último número
Muestra solo los 3 primeros elementos
"""

numeros = [1,2,3,4,5]

print(numeros)

numeros.append(6)

print(numeros)

numeros.pop()

print(numeros)

print(numeros[0:3])