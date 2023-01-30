"""
Author: Damian Archer
Date: 1/9/2023
File: BankAccount.py
Purpose: PCPP Certification Exercises - @property, getter, setter, and deleter methods

"""

class AccountException(Exception):
    pass

class BankAccount():
    def __init__(self, balance, account_number=234234432432, owner="Damian"):
        self.__balance = balance # declared as private with __
        self.__account_number = account_number
        self.__owner = owner

    @ property
    def owner(self):
        return self.__owner
    
    @property # property getter method defined
    def balance(self):
        return self.__balance
        
    @balance.setter # setter method, works with assignment and augmented assignment operators
    def balance(self, amt):
        if (amt >= 100000):
            print("Large operation >= 100000. Schedule audit.")
        
        if (amt >= 0):
            self.__balance = amt
        else:
            raise AccountException("Invalid balance alteration, cannot set to negative number {}".format(amt))
    
    @balance.deleter # deleter method
    def balance(self):
        self.__balance = None
        
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self, number):
        raise AccountException("Cannot change account number from {} to {}".format(self.__account_number, number))
        
    @account_number.deleter
    def account_number(self):
        if self.__balance != 0:
            raise AccountException("Cannot delete account with balance {}, zero the balance first".format(self.__balance))
        else:
            self.__account_number = None
            print("Account has been deleted")
    

    def __repr__(self):
        return ("{}\nAccount Details\n{}\n" \
                "Balance: {} \n" \
                "Account Number: {} \n" \
                "Owner: {}\n").format("*"*16,"*"*16,self.balance, self.account_number, self.owner)


print("INSTRUMENTATION")
acct = BankAccount(1000)

# try setting to -200
try:
    acct.balance = -200
except AccountException as e:
    print(e)

# try changing account number
try:
    acct.account_number = 12345454322
except AccountException as e:
    print(e)

# make a large alteration, requiring audit
try:
    acct.balance += 1000000
except AccountException as e:
    print(e)

# try deleting account
try:
    del acct.account_number
except AccountException as e:
    print(e)

# print the balance
print()
print(acct)
print("Zero the balance now")
try:
    acct.balance = 0
    print(acct)
    print("Deleting account")
    del acct.account_number
except AccountException as e:
    print(e)
        
    
