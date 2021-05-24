'''###Úkol 2U3 - Kořeny kvadratické rovnice
Napište program, který požádá uživatele o zadání koeficientů kvadratické rovnice. Kvadratická rovnice má tvar a*x^2 + b*x + c = y. Koeficienty jsou násobky neznámé x, takže a, b, c. Program vypíše pro zadanou rovnici kořeny, tzn. hodnoty x, kde je funkční hodnota y = 0. Problém řešte pomocí výpočtu diskriminantu, který vám napoví, kolik kořenů bude rovnice mít, a následně ho i použijte pro výpočet konkrétních hodnot kořenů.

Nápověda: https://cs.wikipedia.org/wiki/Kvadratick%C3%A1_rovnice

Kalkulačka pro ověření: https://www.hackmath.net/cz/kalkulacka/kvadraticka-rovnice
'''

print("Program na výpočet kvadraticke rovnice. \nTvar rovnice: ax^2+bx+c=0")
a=float(input("Zadej koeficient a:"))
b=float(input("Zadej koeficient b:"))
c=float(input("Zadej koeficient c:"))
if a!=0:
    D=b**2-4*a*c
#    print (D)
    if D>0:
        x1=(-b+D)/(2*a)
        x2=(-b-D)/(2*a)
        print("Rovnice má kořen x1 = ", x1, "a kořen x2 = ", x2)
    elif D==0:
        x1=(-b+D)/2*a
        print("Rovnice má kořen x1 = ",x1, "a kořen x2 = ",x1)
    elif D<0:
        print("Rovnice má řešení v oboru komplexních čísel")
else: print("Rovnice neni kvadratická")


