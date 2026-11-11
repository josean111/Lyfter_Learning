# Cree una clase de BankAccount que:
# Tenga un atributo de balance.
# Tenga un método para ingresar dinero.
# Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
# Tenga un atributo de min_balance que se pueda asignar al crearla.
# Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. 
# Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        print(f"I have created a new bank account with {balance}")

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative... or can it? :(")
            return
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Tried to withdraw {amount}. Insufficient funds")
            return

        self.__balance -= amount
        print(f"Withdraw {amount}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.__min_balance = min_balance
        print(f"But it has a minimum balance of {min_balance}")

    def withdraw(self, amount):
        if amount > self.get_balance(): 
            print(f"Tried to withdraw {amount}. Insufficient funds")
            return

        if (self.get_balance() - amount) < self.__min_balance:
            print(f"Cannot withdraw {amount}: minimum balance of {self.__min_balance} required")
            return

        super().withdraw(amount) #I know this repeats the insufficient funds validation, but wanted to explore more super usability :)

def main():
    account = BankAccount(10000)
    account.deposit(5000)
    account.withdraw(2000)
    print(f"My account balance is: {account.get_balance()}")
    account.withdraw(20000)
    print(f"My account balance is: {account.get_balance()}")

    print()
    savings = SavingsAccount(10000, 3000)
    savings.deposit(2000)
    savings.withdraw(4000)
    print(f"My SAVINGS account balance is: {savings.get_balance()}\n")
    savings.withdraw(40000)
    print(f"My SAVINGS account balance is: {savings.get_balance()}\n")
    savings.withdraw(7000)
    print(f"My SAVINGS account balance is: {savings.get_balance()}")

    print()
    last_one = BankAccount(1000)
    last_one.set_balance(-100)

if __name__ == "__main__":
    main()