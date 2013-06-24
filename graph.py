from matplotlib import pyplot
from Stocks import Stocks
from AutonomicFunctions import monitor, analyze
from KnowledgeBase import KnowledgeBase
from planning import Planner
from executing import Executor

def main():
	stocks = Stocks(initialPrice=100, initialNumber=0, initialBank=5000)
	knowledge_base = KnowledgeBase(500)
	planner = Planner(knowledge_base)
	executor = Executor(stocks, knowledge_base)

	prices = []
	monies = []
	for i in range(100):
		stocks.stockFlux()

		current_price = monitor(stocks)
		stock_trend = analyze(knowledge_base, current_price)
		plan = planner.plan(stock_trend)
		executor.execute(plan)

		prices.append(stocks.checkPrice())
		monies.append(stocks.checkBank())

	stocks.sell(stocks.checkAmount())
	prices.append(stocks.checkPrice())
	monies.append(stocks.checkBank())

	scaled_prices = map(lambda x: x*10, prices) # Scaling reads a little better
	pyplot.plot(scaled_prices)
	pyplot.plot(monies, color='red')
	pyplot.show()

if __name__ == "__main__":
	main()
