import math

class Planner:
	def __init__(self, knowledge_base):
		self.knowledge_base = knowledge_base

	def plan(self, stock_trend):
		direction = stock_trend["direction"]
		magnitude = stock_trend["magnitude"]

		change_amount = magnitude
		if direction is "falling":
			change_amount *= -1

		buy_or_sell = self.knowledge_base.buyOrSell(change_amount)
		amount = abs(buy_or_sell)

		if buy_or_sell > 0:
			return {"action": "buy", "amount": amount}
		elif buy_or_sell < 0:
			return {"action": "sell", "amount": amount}
		else:
			return {"action": "hold"}
