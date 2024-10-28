# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

N1 = int(input("Ingresa el primer número: "))
N2 = int(input("Ingresa el segundo número: "))
D = N1/N2

if N2 == 0:
    print("El segundo número es 0")
else:
    print(f'La división es: { D }')
