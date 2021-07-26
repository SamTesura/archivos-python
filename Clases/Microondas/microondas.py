import math
import assets
import os

ERROR_MSG = ">> ERROR! Intentelo de nuevo.\n"

menu = """
------------------------------------------------------------------   
SELECCIONE SU CÁLCULO DESEADO:
1. Linea de vista, perdida en el espacio libre y punto de recepción
2. Punto de reflexión
3. Análisis de fresnel
4. Rango de frecuencias
0. Salir\n"""

#Funciones auxiliares
def input_float(msg):
    while True:
        x = input(msg)
        try:                #Loop to only accept floating
            return float(x)
        except ValueError:
            print(ERROR_MSG)

#***Menú de selección***
def selection_menu():
    while True:     #Loop to only accept floating
        print(menu)

        question = input("    >> ").lower
        try:
            question = int(question)
            break
        except: print(ERROR_MSG)

    if  question == 1:
        perdida_espaciolibre()
    elif question == 2:
        punto_reflexion()
    elif question == 3:
        analisis_fresnel()
    elif question == 4:
        rango_frecuencia()
    elif question == 0:
        return
    else:
        print(ERROR_MSG)
        selection_menu()
#***Fin de Menú de selección***

#  __   __   __   __   __                   __  
# |__) |__) /  \ / _` |__)  /\   |\/|  /\  /__` 
# |    |  \ \__/ \__> |  \ /~~\  |  | /~~\ .__/ 
                                              
#__________________Linea de vista, perdida en el espacio libre y punto de recepción__________________
def perdida_espaciolibre():
    os.system('cls')
    #Perdida en el espacio libre. Datos
    #Altura del punto 1
    h1 = input_float("h1 (mts): ")
    #Altura del punto 1
    h2 = input_float("h2 (mts): ")
    #Linea de vista
    d_max = 4.12*(math.sqrt(h1)+math.sqrt(h2))
    print(assets.d_max_formula)
    print(f"Dmax = {d_max} Kms. *Linea de vista*\n")
    #Distancia desde el punto 1 hasta el punto 2
    d = input_float("d (Km): ")
    #frecuencia
    f = input_float("frecuencia (GHz): ")
    #Pérdida en el espacio libre
    lo = 32.5+20*math.log10(d)+20*math.log10(f*1000)
    print(assets.lo_formula)
    print(f"Lo dB = {lo} dB\n")
    #Potencia de la antena emisora
    ptx = input_float("Potencia de la antena emisora (Watts): ")
    #Ganancia de la antena transmisor
    gtx = input_float("Ganancia de la antena transmisora (dB): ")
    #Ganancia de la antena receptora
    grx = input_float("Ganancia de la antena receptora (dB): ")
    #Potencia del emisor en dBm
    ptx_dbm = 10*math.log10(1000*ptx)
    print(assets.ptx_dbm_formula)
    print(f"Ptx en dBm = {ptx_dbm}\n")
    #Potencia del receptor
    prx = ptx_dbm + gtx + grx - lo
    print(assets.prx_formula)
    print(f"Prx = {prx} dBm")
    #THE FINAL QUESTION
    selection_menu()

#_________________________________________Punto de reflexión__________________________________________
def punto_reflexion():
    os.system('cls')
    #Punto de reflexión. Datos
    #Altura del punto 1
    h1 = input_float("h1 (mt): ")
    #Altura del punto 1
    h2 = input_float("h2 (mt): ")
    #Distancia desde el punto 1 hasta el punto 2
    d = input_float("d (Km): ")
    k = (4/3)
    a = 6370
    #_____CÁLCULOS_____TO SHOW AND COPY_____
    os.system('cls')
    print(f"h1: {h1} mts \nh2: {h2} mts \nd: {d} kms\n")
    #Cálculo de c
    c = (h1-h2)/(h1+h2)
    print(assets.c_formula)
    print(f"c = {c}")
    #Cálculo de m
    m = (((d)**2)/(4*k*a*((0.001*h1)+(0.001*h2))))
    print(assets.m_formula)
    print(f"m = {m}")
    #Cálculo de b o buscar en la tabla
    b = c/(1+m*(math.sqrt(1-(c**2))))
    print(assets.b_formula)
    print(f"b = {c}\n")
    #Cálculo de d1
    d1 = (d/2)*(1+b)
    print(assets.d1_formula)    
    print(f"d1 = {d1} Km\n")
    #Cálculo de d2    
    d2 = (d/2)*(1-b)
    print(assets.d2_formula)
    print(f"d2 = {d2} Km")
    #THE FINAL QUESTION
    selection_menu()

