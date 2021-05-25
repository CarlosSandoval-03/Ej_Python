from typing import Counter
from Ej35a42 import limpiarConsola


def metodoIndex(element, seeker):
    count = 0
    for parts in element:
        if parts == seeker:
            return count
        else:
            count += 1
    return -1


def metodoSplit(string: str, separador=" ") -> list:
    listOfTerms = []
    temp = ""
    for element in string:
        if element != separador:
            temp += element
        else:
            listOfTerms.append(temp)
            temp = ""
    if len(temp) > 0:
        listOfTerms.append(temp)
    return listOfTerms

# Un polinomio de grado n, como P(x) = anxn + an−1xn−1 + ⋯ + a1x1 + a0x0 se puede representar mediante un arreglo de reales de la siguiente manera: (a0,a1,...,an−1,an).
# Usando esta representacion hacer un programa que le permita al usuario leer dos polinomios y escoger mediante un menu, una de las siguientes operaciones sobre dichos polinomios:


def meterPolinomios() -> list:
    limpiarConsola()


# 43. Evaluar: Lee un real e imprime la evaluacion de los dos polinomios en dicho dato.
# 44. Sumar: Calcula el polinomio suma y lo imprime.
# 45. Resta: Calcula el polinomio resta y lo imprime.
# 46. Multiplicar: Calcula el polinomio multiplicacion y lo imprime.
# 47. Dividir: Calcula el polinomio division del primer polinomio por el segundo y lo imprime.
# 48. Residuo: Calcula el polinomio residuo de la division del primero por el segundo y lo imprime.
# 49. Salir: Permite salir de la aplicacion al usuario.
# Despues de realizada la operacion el menu se debe presentar de nuevo hasta que el usuario desee salir.


def main():
    pass


if __name__ == "__main__":
    main()
