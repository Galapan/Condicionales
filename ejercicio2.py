N1 = int(input("Ingresa el primer número: "))
N2 = int(input("Ingresa el segundo número: "))
if N1 == N2:
    print("Ambos número son iguales")
elif N1 > N2:
    print(f'El { N1 } es mayor')
else:
    print(f'El { N2 } es mayor')