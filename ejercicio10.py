#Programa que pida tres números y los muestre ordenados (de mayor a menor);

N1 = int(input("Ingresa el primer número: "))
N2 = int(input("Ingresa el segundo número: "))
N3 = int(input("Ingresa el tercer número: "))

if N1 >= N2 and N1 >= N3:
    if N2 >= N3:
        print("Orden de mayor a menor:", N1, N2, N3)
    else:
        print("Orden de mayor a menor:", N1, N3, N2)
elif N2 >= N1 and N2 >= N3:
    if N1 >= N3:
        print("Orden de mayor a menor:", N2, N1, N3)
    else:
        print("Orden de mayor a menor:", N2, N3, N1)
else:
    if N1 >= N2:
        print("Orden de mayor a menor:", N3, N1, N2)
    else:
        print("Orden de mayor a menor:", N3, N2, N1)