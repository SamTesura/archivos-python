#Import and variables to define
from art import logo, vs
from game_data import data
from random import randint
import os

error_int = "ERROR! Intentelo de nuevo."

#Funciton to get a randum number
def random_number():
    ran_num = randint(0, len(data)-1)
    return ran_num

#Main program
def higher_lower():
    os.system('cls')    #Clear the screen
    print(logo)         
    score = 0

    ran_num_a = random_number()
    #Get a random artist form the list 'data'
    famous_a = data[ran_num_a]  

    while True:

        while True:         #Loop to avoid the same numbers in A and B
            ran_num_b = random_number()
            if ran_num_a != ran_num_b:
                break
        #Get a random artist form the list 'data'
        famous_b = data[ran_num_b]  

        #Numbers of followers for A and B from dictionary 'data'
        followers_a = famous_a["follower_count"]
        followers_b = famous_b["follower_count"]
        #Print A, B and a Vs. logo
        print(f'Compare A: {famous_a["name"]}, a {famous_a["description"]}, from {famous_a["country"]}')
        print(vs)
        print(f'Compare B: {famous_b["name"]}, a {famous_b["description"]}, from {famous_b["country"]}')
        
        while True:     #Loop to only accept A or B     
            game_question = input("\nWho has more followers? Type 'A' or 'B': ").lower()
            if game_question == "a" or game_question == "b":
                break
            else:
                print(error_int)
        #Comparision to see if answer is correct or not.
        if followers_a > followers_b and game_question == "a" or followers_a < followers_b and game_question == "b":
            score += 1
            famous_a = famous_b
            os.system('cls')    #Clear the screen
            print(logo)
            print(f"Your score is: {score}")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}\n")
            print(f'{famous_a["name"]} has {famous_a["follower_count"]}M followers, while {famous_b["name"]} has {famous_b["follower_count"]}M\n')
            break

    #THE FINAL QUESTION
    while True:     #Loop to only accpet 'y' o 'n'
        question = input("Would you like to play again? Type 'y' for yes, type 'n' to pass: ").lower()
        if question == "y" or question == "n":
            break
        else:
            error_int()

    if question == 'y':
        higher_lower()
        #Recursion. Call my function inside of itself to start again from scratch

#Call my function to start the program
higher_lower()

