#1
estudiantes = ['Erick', 'Luis', 'Sofía']

print(*estudiantes, sep=", ")

nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
if nuevo_estudiante.isalpha():
    estudiantes.append(nuevo_estudiante)
    print(*estudiantes, sep=", ")
else:
    print("El nombre del estudiante debe contener solo letras.")
    print(*estudiantes, sep=", ")

estudiante_eliminado = input("Ingresa el nombre del estudiante a eliminar: ")
if estudiante_eliminado.isalpha():
    pass
else:
    print("El nombre del estudiante debe contener solo letras.")
    print(*estudiantes, sep=", ")
    estudiante_eliminado = ""
if estudiante_eliminado in estudiantes:
    estudiantes.remove(estudiante_eliminado)
    print(*estudiantes, sep=", ")
else:
    print(f"El estudiante {estudiante_eliminado} no está en la lista.")
    print(*estudiantes, sep=", ")

estudiantes.sort()
print("Lista de estudiantes ordenada:")
print(*estudiantes, sep=", ")

#2

calificaciones = {'Erick': 8, 'Luis': 9, 'Sofía': 7}

nuevo_estudiante = input("Ingresa el nombre del estudiante para agregar su calificación: ")
if nuevo_estudiante.isalpha():
    pass
else:
    print("El nombre del estudiante debe contener solo letras.")
    print(*calificaciones, sep=", ")
    nuevo_estudiante = ""
try:
    nueva_calificacion = int(input(f"Ingresa la calificación de {nuevo_estudiante}: "))
except ValueError:
    print("La calificación debe ser un número entero.")
    print(*calificaciones, sep=", ")
    nueva_calificacion = 0
else:
    if 0 <= nueva_calificacion <= 10:
        calificaciones[nuevo_estudiante] = nueva_calificacion
        print(*calificaciones, sep=", ")
    else:
        print("La calificación debe estar entre 0 y 10.")
        print(*calificaciones, sep=", ")
        nueva_calificacion = 0


actualizar_estudiante = input("Ingresa el nombre del estudiante cuya calificación deseas actualizar: ")
if actualizar_estudiante.isalpha():
    pass
else:
    print("El nombre del estudiante debe contener solo letras.")
    print(*calificaciones, sep=", ")
    actualizar_estudiante = ""
if actualizar_estudiante in calificaciones:
    try:
        nueva_calificacion = int(input(f"Ingresa la nueva calificación de {actualizar_estudiante}: "))
    except ValueError:
        print("La calificación debe ser un número entero.")
        print(*calificaciones, sep=", ")
    else:
        if 0 <= nueva_calificacion <= 10:
            calificaciones[actualizar_estudiante] = nueva_calificacion
            print(*calificaciones, sep=", ")
        else:
            print("La calificación debe estar entre 0 y 10.")
            print(*calificaciones, sep=", ")
else:
    print(f"El estudiante {actualizar_estudiante} no está en el diccionario.")
    print(*calificaciones, sep=", ")

buscar_estudiante = input("Ingresa el nombre del estudiante para buscar su calificación: ")
if buscar_estudiante.isalpha():
    pass
else:
    print("El nombre del estudiante debe contener solo letras.")
    print(*calificaciones, sep=", ")
    buscar_estudiante = ""
if buscar_estudiante in calificaciones:
    print(f"La calificación de {buscar_estudiante} es: {calificaciones.get(buscar_estudiante)}")
else:
    print(f"El estudiante {buscar_estudiante} no está en el diccionario.")

for estudiante in calificaciones:
    print(f"{estudiante}: {calificaciones[estudiante]}")

nota_media = sum(calificaciones.values()) / len(calificaciones)
print(f"La nota media de la clase es: {nota_media}")

#3

file = open("alumnos.txt", "w")
for estudiante in calificaciones:
    file.write(f"{estudiante}: {calificaciones[estudiante]}\n")
file.close()

