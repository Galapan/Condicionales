# Realiza un programa que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Ingresa la base: "))
exp = int(input("Ingresa el exponente: "))

if exp>0:
    r = base ** exp
    print(f'El resultado es: { r }')
elif exp==0:
    print("El resultado es 1")
else:
    r = 1/(base ** abs(exp))
    print(f'El resultado es { r }')
