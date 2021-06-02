# Desarrollar un algoritmo que permita sumar dos matrices de numeros reales (enteros).
from Ej35a42 import limpiarConsola


def meter_matrices(arreglo: list) -> list:
    def operacion(arreglo):
        a = input('Ingrese numeros a insertar en la columna: ')
        if a != '#':
            if a != '!':
                try:
                    a = list(map(float, a.split()))
                    arreglo.append(a)
                    operacion(arreglo)
                except:
                    print('Valor invalido, por favor ingrese valores reales')
                    operacion(arreglo)
            else:
                print('Ultima columna removido')
                arreglo.pop()
                operacion(arreglo)
        else:
            return arreglo
    print('---- Finalice secuencia con "#" - Remueva el ultima columna con "!" ----')
    operacion(arreglo)
    return arreglo


def comprobacion_matrices_igual_orden(mat1: list, mat2: list) -> bool:
    n, m = len(mat1), len(mat2)
    if n == m:
        temp1 = 0
        temp2 = 0
        for fila in mat1:
            for valor in fila:
                temp1 += 1
        for fila in mat2:
            for valor in fila:
                temp2 += 1
        if temp1 == temp2:
            return True
        else:
            return False
    else:
        return False


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


def main():
    matriz1 = []
    matriz2 = []

    # Matriz 1
    limpiarConsola()
    print('Matriz 1')
    meter_matrices(matriz1)

    # Matriz 2
    limpiarConsola()
    print('Matriz 2')
    meter_matrices(matriz2)

    if (comprobacion_matrices_igual_orden(matriz1, matriz2)):
        temp = suma_matrices(matriz1, matriz2)
        print(f'La suma de la matriz A+B es: {temp}')
    else:
        print('ERROR: La suma de dos matrices solamente se puede realizar entre matrices del mismo orden')


if __name__ == '__main__':
    main()
