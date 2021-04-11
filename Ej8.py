#!/usr/bin/env python
# -*- coding: utf-8 -*-
#8. Dados dos naturales, determinar si son primos relativos.
def mcd(primerValor, segundoValor):
    if primerValor > segundoValor:
        if primerValor%segundoValor == 0:
            return segundoValor
        else:
            return mcd(segundoValor, primerValor%segundoValor)
    else:
        return mcd(segundoValor,primerValor)
        
def ejOcho(a, b):
    if mcd(a,b) == 1:
        print("Son primos relativos")
    else:
        print("No son primos relativos")
        
def main():
    primerValor = int(input("Ingrese el valor de A: "))
    segundoValor = int(input("Ingrese el valor de B: "))
    ejOcho(primerValor,segundoValor)

if __name__ == "__main__":
    main()