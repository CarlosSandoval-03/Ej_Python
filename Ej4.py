#Al granjero se le daño el corral y no sabe si volver a cercar el corral con madera, alambre de púas o poner reja de metal. Si va a cercar con madera debe poner 4
#hileras de tablas, con varilla 8 hileras y con alambre solo 5 hileras, él quiere saber que es lo menos costoso para cercar si sabe que el alambre de púas vale P
#por metro, las tablas a Q por metro y las varillas S por metro. Dado el tamaño del corral y los precios de los elementos, ¿cuál cerramiento es el más económico?.
def ejCuatro(corralN,corralM,madera,varillas,puas):
    if not corralM <= 0 or corralN <= 0:
        corralPerimetro = (corralM * 2) + (corralN * 2)
        if madera >= 0 and varillas >= 0 and puas >= 0:
            maderaTotal = (madera * 4) * corralPerimetro
            varillasTotal = (varillas * 8) * corralPerimetro
            puasTotal = (puas * 5) * corralPerimetro
            if maderaTotal < varillasTotal and maderaTotal < puasTotal:
                return("La mejor opcion es la madera, con un costo total de:", maderaTotal)
            elif varillasTotal < maderaTotal and varillasTotal < puasTotal:
                return("La mejor opcion son las Varillas, con un costo total de:", varillasTotal)
            elif puasTotal < varillasTotal and puasTotal < maderaTotal:
                return("La mejor opcion son las Puas, con un costo total de:", puasTotal)
        else:
            return("Error Precios Materiales")
    else:
            return("Error medicion corral")
            
def main():
    alto = float(input("Ingrese el alto del corral: "))
    ancho = float(input("Ingrese el ancho del corral: "))
    madera = float(input("Ingrese costo de la madera (m): "))
    varilla = float(input("Ingrese costo de la varilla (m): "))
    puas = float(input("Ingrese costo del alambre de puas (m): "))
    print(ejCuatro(alto,ancho,madera,varilla,puas))

if __name__ == "__main__":
    main()
