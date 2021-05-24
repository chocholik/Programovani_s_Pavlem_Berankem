'''
###Úkol 1U4 - Kam doletí oštěp?
Napište program, který přijme už uživatele velikost rychlosti oštěpu a úhel, pod kterým byl oštěp vržen. Program následně vypíše na obrazovku vzdálenost, do které oštěp doletěl (nápověda: model šikmého vrhu)
'''

import math

v = float(input("Zadej rychlost oštěpu v m/s: "))
u = float(input("Zadej uhel výstřelu ve stupních: "))
u_rad=math.radians(u)
vysledek = (v**2*math.sin(2*u_rad)/9.8)
print(f"Vzdálenost kam oštěp doletěl je {vysledek} m.")
