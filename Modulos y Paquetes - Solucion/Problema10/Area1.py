from POO_solucion.Problema3 import CIRCULO
from POO_solucion.Problema4 import RECTANGULO
from fig_geometricas.cuadrado import Cuadrado

def mostrar_menu():
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = CIRCULO(radio)
            print("El área del círculo es:", circulo.circulo_area())
        elif opcion == "2":
            largo = float(input("Ingrese la base del rectángulo: "))
            ancho = float(input("Ingrese la altura del rectángulo: "))
            rectangulo = RECTANGULO(largo, ancho)
            print("El área del rectángulo es:", rectangulo.calcular_area_rectangulo())
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print("El área del cuadrado es:", cuadrado.calcular_area_cuadrado())
        elif opcion == "4":
            print("Hasta luego, fue un placer ayudarte...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()