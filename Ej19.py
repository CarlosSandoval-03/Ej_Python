def ejDiezNueve(p, k, t):
    p = round(float(p))
    k = round(float(k))
    t = round(float(t))
    return t / (p * k)


def main():
    print("19. Si en la UN están podando árboles y cada rama tiene P hojas, y a cada árbol le quitaron K ramas, cuántos árboles se deben podar para obtener T hojas?.")
    hojas = input("Cuantas hojas hay por rama?: ")
    ramas = input("Cuantas ramas hay por arbol?: ")
    total = input("Cuantas hojas quieres obtener?: ")
    print("El total de arboles es:", ejDiezNueve(hojas, ramas, total))


if __name__ == "__main__":
    main()
