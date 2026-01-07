"""
EJERCICIO 5 – Arrays
-------------------
Crea un array de enteros y:

from array import array
nums = array( ... )

Cambia el valor del primer elemento
Intenta asignar un valor de tipo incorrecto
"""

from array import array

nums = array('i', [1, 2, 3, 4, 5])

print(nums)

nums[0] = 'hola'
