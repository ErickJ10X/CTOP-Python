notas =[]

for i in range(3):
    nota = float(input(f"Introduce la nota {i+1}: "))
    notas.append(nota)

def calcularPromedio(notas):
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

print(f"El promedio de las notas es: {calcularPromedio(notas)}")