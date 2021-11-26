class Kutya:
    """Kutyák osztálya"""
    def __init__(self,nev:str,fajta:str):
        self.nev = nev
        self.fajta = fajta
        self.jol_lakott = 100
        self.szomjusag = 100
        self.kedv = 100


    def jatek(self,idotartam: int):
        self.kedv += idotartam
        if self.kedv > 100:
            self.kedv = 100
        self.szomjusag -= 20
        if self.szomjusag < 0:
            self.szomjusag = 0
        self.jol_lakott -= 30
        if self.jol_lakott < 0:
            self.jol_lakott = 0

    def allapot(self):
        print(self.nev,"Jóllakotsága: " ,self.jol_lakott,"Szomjúság: ",self.szomjusag, "kedv:",self.kedv)

