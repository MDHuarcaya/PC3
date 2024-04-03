
import operaciones

def main():
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))

        print("El resultado de la suma es :", operaciones.suma(a, b))
        print("El resultado de la restaes :", operaciones.resta(a, b))
        print("El resultado del producto es:", operaciones.producto(a, b))
        print("El resultado de la división es:", operaciones.division(a, b))
    except ValueError:
        print("Tipo de dato no válido, ingrese bien los valores")

if __name__ == "__main__":
    main()


