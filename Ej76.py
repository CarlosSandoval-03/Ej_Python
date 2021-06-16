# 76. Desarrollar un algoritmo que determina si una cadena de caracteres es frase pal´ındrome. Una cadena se dice frase pal´ındrome si la cadena 
# al eliminarle los espacios es pal´ındrome.
from metodosTemp import limpiarConsola
from Ej75 import palindrome


def eliminar_espacios_cadena(cadena:str) -> str:
    cadena = cadena.split()
    temp = ''
    for i in range(len(cadena)):
        temp += cadena[i]
    return temp


def palindrome_frase(cadena:str) -> bool:
    if palindrome(eliminar_espacios_cadena(cadena)):
        return True
    else:
        return False


def main():
    limpiarConsola()
    string = str(input('Ingrese la cadena a evaluar como palindrome de frase: '))
    if palindrome_frase(string):
        print('Es palindrome')
    else:
        print('No es palindrome')


if __name__ == '__main__':
    main()
