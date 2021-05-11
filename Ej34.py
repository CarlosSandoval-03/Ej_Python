from typing import Deque
from Ej22 import criba
from Ej27 import maximoArreglo
# Hacer un algoritmo que calcule el M´ınimo Com´un M´ultiplo (MCM) para un arreglo de enteros positivos.
# Ejemplo.
# Arreglo: (12,20,30,15)


def cuentaArreglo(arreglo, buscar):
    veces = 0
    for elemento in arreglo:
        if elemento == buscar:
            veces += 1
    return veces


def indiceArreglo(arreglo, buscar):
    i = -1
    for elemento in arreglo:
        if elemento != buscar:
            i += 1
        else:
            i += 1
            break
    return i


def arregloEntero(arreglo):
    lista = []
    for elemento in arreglo:
        try:
            elemento1 = int(elemento)
            lista.append(elemento1)
        except:
            elemento1 = round(elemento)
            lista.append(elemento1)
    return lista


def simplificarEnPrimos(arreglo) -> list:
    valores = {}
    primos = criba(maximoArreglo(arregloEntero(arreglo)))
    i = 0
    for numero in arreglo:
        listaDivisores = []
        for divisores in primos:
            while numero % divisores == 0:
                listaDivisores.append(divisores)
                numero /= divisores
        valores[i] = (listaDivisores)
        i += 1
    return valores


def mcm(arreglo):
    diccionario = simplificarEnPrimos(arreglo)
    i = 0
    x = diccionario[i]
    y = diccionario[i+1]
    return x, y, diccionario


def main():
    print(mcm([10, 20, 30]))


if __name__ == "__main__":
    main()
