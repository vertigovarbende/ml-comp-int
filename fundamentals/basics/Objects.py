class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0:
            self.balance = self.balance + amount
            print(f'Deposited {amount}')
            print(f'New balance is: {self.balance}')
        else:
            print(f'{amount} is an invalid amount')

    def withdraw(self, amount):
        # should also check that amount is a numerical value!
        if 0 < amount <= self.balance:  # amount > 0 and amount <= self.balance -> you can also use this!
            self.balance = self.balance - amount
            print(f'Withdrawal: {amount}')
            print(f'New Balance: {self.balance}')
        else:
            if amount < 0:
                print(f'{amount} is an invalid amount')
            else:
                print("Insufficent funds")
                print(f'Current balance is {self.balance}')


my_account = Account('123-456', 'savings', 1_000.00)

print()
# States
print("States")
print(my_account.account_number)
print(my_account.account_type)
print(my_account.balance)

print()
# Functionality
print("Functionality")
my_account.deposit(100)
my_account.withdraw(600)
my_account.withdraw(10_000)

print()
# Integer is an object
print(10 + 15)
print((10).__add__(25))

print()
# Float is an object
print(0.125.__add__(0.125))
# 0.25
print(0.125.as_integer_ratio())
# (1, 8)
print(0.75.as_integer_ratio())
# (3, 4)
