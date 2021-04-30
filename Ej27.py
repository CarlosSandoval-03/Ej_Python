from Ej23 import meterNumeros
# 27. Desarrollar un algoritmo que calcule el máximo de un arreglo de números enteros (reales).
def ejVeinteSiete(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    return x

def main():
    x = []
    meterNumeros(x)
    print("El valor máximo es:",ejVeinteSiete(x))
    
if __name__ == "__main__":
    main()