from Ej35a42 import limpiarConsola
from metodosTemp import inversoArreglo, maximoArreglo
from metodosTemp import metodoIndex
from Ej35a42 import verificionNoRepeticion
# Metodo Split ------------------------------------


def splitPolinomios(polinomio: str) -> list:
    listOfTerms = []
    temp = ''
    for element in range(len(polinomio)):
        if polinomio[element] == '+' or polinomio[element] == '-':
            listOfTerms.append(temp)
            temp = ''
        temp += polinomio[element]
    listOfTerms.append(temp)
    if listOfTerms[0] == '':
        listOfTerms.pop(0)
    return listOfTerms
# Coeficientes ------------------------------------


def coeficienteSubOperacion(polinomios: int) -> float:
    temp = ''
    i = 0
    while i < (len(polinomios)) and polinomios[i] != 'x':
        temp += polinomios[i]
        i += 1
    return float(temp)


def coeficientes(listaPolinomios: list) -> list:
    listOfCoefficients = []
    for i in range(len(listaPolinomios)):
        listOfCoefficients.append(coeficienteSubOperacion(listaPolinomios[i]))
    return listOfCoefficients
# Exponentes ------------------------------------


def exponenteSubOperacion(listaExponentes: int) -> int:
    n = len(listaExponentes)
    if listaExponentes[n-1] == 'x':
        return 1
    i = 0
    while i < n and listaExponentes[i] != 'x':
        i += 1
    if i == n:
        return 0
    else:
        temp = ''
        for j in range(i+2, n):
            temp += listaExponentes[j]
        return int(temp)


def exponentes(listaPolinomios: list) -> list:
    listOfExponents = []
    for i in range(len(listaPolinomios)):
        listOfExponents.append(exponenteSubOperacion(listaPolinomios[i]))
    return listOfExponents
# Grado ------------------------------------


def maximoGrado(listaExponentes: list) -> int:
    return maximoArreglo(listaExponentes)
# Lista Polinomio ------------------------------------


def meterPolinomios(coeficienteLista: list, exponenteLista: list) -> list:
    m = len(coeficienteLista)
    poliniomio = [0 for i in range(maximoGrado(exponenteLista) + 1)]
    for i in range(m):
        poliniomio[exponenteLista[i]] = coeficienteLista[i]
    return poliniomio

# Un polinomio de grado n, como P(x) = anxn + an−1xn−1 + ⋯ + a1x1 + a0x0 se puede representar mediante un arreglo de reales de la siguiente manera: (a0,a1,...,an−1,an).
# Usando esta representacion hacer un programa que le permita al usuario leer dos polinomios y escoger mediante un menu, una de las siguientes operaciones sobre dichos polinomios:


def polinomio(string: str) -> list:
    temp = splitPolinomios(string)
    expo = exponentes(temp)
    coef = coeficientes(temp)
    return meterPolinomios(coef, expo)
# 43. Evaluar: Lee un real e imprime la evaluacion de los dos polinomios en dicho dato.


def evaluarSimple(polinomio: list, real: float) -> list:
    n = len(polinomio)
    pos = 0
    listaFinal = []
    while pos < n:
        for termino in polinomio:
            listaFinal.append(str(termino) + '(' + str(real ** pos) + ')')
            pos += 1
    return listaFinal


def evaluar(polinomio1: list, polinomio2: list, real: float) -> tuple:
    return (evaluarSimple(polinomio1, real), evaluarSimple(polinomio2, real))
# 44. Sumar: Calcula el polinomio suma y lo imprime.


def sumarPolinomios(polinomio1: list, polinomio2: list) -> list:
    sumar = []
    for i in range(len(polinomio1)):
        temp = polinomio1[i] + polinomio2[i]
        sumar.append(temp)
    return sumar

# 45. Resta: Calcula el polinomio resta y lo imprime.


def restarPolinomios(polinomio1: list, polinomio2: list) -> list:
    restar = []
    for i in range(len(polinomio1)):
        temp = polinomio1[i] - polinomio2[i]
        restar.append(temp)
    return restar
# 46. Multiplicar: Calcula el polinomio multiplicacion y lo imprime.


