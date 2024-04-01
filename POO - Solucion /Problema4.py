

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

# Crear objetos de la clase RECTANGULO
rectangulo1 = RECTANGULO(5, 10)
rectangulo2 = RECTANGULO(7, 8)

# Calcular y mostrar el área de los rectángulos
print("El área del rectángulo 1 es:", rectangulo1.calcular_area())
print("El área del rectángulo 2 es:", rectangulo2.calcular_area())