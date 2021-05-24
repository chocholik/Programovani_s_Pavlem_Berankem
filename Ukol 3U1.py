'''
Napište algoritmus, který vypíše všechna prvočísla v rozmezí, které zadal uživatel. Potřebujete dvojný cyklus.
'''
min = int(input("Zadej minimu: "))
max = int(input("Zadej maximum: "))
cisla = []
prvocisla = []

while min != max+1:
  cisla.append(min)
  min += 1
#print(cisla)
for i in cisla:
  if cisla[i-1] == 2:
    prvocisla.append(cisla[i-1])
  elif cisla[i-1] == 3:
    prvocisla.append(cisla[i-1])
  elif cisla[i-1] == 5:
    prvocisla.append(cisla[i-1])
  elif cisla[i-1]%2 != 0 and cisla[i-1]%3 != 0 and cisla[i-1]%5 != 0:
      prvocisla.append(cisla[i-1])
prvocisla.remove(1)
print(prvocisla)