print("13. Dado un natural, determinar si es un número de Fibonacci o no.")


def cuadradoPerfecto(x):
    y = int(x ** 0.5)
    return y*y == x


def siNumero(num):
    return cuadradoPerfecto(5*(num**2) + 4) or cuadradoPerfecto(5*(num**2) - 4)


def ejTrece(numero):
    if numero >= 0:
        if siNumero(numero) == True:
            return [True, numero]
        else:
            return [False, numero]
    else:
        return ["Error"]


def main():
    numero = int(input("Ingrese el valor a comprobar: "))
    valor = ejTrece(numero)
    if valor[0] == True:
        print(valor[1], "es un numero Fibonacci")
    elif valor[0] == "Error":
        print("El numero debe ser natural")
    else:
        print(valor[1], "NO es un numero Fibonacci")


if __name__ == "__main__":
    main()
