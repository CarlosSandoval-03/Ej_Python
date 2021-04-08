#22. Implementar la criba de Eratostenes para calcular los números primos en el rango 1 a n, donde n es un número natural dado por el usuario.
def ejVeinteDos(n):
    n = int(n)
    if n >= 0:
        numeros = list(range(2, n+1))
        i = 0
        while(numeros[i]*numeros[i] <= n):
            for num in numeros:
                if num <= numeros[i]:
                    continue
                elif num % numeros[i] == 0:
                    numeros.remove(num)
                else:
                    pass
            i += 1
        print(numeros)
    elif n == 1 or n == 0:
        print("No son evaluables")
    else:
        print("El valor ingresado no es natural")
        
def main():
    n = input("Ingrese el numero natural a evaluar: ")
    ejVeinteDos(n)
    
if __name__ == "__main__":
    main()