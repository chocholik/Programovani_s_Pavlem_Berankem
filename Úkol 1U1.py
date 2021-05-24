'''Úkol 1U1 - Převodník teploty
Napište program, který načte od uživatele teplotu ve stupňích Celsia a vypíše ji na obrazovku v Kelvinech a Fahrenheitech.
'''

teplota=float(input("Zadej teplotu ve stupních celsia: "))
print (f"Teplota v Kelvinech je {teplota + 273.15} a teplota ve Farenhaitech je {teplota *1.8 + 32}")