def create_account(initial_balance):
    def deposit(amount):
        nonlocal initial_balance
        initial_balance += amount
        return initial_balance
    return deposit

account = create_account(100)

print(account(50))
print(account(20))