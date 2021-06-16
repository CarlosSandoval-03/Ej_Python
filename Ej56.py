# 56. Desarrollar un programa que calcule el determinante de una matriz cuadrada.
from metodosTemp import leer_matriz_enteros
from metodosTemp import limpiarConsola


def determinante_matriz(matriz:list, total = 0) -> float:
    indices = list(range(len(matriz)))

    if len(matriz) == 2: # Caso matriz cuadrada retorno sub determinante
        total = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]
        return total

    for i in range(len(indices)): # Sub matriz
        matriz_copia = matriz.copy() # Se copia
        matriz_copia = matriz_copia[1:] # Seelimina la primera fila
        alto = len(matriz_copia) # Calculo rango altura

        for k in range(alto):
            matriz_copia[k] = matriz_copia[k][0:indices[i]] + matriz_copia[k][indices[i] + 1:] # Se elimina columna

        temp = (-1) ** (indices[i] % 2)
        sub_det = determinante_matriz(matriz_copia) # Recursividad
        
        total += temp * matriz[0][indices[i]] * sub_det # Suma de cada retorno funcion recursiva
    return total # Retorno valor determinante


def main():
    limpiarConsola()
    # Creacion de la matriz
    n = int(input('Ingrese el tamaño de la matriz: '))
    matriz = leer_matriz_enteros(n, n)
    
    print(f'La determiante de la matriz: {matriz}\nEs: {determinante_matriz(matriz)}')

if __name__ == '__main__':
    main()
