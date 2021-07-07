import random 
import os
from assets import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def error_int():
    print("ERROR! Intentelo de nuevo.")

#######################################################    

def blackjack():
    os.system('cls')
    print(logo)

    #Asigno 2 cartas aeatorias al usuario
    cards_user = [random.choice(cards), random.choice(cards)]
    total_user = sum(cards_user)
    #Verifico si las dos son 11 y hago que una de ellas valga 1
    if cards_user[0] == 11 and cards_user[1] == 11:
        cards_user[0] = 1
        total_user = sum(cards_user)

    #Asigno 2 cartas aeatorias al dealer
    cards_pc = [random.choice(cards), random.choice(cards)]
    total_pc = sum(cards_pc)
    #Verifico si alguno de los dos tiene Blackjack. Si son ambos, gana PC
    if total_pc == 21:
        print("Lose with a Blackjack 💀")
        return
    elif total_user == 21:
        print("Win with a Blackjack 😎")
        return

    #Muestro los valores de user y la primera carta de PC
    print(f"    Your cards: {cards_user}, current score: {total_user}")
    print(f"    Computer's first card: {cards_pc[0]}")
    
    while True:
        #si el user paso 21, pierde 
        if total_user > 21:
            break
        while True:     #Bucle para solo aceptar 'y' o 'n'
            #Pregunto al user si desea coger otra carta
            question = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if question == "y" or question == "n":
                break
            else:
                error_int()
        #si el user quiere otra carta, se les suma a las anteriores
        if question == "y":
            new_card_user = random.choice(cards)
            #Si la nueva carta es ACE, verifico si total_user es mayor que 21 para que valga 1, de lo contrario vale 11.
            if new_card_user == 11 and total_user > 11:
                cards_user.append(1)
            else:
                cards_user.append(new_card_user)

            total_user = sum(cards_user)
            print(f"    Your cards: {cards_user}, current score: {total_user}")
            print(f"    Computer's first card: {cards_pc[0]}")
        #si el user no quiere otra carta, continua
        else:
            break
    #Si el dealer tiene menos de 17, continua cogiendo cartas
    if total_pc < 17:
            new_card_pc = random.choice(cards)
            #Si la nueva carta es ACE, verifico si total_pc es mayor que 21 para que valga 1, de lo contrario vale 11.
            if new_card_pc == 11 and total_pc > 11:
                cards_pc.append(1)
            else:
                cards_pc.append(new_card_pc)

            total_pc = sum(cards_pc) 
    
    #Comparacion final para ver cual es si el ganador es el user, el dealer o empate
    while True:
        if total_user > 21:
            print(f"Your final hand: {cards_user}, final score: {total_user}")
            print("You lose")
            break
        elif total_pc > 21:
            print(f"Your final hand: {cards_user}, final score: {total_user}")
            print(f"Computer's final hand: {cards_pc}, final score: {total_pc}")
            print("You win!")
            break                      
        elif total_user < total_pc  or total_user > 21:
            print(f"Your final hand: {cards_user}, final score: {total_user}")
            print(f"Computer's final hand: {cards_pc}, final score: {total_pc}")
            print("You lose")
            break
        elif total_user > total_pc or  total_pc > 21:
            print(f"Your final hand: {cards_user}, final score: {total_user}")
            print(f"Computer's final hand: {cards_pc}, final score: {total_pc}")
            print("You win!")
            break
        elif total_user == total_pc:
            print(f"Your final hand: {cards_user}, final score: {total_user}")
            print(f"Computer's final hand: {cards_pc}, final score: {total_pc}")
            print("It's draw!")
            break

    #THE FINAL QUESTION
    while True:     #Bucle para solo aceptar 'y' o 'n'
        question = input("Would you like to play again? Type 'y' for yes, type 'n' to pass: ").lower()
        if question == "y" or question == "n":
            break
        else:
            error_int()

    if question == 'y':
        blackjack()

blackjack()