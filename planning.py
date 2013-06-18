import math

class Planner:
	def __init__(self, knowledge_base):
		self.knowledge_base = knowledge_base

	def plan(self, stock_held, stock_price, money):
		plan = None

		if self.knowledge_base.is_rising(stock_price) and money > 0:
			amount_to_buy = math.floor(money / stock_price)
			plan = {'action': 'buy', 'amount': amount_to_buy}

		elif self.knowledge_base.is_falling(stock_price):
			amount_to_sell = stock_held
			plan = {'action': 'sell', 'amount': amount_to_sell}

		else:
			plan = {'action': 'hold'}

		self.knowledge_base.record_plan(plan)
		return plan
