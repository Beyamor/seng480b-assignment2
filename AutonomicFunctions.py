from Stocks import Stocks
from KnowledgeBase import KnowledgeBase
from planning import Planner
from executing import Executor

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

myStocks = Stocks(initialPrice=100, initialNumber=0, initialBank=5000)
knowledge_base = KnowledgeBase(500)
planner = Planner(knowledge_base)
executor = Executor(myStocks, knowledge_base)

def mapek_iteration():
	currentStockPrice = monitor(myStocks)
	stock_trend = analyze(knowledge_base, currentStockPrice)
	plan = planner.plan(stock_trend)
	executor.execute(plan)

def run_stock_loop(number_of_iterations):
	initial_value = myStocks.checkBank()

	for i in range(number_of_iterations):
		myStocks.stockFlux()
		mapek_iteration()
		print(myStocks)

	print("\nSelling remaining {0} stocks for ${1}".format(myStocks.checkAmount(), myStocks.quantity_value(myStocks.checkAmount())))
	myStocks.sell(myStocks.checkAmount())
	final_value = myStocks.checkBank()
	print("Made ${0}".format(final_value - initial_value))

def main():
	run_stock_loop(100)

if __name__ == "__main__":
	main()

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
