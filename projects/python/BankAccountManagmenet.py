'''

    This is a bacnk account management system that allows user to create account , to deposit money, to see their account balance
    towithdraw money,check account balace and showing them their transaction history that can be using oop
    and related concepts
'''
import random

class BankAccount:
    def __init__(self,fname,lname,account_balance,phone,accounts,account_no):
        self.fname =fname
        self.lname = lname
        self.phone = phone
        self.account_balance = account_balance
        self.accounts = accounts
        self.account_no = account_no

    def deposit(self):
        amount = int(input("Pleae enter the ammount you want to deposit:   "))
        self.account_balance += amount

    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw:  "))
        if amount > self.account_balance:
            print(f'Your account is insufficent to withdraw\n\tBalance:{self.account_balance}') 
        else:
            self.account_balance -= amount
            print(f"you sucessfuly withdraw {amount} birr and your current balance is {self.account_balance}")

    def check_balance(self):
        return f'Your account balance is {self.account_balance}'
    
    def create_account(self):
        self.accounts = []
        self.fname = input("Enter your first name:  ")
        self.lname = input("Enter you fathers name:  ")
        self.phone = int(input("Enter your phone number: "))

        

        print("Your account is created sucessfully")
        self.account_no = random.randint(1_000_000_000_000,1_000_000_000_000_000_000)

        self.accounts.append((self.fname,self.lname,self.phone,self.account_no))
        print(f'Your account number is {self.account_no}')
