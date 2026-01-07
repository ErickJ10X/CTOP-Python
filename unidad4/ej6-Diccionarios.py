"""
EJERCICIO 6 – Diccionarios
--------------------------
Crea un diccionario con información de una persona:

nombre
edad

Luego, añade la clave "ciudad"
Elimina la clave "edad"
"""

Persona = {
    "nombre": "Lucas",
    "edad": 24
}

print(Persona)

Persona["ciudad"] = "Granada"

print(Persona)

Persona.pop("edad")
print(Persona)