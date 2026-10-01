
class BankAccount:
    def __init__(self, account_holder, initial_balance):# constructor with parameter 
        self.account_holder = account_holder #public
        self.__balance = initial_balance  #private 
# Getter
    def get_balance(self):
        return self.__balance
# Setter 
    def deposit(self, amount):
        self.__balance += amount


# Create object
my_account = BankAccount("Alice", 1000)

# Deposit money
my_account.deposit(500)

# Access private variable using name mangling
print(my_account._BankAccount__balance)

# This is generally bad practice in production because it
# bypasses encapsulation and can lead to unintended changes
