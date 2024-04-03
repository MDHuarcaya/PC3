

import random

def num_aleatorios():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista de números aleatorios generados: ")
    print(lista)

def ordenar_lista(lista):
    numeros_ordenados = sorted(lista)
    print("Lista con numeros ordenados: ")
    print(numeros_ordenados)
    

