#!/usr/bin/env python
# -*- coding: utf-8 -*-
#7. Determinar si un numero es primo.
def ejSiete(numero, i=2):
    if i >= numero:
        print("Es primo")
        return True
    elif numero%i != 0:
        return ejSiete(numero, i + 1)
    else:
        print("No es primo", i, "es divisor")
        return False
    
def main():
    a = int(input("Elija el numero: "))
    ejSiete(a)
    
if __name__ == "__main__":
    main()