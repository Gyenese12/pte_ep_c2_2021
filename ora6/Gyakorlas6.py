kmh = float(input("Kérek egy számot (km/h): "))
ms = kmh / 3.6
print("Az érték m/s-ban: ",ms)


import math
import random
Listaparos = []
Listaparatlan = []
lista = []
for a in range(20):
    n = random.randint(1,200)
    lista.append(n)
for i in range(len(lista)) :
    if lista[i] % 2 == 0: Listaparos.append(lista[i])
    if lista[i] % 2 == 1: Listaparatlan.append(lista[i])
print("Páros " , Listaparos)
print("Páratlan: ",Listaparatlan)

a = float(input("Kérem a oldal hosszát: "))
b = float(input("Kérem b oldal hosszát: "))
c = float(input("Kérem c oldal hosszát: "))
d = (a+b+c)/2
Terulet = math.sqrt(d*(d-a)*(d-b)*(d-c))
print("Terület: " ,Terulet," Kerület: ",(a+b+c))
