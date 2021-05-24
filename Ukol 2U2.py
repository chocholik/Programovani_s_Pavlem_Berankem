'''###Úkol 2U2 - Šťastný zákazník
Napište program, který požádá uživatele o název produktu, který chce zakoupit, a o datum narození. Produkty se tisknou na začátku programu na obrazovku (viz. předpřipravený kód). Doprogramujte následující:
1. pokud se produkt nenachází v obchodě, pak program vynadá uživateli, že volí neexistující zboží
2. pokud se produkt nachází v obchodě, pak program vypíše cenu zboží
3. pokud se produkt nachází v obchodě a uživatel má dnes narozeniny, pak program pogratuluje uživateli a cena bude poloviční'''

from datetime import datetime

#ziskani dnesniho data (mesic-den)
dnesni_datum = datetime.today().strftime("%m-%d")

#seznam zbozi v obchode
zbozi = "tatranka, jablko, okurka"

tatranka = 10
jablko = 6
okurka = 14

print(f"Máme {zbozi}")
pozadavek = input("Jaké zboží chcete koupit? ")
datum_narozeni = input("Zadej datum narození ve formátu mm-dd: ")

if pozadavek not in zbozi:
  print ("Jedeš ty holoto! Tohle tu neni a nikdy nebude!")
elif dnesni_datum == datum_narozeni:
  print (f"Gratuluju ti. Máš narozky! Dostáváš 50% slevu.")
  if pozadavek == "tatranka":
    print (f"Cena tatranky je {tatranka/2} Kč")
  elif pozadavek == "jablko":
    print (f"Cena jablka je {jablko/2} Kč")
  elif pozadavek == "okurka":
      print (f"Cena okurky je {okurka/2} Kč")

else:
  if pozadavek == "tatranka":
    print (f"Cena tatranky je {tatranka} Kč")
  elif pozadavek == "jablko":
    print (f"Cena jablka je {jablko} Kč")
  elif pozadavek == "okurka":
      print (f"Cena okurky je {okurka} Kč")

