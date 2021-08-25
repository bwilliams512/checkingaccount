"""
In this project, I created a Python class that can be used
to create and manipulate a personal checking account.

The console should show:
The account holder name and initial balance
The deposit (along with the balance)
The withdrawal (along with the balance)
The checking account’s most recent information
"""

class CheckingAccount(object):
  # add a member variable to represent the starting balance
  balance = 0
  
  # add method that will make sure that whatever name the user types will be attributed to that object
  def __init__(self, name):
    self.name = name

  # add method that returns the bank account information
  def __repr__(self):
    return "%s's checking account. Balance: $%.2f" % (self.name, self.balance)

  # add a method that can print the user balance only 
  def show_balance(self):
    print("Balance: $%.2f" % (self.balance))

  # add a method that allows deposits to the bank account
  def deposit(self, amount):
    self.amount = amount
    # add if statement that checks if amount is less than or equal to zero
    if amount <= 0:
        print("Invalid amount entered. Try again")
        return
    else:
        print("Deposited amount: $%.2f" % (self.amount))
        self.balance += amount
        self.show_balance()

  # add a method that allows withdrawals from the bank account
  def withdraw(self, amount):
    self.amount = amount
    # add if statement that checks if amount is less than or equal to zero
    if amount > self.balance:
        print("Withdrawal error: insufficient funds")
        return
    else:
        print("Withdarawal amount: $%.2f" % (self.amount))
        self.balance -= amount
        self.show_balance()
    
# first - create a CheckingAccount object to test it out
my_account = CheckingAccount("Stella McCartney")
print(my_account)

# second - call the show_balance() method on my_account
my_account.show_balance()

# third - test the deposit() method 
my_account.deposit(2000)

# fourth - test the withdraw() method 
my_account.withdraw(1000)

# last - let's see if the __repr__() method accurately reflects the changes to my_account
print(my_account)
