class Bank_Account:
    def __init__(self,int_rate =0, balance = 0): #balance will default to zero if no amount is given
      self.int_rate = int_rate
      self.balance = balance

    def deposit(self, amount):
      self.balance += amount
      return self

    def withdraw(self, amount):
      if (self.balance - amount) > 0:
        self.balance -= amount
      else: 
        print('Sorry, but you do not have enough funds to withdraw money. Your balance:', {self.balance})
      return self

    def display_account_info(self):
      print(self.balance)
      return self

    def yield_interest(self):
      if self.balance > 0:
        self.balance += (self.balance * self.int_rate) #  increases the account balance by the current balance * the interest rate (as long as the balance is positive)
      else: 
        print('Your account balance is negative')
      return self


acct1 = Bank_Account()
acct1.deposit(100)
acct1.deposit(300)
acct1.withdraw(140)
print(acct1.display_account_info())
print(acct1.withdraw(340))

