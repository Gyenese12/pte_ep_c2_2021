class sik_pontok:
    def __init__(self,pont1: int,pont2: int):
        self.pont1 = pont1
        self.pont2 = pont2

    def tavolsag(self,other):
        return ((self.pont1-other.pont1)**2 + (self.pont2-other.pont2)**2)**0.5

class Teglalap:
    """Óra mutató járásával megeggyező irányba adja meg"""
    def __init__(self,s1: sik_pontok , s2: sik_pontok ,s3: sik_pontok,s4: sik_pontok):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def oldalhossz(self):
        return [self.s1.tavolsag(self.s2),self.s1.tavolsag(self.s4)]

    def ker(self):
        oldalak = self.oldalhossz()
        return 2* oldalak[1] +oldalak[2]

    def ter(self):
        oldalak = self.oldalhossz()
        return oldalak[1] * oldalak[2]


class Negyzet(Teglalap) :

    def __init__(self,s1: sik_pontok , s2: sik_pontok ,s3: sik_pontok,s4: sik_pontok):
        super().__init__(s1,s2,s3,s4)

    def kerulet(self):
        return self.s1.tavolsag(self.s2) *4

    def terulet(self):
        return self.s1.tavolsag(self.s2)**2

p1 = sik_pontok(0,0)
p2 = sik_pontok(0,5)
print(sik_pontok.tavolsag(p1,p2))

negyzet = Negyzet(sik_pontok(4,0),sik_pontok(4,4),sik_pontok(0,0),sik_pontok(4,4))