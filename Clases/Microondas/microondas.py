import os
import math

def logo ():
    print("""

            _                                _           
      /\/\ (_) ___ _ __ ___   ___  _ __   __| | __ _ ___ 
     /    \| |/ __| '__/ _ \ / _ \| '_ \ / _` |/ _` / __|
    / /\/\ \ | (__| | | (_) | (_) | | | | (_| | (_| \__ \

    \/    \/_|\___|_|  \___/ \___/|_| |_|\__,_|\__,_|___/
                                                        

    """)

def error_int():
    print(" ERROR! Intentelo de nuevo.")


#  ___  __   __                        __  
# |__  /  \ |__)  |\/| |  | |     /\  /__` 
# |    \__/ |  \  |  | \__/ |___ /~~\ .__/ 
                                         
#***Fórmulas de perdida espacio libre***
def d_max_formula():
    print("\nDmax = 4.12•[√(h1)+√(h2)]")

def lo_formula():
    print("\nLo dB = 32.5+20•log(d(km))+20•log(f(GHz))")

def ptx_dbm_formula():
    print("\nP(dBm) = 10•log10(1000•Ptx)")

def prx_formula():
    print("Prx(dBm) = Ptx(dbm) + Gtx(dB) + Grx(dB) - Lo(dB)")

#***Fórmulas de punto de reflexión***
def c_formula():
    print("""
        (h1-h2)
    c = -------
        (h1+h2)
    """)

def m_formula():
    print("""
                (d^2)
    m = -----------------------------
        4•k•a•((0.001•h1)+(0.001•h2))
    """)

def b_formula():
    print("""
            c
    b = -------------   o buscar en la tabla         
        [1+m•√(1-c2)]
    """)

def d1_formula():
    print("\nd1 = (d/2)*(1+b)")

def d2_formula():
    print("\nd2 = (d/2)*(1-b) o d2 = d-d1\n")

#Fórmulas del análisis de Fresnel
def rf_formula():
    print("""
              ___________
             / n•λ•d1•d2
    Rf = \  /  ---------
          \/     d1+d2  
    """)

def l_ambda_formula():
    print("λ = C/f")

#  ___            ___  __   __                        __  
# |__  | |\ |    |__  /  \ |__)  |\/| |  | |     /\  /__` 
# |    | | \|    |    \__/ |  \  |  | \__/ |___ /~~\ .__/ 


#***Menú de selección***
def the_question():
    while True:     #Loop to only accept floating
        question = input("""
    ------------------------------------------------------------------   
    SELECCIONE SU CÁLCULO DESEADO:
    1. Linea de vista, perdida en el espacio libre y punto de recepción
    2. Punto de reflexión
    3. Análisis de fresnel
    0. Salir
    """)
        try: 
            question = int(question)
            break
        except: error_int()
    if  question == 1:
        perdida_espaciolibre()
    elif question == 2:
        punto_reflexion()
    elif question == 3:
        analisis_fresnel()
    elif question == 0:
        return
    else:
        error_int()
        the_question()
#***Fin de Menú de selección***


#  __   __   __   __   __                   __  
# |__) |__) /  \ / _` |__)  /\   |\/|  /\  /__` 
# |    |  \ \__/ \__> |  \ /~~\  |  | /~~\ .__/ 
                                              
#__________________Linea de vista, perdida en el espacio libre y punto de recepción__________________
def perdida_espaciolibre():
    os.system('cls')
    #Perdida en el espacio libre. Datos
   
    #Altura del punto 1
    while True:
        h1 = input("h1 (mts): ")
        try:            #Loop to only accept floating
            h1 = float(h1)
            break
        except: error_int()
    #Altura del punto 1
    while True:     
        h2 = input("h2 (mts): ")
        try:            #Loop to only accept floating
            h2 = float(h2)
            break
        except: error_int()

    #Linea de vista
    d_max = 4.12*(math.sqrt(h1)+math.sqrt(h2))
    d_max_formula()
    print(f"Dmax = {d_max} Kms. *Linea de vista*\n")
    
    #Distancia desde el punto 1 hasta el punto 2
    while True:     
        d = input("d (Km): ")
        try:            #Loop to only accept floating
            d = float(d)
            break
        except: error_int()
    #Frecuencia
    while True:
        f = input("frecuencia (GHz): ")
        try:            #Loop to only accept floating
            f = float(f)
            break
        except: error_int()    
    
    #Pérdida en el espacio libre
    lo = 32.5+20*math.log10(d)+20*math.log10(f*1000)
    lo_formula()
    print(f"Lo dB = {lo} dB\n")
    
    while True:
        ptx = input("Potencia de la antena emisora (Watts): ")
        try:            #Loop to only accept floating
            ptx = float(ptx)
            break
        except: error_int()  
 
    while True:
        gtx = input("Ganancia de la antena transmisora (dB): ")
        try:            #Loop to only accept floating
            gtx = float(gtx)
            break
        except: error_int() 

    while True:
        grx = input("Ganancia de la antena receptora (dB): ")
        try:            #Loop to only accept floating
            grx = float(grx)
            break
        except: error_int() 
    
    #Potencia del emisor en dBm
    ptx_dbm = 10*math.log10(1000*ptx)
    ptx_dbm_formula()
    print(f"Ptx en dBm = {ptx_dbm}\n")
    #Potencia del receptor
    prx = ptx_dbm + gtx + grx - lo
    prx_formula()
    print(f"Prx = {prx} dBm")

    #THE FINAL QUESTION
    the_question()

