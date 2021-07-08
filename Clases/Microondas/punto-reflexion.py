import os

def error_int():
    print("ERROR! Intentelo de nuevo.")

while True:
    os.system('cls')
    

    while True:     #Loop to only accept floating
        h1 = input("h1: ")
        try: 
            h1 = float(h1)
            break
        except: error_int()

    while True:     #Loop to only accept floating
        h2 = input("h2: ")
        try: 
            h2 = float(h2)
            break
        except: error_int()

    while True:     #Loop to only accept floating
        d = input("d: ")
        try: 
            d = float(d)
            break
        except: error_int()

    k = (4/3)
    a = 6370

    c = (h1-h2)/(h1+h2)
    print(f"c = {c}")
    m = (((d)**2)/(4*k*a*((0.001*h1)+(0.001*h2))))
    print(f"m = {m}")

    while True:     #Loop to only accept floating
        b = input("Buscar el parámetro b en la tabla. b : ")
        try: 
            b = float(b)
            break
        except: error_int()

    d1 = (d/2)*(1+b)
    print(f"d1 = {d1}")
    d2 = (d/2)*(1-b)
    print(f"d2 = {d2}")

    #THE FINAL QUESTION
    while True:     #Loop to only accpet 'y' o 'n'
        question = input("Would you like to play again? Type 'y' for yes, type 'n' to pass: ").lower()
        if question == "y" or question == "n":
            break
        else:
            error_int()

    if question == 'n':
        break