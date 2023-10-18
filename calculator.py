'''
Ejercicio 1: Calculadora Simple

Escribe un programa en Python que actúe como una calculadora simple. El programa debe:

Solicitar al usuario dos números (pueden ser decimales) y una operación matemática (+, -, *, o /).
Realizar la operación seleccionada en los dos números ingresados.
Mostrar el resultado en pantalla.


'''

num1 = int(input())
num2 = int(input())
operator = str(input())

def operation(num1,num2,operator):
    match operator:
        case '+':
            print(num1+num2)
        case '-':
           print(num1-num2)
        case "*":
            print(num1*num2)
        case "/":
            print(num1/num2)
        case default:
            print("Please, insert a valid command.")

operation(num1,num2,operator)   