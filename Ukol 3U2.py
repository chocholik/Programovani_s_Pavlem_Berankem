###Úkol 3U2 - Hra šibenice
###Naprogramujte hru šibenice. Hráč hádá písmena v tajence a pokud písmeno neuhodne, ubírá se mu život. ###

#tajenka = "kokos"
nzivotu = 3
skore = 0
max_skore = 0
tajenka_list = []
tajenka_uhadnuto = []

tajenka = input("Zadej co budeš hádat: ").strip().lower()

for pismenko in tajenka: #naplnění listu písmeny
    if pismenko.isalpha():
        tajenka_list.append(pismenko)
        tajenka_uhadnuto.append("_")
    else:
        tajenka_list.append(False)
        tajenka_uhadnuto.append(pismenko)

for i in tajenka_list: #Spočítám si max skore
    if bool(i) == True:
        max_skore += 1
print(f"Hledáme tuto tajenku:\n{tajenka_uhadnuto}")

while nzivotu != 0 and skore != max_skore: #budu prohledávat tajenku, co najdu, to odstraním z tajenky a ukážu to hráči
    znak = input("Zadej písmenko z hádanky: ").strip( ).lower()
    if znak in tajenka_list:
        for pismenko in tajenka_list:
            if znak == pismenko:
                tajenka_uhadnuto[tajenka_list.index(znak)] = pismenko
                tajenka_list[tajenka_list.index(znak)] = False
                skore += 1
    elif len(znak) > 1 or not znak.isalpha():
        print("Zadej pouze 1 písmenko")
    else:
        nzivotu -= 1
        print(f"Přišel si o život, zbývá {nzivotu}")
    print(f"\nStav:\nmáš uhádnuto {tajenka_uhadnuto}\nSkore je: {skore}\nZbává ti životů: {nzivotu}\n")
if nzivotu == 0:
  print(f"A je hotovo, přišel si o všechny životy. Dosažené skora je {skore}")
else:
  print(f"Gratuluji!!!!!\nVyhrál jsi!!!!\nZískal jsi body: {skore}\nZbývá životů: {nzivotu}")

''' HLOUPA VERZE
while nzivotu != 0 and skore != len(tajenka):
#  print(nzivotu != 0)
#  print(skore != len(tajenka))
  znak = input("Zadej písmenko z hádanky: ")
  if znak in tajenka:
    skore += tajenka.count(znak) 
    print(f"Uhadl jsi, přičtene body: {tajenka.count(znak)}, celkovy pocet bodu je {skore}")
  else:
    nzivotu -= 1
    print(f"přišel si o žovot, zbývá {nzivotu}")
if nzivotu == 0:
  print(f"A je hotovo, přišel si o všechny životy. Dosažené skora je {skore}")
else:
  print(f"Gratuluji, vyhrál jsi. Získal jsi {skore} bodů a ještě máš {nzivotu} život(y)")
'''

