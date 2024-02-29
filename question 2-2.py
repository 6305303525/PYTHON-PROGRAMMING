class Account:
    def __init__(self, balance):
        self.balance = balance
        self.min_balance = 0

    def withdraw(self, amount):
        if ((self.balance - amount) >= self.min_balance):
            return amount
        else:
            return 0

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
        self.min_balance = 500

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
        self.min_balance = 0

a1 = SavingsAccount(1000)
a2 = CurrentAccount(1000)
accounts = [a1, a2]
for account in accounts:
    print(account.withdraw(1000))
