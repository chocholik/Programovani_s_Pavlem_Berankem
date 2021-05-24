'''Úkol 1U2 - Délka přepony trojúhelníku
Napište program, který přijme od uživatele délku odvěsen pravoúhlého trojúhelníka a vypočte délku přepony.
'''
import math

a=float(input("Zadej stranu a: "))
b=float(input("Zadej stranu b: "))
print(f"Délka přepony je: {math.sqrt(a ** 2 + b ** 2)}")