'''
Created on Jun 14, 2013

@author: Curtis
'''

class KnowledgeBase(object):

    def __init__(self,sellAllPoint):
        self.sellAll= sellAllPoint
        self.lastPrice = 100
        self.previousStock = []
       
    #if stock goes down sell, if it goes up sell 
    def buyOrSell(self,amountChange):
        if amountChange < -10:
            return -10
        elif amountChange < -5:
            return -5
        elif amountChange < -1:
            return 1
        elif amountChange == 0:
            return 0
        elif amountChange < 1:
            return 1
        elif amountChange < 5:
            return 5
        elif amountChange <= 10:
            return 10
    
    #store info of most recent stockPrice
    def mostRecentStockPrice(self,lastPrice):
        self.lastPrice = lastPrice
        self.previousStock.append(self.lastPrice)
