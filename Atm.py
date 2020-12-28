class Atm(object):
    def __init__(self, balance, cash_withdrawl):
        self.balance = balance
        self.cash_withdrawl = cash_withdrawl
        self.remaining_balance = balance - cash_withdrawl
    
    def print__balance(self):
        print("Balance in your account is ₹ " + str(self.balance))

    def print__cash__withdrawl(self):
        print("Cash withdrawn from your account is ₹ " + str(self.cash_withdrawl))

    def print__remaining__balance(self):
        print("Remaining balance in your account is ₹ " + str(self.remaining_balance))

person = Atm(100000, 2500)

print(person.print__balance())
print(person.print__cash__withdrawl())
print(person.print__remaining__balance())