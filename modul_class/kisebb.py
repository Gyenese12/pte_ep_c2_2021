def kisebb(lista : list[float], szam: float)-> int:
    db = 0
    for i in lista:
        if i < szam:
            db+=1
    return db