# PROJECT
'''Write a python program to replicate a banking system.Following features are mandatory
1.Account login
2.Amount depositing
3.Amount withdrawal'''

class Bank:

    def __init__(self,account_number,pin,balance_amount):
        print("executed successfully")
        self.account_number=account_number
        self.pin=pin
        self.balance_amount=balance_amount
    def account_login(self):
        n=int(input("Enter your account number:"))
        b=int(input("Enter your pin number:"))
        if n==account_number:
            b=pin
            print("login successfully")
        else:
            print("Account number invalid")
    def amount_depositing(self,amount):
        if amount>0:
            self.balance_amount+=amount
            print("Total amount is",self.balance_amount)
        else:
            print("Invalid amount")
    def amount_withdrawal(self,amount):
        if amount>0 and amount <=self.balance_amount:
            self.balance_amount-=amount
            print("Amount withdrew is",withdraw_amount)
        else:
            print("Insufficient balance")
account_number=123456789
pin=9876
balance_amount=500

user1=Bank(account_number,pin,balance_amount)
user1.account_login()

depo_amount=int(input("Enter the amount to deposit:"))
user1.amount_depositing(depo_amount)

withdraw_amount=int(input("Enter the amount to withdrew:"))
user1.amount_withdrawal(withdraw_amount)

