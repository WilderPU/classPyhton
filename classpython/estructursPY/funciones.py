"""
Las funciones son bastantes cheveres para trabajar, con estas nos ahorramso grandes cantidades de lineas
de codigos que pueden ser repetitivas. Estas permiten tener mejor estructurado el código y permite una mejor
lectura de este.
"""
# Para definir una funcion se utiliza la palabra reservada def
def heloword():
    print("Esta funcion es muy simpre y muestra este mensaje al ser llamada")

def suma(a,b):
    print(f"Esta funcion recibe do parametros, estos son 'a={a}' y 'b?{b}' y al final se suman, porque esta funcion es para suma: {a+b}")

def multiplesParametros(*a, otro="Fin"):
    print("Estos son los elementos que recibió la funcion:")
    for i in a:
        print("- ", i)

def parametrosdififerentes(**a):
    for i, j in a.items():
        print(f"Objeto: {i}. Caracterista: {j}.")

def menu():
    print("MENU DE FUNCIONES")
    print("1. Funcion normal/sencilla")
    print("2. Funcion que recibe parametro")
    print("3. Funcion que recibe varios parametros en una misma variable")
    print("4. Funcion que recibe varios diccionarios en el parametros")
    op =int(input("Ingrese el numero de la funcion que desee ver: "))
    if op==1:
        heloword()
    elif op==2:
        suma(12, 3)
    elif op==3:
        multiplesParametros("Carro", "Gato", "Perro", "Sandalia", otro="Otro objeto")
    elif op==4:
        parametrosdififerentes(Carro="Rojo", Perro="Grande",Camisa="Talla M")
    else:
        print("No es la opcion de alguna de las funciones")
        menu()
    menu()

menu()

    