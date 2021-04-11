#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Ej23 import meterNumeros
# 27. Desarrollar un algoritmo que calcule el máximo de un arreglo de números enteros (reales).
def ejVeinteSiete(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    print("El valor máximo es:",x)

def main():
    x = []
    meterNumeros(x)
    ejVeinteSiete(x)
    
if __name__ == "__main__":
    main()