vacas = int(input("Numero de vacas: "))
aves = int(input("Numero de Aves: "))
escorpiones = int(input("Numero de escorpiones: "))
corralN = int(input("Ingrese el alto del corral: "))
corralM = int(input("Ingrese el ancho del corral: "))

# Caso 1
if corralM <= 0 or corralN <= 0:
    print("Error: El area debe ser positiva")
else:
    corralArea = corralN * corralM
    if not vacas <= 0:
        producir = int(input("¿Cuantos litros de leche la vaca produce por metro cuadrado?: "))
        leche = vacas * (producir * corralArea)
        print("En la granja se producen:", leche, "litros de leche")
    else:
        print("No es posible producir leche sin vacas")
# Caso 2
if aves >= 3:
    gallinas = aves / 3
    if not gallinas <= 2:
        gallinasMitad = int(gallinas) / 2
        grupoUno = int(gallinasMitad) * (30 / 3)
        grupoDos = int(gallinasMitad) * (30 / 5)
        huevos = grupoUno + grupoDos
        print("En 1 mes la granja produce:", int(huevos), "huevos")
    else:
        print("No tenemos gallinas de coma flotante O-O")
else:
    print("No tenemos aves negativas")
# Caso 3
if not escorpiones <= 3:
    escorpionesVenta = escorpiones / 3
    escorpionesVenta = int(escorpionesVenta)
    escorpionesGrandes = escorpionesVenta * 50
    escorpionesMedianos = escorpionesVenta * 30
    escorpionesGramos = escorpionesGrandes + escorpionesMedianos
    escorpionesKilos = escorpionesGramos / 1000
    print("Podemos vender:", escorpionesKilos, "kilos, de escorpiones a China")
else:
    print("No tenemos escorpiones suficientes :(")
# Caso 4
if not corralM <= 0 or corralN <= 0:
    corralPerimetro = (corralM * 2) + (corralN * 2)
    madera = int(input("Ingrese costo de la madera (m): "))
    varillas = int(input("Ingrese costo de la varilla (m): "))
    puas = int(input("Ingrese costo del alambre de puas (m): "))
    if madera >= 0 and varillas >= 0 and puas >= 0:
        maderaTotal = (madera * 4) * corralPerimetro
        varillasTotal = (varillas * 8) * corralPerimetro
        puasTotal = (puas * 5) * corralPerimetro
        if maderaTotal > varillasTotal and maderaTotal > puasTotal:
            print("La mejor opcion es la madera, con un costo total de:", maderaTotal)
        if varillasTotal > maderaTotal and varillasTotal > puasTotal:
            print("La mejor opcion son las Varillas, con un costo total de:", varillasTotal)
        if puasTotal > varillasTotal and puasTotal > maderaTotal:
            print("La mejor opcion son las Pueas, con un costo total de:", puasTotal)
    else:
        print("Ush donde dan esos materiales tan baratos")
else:
        print("Uy el corral esta como mal medido, solo digo")