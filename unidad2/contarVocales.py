texto = "Hola, aqui programando en Python"
vocales = "aeiouAEIOU"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1
print("Número de vocales en el texto: ", contador)