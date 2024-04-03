
def main():
    calcular_porcentaje()

def calcular_porcentaje():
    try:
        fraccion = input("Ingresar numeros enteros a  una fracción formato X/Y: ")
        x, y = map(int, fraccion.split('/'))
        if y == 0:
            raise ZeroDivisionError("El denominador no puede ser cero, ingrese bien los datos")
        if x <= 0 or y <= 0 or x > y:
            raise ValueError("La fracción debe ser mayor que cero, el numerador debe ser menor o igual que el denominador")

        porcentaje = (x / y) * 100
        if porcentaje < 1:
            print("Cantidad de combustible en el tanque: E")
        elif porcentaje > 99:
            print("Cantidad de combustible en el tanque: F")
        else:
            print("Cantidad de combustible en el tanque:", str(round(porcentaje)), "%")
    except ValueError as ve:
        print("Error, Solo se permite numeros enteros:", ve)
        calcular_porcentaje()
    except ZeroDivisionError as zde:
        print("Error:", zde)
        calcular_porcentaje()

if __name__ == "__main__":
    main()