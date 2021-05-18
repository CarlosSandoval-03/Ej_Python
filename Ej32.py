print("32. Hacer un algoritmo que dado un número entero no negativo, cree un arreglo de unos y ceros que representa el número en binario al revés.")
# Ejemplo.
#Número: 106
# Arreglo: (0, 1, 0, 1, 0, 1, 1) (representa el número 1101010)
# Ejemplo.
#Número: 389
# Arreglo: (1, 0, 0, 1, 0, 1, 1, 1, 1) (representa el número 111101001)


def decimalBinario(decimal):
    binario = []
    while decimal // 2 >= 1:
        binario.append(decimal % 2)
        decimal = decimal // 2
    binario.append(decimal % 2)
    return binario


def validar(dato):
    if dato >= 0:
        return True
    else:
        return False


def ejTreintaDos(datos):
    if validar(datos):
        resultado = decimalBinario(datos)
        resultado.reverse()
        return resultado
    else:
        return "Datos ingresados invalidos, por favor que sea un entero positivo"


def main():
    a = int(input("Ingrese el valor natural a evaluar: "))
    print("La lista solicitada es:", ejTreintaDos(a))


if __name__ == "__main__":
    main()
