# Autor: Erick Quispe
# Fecha: 14/11/2025
# Descripcion: Comparar el tiempo de ejecucion de un ciclo for y la funcion sum() para sumar numeros del 1 al 1,000,000.

import time

# Medir el tiempo de ejecucion del ciclo for
inicio = time.time()
contador = 0
# Ciclo for para sumar numeros del 1 al 1,000,000
for i in range(1, 1000001):
    contador += i

# Medir el tiempo final
final = time.time()
# Mostrar resultados
print('la suma de los numeros de 1 a 1,000,000 es:', contador)
print('Tiempo de ejecucion del ciclo for:', final - inicio)
# Medir el tiempo de ejecucion de la funcion sum()
inicio = time.time()
print('la suma de los numeros de 1 a 1,000,000 es:', sum(range(1, 1000001)))
# Medir el tiempo final
final = time.time()
# Mostrar resultados
print('Tiempo de ejecucion de la funcion sum():', final - inicio)