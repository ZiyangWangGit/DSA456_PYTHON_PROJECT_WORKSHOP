class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try: 
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount) 
            self.withdraw(amount) 
            account.deposit(amount) 
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error: 
            print(f'\nTransfer interrupted. ❌ {error}')

class InterestRewardsAcct(BankAccount): 
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name): 
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)
