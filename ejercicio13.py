#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".

cd = int(input("Ingresa la cara del dado (1-6): "))

if cd<1 or cd>6:
    print("ERROR: número incorrecto.")
else:
    if cd == 1:
        print("Su cara opuesta es 6")
    elif cd == 6:
        print("Su cara opuesta es 1")
    elif cd == 2:
        print("Su cara opuesta es 5")
    elif cd == 5:
        print("Su cara opuesta es 2")
    elif cd == 3:
        print("Su cara opuesta es 4")
    elif cd == 4:
        print("Su cara opuesta es 3")