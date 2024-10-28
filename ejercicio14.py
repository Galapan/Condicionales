#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.

dia = int(input("Ingresa el día de la semana (1-7): "))

if dia < 1 or dia >7:
    print("Error")

if dia==1:
    print("Domingo")
elif dia==2:
    print("Lunes")
elif dia==3:
    print("Martes")
elif dia==4:
    print("Miercoles")
elif dia==5:
    print("Jueves")
elif dia==6:
    print("Viernes")
elif dia==7:
    print("Sabado")