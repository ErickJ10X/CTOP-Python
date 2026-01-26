# Ra5 a ejercicio 1
# crear una clase Producto con atributos nombre y precio.

# Ra5 b ejercicio 2
# El atributo precio debe ser privado, crear getter y setter para el atributo precio.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio

    def mostrar(self):
        return f"Producto: {self.nombre}, Precio: {self.__precio}"

    def getPrecio(self):
        return self.__precio
    def setPrecio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

# Crear instancias de la clase Producto y mostrar su información.
producto1 = Producto("Laptop", 1200)
producto2 = Producto("Smartphone", 800)

# Mostrar la información de los productos.
print(producto1.mostrar())
print(producto2.mostrar())

# Ra5 c ejercicio 3
# clase productoAlimenticio que herede de Producto y tenga un atributo adicional fecha_de_caducidad.
class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, fecha_de_caducidad):
        super().__init__(nombre, precio)
        self.fecha_de_caducidad = fecha_de_caducidad

    def estaCaducado(self, fecha_actual):
        return fecha_actual > self.fecha_de_caducidad

    def mostrar(self):
        info_base = super().mostrar()
        return f"{info_base}, Fecha de Caducidad: {self.fecha_de_caducidad}"

# Crear instancias de ProductoAlimenticio y mostrar su información.
producto_alim1 = ProductoAlimenticio("Leche", 1.5, "2024-07-01")
print(producto_alim1.mostrar())
print("¿Está caducado?", producto_alim1.estaCaducado("2024-07-02"))

# Ra5 d ejercicio 4
# Usar sqlite3 para almacenar y recuperar productos de una base de datos.
import sqlite3

conexion = sqlite3.connect('productos.db')
cursor = conexion.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    precio REAL,
                    fecha_de_caducidad TEXT
                )
                """)

# Ra5 e ejercicio 5 y Ra f ejercicio 6
# clase gestora de base de datos para crud

class GestorDB:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def insertar_producto(self, producto):
        if isinstance(producto, ProductoAlimenticio):
            self.cursor.execute("INSERT INTO productos (nombre, precio, fecha_de_caducidad) VALUES (?, ?, ?)",
                                (producto.nombre, producto.getPrecio(), producto.fecha_de_caducidad))
        else:
            self.cursor.execute("INSERT INTO productos (nombre, precio, fecha_de_caducidad) VALUES (?, ?, ?)",
                                (producto.nombre, producto.getPrecio(), None))
        self.conexion.commit()

    def obtener_productos(self):
        return self.cursor.execute("SELECT * FROM productos").fetchall()


gestor = GestorDB(conexion)
gestor.insertar_producto(producto1)
gestor.insertar_producto(producto2)

lista_de_productos = gestor.obtener_productos()
for prod in lista_de_productos:
    print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: {prod[2]}, Fecha de Caducidad: {prod[3]}")
