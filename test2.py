class Product:
    def __init__(self, ati, turi, summa, waqit):
        self.ati = ati
        self.turi = turi
        self.summa = summa
        self.waqit = waqit
    def show(self):
        return f'Telefonnin ati {self.ati}\n Telefon turi {self.turi}\n Telefon summasi {self.summa}\n Shiqqan waqiti {self.waqit}'
    
tovar = Product("Telefon","Samsung", "2500000", "2022-jil")
print(tovar.show())
