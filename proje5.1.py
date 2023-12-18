# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:37:29 2023

@author: Aysu
"""

from proje5 import *

Aysu=BankAccount(500,'Aysu')
Sara=BankAccount(2000,'Sara')

Aysu.getBalance()
Aysu.deposit(500)
Aysu.withdraw(5000)
#Aysu.transfer(47852, 'Lara')
Merve=InterestRewardsAcc(500,'Merve')
Merve.getBalance()
Merve.deposit(500)
Merve.transfer(100, Aysu)

Duygu=SavingsAcc(1000, 'Duygu')
Duygu.getBalance()
Duygu.deposit(100)
Duygu.transfer(10000, Aysu)