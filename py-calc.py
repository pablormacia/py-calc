#Calculadora básica, por Pablo Macia

#Funciones de operaciones:
def sumar(a,b): return a+b
def restar(a,b): return a-b
def multiplicar(a,b): return a*b
def dividir(a,b):
    if b==0:
        return "Lo siento, no se puede dividir por cero"
    resultado = a/b
    if resultado.is_integer():
        return int(resultado)
    return resultado

def ingresar_y_validar():
    a=input("Ingresá el primer valor: ")
    b=input("Ingresá el segundo valor: ")
    try:
        a = float(a)
        if a.is_integer():
            a = int(a)
        b = float(b)
        if b.is_integer():
            b=int(b)
        return a,b
    except ValueError:
        return False



print("¡Bienvenidos a la calculadora básica de Python!\n(Utilizá puntos para números decimales)\n")

menu = "Elegí una opción y presioná enter:\na. Sumar\nb. Restar\nc. Multiplicar\nd. Dividir\ne. Salir\nTu opción: "

choise = None

while choise!="e":
    choise = input(menu)
    if choise == "a":
        try:
            a,b = ingresar_y_validar()
            resultado = sumar(a,b)
            print(f"\nResultado de la suma: {resultado}\n")
        except:
            print("\nPor favor, ingresá valores numéricos\n")
    elif choise == "b":
        try:
            a,b = ingresar_y_validar()
            resultado = restar(a,b)
            print(f"\nResultado de la resta: {resultado}\n")
        except:
            print("\nPor favor, ingresá valores numéricos\n")
    elif choise == "c":
        try:
            a,b = ingresar_y_validar()
            resultado = multiplicar(a,b)
            print(f"\nResultado de la multiplicación: {resultado}\n")
        except:
            print("\nPor favor, ingresá valores numéricos\n")   
    elif choise == "d":
        try:
            a,b = ingresar_y_validar()
            resultado = dividir(a,b)
            print(f"\nResultado de la división: {resultado}\n")
        except:
            print("\nPor favor, ingresá valores numéricos\n")   
    elif choise == "e":
        print("\n¡Gracias por utilizar la calculadora básica de Python! Te esperamos pronto\n")
        break
    else:
        print("\nLo siento, seleccioná alguna de las opciones del menú\n")