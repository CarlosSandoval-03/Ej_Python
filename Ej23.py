#23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de números enteros (reales).
def meterNumeros(arreglo):
    def operacion(arreglo):
        a = input("Ingrese numero a insertar en el arreglo: ")
        if a != "#":
            if a != "!":
                try:
                    a = int(a)
                    arreglo.append(a)
                    operacion(arreglo)
                except:
                    print("Valor invalido, por favor ingrese valores enteros")
                    operacion(arreglo)
            else:
                print("Ultimo valor removido")
                arreglo.pop()
                operacion(arreglo)
        else:
            return arreglo
    print("---- Finalice secuencia con '#' - Remueva el ultimo numero con '!' ----")
    operacion(arreglo)
    return arreglo

def sumaArreglo(arreglo):
    n = len(arreglo)
    if n <= 1:
        return arreglo
    else:
        suma = 0
        for i in arreglo:
            suma = suma + i
    return suma

def main():
    x = []
    meterNumeros(x)
    print("La suma de los elementos del arreglo es:",sumaArreglo(x))
    
if __name__ == "__main__":
    main()