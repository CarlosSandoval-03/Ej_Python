#!/usr/bin/env python
# -*- coding: utf-8 -*-
#17. Dado el radio de un cı́rculo, calcular el área y perı́metro del cuadrado, pentágono y hexágono adentro (inscrito en un cı́rculo) y afuera (inscribiendo al cı́rculo).
def raizCuadrada(var):
    x = 1.0
    for k in range(1, 10):
        x = (x + var/x)/2
    return x

def eleccion():
    print("1. Area y Perimetro del Cuadrado (Exteriror)\n2. Area y Perimetro del Cuadrado (Interiror)")
    print("3. Area y Perimetro del Pentagono (Exteriror)\n4. Area y Perimetro del Pentagono (Interiror)")
    print("5. Area y Perimetro del Hexagono (Exteriror)\n6. Area y Perimetro del Hexagono (Interiror)\n")
    elec = int(input("Ingrese problema solicitado: "))
    return elec

def ejDiezSiete(r):
    e = eleccion()
    enunciado = None
    if e == 1:
        area = (2*r) * (2*r)
        perimetro = 8 * r
        problema = "Cuadrado (Exterior)"
        enunciado = True
    elif e == 2:
        area = 2 * r
        perimetro =  4 * raizCuadrada(2*r)
        problema = "Cuadrado (Interno)"
        enunciado = True
    elif e == 3:
        area = ((10 * r * 0.5878/0.8090) * r) / 2
        perimetro = (10 * r * 0.5878) / 0.8090
        problema = "Pentagono (Exterior)"
        enunciado = True
    elif e == 4:
        area = (((5 * r * 0.9510) / 0.8090) * (r * 0.8090)) / 2
        perimetro = (5 * r * 0.9510) / 0.890
        problema = "Pentagono (Interior)"
        enunciado = True
    elif e == 5:
        area = (((6 * r) / 0.866) * (r * 0.866)) / 2
        perimetro = (6 * r) / 0.866
        problema = "Hexagono (Exterior)"
        enunciado = True
    elif e == 6:
        area = ((6 * r) * (r * 0.866)) / 2
        perimetro = 6 * r
        problema = "Hexagono (Interior)"
        enunciado = True
    else:
        enunciado = False
    if enunciado:
        print("\nEl area es:","{:.2f}".format(area),"y el perimetro es:","{:.2f}".format(perimetro),"del",problema)
    else:
        print("\nProblema seleccionado fuera de rango.")
        
def main():
    radio = float(input("Ingrese el radio: "))
    ejDiezSiete(radio)

if __name__ == "__main__":
    main()