"""
EJERCICIO 7 – Diccionarios
--------------------------

Recorre el diccionario anterior e imprime las claves y valores.
"""

Persona = {
    "nombre": "Lucas",
    "edad": 24,
    "ciudad": "Granada"
}

for clave, valor in Persona.items():
    print(f"{clave}: {valor}")