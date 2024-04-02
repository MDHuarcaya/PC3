

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area_rectangulo(self):
        return self.largo * self.ancho

# Crear objetos de la clase RECTANGULO
    
r1 = RECTANGULO(7, 15)
r2 = RECTANGULO(9, 24)
r3 = RECTANGULO(15, 6)

# Calcular y mostrar el área de los rectángulos

print("El área del rectángulo 1 es:", r1.calcular_area_rectangulo())
print("El área del rectángulo 2 es:", r2.calcular_area_rectangulo())
print("El área del rectángulo 3 es:", r3.calcular_area_rectangulo())