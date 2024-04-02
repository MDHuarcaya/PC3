

def obtener_calificaciones():
    try:
        notas = input("Por favor, Ingresar las notas o calificaciones separadas por comas: ")
        notas_lista = notas.split(',')
        notas_entero = [int(cal) for cal in notas_lista]
        return notas_entero
    except ValueError as ve:
        print("Error:", ve)
        return obtener_calificaciones()

def main():
    notas = obtener_calificaciones()
    print(f"Las calificaciones ingresadas son: {notas}")

if __name__ == "__main__":
    main()