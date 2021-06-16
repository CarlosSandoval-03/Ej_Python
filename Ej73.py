# Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera est´a incluida en la segunda. Se dice que una cadena est´a incluida en otra
# si todos los caracteres (con repeticiones) de la cadena est´a en la segunda cadena sin tener en cuenta el orden de los caracteres. 
from metodosTemp import limpiarConsola


def crear_diccionario(cadena:str) -> dict:
    diccionario = {}
    for i in range(len(cadena)):
        diccionario[cadena[i]] = diccionario.get(cadena[i], 0) + 1
    return diccionario   


def evaluar_incluye_sin_orden(subcadena:str, cadena:str) -> bool:
    dict_sub = crear_diccionario(subcadena)
    dict_cadena = crear_diccionario(cadena)
    
    ''' Cada llave corresponde a una letra, estas tienen indexadas un valor numerico que representa las veces que se repite esta letra.
    Se realizara una resta entre valores, si algun valor del diccionario es mayor a 0 indica que la palabra no se contiene en su totalidad '''
    
    for clave, valor in dict_cadena.items():
        for clave1, valor1 in dict_sub.items():
            if clave == clave1:
                dict_sub[clave1] = valor1 - valor

    for clave, valor in dict_sub.items():
        if valor > 0:
            return False
    return True


def main():
    limpiarConsola()
    sub = str(input('Ingrese la subcadena a evaluar: '))
    cadena = str(input('Ingrese la cadena a evaluar: '))

    if evaluar_incluye_sin_orden(sub,cadena):
        print('La subcadena si esta incluida en la cadena')
    else:
        print('No se incluye')


if __name__ == '__main__':
    main()
