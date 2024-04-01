
import gen_num

def main():
    numeros = gen_num.generar_numeros()
    gen_num.mostrar_lista(numeros)
    gen_num.ordenar_lista(numeros)

if __name__ == "__main__":
    main()
