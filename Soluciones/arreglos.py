#22. Implementar la criba de Eratostenes para calcular los números primos en el rango 1 a n, donde n es un número natural dado por el usuario.
def ejVeinteDos(n):
    n = int(n)
    if n >= 0:
        numeros = list(range(2, n+1))
        i = 0
        while(numeros[i]*numeros[i] <= n):
            for num in numeros:
                if num <= numeros[i]:
                    continue
                elif num % numeros[i] == 0:
                    numeros.remove(num)
                else:
                    pass
            i += 1
        print(numeros)
    elif n == 1 or n == 0:
        print("No son evaluables")
    else:
        print("El valor ingresado no es natural")
#23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de números enteros (reales).
def suma(arreglo):
    n = len(arreglo)
    if n == 1:
        print(arreglo)
    else:
        suma = 0
        for i in arreglo:
            suma = suma + i
    return suma
def ejVeinteTres(x):
    print("La suma de los elementos del arreglo es:",suma(x))
#24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).
def ejVeinteCuatro(arreglo):
    n = len(arreglo)
    total = suma(arreglo)
    total /= n
    print("El promedio del arreglo es:",total)
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
#26. Desarrollar un algoritmo que calcule el mı́nimo de un arreglo de números enteros (reales).
def ejVeinteSeis(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i <= x:
            x = i
    print("El valor minimo es:",x)
# 27. Desarrollar un algoritmo que calcule el máximo de un arreglo de números enteros (reales).
def ejVeinteSiete(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    print("El valor máximo es:",x)
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
        print("El producto directo de los dos arreglos es:",productoDirecto)
    else:
        print("Los arreglos no son del mismo tamaño")
#29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La mediana es el número que queda en la mitad del arreglo después de ser
#ordenado.
def ejVeinteNueve(arreglo):
    n = len(arreglo)
    arreglo.sort() # Organiza en orden de menor a mayor
    if n%2 == 0:
        n /= 2
        total = (arreglo[int(n-1)] + arreglo[int(n)]) / 2
        print("La mediana del arreglo:",arreglo,"es:",total)
    elif n%2 != 0:
        n /= 2
        n = round(n)
        print("La mediana del arreglo:",arreglo,"es:",arreglo[n])
#30. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
#Ejemplo.
#vector original: (1, 6, 0, 7, −3, 8, 0, −2, 11)
#vector salida: (1, 6, 7, −3, 8, −2, 11, 0, 0)
#Ejemplo.
#vector original: (0, 11, 36, 10, 0, 17, −23, 81, 0, 0, 12, 11, 0)
#vector salida: (11, 36, 10, 17, −23, 81, 12, 11, 0, 0, 0, 0, 0)
def ejTreinta(arreglo):
    n = len(arreglo)
    for i in arreglo:
        if i == 0:
            arreglo.remove(i)
            arreglo.append(0)
        else:
            continue
    print(arreglo)
### Pruebas Funciones ###
#ejVeinteDos(n = input("Ingrese el numero natural a evaluar: "))
#ejVeinteTres(x = [3,5,4,8,9,10])
#ejVeinteCuatro(arreglo = [3,5,4,8,9,10])
#ejVeinteCinco(arreglo1 = [2,2,1], arreglo2 = [3,3,2])
#ejVeinteSeis(arreglo = [-25,0,23,-1,6,7,8,9,10,-489])
#ejVeinteSiete(arreglo = [-25,0,23,-1,6,7,8,9,10,-489,1000])
#ejVeinteOcho(arreglo1 = [2,2,1,5], arreglo2 = [3,3,2,10])
#ejVeinteNueve(arreglo = [2,2,3,5,5,5,6,6,8,9])
#ejTreinta(arreglo = [1, 6, 0, 7, -3, 8, 0, -2, 11])
#ejTreinta(arreglo = [0, 11, 36, 10, 0, 17, -23, 81, 0, 0, 12, 11, 0])