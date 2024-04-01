
import operaciones

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        print("Suma:", operaciones.suma(a, b))
        print("Resta:", operaciones.resta(a, b))
        print("Producto:", operaciones.producto(a, b))
        print("División:", operaciones.division(a, b))
    except ValueError:
        print("Error: Tipo de dato no válido.")

if __name__ == "__main__":
    main()


