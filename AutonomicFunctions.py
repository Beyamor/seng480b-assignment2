from Stocks import Stocks
from KnowledgeBase import KnowledgeBase

#Check the current stock value and return any changes to prices
def monitor(stock):
    #Check Managed Element
    return stock.checkPrice()

#Use monitor return and check against knowledge base
def analyze(currentStockPrice):
    #Use monitor return and check against knowledge base
    return "not implemented"

myStocks = Stocks()

currentStockPrice = monitor(myStocks)
analyze(currentStockPrice)


'''
print "initial value"
print myStocks.checkBank()
print myStocks.checkAmount()
print myStocks.checkPrice()


print "changeStock"
myStocks.buySellStock(5)
print myStocks.checkBank()
print myStocks.checkAmount()
print myStocks.checkPrice()

print "changeStock"
myStocks.buySellStock(-5)
print myStocks.checkBank()
print myStocks.checkAmount()
print myStocks.checkPrice()

'''