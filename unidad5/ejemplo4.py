import sqlite3

conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()

cursor.execute("""
                    CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    salario REAL
                    )
                """)

# cursor.execute("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", ("Juan Perez", 3000.50))
conexion.commit()

empleados = cursor.execute("SELECT * FROM empleados").fetchall()

for empleado in empleados:
    print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Salario: {empleado[2]}")

cursor.close()
conexion.close()
