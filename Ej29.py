from Ej23 import meterNumeros


def ordenarMenorMayor(arreglo):
    for vuelta in range(1, len(arreglo)):
        for pos in range(len(arreglo) - vuelta):
            if arreglo[pos] > arreglo[pos + 1]:
                x = arreglo[pos]
                arreglo[pos] = arreglo[pos + 1]
                arreglo[pos + 1] = x
    return arreglo


def ejVeinteNueve(arreglo):
    n = len(arreglo)
    ordenarMenorMayor(arreglo)  # Organiza en orden de menor a mayor
    if n % 2 == 0:
        n /= 2
        total = (arreglo[int(n-1)] + arreglo[int(n)]) / 2
        return total
    elif n % 2 != 0:
        n /= 2
        n = round(n)
        return arreglo[n]


def main():
    print("29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La mediana es el número que queda en la mitad del arreglo después de ser ordenado.")
    x = []
    meterNumeros(x)
    print("La mediana del arreglo es:", ejVeinteNueve(x))
    print(ordenarMenorMayor(x))


if __name__ == "__main__":
    main()
