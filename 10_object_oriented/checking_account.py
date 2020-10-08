from account import Account

class Checking(Account):
    def __init__(self, filepath, fee =0):
        Account.__init__(self, filepath)
        self.fee = fee
        
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


# #  filepath

# derek = Checking("10_object_oriented//balance.txt", 1)
# derek.deposit(1200)
# derek.commit()
# print(derek.balance)