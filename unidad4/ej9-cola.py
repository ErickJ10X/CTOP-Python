"""
EJERCICIO 9 – Cola (queue)
-------------------------
Simula una cola usando deque:

from collections import deque

Añade 3 elementos
Elimina el primero
Muestra la cola resultante

append() → añadir
popleft() → quitar el primero
"""

from collections import deque

cola = deque()

cola.append(1)
cola.append(2)
cola.append(3)

print(cola)

cola.popleft()

print(cola)