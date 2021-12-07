class BankAccount:

    def __init__(self, int_rate, balance,):
        self.int_rate = int_rate
        self.balance = balance
        self.name=self

    def deposit(self, amount):
        self.balance +=amount
        return self

    def withdraw(self,amount):
        if (self.balance - amount) >=0:
            self.balance -=amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_user_balance(self):
        print(f"Balance:{self.balance}")

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self
# Akira_account = BankAccount("Akira")
# ousmane_account = BankAccount("ousmane")
Akira_account = BankAccount(0.02,6000)
ousmane_account = BankAccount(0.03, 1000)

Akira_account.deposit(800).deposit(50).deposit(90).withdraw(2500)
Akira_account.display_user_balance ()

ousmane_account.deposit(140).withdraw(630).withdraw(370).withdraw(200)
ousmane_account.display_user_balance()