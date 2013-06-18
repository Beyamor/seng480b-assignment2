from knowledge import KnowledgeBase
from planning import Planner
from executing import Executor

class Manager:
	def __init__(self):
		knowledge_base = KnowledgeBase()
		self.planner = Planner(knowledge_base)
		self.executor = Executor(knowledge_base)

	def do_a_thing(self):
		plan = self.planner.plan(100, 100, 100)
		self.executor.execute(plan)

manager = Manager()
manager.do_a_thing()
