# models.py
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        if id in self.productos:
            if nombre:
                self.productos[id].actualizar_nombre(nombre)
            if cantidad is not None:
                self.productos[id].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id].actualizar_precio(precio)

    def buscar_producto(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        return list(self.productos.values())