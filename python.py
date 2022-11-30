class BankAccount:

    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self.balance)

    def deposit(self, amt):
        self.balance += amt

        return self
    
    def withdraw(self, amt):
        if self.balance > amt:
            self.balance -= amt
            return self
        else:
            print("insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * (1.0 + self.int_rate)
        return self
    
    # @classmethod
    # def all_accounts_info(cls):
    #     for one_account in cls.all_accounts:
    #         print(one_account)


account1 = BankAccount(.02, 1000)
account2 = BankAccount(.15, 2000)

account1 = account1.deposit(50).deposit(100).deposit(200).withdraw(30).yield_interest().display_account_info()
account2 = account2.deposit(200).deposit(200).withdraw(50).withdraw(100).withdraw(400).withdraw(200).yield_interest().display_account_info()

# BankAccount.all_accounts_info()


##get the info of the updated accounts after the object methods are run.
## which means, we need to update the class variable as the object methods run.
# # in order to do so, we need to create a dicttionary with a specific key.