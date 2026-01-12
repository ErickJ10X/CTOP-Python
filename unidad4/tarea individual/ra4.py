# RA4_A - Ejercicio 1
# lista de productos
productos = ['cafe', 'azucar', 'leche', 'pan', 'mantequilla']

# imprimir la lista de productos ()
print('productos:')
print(*productos, sep=', ')

# imprimir primer elemento de la lista
print('primer producto:')
print(productos[0])

# imprimir ultimo elemento de la lista
print('ultimo producto:')
print(productos[-1])

# añadir un nuevo elemento a la lista y imprimir la lista actualizada
productos.append('huevos')
print(*productos, sep=', ')

# Ra4_B- Ejercicio 2

# ordenar productos alfabeticamente y mostrar la lista ordenada
print('Productos sin ordenar:')
print(*productos, sep=', ')
productos.sort()
print('Productos ordenados:')
print(*productos, sep=', ')

# eliminar un producto concreto de la lista e imprimir la lista actualizada
productos.remove('leche')
print('Productos despues de eliminar leche:')
print(*productos, sep=', ')

# Ra4_C - Ejercicio 3
# crear un diccionario con el stock de los productos
stock = {
    'cafe': 10,
    'azucar': 5,
    'leche': 8,
    'pan': 15,
    'mantequilla': 7}

for producto, cantidad in stock.items():
    print(f'{producto}: {cantidad}')

# funciones

# funcion para obtener el total de productos en stock
def total_de_productos(stock):
    total = sum(stock.values())
    return total

# funcion para obtener los productos con stock mayor a una cantidad dada
def productos_con_stock_mayor_a(stock, cantidad):
    productos = []
    for producto, stock_cantidad in stock.items():
        if stock_cantidad > cantidad:
            productos.append(producto)
    return productos

# probar las funciones
total = total_de_productos(stock)
print(f'Total de productos en stock: {total}')
productos_mayores_a_7 = productos_con_stock_mayor_a(stock, 7)
print(f'Productos con stock mayor a 7: {productos_mayores_a_7}')

# Ra4_D - Ejercicio 4

productos_t = tuple(productos)

"""
Una tupla es una estructura de datos similar a una lista, pero a diferencia de las listas, 
las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. 

ejemplo:
si los datos de productos no van a cambiar, es mejor usar una tupla para representarlos,
ya que esto garantiza que los datos permanezcan constantes a lo largo del programa.
Esto mejora la seguridad y la integridad de los datos.
"""

# Ra4_E - Ejercicio 5
#diccionario anidado
almacen = {
    'cafe': {'precio': 1.5, 'stock': 10},
    'azucar': {'precio': 0.8, 'stock': 5},
    'leche': {'precio': 1.2, 'stock': 8},
    'pan': {'precio': 1.0, 'stock': 15},
    'mantequilla': {'precio': 2.0, 'stock': 7}
}

# precio de un producto concreto
producto = 'cafe'
precio_cafe = almacen[producto]['precio']
print(f'El precio del {producto} es: {precio_cafe}')

# productos con stock menor a una cantidad dada
def productos_con_stock_menor_a(almacen, cantidad):
    productos = []
    for producto, info in almacen.items():
        if info['stock'] < cantidad:
            productos.append(producto)
    return productos
productos_menores_a_8 = productos_con_stock_menor_a(almacen, 8)
print(f'Productos con stock menor a 8: {productos_menores_a_8}')

# calcular el valor total del stock
def valor_total_del_stock(almacen):
    total = 0
    for producto, info in almacen.items():
        total += info['precio'] * info['stock']
    return total
valor_total = valor_total_del_stock(almacen)
print(f'Valor total del stock: {valor_total}')