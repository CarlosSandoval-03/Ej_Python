from Ej23 import meterNumeros
#24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).
def suma(arreglo):
    n = len(arreglo)
    if n == 1:
        print(arreglo)
    else:
        suma = 0
        for i in arreglo:
            suma = suma + i
    return suma

def ejVeinteCuatro(arreglo):
    n = len(arreglo)
    total = suma(arreglo)
    total /= n
    print("El promedio del arreglo es:",total)
    
def main():
    x = []
    meterNumeros(x)
    ejVeinteCuatro(x)
    
if __name__ == "__main__":
    main()