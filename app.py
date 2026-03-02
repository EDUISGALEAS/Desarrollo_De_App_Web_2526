from flask import Flask, render_template, request, redirect

app = Flask(__name__)

productos = []

@app.route("/")
def inicio():
    return render_template("index.html", productos=productos)

@app.route("/about")
def about():
    return render_template("about.html")  # Página Acerca de

@app.route("/productos")
def productos_page():
    return render_template("index.html", productos=productos)  # Lista de productos

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    cantidad = request.form["cantidad"]

    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)