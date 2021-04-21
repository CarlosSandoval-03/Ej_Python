#!/usr/bin/env python
# -*- coding: utf-8 -*-
#7. Determinar si un numero es primo.
def ejSiete(numero, i=2):
    if i >= numero and numero > 0:
        return "Es primo"
    elif numero%i != 0:
        return ejSiete(numero, i + 1)
    elif numero < 0:
        return "El valor indicado no puede ser evaluado"
    else:
        return "No es primo", i, "es divisor"
    
def main():
    a = int(input("Elija el numero: "))
    print(ejSiete(a))
    
if __name__ == "__main__":
    main()
