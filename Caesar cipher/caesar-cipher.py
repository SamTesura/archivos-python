from assets import logo, caesar
import os
os.system('cls')
print(logo)

while True:

    #Entradas
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Si 'shift' se pasa de la cantidad de letras, me mantengo restáandole 26 hasta que sea
    # menor que la cantidad de letras. Esta va a coicidir con la posición de la misma manera 
    # que si le diera vueltas a 'alphabet'
    while shift > 26:
        shift = shift - 26

    #Llamo a la función 'caesar' con sus parámetros.
    caesar(text, shift, direction)

    #Mientras la variable 'final_question' no diga 'yes' o 'no' se mantiene preguntando
    while True:
        final_question = input("Would you like to continue? Type 'Yes' or 'No' \n").lower()
        if final_question == "yes" or final_question == "no":
            break
    #Pregunto si quiere terminar el programa o continuar
    if final_question == 'no':
        print("Goodbye!")
        break