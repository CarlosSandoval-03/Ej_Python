from Ej23 import meterNumeros
#31. Suponga que un arreglo de enteros esta lleno de unos y ceros y que el arreglo representa un número binario al revés. Hacer un algoritmo que calcule los números
#en decimal que representa dicho arreglo de unos y ceros.
#Ejemplo.
#Entrada: (0, 1, 0, 1, 0, 1, 1) (representa el número 1101010).
#Salida: 106
#Ejemplo.
#Entrada: (1, 0, 0, 1, 0, 1, 1, 1, 1) (representa el número 111101001).
#Salida: 389
def ejTreintaUno(arreglo):
    meterNumeros(arreglo)
    if validacion(arreglo):
        arreglo.reverse()
    else:
        print("Por favor ingrese valores validos (0 y 1)")
    
def validacion(arreglo):
    for i in arreglo:
        if i == 0 or i == 1:
            a = True
            continue
        else:
            a = False
            break
    return a

def binario(arreglo):
    #print(0b1001) "Ob" es para base binaria no hay que hacer conversion
    a = None
    
def main():
    x = []
    ejTreintaUno(x)
    print(x)

if __name__ == "__main__":
    main()