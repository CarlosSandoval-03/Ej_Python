# Desarrollar un algoritmo que dado un entero, reemplace en una matriz todos los numeros mayores a un numero dado por un uno y todos los menores o iguales por un cero.
from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros


def reemplazar_matriz(matriz:list,entero:int) -> list:
    nueva_matriz = []
    for i in range(len(matriz)):
        temp_array = []
        for k in range(len(matriz[i])):
            if matriz[i][k] > entero:
                temp_array.append(1)
            else:
                temp_array.append(0)
        nueva_matriz.append(temp_array)
    return nueva_matriz


def main():
    limpiarConsola()
    # Matriz 1
    n1 = int(input('Ingrese el valor de filas de la matriz: '))
    m1 = int(input('Ingrese el valor de columnas de la matriz: '))
    
    a = leer_matriz_enteros(n1,m1)
    x = int(input('Ingrese el entero a evaluar: '))

    total = reemplazar_matriz(a,x)
    print(f'La matriz resultante del valor {x} es: {total}')

if __name__ == '__main__':
    main()
