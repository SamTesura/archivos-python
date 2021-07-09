import os
def logo ():
    print("""

            _                                _           
      /\/\ (_) ___ _ __ ___   ___  _ __   __| | __ _ ___ 
     /    \| |/ __| '__/ _ \ / _ \| '_ \ / _` |/ _` / __|
    / /\/\ \ | (__| | | (_) | (_) | | | | (_| | (_| \__ \

    \/    \/_|\___|_|  \___/ \___/|_| |_|\__,_|\__,_|___/
                                                        

    """)

def error_int():
    print("ERROR! Intentelo de nuevo.")

def punto_reflexion():
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
    print(f"\nc = {c}")
    m = (((d)**2)/(4*k*a*((0.001*h1)+(0.001*h2))))
    print(f"m = {m}")

    while True:     #Loop to only accept floating
        b = input("\nBuscar el parámetro b en la tabla. b : ")
        try: 
            b = float(b)
            break
        except: error_int()

    d1 = (d/2)*(1+b)
    print(f"\nd1 = {d1}")
    d2 = (d/2)*(1-b)
    print(f"d2 = {d2}")

    #THE FINAL QUESTION
    while True:     #Loop to only accpet 'si' o 'no'
        question = input("\nQuieres buscar el punto de reflexión nuevamente?\nEscribe 'si' o 'no': ").lower()
        if question == "si" or question == "no":
            break
        else:
            error_int()

    if question == 'si':
        punto_reflexion()
        #Recursion. Call my function inside of itseld to start again from scratch




while True:     #Loop to only accpet 'si' o 'no'
    os.system('cls')
    logo()
    question = input("\nQuieres buscar el punto de reflexión entre dos puntos?\nEscribe 'si' o 'no': ").lower()
    if question == "si" or question == "no":
        break
    else:
        error_int()

if question == 'si':
    punto_reflexion()
    #Start the program