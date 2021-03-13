#5. Función potencia de un entero elevado a un entero.
def ejCinco(a, b):
    resultado = int(a) ** int(b)
    print(resultado)
#6. Una función que determine si un número es divisible por otro.
def ejSeis(a, b):
    resultado = a % b
    if resultado > 0:
        print("No es divisible")
    else:
        print("Es divisible")
#7. Determinar si un número es primo.
def ejSiete(num, d=2):
    if d >= num:
        print("Es primo")
        return True
    elif num % d != 0:
        return ejSiete(num, d + 1)
    else:
        print("No es primo", d, "es divisor")
        return False
#8. Dados dos naturales, determinar si son primos relativos.
def ejOcho(a, b):

#9. Determinar si un número es múltiplo de la suma de otros dos números.
#10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado.
#11. Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.
#12. Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del polinomio en ese número.
#13. Dado un natural, determinar si es un número de Fibonacci o no.

######## Pruebas Funciones ########
#ejCinco(int(input("Ingrese el valor de A:")), int(input("Ingrese el valor de B:")))
#ejSeis(int(input("Ingrese el valor de A:")), int(input("Ingrese el valor de B:")))
#ejSiete(int(input("Elija el numero: ")))
ejOcho(3, 8)