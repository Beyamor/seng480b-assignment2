class Executor:
	def __init__(self, knowledge_base):
		self.knowledge_base = knowledge_base

	def execute(self, plan):
		self.knowledge_base.record_execution(plan['action'])
