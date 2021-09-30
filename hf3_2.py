a=int(input("Kérem a termék árát: "))
if(a < 10000) : print("A termékre 10% kedvezmény van. A végleges ár: {}Ft".format(a-a//10))
elif(a>=10000) : print("A termékre 20% kedvezmény van. A végleges ár: {}Ft".format(a-a//10*2))