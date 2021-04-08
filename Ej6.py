#6. Una función que determine si un número es divisible por otro.
def ejSeis(a, b):
    if a%b != 0:
        print("No es divisible")
    else:
        print("Es divisible")

def main():
    primerValor = int(input("Ingrese el valor de A:"))
    segundoValor = int(input("Ingrese el valor de B:"))
    ejSeis(primerValor,segundoValor)

if __name__ == "__main__":
    main()