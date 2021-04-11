#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las gallinas ponen 1 huevo cada 3 dı́as y la otra mitad 1 huevo cada 5 dı́as, ¿en un mes cuántos
#huevos producen? (1 mes ≡ 30 dı́as).
def ejDos(aves):
    if aves >= 3:
        gallinas = aves / 3
        if not gallinas <= 2:
            gallinasMitad = int(gallinas) / 2
            grupoUno = int(gallinasMitad) * (30 / 3)
            grupoDos = int(gallinasMitad) * (30 / 5)
            huevos = grupoUno + grupoDos
            print("En 1 mes la granja produce:", int(huevos), "huevos")
        else:
            print("Aves existentes insuficientes")
    else:
        print("Aves existentes insuficientes")
        
def main():
    a = aves = int(input("Numero de Aves: "))
    ejDos(a)
    
if __name__ == "__main__":
    main()