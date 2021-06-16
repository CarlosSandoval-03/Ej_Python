def ejDiez(a, b, c, x):
    return (a * (x**2)) + (b * x) + c


def main():
    print("10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado. Ax^2+bx+c")
    coefA = float(input("Ingrese coeficiente A: "))
    coefB = float(input("Ingrese coeficiente B: "))
    coefC = float(input("Ingrese coeficiente C: "))
    valor = float(input("Ingrese el valor x: "))
    print("El valor dado es:", ejDiez(coefA, coefB, coefC, valor))


if __name__ == "__main__":
    main()
