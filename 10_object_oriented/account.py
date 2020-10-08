class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdrawl(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account = Account("10_object_oriented//balance.txt")

# print("Strating Balance")
# print(account.balance)

# account.deposit(100)
# print("After Deposit")
# print(account.balance)

# # Committing to the file
# account.commit()

