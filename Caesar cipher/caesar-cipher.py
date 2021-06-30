from art import logo, caesar

print(logo)

e = True
while e == True:
    r = True
    while r == True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            r = False

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    while shift > 26:
        shift = shift - 26

    caesar(text, shift, direction)

    final_question = input("Would you like to continue? Type 'Yes' or 'No' \n").lower()
    if final_question == 'no':
        e = False