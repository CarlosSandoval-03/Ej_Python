#!/usr/bin/env python
# -*- coding: utf-8 -*-
#32. Hacer un algoritmo que dado un número entero no negativo, cree un arreglo de unos y ceros que representa el número en binario al revés.
#Ejemplo.
#Número: 106
#Arreglo: (0, 1, 0, 1, 0, 1, 1) (representa el número 1101010)
#Ejemplo.
#Número: 389
#Arreglo: (1, 0, 0, 1, 0, 1, 1, 1, 1) (representa el número 111101001)
def decimalBinario(decimal):
    binario = ""
    if decimal == 0:
        binario = "0"
        return binario
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

def convertirLista(cadena):
    arreglo = []
    for elemento in cadena:
        arreglo.append(elemento)
    return arreglo
        
def ejTreintaDos(datos):
    if validar(datos):
        resultado = convertirLista(decimalBinario(datos))
        resultado.reverse()
        print("La lista solicitada es:",resultado)
    else:
        print("Datos ingresados invalidos, por favor que sea un entero positivo")
    
def validar(dato):
    if dato >= 0:
        return True
    else:
        return False

def main():
    a = int(input("Ingrese el valor natural a evaluar: "))
    ejTreintaDos(a)
    
if __name__ == "__main__":
    main()