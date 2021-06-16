#Si los escorpiones de la granja se venden a China, y hay escorpiones de tres diferentes tamaños: pequeños (con un peso de 20 gramos), medianos (con un peso 30 gramos)
#y grandes (con un peso de 50 gramos), ¿cuántos kilos de escorpiones se pueden vender sin que decrezca la población a menos de 2/3?.
def ejTres(escorpiones):
    if not escorpiones <= 3:
        escorpionesVenta = escorpiones // 3
        escorpionesVenta = int(escorpionesVenta)
        #Teniendo en cuenta que se venderan los escorpiones que representen mayor valor a la venta se consideran unicamente Grandes y Medianos
        escorpionesGrandes = escorpionesVenta * 50
        escorpionesMedianos = escorpionesVenta * 30
        escorpionesGramos = escorpionesGrandes + escorpionesMedianos
        escorpionesKilos = escorpionesGramos / 1000
        return escorpionesKilos
    else:
        return "Escorpiones insuficientes"

def main():
    a = int(input("Numero de escorpiones: "))
    print("Podemos vender:", ejTres(a), "kilos de escorpiones")

if __name__ == "__main__":
    main()
