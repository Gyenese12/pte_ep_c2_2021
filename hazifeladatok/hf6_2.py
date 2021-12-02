szoveg = input("Kérek egy mondatot: ")
vegsoszoveg = ""
for i in szoveg:
    if i >= 'a' and i <='z':
        vegsoszoveg += i.upper()
    if i >= 'A' and i <= 'Z':
        vegsoszoveg+= i.lower()
print(f"Eredeti szöveg: {szoveg} \n"
      f"forditott szöveg: {vegsoszoveg}")