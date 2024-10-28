#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

chain = input("Ingresa la cadena de texto: ")

if chain == chain.upper() and chain.isalpha():
    print("Una letra es mayúscula")
else:
    print("No hay niguna mayúscula")

