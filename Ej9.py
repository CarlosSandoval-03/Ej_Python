#9. Determinar si un número es múltiplo de la suma de otros dos números.
def ejNueve(a, b, c):
    numero = a + b
    if numero > c and numero != 0:
        return (1,c,numero)
    elif numero == 0:
        return (2)
    else:
        if c % numero == 0:
            multiplo = c / numero
            return (3,c,numero,multiplo)
        else:
            return (4,c,numero)

def mensajes(args) -> tuple:
    args = list(args)
    if args[0] == 1:
        print(args[1],"no es multiplo de",args[2])
    elif args[0] == 2:
        print("0 es multiplo de todos los numeros")
    elif args[0] == 3:
        print(args[1],"es multiplo de", args[2],"(El numero",int(args[3]),"es el multiplo)")
    elif args[0] == 4:
        print(args[1],"no es multiplo de",args[2])
    else:
        print("Error")

def main():
    a = int(input("Ingrese el numero a sumar A: "))
    b = int(input("Ingrese el numero a sumar B: "))
    c = int(input("Ingrese la incognita (posible multiplo): "))
    mensajes(ejNueve(a,b,c))

if __name__ == "__main__":
    main()