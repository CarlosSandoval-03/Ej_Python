from Ej30 import nuevoMeterNumeros
from Ej8 import mcdDosValores
# Ejemplo.
#Arreglo: (12,20,14,124,72,2458)
# MCD del arreglo: 2


def mcdArreglo(arreglo):
    mcd = mcdDosValores(arreglo[0], arreglo[1])
    for i in range(2, len(arreglo)):
        mcd = mcdDosValores(mcd, arreglo[i])
    return mcd


def main():
    print("33. Hacer un algoritmo que calcule el Maximo Comun Divisor (MCD) para un arreglo de enteros positivos.")
    lista = nuevoMeterNumeros()
    print("El maximo comun divisor de", lista, "es", mcdArreglo(lista))


if __name__ == "__main__":
    main()
