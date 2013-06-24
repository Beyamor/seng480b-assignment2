#Check the current stock value and return any changes to prices
def monitor(stock):
    #Check Managed Element
    return stock.checkPrice()

#Use monitor return and check against knowledge base
def analyze(knowledge_base, currentStockPrice):
    #Use monitor return and check against knowledge base
    stock_difference = currentStockPrice - knowledge_base.lastPrice
    knowledge_base.doAnalyze(currentStockPrice)

    direction = None
    if stock_difference > 0:
	    direction = "rising"
    elif stock_difference < 0:
	    direction = "falling"
    else:
	    direction = "holding"

    return {"direction": direction, "magnitude": abs(stock_difference)}

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
