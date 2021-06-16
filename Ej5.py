print("5. Función potencia de un entero elevado a un entero.")


def ejCinco(a, b):
    resultado = int(a) ** int(b)
    return(resultado)


def main():
    primerValor = int(input("Ingrese el valor de A:"))
    segundoValor = int(input("Ingrese el valor de B:"))
    print("El resultado es:", ejCinco(primerValor, segundoValor))


if __name__ == "__main__":
    main()
