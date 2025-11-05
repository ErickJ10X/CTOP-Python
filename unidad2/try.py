texto = "";

try:
    f = open("archivo.txt", "r")
    texto = f.read()
    f.write("hola, ke hase")
except IndexError as e:
    print("Error: ", e)
else:
    print("Finalizo sin errores")
finally:
    f.close()