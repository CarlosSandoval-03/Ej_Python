# 52. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros
from Ej23 import sumaArreglo
from Ej51 import columna_matriz


def suma_columna(matriz: list, eleccion: int) -> float:
    return sumaArreglo(columna_matriz(matriz, eleccion-1))


def main():
    limpiarConsola()
    # Matriz 1
    n1 = int(input('Ingrese el valor de filas en la matriz 1: '))
    m1 = int(input('Ingrese el valor de columnas en la matriz 1: '))
    a = leer_matriz_enteros(n1, m1)
    b = int(input(f'Seleccione la columna a sumar (De 1 a {m1}): '))
    if b > m1:
        limpiarConsola()
        print('Columna invalida, se tomara el maximo valor permitido')
        b = m1
    elif b < 0:
        limpiarConsola()
        print('Columna invalida, se tomara el minimo valor permitido')
        b = 1
    total = suma_columna(a, b)
    print(f'La suma de la columna {b} es: {total}')


if __name__ == '__main__':
    main()
