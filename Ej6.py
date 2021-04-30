#6. Una función que determine si un número es divisible por otro.
def ejSeis(a, b):
    if a%b != 0:
        return("No es divisible")
    else:
        return("Es divisible")

def main():
    primerValor = float(input("Ingrese el valor de A:"))
    segundoValor = float(input("Ingrese el valor de B:"))
    print(ejSeis(primerValor,segundoValor))

if __name__ == "__main__":
    main()
