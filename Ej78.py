#78. Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de caracteres. 
# El corrimiento circular a derecha de una cadena es poner el ultimo caracter de la cadena como primer caracter de la misma.
from metodosTemp import limpiarConsola
from Ej74 import inverso_cadena
from Ej77 import corrimiento_circular_izq


def corrimiento_circular_der(cadena:str) -> str:
    temp = corrimiento_circular_izq(inverso_cadena(cadena))
    return inverso_cadena(temp)


def main():
    limpiarConsola()
    string = str(input('Ingrese la cadena: '))
    print(f'Salida: {corrimiento_circular_der(string)}')


if __name__ == '__main__':
    main()