#_________________________________________Análisis de Fresnel_________________________________________
def analisis_fresnel():
    os.system('cls')
    #Análisis de Fresnel. Datos
    #Entrada de la distancia total
    d = input_float("d (Km): ")
    #Altura del punto 1
    h1 = input_float("h1 (mt): ")
    #Altura del punto 1
    h2 = input_float("h2 (mt): ")
    #Entrada del punto más alto
    h0 = input_float("h0 (mt) Punto más alto: ")
    #Entrada de la distancia desde el punto de transmisión hasta el punto mas alto
    d1_ = input_float("d1 (Km) (fresnel): ")
    #distancia desde el punto de mas alto hasta el punto de recepción
    d2_ = d - d1_
    print(f"d2 (km) (fresnel): {d2_}")
    #Entrada de la frecuencia
    f = input_float("frecuencia (GHz): ")
    #_____CÁLCULOS_____TO SHOW AND COPY_____
    os.system('cls')
    print(f"d: {d} kms \nPunto más alto: {h0} mts \nd1: {d1_} kms \nd2: {d2_} kms \nfrecuencia: {f} GHz\n") 

    c = 300000000
    n = 1
    d *= 1000
    d1_ *= 1000
    d2_ *= 1000
    #Cálculo de lambda
    print(assets.l_ambda_formula)
    l_ambda = c / (f*1000000000)
    print(f"λ = {l_ambda} metros")
    #Cálculo de Fresnel
    rf = (math.sqrt((n*l_ambda*d1_*d2_)/(d1_+d2_)))
    print(assets.rf_formula)
    print (f"Rf = {rf} mt")
    #Cálculo de la Altura total
    ht = ((h1*(d2_/1000) + h2*(d1_/1000))/(d/1000)) - (0.088*(d1_/1000)*(d2_/1000))
    print(assets.ht_formula)
    print(f"ht = {ht} mts.\n")
    #Cálculo de ht-h0
    ht_h0 = ht-h0
    print(f"ht-h0 = {ht} - {h0} = {ht_h0} mts\n")

    if ht_h0 >= rf:
        print("ht-h0 >= Rf ∴ El obstaculo no corta el radio de Fresnel\n")
    elif ht_h0 < rf:
        print("ht-h0 < Rf ∴ El obstaculo corta el radio de Fresnel\n")
        print("¿Cuántos metros deberia aumentar a la antena receptora para evitar el corte?\n")
        #Cálculo de ht
        ht = h0 + rf
        print(assets.ht_formula2)
        print(f"ht = {ht} mts.\n")
        #Cálculo de h2
        h2 = (d/1000) * ((ht - ((h1*(d2_/1000))/(d/1000)) + (0.088*(d1_/1000)*(d2_/1000))) / (d1_/1000))
        print(assets.h2_formula)
        print(f"h2 = {h2} mts.\n")
        print(f"La altura minima de la antena receptora es {h2} metros")



    #THE FINAL QUESTION
    selection_menu()

#_________________________________________Rango de frecuencia_________________________________________
def rango_frecuencia():
    os.system('cls')

    valor = input_float("frecuencia: ")
    
    letra = ["K", "M", "G", "", " "]
    while True:
        notacion = input("Notación (Nada, K, M o G): ").upper()
        if notacion in letra:
            break
        else: print(ERROR_MSG)
        
    #Variables de notación
    K = float(1*10**3)
    M = float(1*10**6)
    G = float(1*10**9)

    if notacion == "" or notacion == " ":
        notacion1 = 1
    elif notacion == "K":
        notacion1 = K
    elif notacion == "M":
        notacion1 = M
    elif notacion == "G":
        notacion1 = G

    frecuencia = valor * notacion1

    if frecuencia < 3:
        rango = "está fuera del rango del espectro"
    elif frecuencia >= 3 and frecuencia < 30:
        rango = "pertenece al rango ELF"
    elif frecuencia >= 30 and frecuencia < 300:
        rango = "pertenece al rango SLF"
    elif frecuencia >= 300 and frecuencia < 3000:
        rango = "pertenece al rango ULF"
    elif frecuencia >= 3*10**3 and frecuencia < 30*10**3:
        rango = "pertenece al rango VLF"
    elif frecuencia >= 30*10**3 and frecuencia < 300*10**3:
        rango = "pertenece al rango LF"
    elif frecuencia >= 300*10**3 and frecuencia < 3000*10**3:
        rango = "pertenece al rango MF"
    elif frecuencia >= 3*10**6 and frecuencia < 30*10**6:
        rango = "pertenece al rango HF"
    elif frecuencia >= 30*10**6 and frecuencia < 300*10**6:
        rango = "pertenece al rango VHF"
    elif frecuencia >= 300*10**6 and frecuencia < 3000*10**6:
        rango = "pertenece al rango UHF"
    elif frecuencia >= 3*10**9 and frecuencia < 30*10**9:
        rango = "pertenece al rango SHF"
    elif frecuencia >= 30*10**9 and frecuencia < 300*10**9:
        rango = "pertenece al rango THF o THz"
    else:
        rango = "está fuera del rango del espectro"
    
    print(f"\n{valor}{notacion}Hz  {rango}.\n")
    
    #THE FINAL QUESTION
    selection_menu()
#  ___            __   __   __   __   __                   __  
# |__  | |\ |    |__) |__) /  \ / _` |__)  /\   |\/|  /\  /__` 
# |    | | \|    |    |  \ \__/ \__> |  \ /~~\  |  | /~~\ .__/ 

#Inicio del programa. Selección de cálculo
os.system('cls')
print(assets.logo)
selection_menu()