'''
Ejercicio 2: Contador de Números Pares

Escribe un programa en Python que haga lo siguiente:

Solicitar al usuario un número entero positivo.
Contar la cantidad de números pares desde 0 hasta el número ingresado.
Mostrar en pantalla el resultado, indicando cuántos números pares se encontraron.


'''

num1 = int(input())
counter = 0

for i in range(0,num1+1):
    if (i%2==0):
        counter+=1

print(f"There are {counter} pair numbers between 0 and {num1}")        




