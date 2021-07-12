from metodosTemp import limpiarConsola
from metodosTemp import matriz_cuadrada
from metodosTemp import leer_matriz_enteros
from Ej30 import nuevoMeterNumeros

def solucionEcuacionMatriz(matriz:list, arregloNumeros:list) -> list:
    if not matriz_cuadrada(len(matriz), len(matriz[0])):
        return None

    count = 0
    for columna in matriz:
        for elemento in columna:
            count += 1

    if count != len(arregloNumeros):
        return None

    matrizFinal = []
    pos = 0
    for c in matriz:
        temp = []
        for e in c:
            x = arregloNumeros[pos] / e
            temp.append(x)
            pos += 1
        matrizFinal.append(temp)

    return matrizFinal

def main():
    n = int(input('Ingrese el tamaño de la matriz: '))
    matriz = leer_matriz_enteros(n,n)
    lista = nuevoMeterNumeros()
    print(f'La matriz solucion es: {solucionEcuacionMatriz(matriz, lista)}')


if __name__ == '__main__':
    main()
