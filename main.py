
class TicketMachine:
    def __init__(self, cost):
        self.cost = cost
        self.balance = 0
        pass

    def get_balance(self):
        return self.balance

    def get_price(self):
        return self.cost

    def insert_money(self, amount):
        self.balance += amount
        return self.balance

    def print_ticket(self):
        if self.balance >= self.cost:
            print("Hier is je ticket")
            self.balance -=self.cost
        else:
            print("Je hebt niet voldoende geld gegeven!")
        
        return self.balance
        

    def refund_balance(self):
        self.balance = 0
        return self.balance


if __name__ == "__main__":
    t1 = TicketMachine(50)
    t2 = TicketMachine(30)  

    t1.insert_money(80)
    print(t1.balance)
    print(t1.print_ticket())
    