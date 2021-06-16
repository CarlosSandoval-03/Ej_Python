#Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de correspondencias de caracteres dada.
# La cadena de correspondencias tiene como el primer caracter el caracter equivalente para el caracter ‘a’, el segundo car´acter para la ‘b’y asi sucesivamente
# hasta la ‘z’. No se tiene traducci´on para las may´usculas ni para la ‘ñ’. 
from metodosTemp import limpiarConsola


def decodificar_cadena(cadena:str, codificarlo:str) -> str:
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    diccionario = {}

    if len(codificarlo) < len(alfabeto):
        return 'La cadena para decodificar no posee suficientes caracteres'

    for i in range(len(alfabeto)):
        diccionario[codificarlo[i]] = alfabeto[i]

    temp = ''
    for k in range(len(cadena)):
        if cadena[k] != 'ñ':
            if cadena[k] != ' ':
                if cadena[k] == cadena[k].lower():
                    for x,y in diccionario.items():
                        if cadena[k] == x:
                            temp += y
                else:
                    temp += cadena[k]
            else:
                temp += ' '
        else:
            temp += 'ñ'
    return temp




def main():
    limpiarConsola()
    string = str(input('Ingrese la cadena a decodificar: '))
    clave = str(input('Ingrese la cadena clave: '))
    print(decodificar_cadena(string, clave))


if __name__ == '__main__':
    main()
