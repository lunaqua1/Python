# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:26:07 2023

@author: Aysu
"""
class BankAccount:
    def __init__(self,baslangicMiktari,hesapAdi):
        self.miktar=baslangicMiktari
        self.hesapAdi=hesapAdi
        print(f"\n Account '{self.hesapAdi}' created.\n Balance:{self.miktar:.2f} Dolar ")
    def getBalance(self):
        print(f"\nAccount '{self.hesapAdi}' balance= $ {self.miktar:.2f}")
        
    def deposit(self,amount):
        self.miktar=self.miktar+amount
        print("\nDeposit complete.")
        self.getBalance()
            
    def islem(self,amount):
         if self.miktar>=amount:
             return
         else:
             raise Exception (
                 f"\n Sorry, account '{self.hesapAdi} only has a a balance of {self.miktar:.2f}$'"
                 
                 )
         
    def withdraw(self,amount):
        try:
         self.islem(amount)
         self.miktar=self.miktar-amount
         print("\nWithdraw complete.")
         self.getBalance()
        except Exception as error:
            print(f"\n Withdraw interrupted: {error}")
            
    def transfer(self,amount,account):
     try:
         print("\n Transfer beginning")
         self.islem(amount)
         self.withdraw(amount)
         account.deposit(amount)
         print("\nTransfer is complete!")
     except Exception as error:
         print(f"\n Transfer is interrupted. {error}")
class InterestRewardsAcc(BankAccount):
         def deposit(self, amount):
          self.miktar=self.miktar+(amount*1.05)
          print("\nDeposit complete")
          self.getBalance()
          
class SavingsAcc(InterestRewardsAcc):
        def __init__(self,baslangicMiktari,hesapAdi):
            super().__init__(baslangicMiktari, hesapAdi)  
            self.fee=5
            
        def withdraw(self,amount):
            try:
                self.islem(amount+self.fee)
                self.miktar=self.miktar-(amount+self.fee)
                print("Withdraw completed")
                self.getBalance()
            except  Exception as error:
                print(f"\n Withdraw interrupted: {error}")
            
            
          
          
    
    
    
    
    
    
         
         
         