# 79. Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de correspondencias de caracteres dada.
# La cadena de correspondencias tiene como el primer caracter el caracter equivalente para el caracter ‘a’, el segundo caracter para la ‘b’y asi sucesivamente hasta la ‘z’. 
# No se tiene traduccion para las mayusculas ni para la ‘ñ’.
from metodosTemp import limpiarConsola


def codificar_cadena(cadena:str, codificarlo:str) -> str:
    #cadena = cadena.lower()
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    diccionario = {}

    if len(codificarlo) < len(alfabeto):
        codificarlo = 'qwertyuiopasdfghjklzxcvbnm' 

    for i in range(len(alfabeto)):
        diccionario[alfabeto[i]] = codificarlo[i]

    temp = ''
    for k in range(len(cadena)):
        if cadena[k] != ' ':
            if cadena[k] == cadena[k].lower():
                for x,y in diccionario.items():
                    if cadena[k] == x:
                        temp += y
            else:
                temp += cadena[k]
        else:
            temp += ' '
    return temp



def main():
    limpiarConsola()
    string = str(input('Ingrese la cadena: '))
    dic = str(input('Ingrese el diccionario para codificar: '))

    print(codificar_cadena(string,dic))


if __name__ == '__main__':
    main()
