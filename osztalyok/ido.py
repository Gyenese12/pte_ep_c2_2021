class ido:
    def __init__(self,ora:int,perc:int,masodperc:int):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc

    def print_ido(self):
        if self.ora < 10 :
            print(f"0{self.ora}:",end="")
        else:
            print(f"{self.ora}:",end="")
        if self.perc < 10 :
            print(f"0{self.perc}:",end="")
        else:
            print(f"{self.perc}:",end="")
        if self.masodperc < 10:
            print(f"0{self.masodperc}")
        else:
            print(f"{self.masodperc}")

ido1 = ido(3,4,15)
ido.print_ido(ido1)