'''
Created on Jun 14, 2013

@author: Curtis
'''
import logging

class KnowledgeBase(object):

    def __init__(self,sellAllPoint):
        self.sellAll= sellAllPoint
        self.lastPrice = 100
        self.previousStock = []
        self.historicalAvg = 0.0
		
	self.logger = logging.getLogger()
	with open('./stockRecord.log', 'w'):
		pass
	self.hdlr = logging.FileHandler('./stockRecord.log')
	self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	self.hdlr.setFormatter(self.formatter)
	self.logger.addHandler(self.hdlr)
	self.logger.setLevel(logging.INFO)
        
       
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
    def setMostRecentStockPrice(self,lastPrice):
        self.lastPrice = lastPrice
        self.previousStock.append(self.lastPrice)
        
    def calcAvg(self,lastPrice):
    	    self.historicalAvg+=lastPrice
    	    self.historicalAvg=self.historicalAvg/2
    	    
    def doAnalyze(self,lastPrice):
    	    self.setMostRecentStockPrice(lastPrice)
    	    self.calcAvg(lastPrice)
    	    
    def doExecute(self,msg):
    	    
    	    self.logger.info(str(msg)+": $"+str(self.lastPrice))
    	    None
    	    
