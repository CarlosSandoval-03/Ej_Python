import math
print("18. Si una araña utiliza un patrón de hexágono regular para su telaraña, y cada hexágono está separado del otro por 1cm, y la araña quiere hacer una telaraña de πr(2) ¿qué cantidad de telaraña requiere la araña?.")


def ejDiezOcho(r):
    x = (math.pi * (r**2)) + 1
    perimetro = 6 * r
    cm = (x / perimetro)
    return "La araña necesitara:", "{:.2f}".format(cm), "cm"


def main():
    radio = float(input("Ingrese el radio: "))
    print(ejDiezOcho(radio))


if __name__ == "__main__":
    main()
