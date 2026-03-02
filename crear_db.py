import sqlite3

# Conectar (o crear) la base de datos
conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

# Crear tabla productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
)
''')

conn.commit()
conn.close()

print("Base de datos y tabla productos creada correctamente.")