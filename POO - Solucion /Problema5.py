

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
    
    def display(self):
        print("Nombre del estudiante:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad del estudiante:", self.edad)
        else:
            print("Edad del estudiante: No asignada")
        if self.notas:
            print("Notas del estudiante:", self.notas)
        else:
            print("Notas del estudiante: No asignadas")
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, nota):
        self.notas.append(nota)

# Crear objetos de la clase Alumno
alumno1 = Alumno("Juan", "A001")
alumno2 = Alumno("María", "A002")

# Mostrar información del estudiante
alumno1.display()

# Asignar edad al estudiante
alumno1.setAge(20)

# Asignar notas al estudiante
alumno1.setNota(90)
alumno1.setNota(85)

# Mostrar información actualizada del estudiante
alumno1.display()
