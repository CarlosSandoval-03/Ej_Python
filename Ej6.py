def ejSeis(a, b):
    if a % b != 0:
        return False
    else:
        return True


def mensajes(valor=None):
    if valor:
        print("Es divisible")
    else:
        print("No es divisible")


def main():
    print("6. Una función que determine si un número es divisible por otro.")
    primerValor = float(input("Ingrese el valor de A: "))
    segundoValor = float(input("Ingrese el valor de B: "))
    mensajes(ejSeis(primerValor, segundoValor))


if __name__ == "__main__":
    main()
