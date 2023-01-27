class Bank_Account:
    def __init__(self,int_rate =0, balance = 0): #balance will default to zero if no amount is given
      self.int_rate = int_rate
      self.balance = balance

    def deposit(self, amount):
      self.balance += amount
      print("your current balance after deposit", self.balance)
      return self

    def withdraw(self, amount):
      if (self.balance - amount) >= 0:
        self.balance -= amount
        print("your current balance after withdraw", self.balance)
      else: 
        print('Sorry, but you do not have enough funds to withdraw money. Your balance:', {self.balance})
      return self

    def display_account_info(self):
      return self.balance

    def yield_interest(self):
      if self.balance > 0:
        self.balance += (self.balance * self.int_rate) #  increases the account balance by the current balance * the interest rate (as long as the balance is positive)
      else: 
        print('Your account balance is negative')
      return self


class User:
    def __init__(self, username, account):
        self.username = username
        self.account = account
        print(self.account)

    def displayUserBalance(self):
        print("-" * 80)
        print(f"Getting {self.username}'s balance")
        print(f"User: {self.username}, Balance: ${self.account.display_account_info()}")
        return self

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount):
        self.account.withdraw(amount)

    def transferMoney(self, otherUser, amount):
        print("-" * 80)
        print(
            f"Transferring {amount} from {self.username} to {otherUser.username}.")
        self.withdraw(amount)
        otherUser.deposit(amount)
        print("Transfer Complete")

user1_acoount = Bank_Account()
user2_acoount = Bank_Account()
new_user = User('newuser', user1_acoount)
new_user.deposit(1500)
otherUser = User('otheruser', user2_acoount)
new_user.transferMoney(otherUser, 500)
new_user.displayUserBalance()
otherUser.displayUserBalance()