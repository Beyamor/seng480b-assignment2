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
    knowledge_base.mostRecentStockPrice(currentStockPrice)

    direction = None
    if stock_difference > 0:
	    direction = "rising"
    elif stock_difference < 0:
	    direction = "falling"
    else:
	    direction = "holding"

    return {"direction": direction, "magnitude": abs(stock_difference)}

myStocks = Stocks()
knowledge_base = KnowledgeBase(500)
planner = Planner(knowledge_base)
executor = Executor(myStocks, knowledge_base)

def mapek_iteration():
	currentStockPrice = monitor(myStocks)
	stock_trend = analyze(knowledge_base, currentStockPrice)
	plan = planner.plan(stock_trend)
	executor.execute(plan)

def run_stock_loop(number_of_iterations):
	for i in range(number_of_iterations):
		myStocks.stockFlux()
		mapek_iteration()
		print(myStocks)

run_stock_loop(100)

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
