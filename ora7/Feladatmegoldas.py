from easygui import *
import math
distance = enterbox("Kérem a kőr átmérőjét: ",title="Adatbekérés")
try :
    diameter = float(distance)
    if(diameter > 0) :
        r = diameter / 2
        Kerulet = 2 * r * math.pi
        Terulet =r ** 2 * math.pi
        msgbox(f"Kerülete: {Kerulet:.3f} Területe: {Terulet:.3f}")

except ValueError :
    msgbox("Nem megfelelő átmérő" , title="hiba")
