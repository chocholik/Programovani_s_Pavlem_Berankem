'''###Úkol 2U1 - Programátore nezlob se
Napište program, který imituje jeden hod kostkou ve hře Člověče nezlob se. Postavička se nachází na políčku 1. Hra vyzve uživatele k hodu. Podle čísla, jenž padne na 6-stěnné kostce, se postavička o příslušný počet pozic posune na nové políčko. Hod kostkou je řízen náhodným generátorem. Pokud padne číslo 6, pak hráč hází znovu (max 1x).
'''

import random

print("Nacházíte se na poli: 1")
pole = 1
i = random.randint(1,6)
print(f"Gratuluju, hodil jste {i}")
if i == 6:
  print("Házíte ještě jednou.")
  j = random.randint(1,6)
  print(f"Gratuluju, v druhím hodu jste hodil {j}")
  i = i + j
print(f"Posunul jste se na pole: {i+1}")

