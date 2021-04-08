#23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de números enteros (reales).
def ejVeinteTres(arreglo):
    n = len(arreglo)
    if n == 1:
        print(arreglo)
    else:
        suma = 0
        for i in arreglo:
            suma = suma + i
    print("La suma de los elementos del arreglo es:",suma)

def meterNumeros(arreglo):
    a = input("Ingrese numero a insertar en el arreglo (Finalice secuencia con '#'): ")
    if a != "#":
        a = int(a)
        arreglo.append(a)
        meterNumeros(arreglo)
    else:
        return arreglo

def main():
    x = []
    meterNumeros(x)
    ejVeinteTres(x)
    
if __name__ == "__main__":
    main()