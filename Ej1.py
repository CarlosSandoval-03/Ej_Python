#En una granja se crı́an un número de V - Vacas, A - Aves (pollos y gallinas) y E - escorpiones.
#Las vacas están encerradas en un corral de N × M metros cuadrados, las aves en un galpón y los escorpiones en vitrinas.
#1. Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿cuántos litros de leche se producen en la granja?.
def ejUno(vacas,corralN,corralM, producir):
    if corralM <= 0 or corralN <= 0:
        return impresionMensajes(0)
    else:
        corralArea = corralN * corralM
        if vacas > 0:
            leche = (corralArea / producir) * float(vacas)
            return impresionMensajes(1,leche)
        else:
            return impresionMensajes(2)

def impresionMensajes(x,value = 0.0):
    if x == 0:
        print("Error: El area debe ser positiva")
    elif x == 1:
        print("En la granja se producen:", value, "litros de leche")
    else:
        print("No es posible producir leche sin vacas")

def main():
    a = int(input("Numero de vacas: "))
    b = float(input("Ingrese el alto del corral: "))
    c = float(input("Ingrese el ancho del corral: "))
    d = float(input("Cuantos litros de leche la vaca produce por metro cuadrado?: "))
    ejUno(a,b,c,d)

if __name__ == "__main__":
    main()
