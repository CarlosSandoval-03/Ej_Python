#!/usr/bin/env python
# -*- coding: utf-8 -*-
#10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado. Ax^2+bx+c
def ejDiez(a,b,c,x):
    resultado = (a * (x**2)) + (b * x) + c
    print("El valor dado es:",resultado)
    
def main():
    coefA = float(input("Ingrese coeficiente A: "))
    coefB = float(input("Ingrese coeficiente B: "))
    coefC = float(input("Ingrese coeficiente C: "))
    valor = float(input("Ingrese el valor x: "))
    ejDiez(coefA,coefB,coefC,valor)

if __name__ == "__main__":
    main()
