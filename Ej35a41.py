import os
from Ej30 import nuevoMeterNumeros


def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# Usando esta representación hacer un programa que le permita al usuario leer dos conjuntos de enteros y escoger mediante un menu, una de las siguientes operaciones sobre ellos:


def verificionNoRepeticion(arreglo) -> list:
    eliminacionRepetidos = []
    for elemento in arreglo:
        if not elemento in eliminacionRepetidos:
            eliminacionRepetidos.append(elemento)
        else:
            continue
    return eliminacionRepetidos

# 35. Union: Calcula en un arreglo la union de los conjuntos y la imprime.


def unionArreglos():
    pass
# 36. Intersección: Calcula en un arreglo la intersección de los conjuntos y la imprime.


def interseccionArreglos():
    pass
# 37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.


def diferenciaArreglos():
    pass
# 38. Diferencia simétrica: Calcula en un arreglo la diferencia simétrica de los conjuntos y la imprime.


def difSimetricaArreglos():
    pass
# 39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los conjuntos y lo imprime.


def perteneceArreglos():
    pass
# 40. Contenido: Determina si el primer conjunto esta contenido en el segundo y lo imprime.


def contenidoArreglos():
    pass
# 41. Salir: Permite al usuario salir de la aplicación.


def menuPrincipal():
    print("!---------------------------------------------------- Bienvenido a Los Conjuntos Como Arreglos ----------------------------------------------------!\nPrimer Arreglo:")
    arreglo1 = verificionNoRepeticion(nuevoMeterNumeros())
    print("\nSegundo Arreglo:")
    arreglo2 = verificionNoRepeticion(nuevoMeterNumeros())
    print("!----------------------- En caso de que el valor sea diferente a los mostrados aqui, tomara la eleccion valida mas cercana -----------------------!")
    eleccionUsuario = input(
        "Ingrese operacion a realizar:\n1. Union\n2. Interseccion\n3. Diferencia\n4. Diferencia Simetrica\n5. Pertenece\n6. Contenido\n7. Finalizar programa\nEleccion: ")
    try:
        eleccionUsuario = int(eleccionUsuario)
        if eleccionUsuario > 7:
            eleccionUsuario = 7
        elif eleccionUsuario < 1:
            eleccionUsuario = 1
        return arreglo1, arreglo2, eleccionUsuario
    except:
        limpiarConsola()
        print("! ERROR: VALORES INGRESADOS INVALIDOS, POR FAVOR INGRESE UN ENTERO !")
        main()


def main():
    funcionMenu = menuPrincipal()
    arreglo1 = funcionMenu[0]
    arreglo2 = funcionMenu[1]
    eleccionUsario = funcionMenu[2]
    while eleccionUsario != 7:
        if eleccionUsario == 1:
            unionArreglos()
            break
        elif eleccionUsario == 2:
            interseccionArreglos()
            break
        elif eleccionUsario == 3:
            diferenciaArreglos()
            break
        elif eleccionUsario == 4:
            difSimetricaArreglos()
            break
        elif eleccionUsario == 5:
            perteneceArreglos()
            break
        elif eleccionUsario == 6:
            contenidoArreglos()
            break
    print(funcionMenu)
    print("Final ciclo")


if __name__ == "__main__":
    main()
