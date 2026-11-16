"""
Define classes to model the following different kinds of bank accounts:

A bank account has:
- an ID
- a balance
- a method for depositing money 

Then there are checking accounts, which additionally have:
- a method for withdrawing money

There are also savings accounts, which:
- do not allow withdrawals
- give a 2% bonus for each deposit

Extra: allow the bonus on a savings account to be set when account is created.
"""

class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise Exception("Insufficient balance")

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount * 1.02


# Test code
c = CheckingAccount("1234-C")
c.deposit(100)
c.withdraw(75)
assert c.balance == 25

s = SavingsAccount("1234-S")
s.deposit(500)
assert s.balance == 510
try:
    s.withdraw(110)
except:
    pass
else:
    raise AssertionError("Withdraw now allowed")
