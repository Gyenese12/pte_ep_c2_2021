
def abetuk(a: int):
    szoveg = ""
    for i in range(a):
        szoveg+="a"
    print(szoveg,end="")

def xbetuk(a: int):
    szoveg = ""
    for i in range(a):
        szoveg+="x"
    print(szoveg,end="")

def pbetuk(a: int):
    szoveg = ""
    for i in range(a):
        szoveg+="p"
    print(szoveg,end="")

a = int(input("Kérem adja meg hány darab a betüt irjon ki"))
x = int(input("Kérem adja meg hány darab x betüt irjon ki"))
p = int(input("Kérem adja meg hány darab p betüt irjon ki"))

print(abetuk(a),xbetuk(x),pbetuk(p),end="")