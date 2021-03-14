#5. Función potencia de un entero elevado a un entero.
def ejCinco(a, b):
    resultado = int(a) ** int(b)
    print(resultado)
#6. Una función que determine si un número es divisible por otro.
def ejSeis(a, b):
    resultado = a % b
    if resultado != 0:
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
    def mcd(x, y):
        if x > y:
            if x % y == 0:
                return y
            else:
                return mcd(y, x%y)
        else:
            return mcd(y,x)
    if mcd(a,b) == 1:
        print("Son primos relativos")
    else:
        print("No son primos relativos")
#9. Determinar si un número es múltiplo de la suma de otros dos números.
def ejNueve(a, b, c):
    num = a + b
    if num > c:
        print(c,"no es multiplo de",num)
    else:
        if c % num == 0:
            multi = c / num
            print(c, "es multiplo de", num,"(El numero",int(multi),"es el multiplo)")
        else:
            print(c,"no es multiplo de",num)        
#10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado. Ax^2+bx+c
def ejDiez(a,b,c,x):
    resultado = (a * (x*x)) + (b * x) + c
    print("El valor dado es:",resultado)
#11. Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.
def ejOnce(a,b,x):
    resultado = (a * x) + b
    print("El coeficiente lineal de la derivada es:", resultado)
#12. Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del polinomio en ese número.
def ejDoce(a,b,x):
    var = a * x
    resultado = 2 * var
    resultado += b
    print("La derivada en el punto",x,"es",resultado)
#13. Dado un natural, determinar si es un número de Fibonacci o no.
def ejTrece(num):
    def raizCuadrada(var):
        x = 1.0
        for k in range(1, 10):
            x = (x + var/x)/2
        return x
    def cuadradoPerfecto(x): 
        s = int(raizCuadrada(x)) 
        return s*s == x 
    def siNumero(n):  
        return cuadradoPerfecto(5*n*n + 4) or cuadradoPerfecto(5*n*n - 4) 

    if siNumero(num) == True: 
        print(num,"es un numero Fibonacci")
    else: 
        print(num,"NO es un numero Fibonacci")
######## Pruebas Funciones ########
#ejCinco(int(input("Ingrese el valor de A:")), int(input("Ingrese el valor de B:")))
#ejSeis(int(input("Ingrese el valor de A:")), int(input("Ingrese el valor de B:")))
#ejSiete(int(input("Elija el numero: ")))
#ejOcho(a = int(input("Ingrese el valor de A:")), b = int(input("Ingrese el valor de B:")))
#ejNueve(a = int(input("Ingrese el numero a sumar A: ")), b = int(input("Ingrese el numero a sumar B: ")), c = int(input("Ingrese la incognita (posible multiplo): ")))
#ejDiez(a = int(input("Ingrese coeficiente A: ")),b = int(input("Ingrese coeficiente B: ")),c = int(input("Ingrese coeficiente C: ")),x = int(input("Ingrese el valor dado a X:")))
#ejOnce(a = int(input("Ingrese coeficiente A del polinomio: ")), b = int(input("Ingrese coeficiente B del polinomio: ")), x = int(input("Ingrese valor dado a X: ")))
#ejDoce(a = int(input("Ingrese el coeficiente A: ")), b = int(input("Ingrese el coeficiente B: ")), x = int(input("Ingrese valor dado a X: ")))
#ejTrece(num = int(input("Ingrese el valor a comprobar: ")))