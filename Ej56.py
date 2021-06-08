# 56. Desarrollar un programa que calcule el determinante de una matriz cuadrada.
from metodosTemp import leer_matriz_enteros
from metodosTemp import limpiarConsola
from metodosTemp import matriz_cuadrada
from Ej23 import sumaArreglo

# Caso tamaño matriz = 2
def determinante_matriz_dos(matriz:list) -> float:
    determinante = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    return determinante

# Caso tamaño matriz = 3
def determinante_matriz_tres(matriz:list) -> float:
    matriz_sarrus = matriz.copy()
    matriz_sarrus.append(matriz[0])
    matriz_sarrus.append(matriz[1])
   
    # Determinante
    det1 = []
    det2 = []
    # Primera parte
    det1.append(matriz_sarrus[0][0] * matriz_sarrus[1][1] * matriz_sarrus[2][2])
    det1.append(matriz_sarrus[1][0] * matriz_sarrus[2][1] * matriz_sarrus[3][2])
    det1.append(matriz_sarrus[2][0] * matriz_sarrus[3][1] * matriz_sarrus[4][2])
    
    # Segunda parte   
    det2.append(matriz_sarrus[0][2] * matriz_sarrus[1][1] * matriz_sarrus[2][0])
    det2.append(matriz_sarrus[1][2] * matriz_sarrus[2][1] * matriz_sarrus[3][0])
    det2.append(matriz_sarrus[2][2] * matriz_sarrus[3][1] * matriz_sarrus[4][0])

    # Suma de arreglos
    determinante = sumaArreglo(det1) - sumaArreglo(det2)
    return determinante


def tamano_matriz(n:int, matriz:list) -> str:
    if n == 1:
        total = matriz[0][0]
    elif n == 2:
        total = determinante_matriz_dos(matriz)
    elif n == 3:
        total = determinante_matriz_tres(matriz)
    elif n >= 4:
        total = determinante_matriz_diferente_orden(matriz,n)
    
    return f'El determinante de la matriz es: {total}'



def main():
    limpiarConsola()
    print(determinante_matriz_diferente_orden([[-2,4,5],[6,7,-3],[3,0,2]]))
    print(determinante_matriz_tres([[-2,4,5],[6,7,-3],[3,0,2]]))
    print()
    print(determinante_matriz_diferente_orden([[2,1,-1,2],[4,5,-3,6],[-2,5,-2,6],[4,11,-4,8]]))
#    print(determinante_matriz_diferente_orden([[3,4,1,2],[-2,0,1,3],[2,0,4,-3],[4,5,1,0]],4))
    # Creacion de la matriz
    n = int(input('Ingrese el tamaño de la matriz: '))
    matriz = leer_matriz_enteros(n,n)
    
    print(determinante_matriz_diferente_orden(matriz,n))

if __name__ == '__main__':
    main()
