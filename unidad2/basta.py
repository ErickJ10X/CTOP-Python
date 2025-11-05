palabra = ""
frase = ""
contador = 0

while True:
    palabra = input("Escribe la palabra 'Basta' para terminar: ")
    if palabra == "Basta":
        print(f"¡Has escrito 'Basta'!Has soportado estoicamente {contador} preguntas")
        break
    frase = frase + palabra + " "
    print(frase)
    contador += 1

