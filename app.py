from flask import Flask, render_template, request, redirect
import sqlite3
from models import Producto, Inventario  # Tu archivo models.py

app = Flask(__name__)

# Inicializar inventario
inventario = Inventario()

# Función para cargar productos desde la base de datos
def cargar_productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, cantidad, precio FROM productos")
    for row in cursor.fetchall():
        prod = Producto(row[0], row[1], row[2], row[3])
        inventario.agregar_producto(prod)
    conn.close()

cargar_productos()

# ----------------- RUTAS -----------------

@app.route("/")
def inicio():
    return render_template("index.html", productos=inventario.mostrar_todos())

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    cantidad = int(request.form["cantidad"])
    precio = float(request.form["precio"])

    # Guardar en SQLite
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                   (nombre, cantidad, precio))
    conn.commit()
    id_nuevo = cursor.lastrowid
    conn.close()

    # Guardar en la colección POO
    producto = Producto(id_nuevo, nombre, cantidad, precio)
    inventario.agregar_producto(producto)

    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    # Eliminar de SQLite
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    # Eliminar de la colección POO
    inventario.eliminar_producto(id)

    return redirect("/")

@app.route("/actualizar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    producto = inventario.productos.get(id)
    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])

        # Actualizar SQLite
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET nombre=?, cantidad=?, precio=? WHERE id=?",
                       (nombre, cantidad, precio, id))
        conn.commit()
        conn.close()

        # Actualizar colección POO
        inventario.actualizar_producto(id, nombre, cantidad, precio)

        return redirect("/")

    return render_template("actualizar.html", producto=producto)

@app.route("/buscar", methods=["GET"])
def buscar():
    nombre = request.args.get("nombre", "")
    resultados = inventario.buscar_producto(nombre) if nombre else []
    return render_template("buscar.html", resultados=resultados)

@app.route("/about")
def about():
    return render_template("about.html")

# ----------------- INICIAR APP -----------------
if __name__ == "__main__":
    app.run(debug=True)