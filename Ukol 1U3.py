'''
###Úkol 1U3 - Generování polymeru
Napište program, který přijme od uživatele tvar monomeru (např.: CH2) a z kolika monomerů se polymer skládá (např.: 4) a program na obrazovku vypíše pomocí opakování řetězců tvar takového polymeru (např.: CH2-CH2-CH2-CH2)
'''
monomer = input("Zadej monomer: ")
nasobek = int(input("Zadej násobek: "))
polymer = (monomer + "-")*(nasobek-1)+monomer
print (polymer)