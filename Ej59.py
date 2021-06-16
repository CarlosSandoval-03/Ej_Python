# 59. Desarrollar un programa que tome un arreglo de tama˜no n2 y llene en espiral hacia adentro una matriz cuadrada de tama˜no n.
from metodosTemp import leer_matriz_enteros
from metodosTemp import limpiarConsola
from Ej30 import nuevoMeterNumeros
import math

def matriz_espiral(arreglo:list) -> list:
    n = round(math.sqrt(len(arreglo)))
    matriz_final = [[] for i in range(n)]
    
    pos = 0
    k = 0
    while (pos < len(arreglo) and (k < n)):
        for j in range(n):
            matriz_final[k].append(arreglo[pos])
            pos += 1
        k += 1
    return matriz_final


def main():
    limpiarConsola()

    # Arreglo
    array = nuevoMeterNumeros()
    print(f'La matriz resultante es: {matriz_espiral(array)}')


if __name__ == '__main__':
    main()
