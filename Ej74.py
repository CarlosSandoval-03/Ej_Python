# 74. Desarrollar un algoritmo que invierta una cadena de caracteres.
from metodosTemp import limpiarConsola


def inverso_cadena(cadena:str) -> str:
    temp = ''
    for i in range(len(cadena) -1 , -1, -1):
        temp += cadena[i]
    return temp


def main():
    limpiarConsola()
    string = str(input('Ingrese la cadena a invertir: '))
    print(inverso_cadena(string))


if __name__ == '__main__':
    main()