#_________________________________________Punto de reflexión__________________________________________
def punto_reflexion():
    os.system('cls')
    #Punto de reflexión. Datos

    #Altura del punto 1
    while True:
        h1 = input("h1 (mt): ")
        try:            #Loop to only accept floating
            h1 = float(h1)
            break
        except: error_int()
    #Altura del punto 1
    while True:     
        h2 = input("h2 (mt): ")
        try:            #Loop to only accept floating
            h2 = float(h2)
            break
        except: error_int()
    #Distancia desde el punto 1 hasta el punto 2
    while True:     
        d = input("d (Km): ")
        try:            #Loop to only accept floating
            d = float(d)
            break
        except: error_int()

    k = (4/3)
    a = 6370

    #_____CÁLCULOS_____TO SHOW AND COPY_____
    os.system('cls')
    print(f"h1: {h1} mts \nh2: {h2} mts \nd: {d} kms\n")

    #Cálculo de c
    c = (h1-h2)/(h1+h2)
    c_formula()
    print(f"c = {c}")
    #Cálculo de m
    m = (((d)**2)/(4*k*a*((0.001*h1)+(0.001*h2))))
    m_formula()
    print(f"m = {m}")
    #Cálculo de b o buscar en la tabla
    b = c/(1+m*(math.sqrt(1-(c**2))))
    b_formula()
    print(f"b = {c}\n")
    #Cálculo de d1
    d1 = (d/2)*(1+b)
    d1_formula()    
    print(f"d1 = {d1} Km\n")
    #Cálculo de d2    
    d2 = (d/2)*(1-b)
    d2_formula()
    print(f"d2 = {d2} Km")

    #THE FINAL QUESTION
    the_question()

#_________________________________________Análisis de Fresnel_________________________________________
def analisis_fresnel():
    os.system('cls')
    #Análisis de Fresnel. Datos

    #Entrada de la distancia total
    while True:
        d = input("d (Km): ")
        try:            #Loop to only accept floating
            d = float(d)
            break
        except: error_int()
    #Entrada del punto más alto
    while True:
        h_max = input("Punto más alto (mt): ")
        try:            #Loop to only accept floating
            h_max = float(h_max)
            break
        except: error_int()
    #Entrada de la distancia desde el punto de transmisión hasta el punto mas alto
    while True:
        d1_ = input("d1 (Km) (fresnel): ")
        try:            #Loop to only accept floating
            d1_ = float(d1_)
            break
        except: error_int()

    #distancia desde el punto de mas alto hasta el punto de recepción
    d2_ = d - d1_
    print(f"d2 (km) (fresnel): {d2_}")

    #Entrada de la frecuencia
    while True:
        f = input("frecuencia (GHz): ")
        try:            #Loop to only accept floating
            f = float(f)
            break
        except: error_int()

    #_____CÁLCULOS_____TO SHOW AND COPY_____
    os.system('cls')
    print(f"d: {d} kms \nPunto más alto: {h_max} mts \nd1: {d1_} kms \nd2: {d2_} kms \nfrecuencia: {f} GHz\n") 

    c = 300000000
    n = 1
    d *= 1000
    d1_ *= 1000
    d2_ *= 1000
    #Cálculo de lambda
    l_ambda_formula()
    l_ambda = c / (f*1000000000)
    print(f"λ = {l_ambda} metros")
    #Cálculo de Fresnel
    rf = (math.sqrt((n*l_ambda*d1_*d2_)/(d1_+d2_)))
    rf_formula()
    print (f"Rf = {rf} mt")

    
    #THE FINAL QUESTION
    the_question()


#  ___            __   __   __   __   __                   __  
# |__  | |\ |    |__) |__) /  \ / _` |__)  /\   |\/|  /\  /__` 
# |    | | \|    |    |  \ \__/ \__> |  \ /~~\  |  | /~~\ .__/ 



#Inicio del programa. Selección de cálculo
os.system('cls')
logo()
the_question()