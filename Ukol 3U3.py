'''
###Úkol 3U3 - Součet matic
Požádejte uživatele, aby naplnil dvě matice hodnotami. Celý mechanismus je na vás, ale uvažujte o tom tak, že by
uživatel měl zadat, kolik mají matice řádku a sloupců. Pokud to jde, tak vypište jejich součet na obrazovku. Budete
potřebovat dvojný cyklus.
Algoritmus: https://cs.wikipedia.org/wiki/S%C4%8D%C3%ADt%C3%A1n%C3%AD_matic
'''

a_radky = int(input("Zadej kolik chceš aby měla matice A řádků: "))
a_sloupce = int(input("Zadej kolik chceš aby měla matice A sloupců: "))
b_radky = int(input("Zadej kolik chceš aby měla matice B řádků: "))
b_sloupce = int(input("Zadej kolik chceš aby měla matice B sloupců: "))
matice_A = []
matice_B = []
soucet_matic = []

if a_radky == b_radky and a_sloupce == b_sloupce: #pokud mají stejný rozměr šcítáme
    for m in range(a_radky): #iteruju přes řádky
        radek =[]
        for n in range(a_sloupce): #iteruju přes sloupce
            radek.append(int(input(f"Zadejte hodnotu pro matici A. Pozice[{m}, {n}]: "))) #do řádku přidávám jednotliví slouce
        matice_A.append(radek)  #řádek přidávám do matice
    for m in range(b_radky):
        radek = []
        for n in range(b_sloupce):
            radek.append(int(input(f"Zadejte hodnotu pro matici B. Pozice[{m}, {n}]: ")))
        matice_B.append(radek)

    for m in range(a_radky):
        radek = []
        for n in range(a_sloupce):
            radek.append(matice_A[m][n]+matice_B[m][n])
        soucet_matic.append(radek)

    print(f"matice A + matice B:\n"
          f"{matice_A[0]} + {matice_B[0]}\n"
          f"{matice_A[1]} + {matice_B[1]}\n"
          f"Součet matic:\n"
          f"{soucet_matic[0]}\n"
          f"{soucet_matic[1]}")

else:
    print("Matice nelze sečíst, nemají stejný rozměr")