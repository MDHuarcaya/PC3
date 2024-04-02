

class Producto:
    # Constructor de clase
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catálogo:
    def __init__(self):
        self.productos = []

    def agg_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print("Nombre:", producto.nombre)
            print("Precio:", producto.precio)
            print("Año:", producto.año)
            print()

# Crear objetos de la clase Producto
            
producto1 = Producto("Batería de auto", 323, 2022)
producto2 = Producto("Rueda o llanta", 460, 2023)

# Crear objeto de la clase Catálogo y agregar productos

catálogo = Catálogo()
catálogo.agg_producto(producto1)
catálogo.agg_producto(producto2)

# Mostrar lista de productos en el catálogo
catálogo.mostrar_productos()
