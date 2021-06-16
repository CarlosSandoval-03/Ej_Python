#71. Desarrollar un algoritmo que reciba como entrada un caracter y de como salida el numero de ocurrencias de dicho caracter en una cadena de caracteres.
from metodosTemp import limpiarConsola


def conteo_cadena(caracter:str, cadena = 'Hola Mundo!') -> int:
    count = 0
    for i in range(len(cadena)):
        if caracter == cadena[i]:
            count += 1
    return count


def main():
    limpiarConsola()
    texto = str(input('Digite el texto a evaluar: '))
    caracter = str(input('Ingrese el caracter que desea contar: '))
    if len(caracter) > 1:
        caracter = caracter[0]
    print(f'En el texto:\n\t-{texto}\n\nEl caracter ({caracter}) se encuentra un total de: {conteo_cadena(caracter,texto)} veces')


if __name__ == '__main__':
    main()
