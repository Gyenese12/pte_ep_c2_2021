import math

sugar = 3
terfogat = sugar**2*math.pi
print(terfogat)

koordinata1 = 3
koordinata2 = 5
if(koordinata1 < koordinata2): print("Távolság: ", koordinata2-koordinata1)
if(koordinata1 > koordinata2): print("Távolság: ", koordinata1-koordinata2)


str_tomb = ["almaszár" , "kerékgyártó" , "Flóra-pihenő" , "malomvölgy" , "Misina" , "Égercőlgyi tó" , "Tenkes" , "Zsolnay-tó"]
for x in str_tomb:
            if(len(x) > 10) : print("Szó:",x,"Hossz: " , len(x) , "hosszabb mint 10")
            else: print("Szó: " , x ," hossz: " , len(x))