def bemenet(lista: list[float])-> float:
    temp = 0
    for i in lista :
        if i > temp:
            temp = i
    return temp

listam = []
for i in range(5):
    szam = float(input(f"Kérem a {i+1}. Számot: "))
    listam.append(szam)

print(f"Listában a legnagyobb szám: {bemenet(listam)}")
