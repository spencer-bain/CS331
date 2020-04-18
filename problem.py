from node import *

class Problem:

	def __init__(self,start=None,goal=None):

		self.start = start
		self.goal = goal
	
	def goaltest(self,child):
		if(self.goal.state == child.state):
			return True
		else:
			return False

	def actions(self,node):
		node.generatechildren()
		return node.actions
