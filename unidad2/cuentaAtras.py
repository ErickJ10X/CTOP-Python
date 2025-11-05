import time;

def cuenta_atras(segundos):
    while segundos:
        print(f"{segundos}...")
        time.sleep(0.5)
        segundos -= 1
    print("¡Tiempo terminado!")

segundosPedidos = int(input("Ingrese el número de segundos para la cuenta atrás: "))

cuenta_atras(segundosPedidos)
