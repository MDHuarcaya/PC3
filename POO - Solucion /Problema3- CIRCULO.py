
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calculo_area(self):
        return math.pi * (self.radio ** 2)

# Creando objetos a partir de mi clase 
    
c1 = CIRCULO(4)
c2 = CIRCULO(8)
c3 = CIRCULO(12)
c4 = CIRCULO(60)
c5 = CIRCULO(400)

# El área de los círculos
print("El área del círculo 1 es:", c1.calculo_area())
print("El área del círculo 2 es:", c2.calculo_area())
print("El área del círculo 1 es:", c3.calculo_area())
print("El área del círculo 2 es:", c4.calculo_area())
print("El área del círculo 2 es:", c5.calculo_area())