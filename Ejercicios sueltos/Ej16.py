#16. Dado el radio de un cı́rculo, calcular el área del triángulo que circunscribe el circulo (triangulo afuera).
def ejDiezSeis(r):
    x = 4.84 * r
    y = 2.42 * r
    z = (x * y) / 2
    print("Aproximadamente:","{:.2f}".format(z))

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    ejDiezSeis(radio)
    
if __name__ == "__main__":
    main()