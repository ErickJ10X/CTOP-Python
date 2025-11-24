contador = 0
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre + "! Bienvenido/a al programa.")
for i in nombre:
    contador += 1
print(f"Tu nombre tiene {contador} letras.")
