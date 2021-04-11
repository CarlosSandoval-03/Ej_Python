#!/usr/bin/env python
# -*- coding: utf-8 -*-
#14. Dadas la pendiente y el punto de corte de dos rectas, determinar si son paralelas, perpendiculares o ninguna de las anteriores.
def ejCatorce(m1,m2,puntoCorte):
    operacion = m1 * m2
    if m1 == m2 and puntoCorte == []:
        print("Rectas paralelas")
    elif operacion == -1 and puntoCorte != []:
        print("Rectas perpendiculares") 
    else:
        print("Las rectas no se reconoce como alguna de las anteriores")

def main():
    pendienteUno = int(input("Ingrese el valor de la pendiente A a evaluar: "))
    pendienteDos = int(input("Ingrese el valor de la pendiente B a evaluar: "))
    corte = list(input("Ingrese el punto de corte de las rectas (Si no hay punto de corte deje el espacio vacio): "))
    ejCatorce(pendienteUno,pendienteDos,corte)

if __name__ == "__main__":
    main()
    