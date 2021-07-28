logo = """
        _                                _           
  /\/\ (_) ___ _ __ ___   ___  _ __   __| | __ _ ___ 
 /    \| |/ __| '__/ _ \ / _ \| '_ \ / _` |/ _` / __|
/ /\/\ \ | (__| | | (_) | (_) | | | | (_| | (_| \__ \ 
\/    \/_|\___|_|  \___/ \___/|_| |_|\__,_|\__,_|___/                                                     
    """

#  ___  __   __                        __  
# |__  /  \ |__)  |\/| |  | |     /\  /__` 
# |    \__/ |  \  |  | \__/ |___ /~~\ .__/ 
                                         
#***Fórmulas de punto de reflexión***
def c_formula(x):
    print(f"""
        (h1-h2)
    c = ------- = {x}
        (h1+h2)\n""")

def m_formula(x):
    print(f"""
                (d^2)
    m = ----------------------------- = {x}
        4•k•a•((0.001•h1)+(0.001•h2))\n""")

def b_formula(x):
    print(f"""
            c
    b = -------------   o buscar en la tabla = {x}         
        [1+m•√(1-c2)]\n""")

#Fórmulas del análisis de Fresnel
def rf_formula(x):
    print(f"""
              ___________
             / n•λ•d1•d2
    Rf = \  /  ---------  = {x} mts
          \/     d1+d2\n""")

def ht_formula(x):
    print(f"""
        h1•d2 + h2•d1
    ht = ---------------  -  0.0588•d1•d2 = {x} mts
            d\n""")

def h1_formula(x):
    print(f"""
            (ht - (h2•d1 / d) + (0.0588•d1•d2))
    h1 = d • ------------------------------------ = {x} mts
                            d2
    """)

def h2_formula(x):
    print(f"""
            (ht - (h1•d2 / d) + (0.0588•d1•d2))
    h2 = d • ------------------------------------ = {x} mts
                            d1
    """)
    