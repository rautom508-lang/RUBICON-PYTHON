class BankAccount:
    def __init__(self,account_holder,initial_balance):
        
        self.account_holder=account_holder
      
        self.__initial_balance=initial_balance


    def get_accName(self):
        return self.account_holder
    def get_balance(self):
        return self.initial_balance



        
    
my_account = BankAccount("Alice", 1000)

print(my_account.get_accName())
print(my_account.get_balance())
