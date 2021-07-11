import os

def logo ():
    print("""
                 _           _       _     _                  _             
        /\      | |         (_)     (_)   | |                (_)            
       /  \   __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _  ___ _  ___  _ __  
      / /\ \ / _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ __| |/ _ \| '_ \ 
     / ____ \ (_| | | | | | | | | | | \__ \ |_| | | (_| | (__| | (_) | | | |
    /_/    \_\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\___|_|\___/|_| |_|
    
    """)

def error_int():
    print("ERROR! Intentelo de nueValor_prestamo.")



def calculos():
    os.system('cls')
    logo()

    print("""
    Ejemplo:
    Fulanito solicita un préstamo en el banco por un valor de 500k a 5 años a una tasa del 12% y ella tiene un
    ingreso de 60k. Determine la cuota de capital en interés a pagar mensualmente y su capacidad de pago

    """)

    while True:
        valor_prestamo = input("Valor del prestamo: ")
        try:            #Loop to only accept floating
            valor_prestamo = float(valor_prestamo)
            break
        except: error_int()

    while True:
        tiempo_prestamo = input("Tiempo en años: ")
        try:            #Loop to only accept floating
            tiempo_prestamo = float(tiempo_prestamo)
            break
        except: error_int()

    while True:
        tasa = input("Tasa: ")
        try:            #Loop to only accept floating
            tasa = float(tasa)
            break
        except: error_int()
    
    while True:
        ingreso = input("Ingresos: ")
        try:            #Loop to only accept floating
            ingreso = float(ingreso)
            break
        except: error_int()

    meses_ano = 12
    meses_prestamo = tiempo_prestamo * meses_ano
    capital_pagar = valor_prestamo / meses_prestamo
    tasa_mensual = (tasa*0.01) / meses_ano
    int_mensual = valor_prestamo * tasa_mensual
    cuota_cap = int_mensual + capital_pagar
    capacidad_pago = cuota_cap/ingreso

    os.system('cls')

    print(f"""
    DATOS
    ___________________________________________________________________
    Valor del prestamo = ${valor_prestamo}
    Tiempo del prestamo = {int(tiempo_prestamo)} año(s)
    Tasa del prestamo = {tasa}%
    Ingresos del cliente = ${ingreso}


    RESULTADOS
    ___________________________________________________________________
    Meses durante el prestamo =
    = Tiempo del prestamo • 12 meses = {int(meses_prestamo)}
    
    Capital a pagar por el prestamo =
    = Valor del prestamo / Meses durante el prestamo = {capital_pagar}
    
    Tasa mensual =
    = Tasa / 12 meses = {tasa_mensual} = {tasa_mensual*100}%
    
    Interes mensual a pagar =
    = Valor del prestamo • Tasa mensual = {int_mensual}
    
    CUOTA DE CAPITAL E INTERES A PAGAR =
    = Interes mensual a pagar + Capital a pagar por el prestamo = {cuota_cap}
    
    CAPACIDAD DE PAGO =
    Cuota de capital e interes a pagar / Ingresos = {capacidad_pago} = {capacidad_pago*100}%
    
    """)

    #THE FINAL QUESTION
    while True:     #Loop to only accpet 'y' o 'n'
        question = input("¿Hacer el calculo nuevamente? Escribe 'si' o 'no': ").lower()
        if question == "si" or question == "no":
            break
        else:
            error_int()

    if question == 'si':
        calculos()
        #Recursion. Call my function inside of itseld to start again from scratch

# os.system('cls')
# logo()
calculos()
