import os
from assets import logo

os.system('cls')
#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def sub(n1, n2):
    return n1 - n2

#Multiply
def mult(n1, n2):
    return n1 * n2
#Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

error_int = "ERROR! Intentelo de nuevo."

def calculator():           #Defino mi funcion calculator
    os.system('cls')        #Limpio la pantalla
    print(logo)

    while True:             #Creo un bloqueo para que solo puedan entrar numeros (float)
        num1 = input("What's the first number?: ")
        try: 
            num1 = float(num1)
            break
        except:
            print(error_int)
        

    for x in operations:    #Navego por el dictionario 'operations' e imprimo los keys
        print(x)

    while True:             #Mantengo mi programa corriendo mientras se quiera seguir con el mismo resultado

        while True:
            op_sym = input("Pick an operation: ")
            if op_sym in operations:
                break
            else:
                print(error_int)

        while True:         #Creo un bloqueo para que solo puedan entrar numeros (float)
            num2 = input("What's the next number?: ")
            try: 
                num2 = float(num2)
                break
            except:
                print(error_int)

        result = operations[op_sym](num1, num2)

        print(f"{num1} {op_sym} {num2} = {result}")

        while True:     #Bucle para solo aceptar 'y' o 'n'
            final_question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            if final_question == "y" or final_question == "n":
                break
            else:
                print(error_int)
        
        if final_question == 'n':
            calculator()
        else:
            num1 = result
            os.system('cls')

calculator()