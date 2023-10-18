'''
scribe un programa en Python que realice lo siguiente:

Solicitar al usuario que ingrese su nombre.
Solicitar al usuario que ingrese su edad.
Convertir la edad ingresada en un número entero.
Verificar si la edad es mayor o igual a 18 años.
Si la edad es mayor o igual a 18, mostrar un mensaje que diga "Nombre, eres mayor de edad." donde "Nombre" es el nombre ingresado por el usuario.
Si la edad es menor a 18, mostrar un mensaje que diga "Nombre, eres menor de edad.".


'''

print("Insert your name: ")
name = input()
print("Insert your age: ")
age = int(input())

if (age < 18):
    print(f"{name.capitalize()}, you are not 18 yet.")
else:
    print(f"{name.capitalize()}, you are over 18.")
