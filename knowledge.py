class KnowledgeBase:
	def __init__(self):
		pass

	def is_rising(self, stock_price):
		return False

	def is_falling(self, stock_price):
		return False

	def record_plan(self, plan):
		print("plan: {0}".format(plan))

	def record_execution(self, execution):
		print("execution: {0}".format(execution))
