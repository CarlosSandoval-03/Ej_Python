import Ej23
print("24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).")


def promedioArreglo(arreglo):
    n = len(arreglo)
    total = Ej23.sumaArreglo(arreglo)
    total /= n
    return total


def main():
    x = []
    Ej23.meterNumeros(x)
    print("El promedio del arreglo es:", promedioArreglo(x))


if __name__ == "__main__":
    main()
