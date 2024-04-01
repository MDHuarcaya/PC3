

def obtener_calificaciones():
    try:
        calificaciones = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones_lista = calificaciones.split(',')
        calificaciones_entero = [int(cal) for cal in calificaciones_lista]
        return calificaciones_entero
    except ValueError as ve:
        print("Error:", ve)
        return obtener_calificaciones()

def main():
    calificaciones = obtener_calificaciones()
    print("Las calificaciones ingresadas son:", calificaciones)

if __name__ == "__main__":
    main()