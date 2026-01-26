
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def obtener_precio(self):
        return self.precio

class Pedido:
    def __init__(self, productos):
        self.productos = productos

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.obtener_precio()
            total += producto.obtener_precio()
        return total

lista_de_productos = [Producto("Camisa", 20), Producto("Pantalones", 40), Producto("Zapatos", 60)]
pedido1 = Pedido(lista_de_productos)
print("Total del pedido 1:", pedido1.calcular_total())