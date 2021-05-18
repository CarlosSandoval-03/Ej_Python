print("11. Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.")


def ejOnce(a, b, c, x):
    return -(2 * a * x)


def main():
    coefA = float(input("Ingrese coeficiente A del polinomio: "))
    coefB = float(input("Ingrese coeficiente B del polinomio: "))
    coefC = float(input("Ingrese coeficiente C del polinomio: "))
    x = int(input("Ingrese valor dado a X: "))
    print("El coeficiente lineal de la derivada (f'(x)=2ax+b) es:",
          ejOnce(coefA, coefB, coefC, x))


if __name__ == "__main__":
    main()
