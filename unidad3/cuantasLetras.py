palabra = input("Escribe una palabra: ")
contador = 0
for letra in palabra:
    contador += 1
print(f"La palabra '{palabra}' tiene {contador} letras.")