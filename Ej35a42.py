import os
from Ej30 import nuevoMeterNumeros
from Ej29 import ordenarMenorMayor


def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def verificionNoRepeticion(arreglo) -> list:
    eliminacionRepetidos = []
    for elemento in arreglo:
        if not elemento in eliminacionRepetidos:
            eliminacionRepetidos.append(elemento)
        else:
            continue
    return eliminacionRepetidos
# Usando esta representación hacer un programa que le permita al usuario leer dos conjuntos de enteros y escoger mediante un menu, una de las siguientes operaciones sobre ellos:
# 35. Union: Calcula en un arreglo la union de los conjuntos y la imprime.


def unionArreglos(arreglo1, arreglo2) -> list:
    return verificionNoRepeticion(arreglo1+arreglo2)
# 36. Intersección: Calcula en un arreglo la intersección de los conjuntos y la imprime.


def interseccionArreglos(arreglo1, arreglo2):
    listaInterseccion = []
    for elemento in arreglo1:
        if elemento in arreglo2:
            listaInterseccion.append(elemento)
    if len(listaInterseccion) == 0:
        listaInterseccion.append("Conjunto Vacio")
        return listaInterseccion
    else:
        return verificionNoRepeticion(listaInterseccion)

# 37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.


def diferenciaArreglos(arreglo1, arreglo2):
    listaDiferencia = []
    for elemento in arreglo1:
        if not elemento in arreglo2:
            listaDiferencia.append(elemento)
    if len(listaDiferencia) == 0:
        listaDiferencia.append("Conjunto Vacio")
        return listaDiferencia
    else:
        return verificionNoRepeticion(listaDiferencia)
# 38. Diferencia simétrica: Calcula en un arreglo la diferencia simétrica de los conjuntos y la imprime.


def difSimetricaArreglos(arreglo1, arreglo2):
    listaDiferenciaSim = []
    for elemento in arreglo1:
        if not elemento in arreglo2:
            listaDiferenciaSim.append(elemento)
    for elemento in arreglo2:
        if not elemento in arreglo1:
            listaDiferenciaSim.append(elemento)
    if len(listaDiferenciaSim) == 0:
        listaDiferenciaSim.append("Conjunto Vacio")
        return listaDiferenciaSim
    else:
        return verificionNoRepeticion(listaDiferenciaSim)
# 39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los conjuntos y lo imprime.


def perteneceArreglos(arreglo1, arreglo2, entero):
    a, b = False, False
    if int(entero) in arreglo1:
        a = True
    if int(entero) in arreglo2:
        b = True
    return a, b
# 40. Contenido: Determina si el primer conjunto esta contenido en el segundo y lo imprime.


def contenidoArreglos(arreglo1, arreglo2):
    x = 0
    for elemento in arreglo1:
        if elemento in arreglo2:
            x += 1
    if x == len(arreglo1):
        return True
    else:
        return False
# 41. Salir: Permite al usuario salir de la aplicación.


def boleanosMenu(arreglo1, arreglo2, eleccionUsuario):
    if eleccionUsuario == 1:
        temp = unionArreglos(arreglo1, arreglo2)
        return ["Union", temp]
    elif eleccionUsuario == 2:
        temp = interseccionArreglos(arreglo1, arreglo2)
        return ["Interseccion", temp]
    elif eleccionUsuario == 3:
        temp = diferenciaArreglos(arreglo1, arreglo2)
        return["Diferencia", temp]
    elif eleccionUsuario == 4:
        temp = difSimetricaArreglos(arreglo1, arreglo2)
        return ["Diferencia Simetrica", temp]
    elif eleccionUsuario == 5:
        entero = int(input("Ingrese el entero a evaluar: "))
        temp = perteneceArreglos(arreglo1, arreglo2, entero)
        return ["Pertenece", temp, entero, "Especial1"]
    elif eleccionUsuario == 6:
        temp = contenidoArreglos(arreglo1, arreglo2)
        return ["Contiene", temp, "Especial2"]
    elif eleccionUsuario == 7:
        return "Finaliza"


def menuPrincipal(Resultado=None, mensaje="", mem=[]):
    limpiarConsola()
    if Resultado:
        print(mensaje)
        arreglo1 = mem
        print("!---------------------------------------------------- Bienvenido a Los Conjuntos Como Arreglos ----------------------------------------------------!\nEl primer Arreglo es:", arreglo1)
        borradoCache = str(input(
            "Si desea eliminar este valor por favor digite ':wq' y el programa olvidara este primer arreglo (En caso opuesto deje el campo vacio): "))
        if borradoCache == ":wq":
            return menuPrincipal(None)
    elif Resultado == None:
        print("!---------------------------------------------------- Bienvenido a Los Conjuntos Como Arreglos ----------------------------------------------------!\nPrimer Arreglo")
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
    except:
        limpiarConsola()
        return main("ValorEntero")
    listaValores = boleanosMenu(arreglo1, arreglo2, eleccionUsuario)
    if listaValores == "Finaliza":
        return main("Exit")
    else:
        operacion = listaValores[0]
        arregloFinal = ordenarMenorMayor(listaValores[1])
        if listaValores[-1] != "Especial1" and listaValores[-1] != "Especial2":
            return [menuPrincipal(True, f"! SOLUCION: El resultado de la operacion '{operacion}' entre conjuntos es: {arregloFinal} !", arregloFinal)]
        elif listaValores[-1] == "Especial1":
            entero = listaValores[2]
            return [menuPrincipal(True, f"! SOLUCION: El resultado de la operacion '{operacion}', donde se busca {entero} es: !\n'{arregloFinal[0]}' en arreglo 1\n'{arregloFinal[1]}' en arreglo 2")]
        elif listaValores[-1] == "Especial2":
            return [menuPrincipal(True, f"! SOLUCION: El resultado de la operacion '{operacion}' es: !\n Es '{arregloFinal}' que el arreglo 2 contiene al arreglo 1")]


def main(salida=""):
    if salida == "Exit":
        print("!---------------------------------------------------- Saliendo De Los Conjuntos Como Arreglos ----------------------------------------------------!")
    elif salida == "ValorEntero":
        print("! ERROR: VALORES INGRESADOS INVALIDOS, POR FAVOR INGRESE UN ENTERO !")
        print("!---------------------------------------------------- Saliendo De Los Conjuntos Como Arreglos ----------------------------------------------------!")
    else:
        x = menuPrincipal()


if __name__ == "__main__":
    main()
