from easygui import *

try:
    ev = enterbox("Kérek egy évszámot: ", title="Adatbekérés")
    evek = int(ev)
    if(evek % 4  != 0 and ev % 100 != 0 and ev % 400 != 0):
        msgbox("Nem szökőév")
    if(evek % 4 == 0 and evek%100!=0 and evek%400!=0) :
        msgbox("Szökőév mert osztható 4-el")
    if (evek % 4 == 0 and ev % 100 == 0 and ev % 400 != 0) :
        msgbox("nem Szökőév mert osztható 4-el és 100-al de 400-al nen")
    if (evek % 4 == 0 and ev %100 == 0 and ev %400 == 0) :
        msgbox("Szökőév mert osztható 4-el 100-al és 400-al")
except ValueError:
    msgbox("Hibás évszám")
