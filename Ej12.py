def ejDoce(a, b, x):
    return (2 * (a * x)) + b


def main():
    print("12. Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del polinomio en ese número.")
    coefA = int(input("Ingrese el coeficiente A: "))
    coefB = int(input("Ingrese el coeficiente B: "))
    numero = int(input("Ingrese valor dado a X: "))
    print("La derivada en el punto indicado es", ejDoce(coefA, coefB, numero))


if __name__ == "__main__":
    main()
