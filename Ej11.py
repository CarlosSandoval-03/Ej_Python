#11. Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.
def ejOnce(a,b,x):
    return (2(a * x)) + b
    
def main():
    coefA = int(input("Ingrese coeficiente A del polinomio: "))
    coefB = int(input("Ingrese coeficiente B del polinomio: "))
    x = int(input("Ingrese valor dado a X: "))
    print("El coeficiente lineal de la derivada es:",ejOnce(coefA,coefB,x))

if __name__ == "__main__":
    main()
