# Desarrollar un algoritmo que determine si una matriz es m´agica. Se dice que una matriz cuadrada es magica si la suma de cada una de sus filas, de cada una de sus columnas y de
# cada diagonal es igual.
from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros
from metodosTemp import inversoArreglo
from metodosTemp import comprobacion_matrices_igual_orden
from Ej53 import suma_fila
from Ej52 import suma_columna
from Ej23 import sumaArreglo


def suma_magica_filas(matriz: list, n1: int) -> float:
    arreglo = []
    for i in range(n1):
        arreglo.append(suma_fila(matriz, i+1))
    return arreglo


def suma_magica_columna(matriz: list, m1: int) -> float:
    arreglo = []
    for i in range(m1):
        arreglo.append(suma_columna(matriz, i+1))
    return arreglo


def suma_diagonal(matriz: list):
    nueva_matriz = []
    n = len(matriz)
    i = 0
    while i < n:
        nueva_matriz.append(matriz[i][i])
        i += 1
    return sumaArreglo(nueva_matriz)


def suma_diagonal_contraria(matriz: list):
    nueva_matriz = []
    for i in range(len(matriz)):
        nueva_matriz.append(inversoArreglo(matriz[i]))
    return suma_diagonal(nueva_matriz)


def esMagica(matriz: list, n1: int, m1: int) -> bool:
    if n1 == m1:
        arreglo = []
        arreglo.append(suma_diagonal(matriz))
        arreglo.append(suma_diagonal_contraria(matriz))

        temp = suma_magica_columna(matriz, m1)
        for i in range(len(temp)):
            arreglo.append(temp[i])

        temp = suma_magica_filas(matriz, n1)
        for k in range(len(temp)):
            arreglo.append(temp[k])

        x = arreglo[0]
        for j in range(len(arreglo)):
            if x == arreglo[j]:
                pass
            else:
                return False
        return True
    else:
        return False


def main():
    limpiarConsola()
    # Matriz 1
    print('!---------------------------------------------------- Comprobar si es una matriz magica ----------------------------------------------------!')
    n1 = int(input('Ingrese el valor de filas en la matriz 1: '))
    m1 = int(input('Ingrese el valor de columnas en la matriz 1: '))
    a = leer_matriz_enteros(n1, m1)
    if esMagica(a, n1, m1):
        limpiarConsola()
        print('!---------------------------------------------------- Comprobar si es una matriz magica ----------------------------------------------------!')
        print('Es una matriz magica')
    else:
        limpiarConsola()
        print('!---------------------------------------------------- Comprobar si es una matriz magica ----------------------------------------------------!')
        print('No lo es')


if __name__ == '__main__':
    main()
