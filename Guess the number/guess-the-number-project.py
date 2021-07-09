import random
import os
from assets import logo

def error_int():
    print("ERROR! Intentelo de nuevo.")

def win(the_correct_number):
    print(f"\nYou got it! The answer was {the_correct_number}.\nt")

def lose():
    print("\nYou've run out of guesses, you lose.\n")


#-----------------------------------------------------------------

#Main program
def guess_the_number():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    #Randomly chose a number between 1 and 100. The correct answer
    the_number = random.randint(1, 100)

    while True:     #Loop to only accpet 'y' o 'n'
        dif_question = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
        if dif_question == "easy" or dif_question == "hard":
            break
        else:
            error_int()

    #Difficulty. Hard: 5 attempts, Easy: 10 attempts
    if dif_question == 'easy':
        attempts = 10
    elif dif_question == 'hard':
        attempts = 5

    while True:
        print(f"You have {attempts} attempts remaining to guess the number.\n")
        
        while True:     #Loop to only accept numbers
            guessed = input("Make a guess: ")
            try: 
                guessed = int(guessed)
                break
            except:
                error_int()


        #comparison to see if it's equal to the correct answer or not
        #if guessed the answer wins
        if guessed == the_number:
            win(the_number)
            break
        #Lose a life if incorrect
        elif guessed != the_number:
            attempts -= 1  
            if guessed > the_number:
                print("\nToo high.")
            elif guessed < the_number:
                print("\nToo low.")
        #If has no more attempts, lose
        if attempts != 0:
            print("\nGuess again")
        else:
            lose()
            break

    #THE FINAL QUESTION
    while True:     #Loop to only accpet 'y' o 'n'
        question = input("Would you like to play again? Type 'y' for yes, type 'n' to pass: ").lower()
        if question == "y" or question == "n":
            break
        else:
            error_int()

    if question == 'y':
        guess_the_number()
        #Recursion. Call my function inside of itseld to start again from scratch
            
#Call my function. Main program            
guess_the_number()
