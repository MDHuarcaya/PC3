

class Producto:
    # Constructor de clase
    def __init__(self, Nombre, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:

    productos = []  # Esta lista contendrá objetos de la clase Productos

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)


p = Pelicula("El Padrino", duracion=175, lanzamiento=1972)
p2 = Pelicula("Avatar", duracion=200, lanzamiento=2008)
catalogo_netflix = Catalogo([p])  # Añado una lista con una película desde el principio
catalogo_amazon = Catalogo([p2])

# mostrando el catalogo de peliculas actual
catalogo_netflix.mostrar()
catalogo_amazon.mostrar()

catalogo_netflix.agregar(Pelicula(titulo='Rapidos y furiosos 9', duracion=150, lanzamiento=2019))
catalogo_netflix.mostrar()

#SOLUCION

class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catálogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print("Nombre:", producto.nombre)
            print("Precio:", producto.precio)
            print("Año:", producto.año)
            print()

# Crear objetos de la clase Producto
producto1 = Producto("Batería de auto", 100, 2022)
producto2 = Producto("Filtro de aceite", 20, 2023)

# Crear objeto de la clase Catálogo y agregar productos
catálogo = Catálogo()
catálogo.agregar_producto(producto1)
catálogo.agregar_producto(producto2)

# Mostrar lista de productos en el catálogo
catálogo.mostrar_productos()
