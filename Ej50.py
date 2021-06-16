# Desarrollar un algoritmo que permita sumar dos matrices de numeros reales (enteros).
from Ej35a42 import limpiarConsola
from metodosTemp import leer_matriz_enteros


def suma_matrices(mat1: list, mat2: list) -> list:
    matriz_total = []

    matriz1 = []
    for i in mat1:
        count = 0
        for k in i:
            matriz1.append(k)
            count += 1
    matriz2 = []
    for a in mat2:
        for b in a:
            matriz2.append(b)

    for z in range(len(matriz1)):
        matriz_total.append((matriz1[z] + matriz2[z]))
    return organizar(matriz_total, count)


def organizar(matriz: list, num_elementos: int):
    matriz_final = []
    grupos = len(matriz) // num_elementos

    pos = 0
    for i in range(grupos):
        temp = []
        for k in range(num_elementos):
            temp.append(matriz[pos])
            pos += 1
        matriz_final.append(temp)
    return matriz_final


def main(mensaje=''):
    matriz1 = []
    matriz2 = []

    if mensaje != '':
        print(mensaje)

    # Comprobar mismo orden
    try:
        n = int(input('Ingrese el valor de filas en la matriz: '))
        m = int(input('Ingrese el valor de columnas en la matriz: '))
    except:
        n = 1
        m = 1
    try:
        # Matriz 1
        limpiarConsola()
        print('Matriz 1')
        matriz1 = leer_matriz_enteros(n, m)

        # Matriz 2
        limpiarConsola()
        print('Matriz 2')
        matriz2 = leer_matriz_enteros(n, m)

        # Suma
        suma = suma_matrices(matriz1, matriz2)
        print(f'La suma de la matriz A+B es: {suma}')
    except:
        limpiarConsola()
        main('ERROR_PROGRAMA_INTENTE_DE_NUEVO')


if __name__ == '__main__':
    main()
