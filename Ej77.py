#77. Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de caracteres. 
# El corrimiento circular a izquierda es pasar el primer caracter de una cadena como ultimo caracter de la misma. 
from metodosTemp import limpiarConsola


def corrimiento_circular_izq(cadena:str) -> str:
    temp = ''
    for i in range(len(cadena)):
        if i == 0:
            continue
        elif i != 0 and i < (len(cadena) - 1):
            temp += cadena[i]
        elif i == (len(cadena) - 1):
            temp += cadena[i]
            temp += cadena[0]
    return temp


def main():
    limpiarConsola()
    string  = str(input('Ingrese la cadena: '))
    print(f'Salida: {corrimiento_circular_izq(string)}')


if __name__ == '__main__':
    main()
