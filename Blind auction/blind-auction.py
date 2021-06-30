
from art import logo
import os
os.system('cls')    #Me sireve para limpiar el terminal en Python
print(logo)

dic = {}
error_int = "ERROR! Intentelo de nuevo."

while True:
     
    name = input("What is your name: ")

    while True:
        bid = input("What's your bid?: $")
        try: 
            bid = int(bid)
            break
        except:
            print(error_int)

        # if type(bid) == int:
        #     break
        # else:
        #     print(error_int)

    dic.update({name : bid})        #Añado el nombre como key y el vid como value en el diccionatio dic

    while True:
        final_question = input("Are there any other bidders? Type 'Yes' or 'No' \n").lower()
        if final_question == "yes" or final_question == "no":
            break
        else:
            print(error_int)

    if final_question == 'no':
        break
    else:
        os.system('cls')

# max_key = max(a_dictionary, key=a_dictionary.get)
max_key = max(dic, key=dic.get)
max_value = dic[max_key]

os.system('cls')
print(f"The winner is {max_key.capitalize()} with a bid of ${max_value}")
