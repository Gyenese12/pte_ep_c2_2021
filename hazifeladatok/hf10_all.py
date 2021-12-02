def bekeres():
    dict = {}
    for i in range(5):
        nev = input("Kérek egy nevet: ")
        telefon = input("Kérek egy telefonszámot: ")
        dict[nev] = telefon
    return dict

def benne(a:dict,nev:str)->str:
    ertek = ""
    temp = 0
    for key,value in a.items():
        if key == nev:
            ertek += f"név: {key} telefonszám: {value}"
            temp+=1
    if(temp == 0):
        ertek+="Nincs ilyen név"
    return ertek




diction = bekeres()
print(benne(diction,"Pista"))