#11. Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.
def ejOnce(a,b,x):
    resultado = (a * x) + b
    print("El coeficiente lineal de la derivada es:", resultado)
    
def main():
    coefA = int(input("Ingrese coeficiente A del polinomio: "))
    coefB = int(input("Ingrese coeficiente B del polinomio: "))
    x = int(input("Ingrese valor dado a X: "))
    ejOnce(coefA,coefB,x)

if __name__ == "__main__":
    main()
