print("22. Implementar la criba de Eratostenes para calcular los números primos en el rango 1 a n, donde n es un número natural dado por el usuario.")


def criba(n):
    n = int(n)
    if n >= 0:
        numeros = list(range(2, n+1))
        i = 0
        # Mientras el cuadrado del elemento i sea menor a n continue el ciclo
        while(numeros[i] ** 2 <= n):
            for num in numeros:
                if num <= numeros[i]:
                    # No evaluar numeros ya descubiertos
                    continue
                elif num % numeros[i] == 0:
                    # Si es divisible lo elimina
                    numeros.remove(num)
                else:
                    # Si no es divisible lo omite
                    pass
            i += 1
        return numeros
    elif n == 1 or n == 0:
        return "No son evaluables"
    else:
        return "El valor ingresado no es natural"


def main():
    n = input("Ingrese el numero natural a evaluar: ")
    print(criba(n))


if __name__ == "__main__":
    main()
