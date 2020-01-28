
class TicketMachine:
    def __init__(self, cost):
        self.cost = cost
        self.balance = 0

    def get_balance(self):
        return self.balance

    def get_price(self):
        return self.cost

    def insert_money(self, amount):
        self.balance += amount

    def print_ticket(self):
        if self.balance >= self.cost:
            print("""
                        <|#################|>
                       < |Ticket 4562      | >
                      <  |Zaal 3           |  >
                      <  |Rij 12           |  >
                       < |Stoel 6          | >
                        <|#################|>
            """)
            self.balance -=self.cost
        else:
            print("Je hebt niet voldoende geld gegeven!")
        
        
    def refund_balance(self):
        print(f"Je hebt {self.balance} teruggekregen")
        self.balance = 0
        


if __name__ == "__main__":
    t1 = TicketMachine(50)
    t2 = TicketMachine(30)  

    print("""
            |***********************|
            |Een ticket kost 50 cent|
            |***********************|
            """)

    t1.insert_money(70) #Je steekt 70 centjes in de de machine
    print("Je hebt geld in de machine gestoken :D")
    print(f"Ticket balance: {t1.get_balance()}") #Je vraagt de balance op --> 70
    t1.print_ticket() #Je print het ticket --> in dit geval heb je genoeg geïnsert om een ticket te kopen
    print()
    print(f"Ticket balance: {t1.get_balance()}") #Je vraagt opnieuw de balance op --> in dit geval 20 omdat er 50 is afgetrokken voor het ticket
    print()
    t1.print_ticket() #Je print het ticket --> 20 is niet genoeg om een ticket te kopen
    print()
    print(f"Ticket balance: {t1.get_balance()}") #Je vraagt opnieuw de balance op --> 20
    print()
    t1.refund_balance() #Dit zorgt ervoor dat je de 20 centjes terugkrijgt
    print()
    print(f"Ticket balance: {t1.get_balance()}") #Nu zie je dat je het geld hebt teruggekregen omdat de balance nu 0 is