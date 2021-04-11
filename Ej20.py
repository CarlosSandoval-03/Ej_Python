#!/usr/bin/env python
# -*- coding: utf-8 -*-
#20. Si un amigo, no tan amigo, me presta K pesos a i pesos de interés diario, ¿cuánto le pagaré en una semana si el interés es simple?, ¿y cuánto si el interés es 
#compuesto?.
def eleccion():
    elec = int(input("Elija el tipo de interes:\n1. Simple\n2. Compuesto\nEleccion: "))
    return elec

def ejVeinte(k,i):
    tipo = None
    e = eleccion()
    if e == 1:
        total = (7*(i/100)) * k
        peticion = "Simple"
        tipo = True
    elif e == 2:
        i = i / 100
        total = k * (1 + i)**7
        peticion = "Compuesto"
        tipo = True
    else:
        tipo = False
        
    if tipo:
        print("El total de pagar a la semana con un interes",peticion,"es $","{:.2f}".format(total))
    else:
        print("Peticion solicitada invalida")

def main():
    k = float(input("Ingrese el valor prestado: "))
    i = float(input("Ingrese el interes diario: "))
    ejVeinte(k,i)

if __name__ == "__main__":
    main()