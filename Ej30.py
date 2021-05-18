print("30. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.")
# Ejemplo.
# vector original: (1, 6, 0, 7, −3, 8, 0, −2, 11)
# vector salida: (1, 6, 7, −3, 8, −2, 11, 0, 0)
# Ejemplo.
# vector original: (0, 11, 36, 10, 0, 17, −23, 81, 0, 0, 12, 11, 0)
# vector salida: (11, 36, 10, 17, −23, 81, 12, 11, 0, 0, 0, 0, 0)


def nuevoMeterNumeros():
    print("Ingrese los valores separados por comas:", end=" ")
    try:
        arreglo = list(map(int, input().split(sep=",")))
        return arreglo
    except:
        print("VALORES INGRESADOS INVALIDOS, POR FAVOR INGRESE SOLO VALORES ENTEROS")


def ejTreinta(arreglo):
    for i in arreglo:
        if i == 0:
            arreglo.remove(i)
            arreglo.append(0)
        else:
            continue
    return(arreglo)


def main():
    x = nuevoMeterNumeros()
    print(ejTreinta(x))


if __name__ == "__main__":
    main()
