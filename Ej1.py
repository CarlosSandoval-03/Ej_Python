#!/usr/bin/env python
# -*- coding: utf-8 -*-
#En una granja se crı́an un número de V - Vacas, A - Aves (pollos y gallinas) y E - escorpiones.
#Las vacas están encerradas en un corral de N × M metros cuadrados, las aves en un galpón y los escorpiones en vitrinas.
#1. Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿cuántos litros de leche se producen en la granja?.
def ejUno(vacas,corralN,corralM):
    if corralM <= 0 or corralN <= 0:
        print("Error: El area debe ser positiva")
    else:
        corralArea = corralN * corralM
        if not vacas <= 0:
            producir = int(input("¿Cuantos litros de leche la vaca produce por metro cuadrado?: "))
            leche = vacas * (producir * corralArea)
            print("En la granja se producen:", leche, "litros de leche")
        else:
            print("No es posible producir leche sin vacas")

def main():
    a = int(input("Numero de vacas: "))
    b = int(input("Ingrese el alto del corral: "))
    c = int(input("Ingrese el ancho del corral: "))
    ejUno(a,b,c)

if __name__ == "__main__":
    main()