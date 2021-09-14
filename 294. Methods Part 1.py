class Accounts:
    #Simple account class with balance

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater then 0 and no more then your account balance.")
        self.show_balance()


    def show_balance(self):
        print(f"Balance is {self.balance}")


if __name__ == '__main__':
    tim = Accounts("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(1000)
