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
                                         
#***Fórmulas de perdida espacio libre***
d_max_formula = "\nDmax = 4.12•[√(h1)+√(h2)]"

lo_formula = "\nLo dB = 32.5+20•log(d(km))+20•log(f(GHz))"

ptx_dbm_formula = "\nP(dBm) = 10•log10(1000•Ptx)"

prx_formula = "Prx(dBm) = Ptx(dbm) + Gtx(dB) + Grx(dB) - Lo(dB)"

#***Fórmulas de punto de reflexión***
c_formula = """
    (h1-h2)
c = -------
    (h1+h2)\n"""

m_formula = """
            (d^2)
m = -----------------------------
    4•k•a•((0.001•h1)+(0.001•h2))\n"""

b_formula = """
        c
b = -------------   o buscar en la tabla         
    [1+m•√(1-c2)]\n"""

d1_formula = "\nd1 = (d/2)*(1+b)"

d2_formula = "\nd2 = (d/2)*(1-b) o d2 = d-d1\n"

#Fórmulas del análisis de Fresnel
rf_formula = """
          ___________
         / n•λ•d1•d2
Rf = \  /  ---------
      \/     d1+d2\n"""

l_ambda_formula = "λ = C/f"