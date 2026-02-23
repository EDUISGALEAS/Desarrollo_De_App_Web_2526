from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Eduardo Galeas Bienvenido al Sistema de ventas – Víveres y Carnes S.A."

@app.route('/producto/<nombre>')
def producto(nombre):
    return f"Producto: {nombre} - Si hay en el inventario."

@app.route('/cliente/<nombre>')
def cliente(nombre):
    return f"Bienvenido {nombre}, El pedido está en proceso."

if __name__ == '__main__':
    app.run(debug=True)