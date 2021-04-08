#19. Si en la UN están podando árboles y cada rama tiene P hojas, y a cada árbol le quitaron K ramas, cuántos árboles se deben podar para obtener T hojas?.
def ejDiezNueve(p,k,t):
    p = int(p)
    k = int(k)
    t = int(t)
    total = t / (p * k)
    print("El total de arboles es:",total)
    
def main():
    hojas = input("Cuantas hojas hay por rama?: ")
    ramas = input("Cuantas ramas hay por arbol?: ")
    total = input("Cuantas hojas quieres obtener?: ")
    ejDiezNueve(hojas,ramas,total)

if __name__ == "__main__":
    main()