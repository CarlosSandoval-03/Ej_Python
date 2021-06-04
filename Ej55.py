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
    a = [[8,1,6],[3,5,7],[4,9,2]]
    x = 5
    print(reemplazar_matriz(a,x))

if __name__ == '__main__':
    main()
