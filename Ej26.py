from Ej23 import meterNumeros
print("26. Desarrollar un algoritmo que calcule el mı́nimo de un arreglo de números enteros (reales).")


def minimoArreglo(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i <= x:
            x = i
    return x


def main():
    x = []
    meterNumeros(x)
    print("El valor minimo es:", minimoArreglo(x))


if __name__ == "__main__":
    main()
