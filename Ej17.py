import math
import Ej16


def areaPoligonoInscrito(radio, numeroLadosPoligono):
    teta = (360 / numeroLadosPoligono) / 2
    x = radio * math.sin(math.radians(teta))
    lado = 2 * x
    perimetro = lado * numeroLadosPoligono
    area = (perimetro * radio) / 2
    return area


def perimetroPoligonoInscrito(radio, numeroLadosPoligono):
    teta = (360 / numeroLadosPoligono) / 2
    x = radio * math.sin(math.radians(teta))
    lado = 2 * x
    perimetro = lado * numeroLadosPoligono
    return perimetro


def impar(apotema, numeroLados):
    return [Ej16.areaCirculoInscrito(apotema, numeroLados), Ej16.perimetroCirculoInscrito(apotema, numeroLados)]


def par(radio, numeroLados):
    return [areaPoligonoInscrito(radio, numeroLados), perimetroPoligonoInscrito(radio, numeroLados)]


def main():
    print("17. Dado el radio de un cı́rculo, calcular el área y perı́metro del cuadrado, pentágono y hexágono adentro (inscrito en un cı́rculo) y afuera (inscribiendo al cı́rculo).")
    comprobacion = int(
        input("El poligono esta inscrito [0] o circunscribe [1] la circunferencia: "))
    radio = float(input("Ingrese el radio: "))
    figura = int(input("Numero de lados del poligono: "))
    # Se comprueba si se puede usar funcion ya definida en el Ej16
    if comprobacion == 1:
        lista = impar(radio, figura)
        print("El area es:", "{:.2f}".format(
            lista[0]), " y el perimetro es:", "{:.2f}".format(lista[1]))
    elif comprobacion == 0:
        lista = par(radio, figura)
        print("El area es:", "{:.2f}".format(
            lista[0]), " y el perimetro es:", "{:.2f}".format(lista[1]))
    else:
        print("Caso invalido, vuelva a intentar")
        main()


if __name__ == "__main__":
    main()
