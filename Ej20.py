def eleccion():
    elec = int(
        input("Elija el tipo de interes:\n1. Simple\n2. Compuesto\nEleccion: "))
    return elec


def simple(a, b):
    return ((7*(b/100)) * a)


def compuesto(a, b):
    return (a * (1 + (b / 100))**7)


def ejVeinte(k, i):
    e = eleccion()
    if e == 1:
        mensajes(True, "Simple", simple(k, i))
    elif e == 2:
        mensajes(True, "Compuesto", compuesto(k, i))
    else:
        mensajes(False, "", None)


def mensajes(tipo, peticion, total):
    if tipo:
        print("El total de pagar a la semana con un interes",
              peticion, "es $", "{:.2f}".format(total))
    else:
        print("Peticion solicitada invalida")


def main():
    print("20. Si un amigo, no tan amigo, me presta K pesos a i pesos de interés diario, ¿cuánto le pagaré en una semana si el interés es simple?, ¿y cuánto si el interés es compuesto?.")
    k = float(input("Ingrese el valor prestado: "))
    i = float(input("Ingrese el interes diario: "))
    ejVeinte(k, i)


if __name__ == "__main__":
    main()
