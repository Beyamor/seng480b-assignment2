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
    
    def quantity_value(self, amount_of_stocks):
        return amount_of_stocks * self.Price

    def buy(self, amount_to_buy):
        cost = self.quantity_value(amount_to_buy)
	if self.Bank - cost < 0:
		error = "Bought more stock than can afford (buying: ${0}; has ${1})".format(
				cost,
				self.Bank)
		raise Exception(error)

        self.Amount += amount_to_buy
        self.Bank -= cost
 
    def sell(self, amount_to_sell):
        if self.Amount - amount_to_sell < 0:
		error = "Sold more stock than is available (selling: {0}; has: {1})".format(
				amount_to_sell,
				self.Amount)
		raise Exception(error)

	self.Amount -= amount_to_sell
        self.Bank += self.quantity_value(amount_to_sell)
    
    def stockFlux(self):
        x = random.randint(-10,10)
        self.Price = max(1, self.Price + x)

    def __str__(self):
	    return "Price: ${0}, amount: {1}, bank: ${2}".format(self.Price, self.Amount, self.Bank)
