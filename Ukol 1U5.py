'''
###Úkol 1U5 - Social distancing
Napište program, který přijme od uživatele souřadnice X a Y dvou osobe. Program následně spočítá o kolik se mají od sebe oddálit nebo jakou mají rezervu. Např.: pokud jejich vzdálenost bude 4 metry a podmínkou je být alespoň dva metry od sebe, pak program vypíše -2 (mají rezervu dva metry).
'''

import math

x1 = float(input("Zadej polohu x první osoby: "))
y1 = float(input("Zadej polohu y první osoby: "))
x2 = float(input("Zadej polohu x druhé osoby: "))
y2 = float(input("Zadej polohu y druhé osoby: "))

odstup = math.sqrt((x1-x2)**2+(y1-y2)**2)

print(f"Osoby mají od rezervy 2 metrů odchylku {2-odstup} m.")