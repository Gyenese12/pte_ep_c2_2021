import math
a = int(input("Kérek egy számot"))
b = int(input("Kérek egy másik számot"))
c = int(input("Kérek egy másik számot"))

gyok = (b**2)-4*a*c

if(gyok > 0):
    megoldas1 = (-1*b-(gyok)**0.5) / (2*a)
    megoldas2 = (-1*b+(gyok)**0.5) / (2*a)
    print(f"Az első megoldás: {megoldas2} Második megoldás: {megoldas1}")

if gyok == 0:
    megoldas = -1*b/2*a
    print(f"Az egyetlen megoldás:{megoldas}")

if gyok < 0:
    print("Nincs megoldás a valós számok halmazán")

