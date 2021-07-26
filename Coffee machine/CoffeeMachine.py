from assets import Logo, MENU, resources
import os # os.system('cls')

ERROR_MSG = ">> ERROR! Please try again.\n"

options = """
------------------------ 
What would you like?

1. Espresso-------$1.50
2. Latte----------$2.50
3. Cappuccino-----$3.00\n"""

options_list = ["espresso", "latte", "capuccino", "report", "off"]

money = 0

#Funciones auxiliares
#------------------------------------------------------------------------------------
def input_int(msg):
    while True:
        x = input(msg)
        try:                #Loop to only accept floating
            return int(x)
        except ValueError:
            print(ERROR_MSG)

#Check resources sufficient
def check_resources(water_check, milk_check, coffee_check):
    if resources["water"] < water_check:
        print("Sorry there is not enough water.")
    elif resources["milk"] < milk_check:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < coffee_check:
        print("Sorry there is not enough coffee.")  
    else:     
        return False
    return True
    
#Process coins. Input how many of each coins were inserted
def insert_coins():
    global total_inserted

    quarters = input_int("How many quarters?: ")
    dimes = input_int("How many dimes?: ")
    nickles = input_int("How many nickles?: ")
    pennies = input_int("How many pennies?: ")

    total_inserted = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return

#Check if has enough money. Transaction successful
def check_coins(coins_check, drink):
    global money

    if total_inserted < coins_check:
        print("Sorry that's not enough money. Money refunded")
        coffee_machine()
    else:
        money += coins_check
        change = total_inserted -  coins_check
        print(f"\nHere is ${round(change,2)} dollars in change.")
        print(f"Here is your {drink}. Enjoy!")
        return

#If everything is ok, make the coffee
def make_coffee(water_check, milk_check, coffee_check):
    #TODO 7: Make Coffee.
    resources["water"] -= water_check
    resources["milk"] -= milk_check
    resources["coffee"] -= coffee_check

#------------------------------------------------------------------------------------

#Programa principal
def coffee_machine():
    
    #Prompt user by asking “ What would you like?
    while True:     #Loop to only accept floating
        print(options)
        question = input(">> ").lower()
        
        if question not in options_list:
            print(ERROR_MSG)
        else: break

    if  question in options_list[0:2]:      #Check if is espresso/latte/cappuccino
        if check_resources(MENU[question]["ingredients"]["water"], MENU[question]["ingredients"]["milk"], MENU[question]["ingredients"]["coffee"]):
            coffee_machine()
        insert_coins()
        check_coins(MENU[question]["cost"], question.capitalize())
        make_coffee(MENU[question]["ingredients"]["water"], MENU[question]["ingredients"]["milk"], MENU[question]["ingredients"]["coffee"])

    #Report
    elif question == "report":
        print(f"""
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${money}
        """)
    #Turn off the Coffee Machine by entering “ off ” to the prompt.
    elif question == "off":
        exit()

    coffee_machine()


os.system('cls')        #Clean the screen
print(Logo)
coffee_machine()        #Call main program