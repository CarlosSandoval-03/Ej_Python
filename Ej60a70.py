from metodosTemp import limpiarConsola
from metodosTemp import leer_matriz_enteros
from Ej30 import nuevoMeterNumeros
from Ej35a42 import verificionNoRepeticion
from metodosTemp import inversoArreglo
from metodosTemp import inSimple


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

# Union

def union_binaria(matriz1:list, matriz2:list) -> list:
    temp = [[0 for x in range(len(matriz1[0]))] for y in range(len(matriz1))]

    for fila in range(len(temp)):
        for columna in range(len(temp[0])):
            if matriz1[fila][columna] == 1 or matriz2[fila][columna] == 1:
                temp[fila][columna] = 1
    return temp

# Interseccion

def interseccion_binaria(matriz1:list, matriz2:list) -> list:
    temp = [[0 for x in range(len(matriz1[0]))] for y in range(len(matriz1))]

    for fila in range(len(temp)):
        for columna in range(len(temp[0])):
            if matriz1[fila][columna] == 1 and matriz2[fila][columna] == 1:
                temp[fila][columna] = 1
    return temp 

# Conversion a conjunto

def conversion_conjunto(matriz:list) -> list:
    lista = []
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            lista.append(matriz[i][k])
    return verificionNoRepeticion(lista)

# Simetria

def simetria_binaria(matriz:list, relacion:list) -> bool:
    lista = conversion_conjunto(matriz)
    
    for i in range(len(relacion)):
        temp = inversoArreglo(relacion[i])
        if not inSimple(temp,relacion):
            return False
    return True

# Reflexibilidad

def reflexibilidad_binaria(matriz:list, relacion:list) -> bool:
    diccionario = {}
    lista = conversion_conjunto(matriz) 

    for j in range(len(lista)):
        diccionario[(lista[j],lista[j])] = 0
    
    for fila in range(len(relacion)):
        for key in diccionario.keys():
            if tuple(relacion[fila]) == key:
                diccionario[key] = diccionario.get(key, 0) + 1

    for value in diccionario.values():
        if value == 0:
            return False
    return True

# Transitividad

def transitividad_binaria(matriz:list, relacion:list) -> bool:
    lista = conversion_conjunto(matriz)
    
    array = []
    temp = []
    pos = 0
    for i in range(len(relacion)):
        x,y = relacion[i]
        if pos%2 == 0:
            temp.append(x)
        else:
            temp.append(y)
        if len(temp) == 2:
            array.append(temp)
            temp = []
        pos += 1
    
    for i in range(len(array)):
        if not inSimple(array[i], relacion):
            return False
    return True

# Orden

def orden_binaria(relacion:list) -> bool:
    pass

# Equivalencia

def equivalencia_binaria(relacion:list) -> bool:
    pass

# Funcion

def funcion_binaria(relacion:list) -> bool:
    pass

# Inyectividad

def inyectividad_binaria(relacion:list) -> bool:
    pass

# Sobreyectividad

def sobreyectividad_binaria(relacion:list) -> bool:
    pass


def eleccion() -> int:
    e = int(input('Por favor seleccione la operacion a elegir:\n1.Union\n2.Interseccion\n3.Simetria\n4.Reflexibilidad\n5.Transitividad\n6.Orden\n7.Equivalencia\n8.Funcion\n9.Inyectividad\n10.Sobreyectividad\n11.Salir\nEleccion: '))
    return e


def menu(matriz1:list, matriz2:list, relacionA:list, relacionB:list) -> str:
    flag = True
    while flag:
        x = eleccion()
        if x == 1:
            temp = union_binaria(matriz1, matriz2)
            operacion = 'union binaria'
        elif x == 2:
            temp = interseccion_binaria(matriz1, matriz2)
            operacion = 'interseccion binaria'
        elif x >= 11: 
            flag = False
        return f'El resultado de la operacion {operacion} es: {temp}'


def main():
    limpiarConsola()
    print(transitividad_binaria([[0,1,2]], [[1,2],[2,1],[1,1],[2,2]]))
    print(transitividad_binaria([[0,1,2]], [[0,1],[1,2],[0,0],[2,1]]))
    '''
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

    print(menu(matriz1, matriz2)) '''


if __name__ == '__main__':
    main()
