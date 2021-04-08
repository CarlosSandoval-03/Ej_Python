from Ej23 import meterNumeros
#25. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño. Sean v = (v 1 , v 2 , . . . , v n ) y
#w = (w 1 , w 2 , . . . , w n ) dos arreglos, el producto de v y w (notado v ⋅ w) es el número: v 1 ∗ w 1 + v 2 ∗ w 2 + ⋯ + v n ∗ w n .
def ejVeinteCinco(arreglo1,arreglo2):
    n1 = len(arreglo1)
    n2 = len(arreglo2)
    if n1 == n2:
        producto = 0
        for i in range(n1):
            producto = producto + (arreglo1[i] * arreglo2[i])
        print("El producto de los dos arreglos es:",producto)
    else:
        print("Los arreglos no son del mismo tamaño")

def main():
    x = []
    y = []
    meterNumeros(x)
    meterNumeros(y)
    ejVeinteCinco(x,y)
    
if __name__ == "__main__":
    main()