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

def simetria_binaria(relacion:list) -> bool: 
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

def orden_binaria(matriz:list, relacion:list) -> bool:
    if not simetria_binaria(relacion) and reflexibilidad_binaria(matriz, relacion) and transitividad_binaria(matriz,relacion):
        return True
    return False

# Equivalencia

def equivalencia_binaria(matriz:list, relacion:list) -> bool:
    if reflexibilidad_binaria(matriz, relacion) and simetria_binaria(relacion) and transitividad_binaria(matriz, relacion):
        return True
    return False

# Funcion

def funcion_binaria(relacion:list) -> bool:
    valores_x = []

    for i in range(len(relacion)):
        x,y = relacion[i]
        if not inSimple(x, valores_x):
            valores_x.append(x)
        else:
            return False
    return True


# Inyectividad

def inyectividad_binaria(relacion:list) -> bool:
    if not funcion_binaria(relacion):
        return None
    
    valores_y = []

    for i in range(len(relacion)):
        x,y = relacion[i]
        if not inSimple(y, valores_y):
            valores_y.append(y)
        else:
            return False
    return True

# Sobreyectividad

def sobreyectividad_binaria(relacion:list) -> bool:
    if not funcion_binaria(relacion):
        return None

    if not inyectividad_binaria(relacion):
        return True
    return False

# Menu ________________________________________________

def eleccion() -> int:
    e = int(input('Por favor seleccione la operacion a elegir:\n1.Union\n2.Interseccion\n3.Simetria\n4.Reflexibilidad\n5.Transitividad\n6.Orden\n7.Equivalencia\n8.Funcion\n9.Inyectividad\n10.Sobreyectividad\n11.Salir\nEleccion: '))
    return e


def crear_relacion() -> list:
    temp = leer_matriz_enteros(int(input('Ingrese la cantidad de relaciones que desea: ')), 2)
    return temp


def matriz_binaria(relacion:list) -> list:
    array1 = nuevoMeterNumeros()
    array2 = nuevoMeterNumeros()
    return crear_matriz_binaria(array1, array2, relacion)
   

def recoleccion_datos() -> tuple:
    e = eleccion()
    if inSimple(e, [1,2]): # Solicita 2 matrices binaria
        print('Matriz 1')
        relacion1 = crear_relacion()
        matriz1 = matriz_binaria(relacion1)
        
        print('Matriz 2')
        x = str(input('Desea mantener la relacion [y/n]: '))
        if x.lower != 'y':
            relacion2 = crear_relacion()
        else:
            relacion2 = relacion1.copy()
        matriz2 = matriz_binaria(relacion2)
        return (e, matriz1, matriz2)
    elif inSimple(e, [3, 8, 9, 10]): # Solicita solo 1 relacion
        relacion = crear_relacion()
        return (e, relacion)
    elif inSimple(e, [4, 5, 6, 7]): # Solicita 1 matriz y 1 relacion
        print('Matriz 1')
        relacion = crear_relacion()
        matriz1 = matriz_binaria(relacion)
        return (e, matriz1, relacion)
    else:
        return (e, None)


def main(mensaje_memoria = '') -> str:
    limpiarConsola()
    
    if mensaje_memoria != '':
        print(mensaje_memoria,'\n\n')
    
    data = recoleccion_datos()
    eleccion = data[0]
    mensaje = None

    if eleccion == 1:
        mensaje = f'El resultado de la operacion "union" es: {union_binaria(data[1], data[2])}'
        main(mensaje)
    elif eleccion == 2:
        mensaje = f'El resultado de la operacion "interseccion" es: {interseccion_binaria(data[1], data[2])}'
        main(mensaje)
    elif eleccion == 3:
        mensaje = f'El resultado de la operacion "simetria" es: {"Verdadero" if simetria_binaria(data[1]) else "Falso"}'
        main(mensaje)
    elif eleccion == 4:
        mensaje = f'El resultado de la operacion "reflexibilidad" es: {"Verdadero" if reflexibilidad_binaria(data[1], data[2]) else "Falso"}'
        main(mensaje)
    elif eleccion == 5:
        mensaje = f'El resultado de la operacion "transitividad" es: {"Verdadero" if transitividad_binaria(data[1], data[2]) else "Falso"}'
        main(mensaje)
    elif eleccion == 6:
        mensaje = f'El resultado de la operacion "orden" es: {"Verdadero" if orden_binaria(data[1], data[2]) else "Falso"}'
        main(mensaje)
    elif eleccion == 7:
        mensaje = f'El resultado de la operacion "equivalencia" es: {"Verdadero" if equivalencia_binaria(data[1], data[2]) else "Falso"}'
        main(mensaje)
    elif eleccion == 8:
        mensaje = f'El resultado de la operacion "funcion" es: {"Es una funcion" if funcion_binaria(data[1]) else "No es una funcion"}'
        main(mensaje)
    elif eleccion == 9:
        mensaje = f'El resultado de la operacion "inyectividad" es: {"Es inyectiva" if inyectividad_binaria(data[1]) else "No es inyectiva"}'
        main(mensaje)
    elif eleccion == 10:
        mensaje = f'El resultado de la operacion "sobreyectividad" es: {"Es sobreyectiva" if sobreyectividad_binaria(data[1]) else "No es sobreyectiva"}'
        main(mensaje)
    elif eleccion == 11:
        print('Hasta la proxima!')


if __name__ == '__main__':
    main()
