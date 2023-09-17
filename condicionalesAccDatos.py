# 1.- Escribe un programa que pida dos números enteros y que calcule su división. 
# Indicará si la división es exacta o no. Debe funcionar igual que en los ejemplos.
# 2.- mejorar el programa para que no se pueda dividir entre 0. 
'''
print("Divisor de números")
print("Inserte el primer número: ")
num1=int(input())
print("Inserte el segundo número: ")
num2=int(input())


if num2==0:
    print("No se puede dividir entre 0. ")
else:    

    if num1%num2!=0:
        print("La división no es exacta. " + "Cociente: " + str(num1/num2) + " " + "Resto: " + str(num1%num2))
    else:
        print("La divisón es exacta." + " Cociente: " + str(num1/num2))

'''
# 3.- Escribe un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.


print("COMPARADOR DE NÚMEROS")
print("Inserte el primer numero")
num1 = input()

print("Inserte el segundo numero")
num2 = input()


