import random

print("Kérek értékeket egy üres sorba ütött enterig")
Lista = []
a = 0
while(a != "") :
        a = input("Szám: ")
        if a!="" : Lista.append(a)
print("Értékek: ",Lista)


Lista_rand = []
for i in range(20):
    Lista_rand.append(random.randint(1,100))
int_max = 0
int_min = 100

for i in Lista_rand :
    if(i > int_max): int_max = i
    if(i < int_min): int_min = i
print(Lista_rand)
print("Maximum: {} Minimm: {}" .format(int_max,int_min))

name = input("Kérem a nevét: ")
nem = ""
while nem!= "f" or nem!="n" or nem!="F" or nem !="N" :
    nem = input("Kérem a Nemét (N/F): ")
if(nem.lower() == "f"): print(name ,"Úr")
if(nem.lower() == "n"): print(name ," Asszony")