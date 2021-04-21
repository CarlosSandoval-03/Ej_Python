#9. Determinar si un número es múltiplo de la suma de otros dos números.
def ejNueve(a, b, c):
    numero = a + b
    if numero > c and numero != 0:
        return c,"no es multiplo de",numero
    elif numero == 0:
        return "0 es multiplo de todos los numeros"
    else:
        if c % numero == 0:
            multiplo = c / numero
            return c, "es multiplo de", numero,"(El numero",int(multiplo),"es el multiplo)"
        else:
            return c,"no es multiplo de",numero

def main():
    a = int(input("Ingrese el numero a sumar A: "))
    b = int(input("Ingrese el numero a sumar B: "))
    c = int(input("Ingrese la incognita (posible multiplo): "))
    print(ejNueve(a,b,c))

if __name__ == "__main__":
    main()