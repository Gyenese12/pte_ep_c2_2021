import math

def terfogat(a: float , b: float , c:float)->float:
    terfogat = a*b*c
    return terfogat

a = float(input("Kérem az első oldalt: "))
b = float(input("Kérem a második oldalt: "))
c = float(input("Kérem a harmadik oldalt: "))
print(f"Térfogata: {terfogat(a,b,c)}")
