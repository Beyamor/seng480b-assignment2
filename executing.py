import math

class Executor:
	def __init__(self, stocks, knowledge_base):
		self.knowledge_base = knowledge_base
		self.stocks = stocks

	def execute(self, plan):
		action = plan["action"]

		if action is "buy":
			max_buyable_amount = int(math.floor(self.stocks.checkBank() / self.stocks.checkPrice()))
			amount = min(plan["amount"], max_buyable_amount)
			self.stocks.buy(amount)
		elif action is "sell":
			max_sellable_amount = self.stocks.checkAmount()
			amount = min(plan["amount"], max_sellable_amount)
			self.stocks.sell(amount)
		else:
			# Holding - do nothing
			pass
