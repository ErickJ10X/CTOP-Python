"""----- APARTADO 1 -----"""


class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn

    def obtener_titulo(self):
        return self._titulo

    def obtener_autor(self):
        return self._autor

    def obtener_isbn(self):
        return self._isbn

    def informacion_libro(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, ISBN: {self._isbn}"


libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-1-56619-909-4")

print(libro1.informacion_libro())
print(libro2.informacion_libro())

"""----- APARTADO 2 -----"""
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamanio):
        super().__init__(titulo, autor, isbn)
        self._tamanio = tamanio

    def obtener_tamanio(self):
        return self._tamanio
    def informacion_libro(self):
        info_base = super().informacion_libro()
        return f"{info_base}, Tamaño: {self._tamanio} MB"

libroDigital1 = LibroDigital("1984", "George Orwell", "978-0-452-28423-4", 1.5)
libroDigital2 = LibroDigital("Fahrenheit 451", "Ray Bradbury", "978-0-7432-4722-1", 2.0)

print(libroDigital1.informacion_libro())
print(libroDigital2.informacion_libro())

"""----- APARTADO 3 -----"""
import sqlite3

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS libros
               (
                   id
                   INTEGER
                   PRIMARY
                   KEY
                   AUTOINCREMENT,
                   titulo
                   TEXT,
                   autor
                   TEXT,
                   isbn
                   TEXT
               )
               """)

def insertar_libro(titulo, autor, isbn):
    cursor.execute("INSERT INTO libros (titulo, autor, isbn) VALUES (?, ?, ?)", (titulo, autor, isbn))
    conexion.commit()

def obtener_libros():
    return cursor.execute("SELECT * FROM libros").fetchall()


insertar_libro(libro1.obtener_titulo(), libro1.obtener_autor(), libro1.obtener_isbn())
insertar_libro(libro2.obtener_titulo(), libro2.obtener_autor(), libro2.obtener_isbn())
insertar_libro(libroDigital1.obtener_titulo(), libroDigital1.obtener_autor(), libroDigital1.obtener_isbn())
insertar_libro(libroDigital2.obtener_titulo(), libroDigital2.obtener_autor(), libroDigital2.obtener_isbn())

libros = obtener_libros()
for libro in libros:
    print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, ISBN: {libro[3]}")

cursor.close()
conexion.close()
