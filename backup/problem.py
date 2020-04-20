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

	def solution(self,node):
		LIST = []
		self.findpathtoroot(node,LIST)
		LIST.append(self.goal)
		return LIST
		
	
	def findpathtoroot(self,node,LIST):
		if node.parent:
			self.findpathtoroot(node.parent,LIST)
			return LIST.append(node.parent)
		else:
			return 
	def evaluation(self,node):
		return self.huristic(node) + 1

	def huristic(self,node):

		if node.state == self.goaltest(node):
		#entering if we have our solution
			return 0

		elif self.goal.state[cl]-self.goal.state[wl] == 0 and self.goal.state[cl] == 3:
		#entering if special case, 3 chicken and 3 wolves
			return 0

		elif node.parent == None:
		#entering if a parent node is the start and we are action 3

			if node.state[wl]-self.start.state[wl]==1 and ndoe.state[cl]-self.start.state[cl]==1:
			#entering if we are action 3
				return node.state[cr]
			
			else:
			#entering if we are not action 3
				return node.state[cr]+3

		elif node.parent.state[br] and node.state[wl]-node.parent.state[wl]==1 and node.state[cl]-node.parent.state[cl]==1:
		#entering if parent boat is right and we are and action 3
			return node.state[cr]

		elif node.parent.state[bl]==1:	
		#entering if parent has the boat on the left
			if node.parent.state[wl]-node.state[wl]==1 and node.parent.state[cl]-node.state[cl]==1:
			#entering if action 3
				return node.state[cr]+3

			elif node.parent.state[wl] == node.parent.state[cl] and node.parent.state[wl]-node.state[wl] == 1:
			#entering if action 5
				return node.state[cr]

			elif node.parent.state[wl] < node.parent.state[cl] and node.parent.state[cl]-node.state[cl]==1:
			#entering if action 4
				return node.state[cr]

			else:
			#entering if action 1 or 2
				return node.state[cr]+3

		return node.state[cr]+3
	
