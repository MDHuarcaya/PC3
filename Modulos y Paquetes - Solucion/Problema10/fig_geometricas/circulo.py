import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def circulo_area(self):
        return math.pi * (self.radio ** 2)
