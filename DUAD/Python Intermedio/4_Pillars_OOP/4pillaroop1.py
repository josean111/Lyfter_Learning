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
        #self.set_balance(balance) # Reutilizo el setter para evitar negativos desde el constructor, pero como tengo el withdraw y el deposit
        if balance < 0:
            raise ValueError("Balance cannot be negative... or can it? :(")
        self.__balance = balance
        print(f"I have created a new bank account with {balance}")

    def get_balance(self):
        return self.__balance

    #v2 remove this set balance since deposit and withdraw already sdo this so - DRY
    # def set_balance(self, balance):
    #     if balance < 0:
    #         raise ValueError("Balance cannot be negative... or can it? :(")
    #     self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError(f"Tried to withdraw {amount}. Insufficient funds")
        self.__balance -= amount
        print(f"Withdraw {amount}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        if min_balance < 0:
            raise ValueError("Minimum balance cannot be negative")
        if balance < min_balance:
            raise ValueError("Initial balance cannot be below minimum balance")
        super().__init__(balance)
        self.__min_balance = min_balance
        print(f"But it has a minimum balance of {min_balance}")

    def get_min_balance(self):
        return self.__min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.get_balance(): 
            raise ValueError(f"Tried to withdraw {amount}. Insufficient funds")
        if (self.get_balance() - amount) < self.__min_balance:
            raise ValueError(f"Cannot withdraw {amount}: minimum balance of {self.__min_balance} required")
        super().withdraw(amount) #I know this repeats the insufficient funds validation, but wanted to explore more super usability :)

def main():
    try:
        account = BankAccount(10000)
        account.deposit(5000)
        account.withdraw(2000)
        print(f"My account balance is: {account.get_balance()}")
    except ValueError as error:
        print(f"Error: {error}")

    try:
        account.withdraw(20000)
        print(f"My account balance is: {account.get_balance()}")
    except ValueError as error:
        print(f"Error: {error}")

    try:
        print()
        savings = SavingsAccount(10000, 3000)
        savings.deposit(2000)
        savings.withdraw(4000)
        print(f"My SAVINGS account balance is: {savings.get_balance()}")
        print(f"Minimum balance: {savings.get_min_balance()}")
    except ValueError as error:
        print(f"Error: {error}")

    try:
        savings.withdraw(7000)
        print(f"My SAVINGS account balance is: {savings.get_balance()}")
    except ValueError as error:
        print(f"Error: {error}")

    try:
        savings.deposit(-500)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        print()
        invalid_account = BankAccount(-100)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        print()
        invalid_savings = SavingsAccount(1000, 3000)
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()