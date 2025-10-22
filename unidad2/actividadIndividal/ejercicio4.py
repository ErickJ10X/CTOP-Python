n = int(input("Ingrese un numero:"))

def numerosPares(n):
    pares = []
    for i in range(n+1):
        if n == 1:
            return "No hay numeros pares"
        if i % 2 == 0:
            print(i)
            pares.append(i)
    return sum(pares)

print(f"La suma de los numeros pares es: {numerosPares(n)}")
