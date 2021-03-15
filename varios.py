#19. Si en la UN están podando árboles y cada rama tiene P hojas, y a cada árbol le quitaron K ramas, cuántos árboles se deben podar para obtener T hojas?.
def ejDiezNueve(p,k,t):
    p = int(p)
    k = int(k)
    t = int(t)
    x = t / (p * k)
    print("El total de arboles es:",x)
#20. Si un amigo, no tan amigo, me presta K pesos a i pesos de interés diario, ¿cuánto le pagaré en una semana si el interés es simple?, ¿y cuánto si el interés es 
#compuesto?.
def ejVeinte(k,i):
    tipo = None
    e = int(input("Elija el tipo de interes:\n1. Simple\n2. Compuesto\nEleccion: "))
    k = float(k)
    i = float(i)
    i = (i / 100) * k
    
    if e == 1:
        total = (k + i) * 7
        peticion = "Simple"
        tipo = True
    elif e == 2:
        semana = (1+(i/k)) * 7
        total = k * semana
        peticion = "Compuesto"
        tipo = True
    else:
        tipo = False
        
    if tipo:
        print("El total de pagar a la semana con un interes",peticion,"es $","{:.2f}".format(total))
    else:
        print("Peticion solicitada invalida")
#21. Un niño se la pasó jugando con fichas de lego, tenia dos tipos de fichas de lego, fichas de cuadros de 1 × 1 (rojas) y fichas de cuadros de 2 × 1 (azules), y 
#le dieron una base de 1 × n cuadritos, ¿de cuántas formas distintas puede ubicar las fichas rojas y azules sobre la base?, ¿y si le dan una ficha amarilla de 1 × 3?.
def ejVeinteUno(num):
    def legos(n):
        if n <= 1:
           return n
        else:
            return(legos(n-1) + legos(n-2))
    def legos_2(n):
        if n <= 2:
               return n
        else:
            return(legos_2(n-1) + legos_2(n-2)) + legos_2(n-3)
        
    num = int(num)
    e = int(input("Eliga el caso 1 o el caso 2 (sin ficha amarilla): "))
    x = None
    
    if e == 1:
        x = legos(num)
        caso = "1"
        mensaje = True
    elif e == 2:
        x = legos_2(num)
        caso = "2"
        mensaje = True
    else:
        mensaje = False
    
    if mensaje:
        print("La cantidad de formas en las que se pueden ubicar las fichas en el caso",caso,"es de",x,"formas posibles")
    else:
        print("Caso solicidato invalido")
### Pruebas Funciones ###
#ejDiezNueve(p = input("Cuantas hojas hay por rama?: "), k = input("Cuantas ramas hay por arbol?: "), t = input("Cuantas hojas quieres obtener?: "))
#ejVeinte(k = input("Ingrese el valor del prestamo: "), i = input("Ingrese el porcentaje de interes (Sin simbolos): "))
#ejVeinteUno(input("Ingrese el valor de n: "))