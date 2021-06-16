def ejSiete(numero, i=2):
    if i >= numero and numero > 0:
        return True
    elif numero % i != 0:
        return ejSiete(numero, i + 1)
    elif numero < 0:
        return False
    else:
        return i


def mensajes(*args):
    if args[0] == True:
        print("Es primo")
    elif args[0] == False and len(args) == 1:
        print("El valor indicado no puede ser evaluado")
    elif (args != True or args != False):
        print("No es primo", args[0], "es divisor")


def main():
    print("7. Determinar si un numero es primo.")
    a = int(input("Elija el numero: "))
    mensajes(ejSiete(a))


if __name__ == "__main__":
    main()
