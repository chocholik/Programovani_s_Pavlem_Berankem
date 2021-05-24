'''###Úkol 2U5 - Je heslo bezpečné?
Napište program, který zjistí, zda vložené heslo obsahuje malá písmena, velká písmena a čísla. Program vypíše sílu hesla na obrazovku a to podle následujícího vzorce:
1. Pokud heslo obsahuje pouze malá písmena nebo pouze velká písmena a žádné číslo (nebo samá čísla), pak se na obrazovku vypíše: "heslo je slabé"
2. Pokud heslo obsahuje kombinaci velkých a malých písmen nebo obsahuje alespoň jedno číslo, tak se na obrazovku vypíše: "heslo je středně silné"
3. Pokud heslo obsahuje jak kombinaci velkých a malých písmen a čísel, tak se vypíše na obrazovku: "heslo je silné"

Nápověda: Pokud chci zjistit, zda se v textu nachází číslo, pak mohu projít všechny písmena v textu a ptát se, zda jsou číslem. Zajímá mě, zda alespoň jeden takový případ nastane v celém textu:

*any(pismeno.isdigit() for pismeno in heslo)*

Obdobně můžete použít i funkce:
- islower()
- isupper()'''

#zadane_heslo = "Password123"
male_pismeno = 0
velke_pismeno = 0
cislice = 0

zadane_heslo = input("Zadejte heslo minimálně o 8 znacích: ")
for i in zadane_heslo:
    if i.islower():
        male_pismeno += 1
    elif i.isupper():
        velke_pismeno += 1
    elif i.isdigit():
        cislice += 1
    else:
        print(f"Chyba. Heslo může obsahovat pouze: velká písemna, malá pismena a čísla.")

if male_pismeno+velke_pismeno+cislice <= 8:
    print("Tvé heslo je moc krátké. Zkus to znovu.")
elif male_pismeno >= 1 and velke_pismeno >= 1 and cislice >= 1:
    print("Tve heslo je silné.")
elif cislice == 0 or (male_pismeno == 0 and velke_pismeno == 0):
    print("Tve heslo je slabe")
else:
    print("Tvé heslo je středně silné")
