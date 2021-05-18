from Ej30 import nuevoMeterNumeros
from Ej8 import mcdDosValores
print("34. Hacer un algoritmo que calcule el M´ınimo Com´un M´ultiplo (MCM) para un arreglo de enteros positivos.")
# Ejemplo.
# Arreglo: (12,20,30,15)
# MCD del arreglo: 60


def mcmArreglo(arreglo):
    mcm = arreglo[0]
    for i in range(1, len(arreglo)):
        mcm = mcm * arreglo[i] // mcdDosValores(mcm, arreglo[i])
    return mcm


def main():
    lista = nuevoMeterNumeros()
    print("El minimo comun multiplo de", lista, "es", mcmArreglo(lista))


if __name__ == "__main__":
    main()
