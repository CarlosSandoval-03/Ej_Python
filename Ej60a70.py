from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros
from Ej30 import nuevoMeterNumeros


def verificar_matriz(producto_cartesiano:list, relacion:list) -> bool:
    for i in range(len(relacion)):
        if producto_cartesiano == relacion[i]:
            return True
    return False


def crear_matriz_binaria(arreglo1:list, arreglo2:list, relacion:list) -> list:
    n,m = len(arreglo1), len(arreglo2)
    matriz = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if verificar_matriz([arreglo1[i], arreglo2[j]], relacion):
                matriz[i][j] = 1
    return matriz


def union_binaria(matriz1:list, matriz2:list) -> list:
    pass




def eleccion() -> int:
    e = int(input('Por favor seleccione la operacion a elegir:\n1.Union\n2.Interseccion\n3.Simetria\n4.Reflexibilidad\n5.Transitividad\n6.Orden\n7.Equivalencia\n8.Funcion\n9.Inyectividad\n10.Sobreyectividad\n11.Salir\nEleccion: '))
    return e


def menu(matriz:list) -> str:
    flag = True
    while flag:
        pass


def main():
    limpiarConsola()

    print('Matriz 1')
    print('Ingrese la relacion para crear las matrices booleanas\n')
    relacion = leer_matriz_enteros(int(input('Ingrese la cantidad de relaciones que desea: ')), 2)
    array1 = nuevoMeterNumeros()
    array2 = nuevoMeterNumeros()
    matriz1 = crear_matriz_binaria(array1, array2, relacion)
   
    limpiarConsola()

    print('Matriz 2')
    if str(input('Desea mantener la relacion [y/n]: ')).lower() != 'y':
        print('Ingrese la relacion para crear las matrices booleanas\n')
        relacion = leer_matriz_enteros(int(input('Ingrese la cantidad de relaciones que desea: ')), 2)
    array3 = nuevoMeterNumeros()
    array4 = nuevoMeterNumeros()
    matriz2 = crear_matriz_binaria(array1, array2, relacion)



if __name__ == '__main__':
    main()
