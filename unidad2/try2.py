lista = [1, 2, 3, 4, 5]

try:
    for numero in lista:
        print(numero)
except IndexError as e:
    print("Error: ", e)
else:
    print("Finalizo sin errores")
finally:
    print("Ejecucion finalizada")