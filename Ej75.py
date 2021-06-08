#Desarrollar un algoritmo que determine si una cadena de caracteres es pal´ındrome. Una cadena se dice pal´ındrome si al invertirla es igual a ella misma.
from metodosTemp import limpiarConsola
from Ej74 import inverso_cadena


def palindrome(cadena:str) -> bool:
    if cadena == inverso_cadena(cadena):
        return True
    else:
        return False


def main():
    limpiarConsola()
    string = str(input('Ingrese la cadena a evaluar: '))
    if palindrome(string):
        print('Es palindrome')
    else:
        print('La cadena NO es palindrome')


if __name__ == '__main__':
    main()