def ubicarPolinomios(listaTerminos: list, exponentes: list) -> list:
    listaUbicacion = ['0.0' for i in range(maximoArreglo(exponentes) + 1)]
    temp1 = inversoArreglo(listaTerminos)
    for k in range(len(temp1)):
        listaUbicacion[k] = temp1[k]
    return lista_textoPolinomio(inversoArreglo(listaUbicacion))


def lista_textoPolinomio(lista: list) -> str:
    pos = 0
    listaFinal = []
    for elemento in lista:
        if elemento != '0.0' or elemento != '0':
            if pos > 0 and pos != 1:
                listaFinal.append(elemento + 'x^' + str(pos))
            elif pos > 0 and pos == 1:
                listaFinal.append(elemento + 'x')
            else:
                listaFinal.append(elemento)
        pos += 1

    temp = ''
    for i in inversoArreglo(listaFinal):
        temp += i
    return temp


def multiplicarPolinomio(polinomio1: list, polinomio2: list) -> list:
    multiplicar = []
    expo = []
    for i in range(len(polinomio1)):
        for k in range(len(polinomio2)):
            temp = polinomio1[i] * polinomio2[k]
            if temp > 0:
                multiplicar.append('+' + str(temp))
                expo.append(i+k)
            elif temp != 0:
                expo.append(i+k)
                multiplicar.append(str(temp))

    counts = {}
    for j in range(len(expo)):
        counts[expo[j]] = counts.get(expo[j], 0) + 1

    copiaMultiplicar = multiplicar.copy()
    operar = []
    listaTemporal = []
    for k, v in counts.items():
        if v > 1:
            for i in range(v):
                index = metodoIndex(expo, k)
                operar.append(copiaMultiplicar[index])  # Debo retornar copia
                copiaMultiplicar.pop(index)
                listaTemporal.append(index)

    sumaTemp = 0
    for h in range(len(operar)):
        sumaTemp += float(operar[h])
        if sumaTemp > 0:
            suma = '+' + str(sumaTemp)
        else:
            suma = str(sumaTemp)
    copiaMultiplicar.insert(listaTemporal[0], suma)
    return ubicarPolinomios(copiaMultiplicar, verificionNoRepeticion(expo))

# 47. Dividir: Calcula el polinomio division del primer polinomio por el segundo y lo imprime.


def eliminar_ceros(lista: list) -> list:
    temp = []
    for i in range(len(lista)):
        if lista[i] == '0':
            pass
        else:
            temp.append(lista[i])
    return temp


def divisionPolinomios(polinomio1: list, polinomio2: list) -> list:
    dividir = []
    expo = []
    for i in range(len(polinomio1)):
        for k in range(len(polinomio2)):
            temp = polinomio1[i] / polinomio2[k]
            if temp > 0:
                dividir.append('+' + str(temp))
                expo.append(i+k)
            elif temp != 0:
                expo.append(i+k)
                dividir.append(str(temp))

    counts = {}
    for j in range(len(expo)):
        counts[expo[j]] = counts.get(expo[j], 0) + 1

    copiadividir = dividir.copy()
    operar = []
    listaTemporal = []
    for k, v in counts.items():
        if v > 1:
            for i in range(v):
                index = metodoIndex(expo, k)
                operar.append(copiadividir[index])  # Debo retornar copia
                copiadividir.pop(index)
                listaTemporal.append(index)

    sumaTemp = 0
    for h in range(len(operar)):
        sumaTemp += float(operar[h])
        if sumaTemp > 0:
            suma = '+' + str(sumaTemp)
        else:
            suma = str(sumaTemp)
    copiadividir.insert(listaTemporal[0], suma)
    return ubicarPolinomios(copiadividir, verificionNoRepeticion(expo))





# 48. Residuo: Calcula el polinomio residuo de la division del primero por el segundo y lo imprime.

