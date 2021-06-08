#72. Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es subcadena de la segunda. (No se deben usar operaciones de 
# subcadenas propias del lenguaje de programaci´on).
from metodosTemp import limpiarConsola
from metodosTemp import inSimple


def verificar_subcadena(subcadena:str, cadena:str) -> bool:
    arreglo1 = cadena.split()
    arreglo2 = subcadena.split()
    for i in range(len(arreglo2)):
        if inSimple(arreglo2[i],arreglo1):
            return True
    return False

def main():
    limpiarConsola()
    sub = str(input('Ingrese la posible subcadena a evaluar: '))
    cadena = str(input('Ingrese la cadena a evaluar: '))
    
    if verificar_subcadena(sub,cadena):
        print('Si es una subcadena')
    else:
        print('No se encuentra en la cadena')


if __name__ == '__main__':
    main()
