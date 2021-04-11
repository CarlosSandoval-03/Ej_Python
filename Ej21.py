#!/usr/bin/env python
# -*- coding: utf-8 -*-
#21. Un niño se la pasó jugando con fichas de lego, tenia dos tipos de fichas de lego, fichas de cuadros de 1 × 1 (rojas) y fichas de cuadros de 2 × 1 (azules), y 
#le dieron una base de 1 × n cuadritos, ¿de cuántas formas distintas puede ubicar las fichas rojas y azules sobre la base?, ¿y si le dan una ficha amarilla de 1 × 3?.
def legos(n):
    if n <= 1:
        return n
    else:
        return(legos(n-1) + legos(n-2))
        
def legos_2(n):
    if n <= 2:
        return n
    else:
        return(legos_2(n-1) + legos_2(n-2)) + legos_2(n-3)

def eleccion():
    elec = int(input("Eliga el caso 1 o el caso 2 (sin ficha amarilla): "))
    return elec

def ejVeinteUno(num):
    e = eleccion()
    x = None
    if e == 1:
        x = legos(num)
        caso = "1"
        mensaje = True
    elif e == 2:
        x = legos_2(num)
        caso = "2"
        mensaje = True
    else:
        mensaje = False
    if mensaje:
        print("La cantidad de formas en las que se pueden ubicar las fichas en el caso",caso,"es de",x,"formas posibles")
    else:
        print("Caso solicidato invalido")
        
def main():
    n = int(input("Ingrese el valor de la 'n': "))
    ejVeinteUno(n)
    
if __name__ == "__main__":
    main()