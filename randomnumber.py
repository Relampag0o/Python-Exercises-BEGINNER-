'''
Ejercicio 4: Juego de Adivinanza

Escribe un programa en Python para jugar un juego de adivinanza. El programa debe:

Generar un número secreto aleatorio entre 1 y 100.
Permitir al usuario hacer intentos para adivinar el número secreto.
Dar pistas al usuario indicando si el número secreto es mayor o menor que el intento actual.
Mostrar un mensaje de felicitación cuando el usuario adivine el número.
Contar y mostrar cuántos intentos le llevó al usuario adivinar el número.
'''


import random


properNumber=random.randint(1,100)
leftTryes = 5
guessed = False


while leftTryes>0 and not guessed:
    print("Insert one number: ")
    userNumber = int(input())


    if userNumber==properNumber:
        leftTryes-=1
        print("Congrats!!")
        guessed = True
    else:
        if userNumber>properNumber:
            print("HINT: The hidden number is smaller than yours.")
            leftTryes-=1
        else:
            print("HINT: The hidden number is bigger than yours.")
            leftTryes-=1

if leftTryes==0:
    print("You dont have more tryes.")
    exit



