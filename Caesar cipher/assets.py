logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_1, shift_1, direction_1):
    i = 0       #Declaro a 'i' como un integer con valor 0
    z = ""      #Declaro a 'z' como un string
    
    #Evalúo la entrada del usuario letra por letra
    for x in text_1:

        #Como 'alphabet' no incluye espacios, símbolos ni números, si hay uno de estos, los dejo como estaba.
        if x not in alphabet:
            z += x
        
        #Evalúo la entrada del usuario letra por letra
        else:
            #En la variable 'i', asigno la posición de cada letra del mensaje
            i = alphabet.index(x)

            #Si 'direction' es 'encode' desplaza a la derecha la cantidad de veces que hay en 'shift' para codificar el mensaje
            if direction_1 == "encode":
                i += shift_1
                z += alphabet[i]

            #Si 'direction' es 'decode' desplaza a la izquierda la cantidad de veces que hay en 'shift' para descifrar el mensaje
            elif direction_1 == "decode":
                i -= shift_1
                z += alphabet[i]
       
    if direction_1 == "encode":
        print(f"The encoded text is: {z}")
    elif direction_1 == "decode":
        print(f"The decoded text is: {z}")