class BankAccount:
    def __init__(self, init_bal):
        self.balance = init_bal

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print(f"You don't have enough money to withdraw ${amt}.")

    def deposit(self, amt):
        self.balance += amt

    def display_balance(self):
        print(f"You have ${self.balance} in your account.")

my_money = BankAccount(init_bal=10)
my_money.display_balance()
my_money.deposit(100)
my_money.display_balance()
my_money.withdraw(1000)
my_money.display_balance()
my_money.withdraw(50)
my_money.display_balance()
