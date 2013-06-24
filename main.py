from Stocks import Stocks
from KnowledgeBase import KnowledgeBase
from monitoring import Monitor
from analyzing import Analyzer
from planning import Planner
from executing import Executor

myStocks = Stocks(initialPrice=100, initialNumber=0, initialBank=5000)
knowledge_base = KnowledgeBase(500)
monitor = Monitor(myStocks)
analyzer = Analyzer(knowledge_base)
planner = Planner(knowledge_base)
executor = Executor(myStocks, knowledge_base)

def mapek_iteration():
	currentStockPrice = monitor.monitor()
	stock_trend = analyzer.analyze(currentStockPrice)
	plan = planner.plan(stock_trend)
	executor.execute(plan)

def run_stock_loop(number_of_iterations):
	initial_value = myStocks.checkBank()

	for i in range(number_of_iterations):
		myStocks.stockFlux()
		mapek_iteration()
		#print(myStocks)

	#print("\nSelling remaining {0} stocks for ${1}".format(myStocks.checkAmount(), myStocks.quantity_value(myStocks.checkAmount())))
	myStocks.sell(myStocks.checkAmount())
	final_value = myStocks.checkBank()
	print("Made ${0}".format(final_value - initial_value))

def main():
	run_stock_loop(100)

if __name__ == "__main__":
	main()
