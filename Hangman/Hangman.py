import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for x in range(0,len(chosen_word)):
    display.append("_")
print(" ".join(display))

lives = 6
guess_list = []

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    i = 0

    if guess not in chosen_word:
        lives -= 1
        print(f'The letter "{guess}" is incorrect. Please try again')
    elif guess in chosen_word:
        for x in chosen_word:
            if guess == x:
                display[i] = guess
            i += 1
        if guess in guess_list:
            print(f'The letter "{guess}" has already been entered. Please try again')
        guess_list += guess

    print(" ".join(display))
    print(stages[lives])

if lives == 0:
    print("You lose.")
else:
    print("You win!")
