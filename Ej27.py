from Ej23 import meterNumeros


def maximoArreglo(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    return x


def main():
    print("27. Desarrollar un algoritmo que calcule el máximo de un arreglo de números enteros(reales).")
    x = []
    meterNumeros(x)
    print("El valor máximo es:", maximoArreglo(x))


if __name__ == "__main__":
    main()
