

def obtener_porcentaje():
    try:
        fraction = input("Ingrese una fracción en el formato X/Y: ")
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError("El denominador no puede ser cero")
        if x <= 0 or y <= 0 or x > y:
            raise ValueError("La fracción debe ser mayor que cero, con el numerador menor o igual que el denominador")

        percentage = (x / y) * 100
        if percentage < 1:
            print("Cantidad de combustible en el tanque: E")
        elif percentage > 99:
            print("Cantidad de combustible en el tanque: F")
        else:
            print("Cantidad de combustible en el tanque:", str(round(percentage)) + '%')
    except ValueError as ve:
        print("Error:", ve)
        obtener_porcentaje()
    except ZeroDivisionError as zde:
        print("Error:", zde)
        obtener_porcentaje()

def main():
    obtener_porcentaje()

if __name__ == "__main__":
    main()