#!/usr/bin/env python
# -*- coding: utf-8 -*-
#13. Dado un natural, determinar si es un número de Fibonacci o no.
def raizCuadrada(var):
    x = 1.0
    for k in range(1, 10):
        x = (x + var/x)/2
    return x

def cuadradoPerfecto(x): 
    y = int(raizCuadrada(x)) 
    return y*y == x 

def siNumero(num):  
    return cuadradoPerfecto(5*num*num + 4) or cuadradoPerfecto(5*num*num - 4)

def ejTrece(numero):
    if numero >= 0:
        if siNumero(numero) == True: 
            print(numero,"es un numero Fibonacci")
        else: 
            print(numero,"NO es un numero Fibonacci")
    else:
        print("El numero debe ser natural")

def main():
    numero = int(input("Ingrese el valor a comprobar: "))
    ejTrece(numero)

if __name__ == "__main__":
    main()