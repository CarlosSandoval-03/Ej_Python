#!/usr/bin/env python
# -*- coding: utf-8 -*-
#15. Dadas la pendiente y el punto de corte de dos rectas, determinar los puntos de intersección al origen.
def ejQuince(m1,b1,m2,b2):
    operacion = (b2-b1) / (m1-m2)
    print(operacion)

def main():
    penUno = int(input("Ingrese el valor de la pendiente A a evaluar: "))
    penDos = int(input("Ingrese el valor de la pendiente B a evaluar: "))
    cortUno = int(input("Ingrese el punto de corte (x): "))
    cortDos = int(input("Ingrese el punto de corte (y): "))
    ejQuince(penUno,cortUno,penDos,cortDos)
    
if __name__ == "__main__":
    main()