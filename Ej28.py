from Ej30 import nuevoMeterNumeros
#28. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de igual tamaño. Sean v = (v 1 , v 2 , . . . , v n ) y 
# w = (w 1 , w 2 , . . . , w n ) dos arreglos, el producto directo de v y w (notado v ∗ w) es el vector: (v 1 ∗ w 1 , v 2 ∗ w 2 , . . . , v n ∗ w n ).
def ejVeinteOcho(arreglo1,arreglo2):
    n1 = len(arreglo1)
    n2 = len(arreglo2)
    if n1 == n2:
        productoDirecto = []
        for i in range(n1):
            resultado = arreglo1[i] * arreglo2[i]
            productoDirecto.append(resultado)
        return productoDirecto
    else:
        return "Error: Los arreglos no son del mismo tamaño"
 
def main():
    x = nuevoMeterNumeros()
    y = nuevoMeterNumeros()
    print("El producto directo de los dos arreglos es:",ejVeinteOcho(x,y))
    
if __name__ == "__main__":
    main()