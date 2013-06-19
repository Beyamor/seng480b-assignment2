'''
Created on Jun 14, 2013

@author: Curtis
'''
import random

class Stocks(object):
    
    def __init__(self, initialPrice=100, initialNumber=1000, initialBank=0):
        self.Price = initialPrice
        self.Amount = initialNumber
        self.Bank = initialBank

    def checkBank(self):
        return self.Bank
    
    def checkPrice(self):
        return self.Price
    
    def checkAmount(self):
        return self.Amount
    
    def buySellStock(self,numberToBuySell):
        self.Amount -= numberToBuySell
        self.Bank += numberToBuySell * self.Price
    
    def stockFlux(self):
        x = random.randint(-10,10)
        self.Price += x

    def __str__(self):
	    return "Price: {0}, amount: {1}, bank: {2}".format(self.Price, self.Amount, self.Bank)
