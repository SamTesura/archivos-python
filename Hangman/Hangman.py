import random
from hangman_art import stages, logo
from hangman_words import word_list

while True:
    #Elijo una palabra aleatoria de 'word_list'
    chosen_word = random.choice(word_list)

    print(logo)
    #Printea la solucion. Comentado
    # print(f'Pssst, the solution is {chosen_word}.')

    display = []        #Declaro a 'display' como una lista vacía
    
    #Evalúo el tamaño de la palabra a descubrir, y la represento con la misma cantidad 
    # de underscores '_' 
    for x in range(0,len(chosen_word)):
        display.append("_")
    print(" ".join(display))

    lives = 6           #Declaro a 'lives' como un integer con valor 6
    guess_list = []     #Declaro a 'guess_list' como una lista vacía

    #Mientras queden underscores '_' en displays, todavía no ha ganado
    #Mientras queden vidas en 'lives', todavía no ha perdido
    while "_" in display and lives > 0:
        guess = input("Guess a letter: ").lower()       #convierto la letra introducida en minuscula
        i = 0           #Declaro a 'i' como un integer con valor 0

        #si la letra es incorrecta, reduce la vida por 1
        if guess not in chosen_word:
            lives -= 1
            print(f'The letter "{guess}" is incorrect. Please try again')
        
        #si la letra es correcta, cambia el underscore en la posicion correspondiente por dicha letra
        elif guess in chosen_word:
            for x in chosen_word:
                if guess == x:
                    display[i] = guess
                i += 1
            
            #Si la letra ya ha sido introducida, se lo deja saber al usuario, pero no penaliza
            if guess in guess_list:
                print(f'The letter "{guess}" has already been entered. Please try again')
            guess_list += guess

        print(" ".join(display))
        print(stages[lives])

    if lives == 0:
        print("You lose.")
    else:
        print("You win!")

    #Pregunto si quiere terminar el programa o continuar
    final_question = input("Would you like to play again? Type 'Yes' or 'No' \n").lower()
    if final_question == 'no':
        print("Goodbye!")
        break