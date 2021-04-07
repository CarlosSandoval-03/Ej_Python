#12. Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del polinomio en ese número.
def ejDoce(a,b,x):
    variable = a * x
    resultado = 2 * variable
    resultado += b
    print("La derivada en el punto",x,"es",resultado)

def main():
    coefA = int(input("Ingrese el coeficiente A: "))
    coefB = int(input("Ingrese el coeficiente B: "))
    numero = int(input("Ingrese valor dado a X: "))
    ejDoce(coefA,coefB,numero)

if __name__ == "__main__":
    main()