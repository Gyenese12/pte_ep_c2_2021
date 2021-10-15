
a = 0
b = 0
c = 0
while a == 0 :
    a = int(input("Kérem a háromszög A oldalát: "))
while b == 0 :
    b = int(input("Kérem a háromszög B oldalát: "))
while c == 0 :
    c = int(input("Kérem a háromszög C oldalát: "))
if(a + b > c and a+c > b and b+c>a):
    if((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)): print("A háromszög derékszögű")
    elif ((a == b and a!=c) or (b==c and b!=a) or (a == c and b!=c)) : print("A háromszög egyenlőszárú")
    elif(a == b and b == c and a ==c) : print("A háromszög egyenlő oldalú")
    else : print("A háromszög általános")
else : print("Ez nem lehet egy háromszög adata")


a = int(input("Kérek egy számot: "))
b = int(input("Kérek egy számot: "))
sum = 0
for number in range(a,b+1):
    if(number%3 == 0 and number%5==0): sum+=number
print(sum)



