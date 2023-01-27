class User:
    def __init__(self, username,balance):
        self.username = username
        self.balance = balance

    def displayUserBalance(self):
        print("-" * 80)
        print(f"Getting {self.username}'s balance")
        print(f"User: {self.username}, Balance: ${self.balance}")
        return self

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.username}")
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount} from {self.username}")
        return self

    def transferMoney(self, otherUser, amount):
        print("-" * 80)
        print(
            f"Transferring {amount} from {self.username} to {otherUser.username}.")
        self.withdraw(amount)
        otherUser.deposit(amount)
        print("Transfer Complete")
       
new_user = User('newuser', 3000)
new_user.deposit(1500)
otherUser = User('otheruser', 10)
new_user.transferMoney(otherUser, 500)
new_user.displayUserBalance()
otherUser.displayUserBalance()


