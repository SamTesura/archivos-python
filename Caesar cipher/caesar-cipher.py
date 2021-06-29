from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r = 0
while r == 0:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        r = 1

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_1, shift_1, direction_1):
    i = 0
    z = ""
    for x in text_1:
        i = alphabet.index(x)
        if direction_1 == "encode":
            i += shift_1
            z += alphabet[i]
        elif direction_1 == "decode":
            i -= shift_1
            z += alphabet[i]
            
    if direction_1 == "encode":
        print(f"The encoded text is {z}")
    elif direction_1 == "decode":
        print(f"The decoded text is {z}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar()
# function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

#TODO-2: What if the user enters a shift that is greater than the number of letters in the
# alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number
# greater than 26. 
#Hint: Think about how you can use the modulus (%).




caesar(text, shift, direction)