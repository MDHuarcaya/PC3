

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
            print("Edad del estudiante: No esta asignado")
        if self.notas:
            print("Notas del estudiante:", self.notas)
        else:
            print("Notas del estudiante: No asignadas")
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, nota):
        self.notas.append(nota)

# Crear objetos de la clase Alumno
alumno1 = Alumno("Alex", "A24205576")
alumno2 = Alumno("Carla", "A2407663")
alumno3 = Alumno ("Marcos","A2457864")

# Mostrar información del estudiante
alumno1.display()
alumno2.display()
alumno3.display()

# Asignar edad al estudiante
alumno1.setAge(20)
alumno2.setAge(24)
alumno3.setAge(19)

# Asignar notas al estudiante
alumno1.setNota(13)
alumno1.setNota(15)
alumno1.setNota(17)
alumno2.setNota(18)
alumno2.setNota(20)
alumno2.setNota(17)
alumno3.setNota(20)
alumno3.setNota(15)
alumno3.setNota(20)

# Mostrar información actualizada del estudiante
alumno1.display()
alumno2.display()
