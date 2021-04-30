#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#16. Dado el radio de un cı́rculo, calcular el área del triángulo que circunscribe el circulo (triangulo afuera).
def areaCirculoInscrito(apotema,numeroLadosPoligono):
    #Al triangulo estar circunscrito el radio de la circuferencia es equivalente a la apotema
    teta = 360 / (2 * numeroLadosPoligono)
    x = apotema * math.tan(math.radians(teta))
    lado = 2 * x
    perimetro = lado * numeroLadosPoligono
    area = (perimetro * apotema) / 2
    return area

def perimetroCirculoInscrito(apotema,numeroLadosPoligono):
    #Al triangulo estar circunscrito el radio de la circuferencia es equivalente a la apotema
    teta = 360 / (2 * numeroLadosPoligono)
    x = apotema * math.tan(math.radians(teta))
    lado = 2 * x
    perimetro = lado * numeroLadosPoligono
    return perimetro

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    print("El area del triangulo es:",areaCirculoInscrito(radio,3))
    
if __name__ == "__main__":
    main()