class BankAccount:


    def __init__(self,nev :str,szamlaszam: str,egyenleg = 0):
        self.nev = nev
        self.szamlaszam = szamlaszam
        self.egyenleg = egyenleg

    def print_egyenleg(self):
        print(self.egyenleg)

    def penzfelvetel(self, amount: int):
        if self.egyenleg > amount :
            self.egyenleg -= amount
            print("Sikeres pénzfelvetel")
        else:
            print("Sikertelen pénzfelvétel.Nincs elég pénz a számlán")

    def penzberekas(self, amount: int):
        self.egyenleg += amount

    def send(self,other,amount:int):
        if self.egyenleg > amount :
            self.egyenleg -= amount
            other.egyenleg +=amount
            print("Sikeres átutalás")
        else:
            print("Sikertelen átutalás.Nincs elég pénz a számlán")


account1 = BankAccount("User1","0000000",100000)
account2 = BankAccount("User1","1111111",0)
account1.print_egyenleg()
account2.print_egyenleg()
account1.penzfelvetel(50000)
account2.penzfelvetel(50000)
account1.print_egyenleg()
account2.print_egyenleg()
account1.penzberekas(20000)
account2.penzberekas(20000)
account1.print_egyenleg()
account2.print_egyenleg()
BankAccount.send(account2)