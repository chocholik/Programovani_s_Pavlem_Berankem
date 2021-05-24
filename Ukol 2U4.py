'''###Úkol 2U4 - Jsem na správné stránce?
Následující program pomocí modulu request stáhne zadanou webovou stránku v proměnné odkaz a získá z ní text (tzv. parsování) pomocí knihovny beautifulsoup (bs4). Jedná se konkrétně o text Listiny základních práv a svobod. Vaším úkolem je požádat uživatele o zadání 3 klíčových slov a vypsat na obrazovku pravdivostní hodnoty (True/False) pro následující dotazy:
1. v textu se nachází všechna 3 klíčová slova
2. v textu se nachází alespoň 1 klíčové slovo
3. v textu se nenachází žádné ze zadaných klíčových slov
4. v textu se nachází první dvě klíčová slova, ale nenachází se tam třetí (přesně v zadaném pořadí)
5. v textu se nachází alespoň dvě klíčová slova (nezávisle na pořadí v zadání)

příklad klíčových slov: člověk, svoboda, prase'''

'''
zadání od Pavla
import bs4
import urllib.request
#!pip install bs4

odkaz = "http://zakony-online.cz/?s5&q5=all"
webova_stranka = str(urllib.request.urlopen(odkaz).read().decode('utf-8'))
text = bs4.BeautifulSoup(webova_stranka).get_text()
print(text)

#prostor pro váš kód
'''

import bs4
import urllib.request
#!pip install bs4

odkaz = "http://zakony-online.cz/?s5&q5=all"
webova_stranka = str(urllib.request.urlopen(odkaz).read().decode('utf-8'))
text = bs4.BeautifulSoup(webova_stranka).get_text()

prvni = input("Zadejte první hledané slovo: ")
druhe = input("Zadejte druhé hledané slovo: ")
treti = input("Zadejte třetí hledané slovo: ")

if prvni in text and druhe in text and treti in text:
  print("1: TRUE V textu se nachází všechna 3 klíčová slova")
else:
  print("1: False")
if prvni in text or druhe in text or treti in text:
  print("1: TRUE V textu se nachází alespoň 1 klíčové slovo")
else:
  print("1: False")
if prvni not in text and druhe not in text and treti not in text:
  print("1: TRUE V textu se nenachází žádné ze zadaných klíčových slov")
else:
  print("1: False")
if prvni in text and druhe in text and treti not in text:
  print("1: TRUE V textu se nachází první dvě klíčová slova, ale nenachází se tam třetí (přesně v zadaném pořadí)")
else:
  print("1: False")
if (prvni in text and druhe in text) or (druhe in text and treti in text) or (prvni in text and treti in text):
  print("1: TRUE V textu se nachází alespoň dvě klíčová slova (nezávisle na pořadí v zadání)")
else:
  print("1: False")