# 51. Desarrollar un algoritmo que permita multiplicar dos matrices de numeros reales (enteros).
from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros
from Ej23 import sumaArreglo


def comprobacion_matrices_multiplicables(n1: int, m1: int, n2: int, m2: int) -> bool:
    if m1 == n2:
        return True
    elif m2 == n1:
        return None
    else:
        return False


def columna_matriz(matriz: list, posicion=0) -> list:
    columna = []
    for fila in range(len(matriz)):
        columna.append(matriz[fila][posicion])
    return columna


def multiplicacion_matrices(mat1: list, mat2: list, m2: int) -> list:
    matriz_total = []
    A = mat1.copy()
    B = mat2.copy()

    for i in range(len(A)):
        operacionFila = []
        flag1 = 0
        while(flag1 < m2):
            temp = []
            col = columna_matriz(B, flag1)
            for k in range(len(A[i])):
                temp.append(A[i][k] * col[k])
            operacionFila.append(sumaArreglo(temp))
            flag1 += 1
        matriz_total.append(operacionFila)
    return matriz_total


def impresion_matriz(matriz: list) -> None:
    for fila in matriz:
        print(fila)


def main():
    limpiarConsola()
    # Matriz 1
    n1 = int(input('Ingrese el valor de filas en la matriz 1: '))
    m1 = int(input('Ingrese el valor de columnas en la matriz 1: '))

    # Matriz 2
    n2 = int(input('\nIngrese el valor de filas en la matriz 2: '))
    m2 = int(input('Ingrese el valor de columnas en la matriz 2: '))

    flag = comprobacion_matrices_multiplicables(n1, m1, n2, m2)
    if flag:
        a = leer_matriz_enteros(n1, m1)
        limpiarConsola()
        b = leer_matriz_enteros(n2, m2)
        multi = multiplicacion_matrices(a, b, m2)
        print('El valor de la multiplicacion entre matrices es:\n')
        impresion_matriz(multi)
    elif flag == None:
        temp = str(input(
            'La multiplicacion no es valida, se puede realizar si las matrices son cambiadas de posicion\nDesea hacerlo? [y/n]: '))
        if temp == 'y' or temp == 'Y':
            a = leer_matriz_enteros(n2, m2)
            limpiarConsola()
            b = leer_matriz_enteros(n1, m1)
            multi = multiplicacion_matrices(a, b, m1)
            print('El valor de la multiplicacion entre matrices (INVERTIDAS) es:\n')
            impresion_matriz(multi)
        else:
            print('Fin del programa \U0001F44B')
    else:
        limpiarConsola()
        print('La matrices no cumplen con los parametros necesarios')
        print('Fin del programa \U0001F44B')


if __name__ == '__main__':
    main()
