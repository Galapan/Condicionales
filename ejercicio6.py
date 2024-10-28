# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

user = input("Ingresa el usuario: ")
password = input("Ingresa la contraseña: ")

if user=="pepe" and password=="asdasd":
    print("El usuario es correcto")
else:
    print("Alguno de los datos es incorrecto")
