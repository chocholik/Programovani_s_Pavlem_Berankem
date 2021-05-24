###Úkol 3U2 - Hra šibenice
###Naprogramujte hru šibenice. Hráč hádá písmena v tajence a pokud písmeno neuhodne, ubírá se mu život. ###

tajenka = "lokus"
nzivotu = 3
skore = 0

''' HLOUPA VERZE  
while nzivotu != 0 and skore != len(tajenka):
#  print(nzivotu != 0)
#ll  print(skore != len(tajenka))
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
