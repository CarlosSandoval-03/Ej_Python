import os


def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def metodoIndex(element, seeker) -> int:
    count = 0
    for parts in element:
        if parts == seeker:
            return count
        else:
            count += 1
    return -1


def metodoSplit(string: str, separador=" ") -> list:
    listOfTerms = []
    temp = ""
    for element in string:
        if element != separador:
            temp += element
        else:
            listOfTerms.append(temp)
            temp = ""
    if len(temp) > 0:
        listOfTerms.append(temp)
    return listOfTerms


def maximoArreglo(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    return x


def minimoArreglo(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i <= x:
            x = i
    return x


def inversoArreglo(arreglo: list) -> list:
    temp = []
    n = len(arreglo)
    for i in range(n-1, -1, -1):
        temp.append(arreglo[i])
    return temp


def inSimple(seeker, arreglo):
    boolean = False
    for elemento in arreglo:
        if elemento == seeker:
            boolean = True
    return boolean


def meter_matrices() -> list:
    arreglo = []
    flag = True
    print('---- Finalice secuencia con "#" - Remueva el ultima columna con "!" ----')
    while flag:
        a = input('Ingrese numeros a insertar en la columna: ')
        if a != '#':
            if a != '!':
                try:
                    a = list(map(float, a.split()))
                    arreglo.append(a)
                except:
                    print('Valor invalido, por favor ingrese valores reales')
            else:
                print('Ultima columna removido')
                arreglo.pop()
        else:
            flag = False
    return arreglo


def leer_matriz_enteros(n, m):
    A = []
    for i in range(n):
        A.append([])
        print('A leer fila', i)
        for j in range(m):
            A[i].append(float(input('A[' + str(i) + ',' + str(j) + '] = ')))
    return A


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


def matriz_cuadrada(n1:int, m1:int) -> bool:
    if n1 == m1:
        return True
    else:
        return False
