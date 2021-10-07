Szoveg = input("Kérek egy Palindromot:")
Lista = []
Reverse_Lista = []
for char in Szoveg :
    Lista.append(char)
    Reverse_Lista.append(char)
Reverse_Lista.reverse()
temp = 0
for i in range(len(Lista)):
    if Reverse_Lista[i] != Lista[i]:
        temp+=1
if(temp > 0) : print("Ez nem egy Palindrom")
else: print("Ez egy Palindrom")


