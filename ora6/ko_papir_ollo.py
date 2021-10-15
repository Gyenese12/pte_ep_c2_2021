import random
valasz = 0
gep = 0
win = False
while (win == True) :
    while valasz > 0 and valasz < 3:
        valasz = int(input("Válasszon 1 -Kő 2 -Papír 3 -olló"))
    gep = random.randint(1,3)
    if(gep == 1 and valasz == 2) :
        print("Maga nyert")
        win = True
    if(gep == 2 and valasz == 1) :
        print("Gép nyert")
        win = True
    if(gep == 1 and valasz == 3) :
        print("Gép nyert")
        win = True
    if(gep == 3 and valasz == 1) :
        print("Maga nyert")
        win = True
    if(gep == 2 and valasz == 3) :
        print("Maga nyert")
        win = True
    if(gep == 3 and valasz == 2) :
        print("Gép nyert")
        win = True
    if(gep == valasz): print("Döntetlen")