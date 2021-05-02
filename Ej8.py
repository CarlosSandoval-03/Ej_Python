#8. Dados dos naturales, determinar si son primos relativos.
def mcdDosValores(primerValor, segundoValor):
    if primerValor > segundoValor:
        if primerValor%segundoValor == 0:
            return segundoValor
        else:
            return mcdDosValores(segundoValor, primerValor%segundoValor)
    else:
        return mcdDosValores(segundoValor,primerValor)
        
def ejOcho(a, b):
    if mcdDosValores(a,b) == 1:
        return "Son primos relativos"
    else:
        return "No son primos relativos" 
        
def main():
    primerValor = int(input("Ingrese el valor de A: "))
    segundoValor = int(input("Ingrese el valor de B: "))
    print(ejOcho(primerValor,segundoValor))

if __name__ == "__main__":
    main()