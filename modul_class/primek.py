def primek(szam: int)-> None:
    maradek = szam
    oszto = 2
    while maradek > 1:
        if maradek % oszto == 0:
            maradek = maradek // oszto
            print(oszto)
        else:
            oszto+=1
