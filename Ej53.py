# 53. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros
from Ej23 import sumaArreglo


def suma_fila(matriz: list, eleccion: int) -> float:
    eleccion = eleccion - 1
    for i in range(len(matriz)):
        if i == eleccion:
            return sumaArreglo(matriz[i])


def main():
    limpiarConsola()
    # Matriz 1
    n1 = int(input('Ingrese el valor de filas en la matriz 1: '))
    m1 = int(input('Ingrese el valor de columnas en la matriz 1: '))
    a = leer_matriz_enteros(n1, m1)
    b = int(input(f'Seleccione la fila a sumar (De 1 a {m1}): '))
    if b > m1:
        limpiarConsola()
        print('Fila invalida, se tomara el maximo valor permitido')
        b = m1
    elif b < 0:
        limpiarConsola()
        print('Fila invalida, se tomara el minimo valor permitido')
        b = 1
    total = suma_fila(a, b)
    print(f'La suma de la fila {b} es: {total}')


if __name__ == '__main__':
    main()
