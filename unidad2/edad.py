edad = int(input("cuantos años tienes? "))

if 1 <= edad <= 15:
    print("Eres un niño")
elif 16 <= edad <= 21:
    print("Eres un adolescente")
elif 22 <= edad <= 35:
    print("Eres un joven")
elif 36 <= edad <= 50:
    print("Eres maduro")
elif 51 <= edad <= 60:
    print("Eres de mediana edad")
elif 61 < edad <= 80:
    print("Eres mayor")
elif 81 <= edad <= 100:
    print("Eres viejo")
else:
    print("Edad centenaria")