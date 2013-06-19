class Executor:
	def __init__(self, stocks, knowledge_base):
		self.knowledge_base = knowledge_base
		self.stocks = stocks

	def execute(self, plan):
		action = plan["action"]

		if action is "buy":
			self.stocks.buySellStock(plan["amount"])
		elif action is "sell":
			self.stocks.buySellStock(plan["amount"] * -1)
		else:
			# Holding - do nothing
			pass