def residuoPolinomios(polinomio1: list, polinomio2: list) -> list:
    residuo = []
    expo = []
    for i in range(len(polinomio1)):
        for k in range(len(polinomio2)):
            temp = polinomio1[i] % polinomio2[k]
            if temp > 0:
                residuo.append('+' + str(temp))
                expo.append(i+k)
            elif temp != 0:
                expo.append(i+k)
                residuo.append(str(temp))

    counts = {}
    for j in range(len(expo)):
        counts[expo[j]] = counts.get(expo[j], 0) + 1

    copiaresiduo = residuo.copy()
    operar = []
    listaTemporal = []
    for k, v in counts.items():
        if v > 1:
            for i in range(v):
                index = metodoIndex(expo, k)
                operar.append(copiaresiduo[index])  # Debo retornar copia
                copiaresiduo.pop(index)
                listaTemporal.append(index)

    sumaTemp = 0
    for h in range(len(operar)):
        sumaTemp += float(operar[h])
        if sumaTemp > 0:
            suma = '+' + str(sumaTemp)
        else:
            suma = str(sumaTemp)
    copiaresiduo.insert(listaTemporal[0], suma)
    return ubicarPolinomios(copiaresiduo, verificionNoRepeticion(expo))

# 49. Salir: Permite salir de la aplicacion al usuario.
# Despues de realizada la operacion el menu se debe presentar de nuevo hasta que el usuario desee salir.
# Test = 2x^3+5x-3 || 4x-3x^2+2x^3

def menu_polinomios() -> tuple:
    limpiarConsola()
    print('!---------------------------------------------------- Bienvenido a Los Polinomios Como Arreglos ----------------------------------------------------!\nPrimer Polinomio: ', end='')
    primer_polinomio = str(input())
    segundo_polinomio = str(input('Segundo Polinomio: '))
    return (primer_polinomio, segundo_polinomio)


def menu_elecciones(polinomio1: str, polinomio2: str) -> tuple:
    limpiarConsola()
    conver_p1 = polinomio(polinomio1)
    conver_p2 = polinomio(polinomio2)
    print(f'Polinomio 1: {polinomio1}\nPolinomio 2: {polinomio2}')
    print("!----------------------- En caso de que el valor sea diferente a los mostrados aqui, tomara la eleccion valida mas cercana -----------------------!")
    eleccionUsuario = int(input(
        "Ingrese operacion a realizar:\n1. Evaluar\n2. Sumar\n3. Restar\n4. Multiplicar\n5. Dividir\n6. Residuo\n7. Finalizar programa\nEleccion: "))
    return (conver_p1, conver_p2, eleccionUsuario)


def operaciones_elecciones(pol1: list, pol2: list, eleccion: int):
    if eleccion == 1:
        num = float(input('Ingrese el valor con el cual evaluar: '))
        temp = evaluar(pol1, pol2, num)
        return ('evaluar', temp)
    elif eleccion == 2:
        temp = sumarPolinomios(pol1, pol2)
        return ('sumar', temp)
    elif eleccion == 3:
        temp = restarPolinomios(pol1, pol2)
        return ('restar', temp)
    elif eleccion == 4:
        temp = multiplicarPolinomio(pol1, pol2)
        return ('multiplicar', temp)
    elif eleccion == 5:
        temp = 'Me falta wey \U0001F605'
        return ('random', temp)
    elif eleccion == 6:
        temp = 'Me falta wey \U0001F605'
        return ('random', temp)
    elif eleccion >= 7:
        return 'EXIT_MENU_OPERATION_404'


def ciclo_menu(flag=True, impresion=False):
    while flag == True and impresion == False:
        x, y = menu_polinomios()
        lista = menu_elecciones(x, y)
        resultado = operaciones_elecciones(lista[0], lista[1], lista[2])
        if resultado != 'EXIT_MENU_OPERATION_404':
            impresion = True
            limpiarConsola()
            print(f'El resultado de {resultado[0]} es: {resultado[1]}')
            continuar = str(input('Ingrese cualquier valor para continuar: '))
            if len(continuar) != 0 or len(continuar) == 0:
                ciclo_menu()
        else:
            print('!---------------------------------------------------- Hasta la proxima \U0001F44B ----------------------------------------------------!')
            flag = False


def main():
    # ciclo_menu()
    print(divisionPolinomios(polinomio('1x^5+2x^3-1x-8'),polinomio('1x^2-2x+1')))


if __name__ == '__main__':
    main()
