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
		if node.state == self.goaltest:
			return 0
		#testing first special case, 3 chicken and 3 wolves
		elif self.goal.state[cl]-self.goal.state[wl] == 0 and self.goal.state[cl] == 3:
			return 0
		elif node.parent == None:
			if self.start.state[wr]-node.state[wl]==1 and self.start.state[cr]-node.state[cl]>=1:
				return node.state[cr]
			else:
				print('wow no one has a parent?')
				return node.state[cr]+3
		else:
			if node.state[bl] and node.parent.state[wr]-node.state[wl] == 1 and node.parent.state[cr]-node.state[cl] == 1:
				return node.state[cr]
			elif node.state[br] and node.parent.state[wl]-node.state[wl] >= 1:
				return node.state[cr]
			else:
				print('here')
				return node.state[cr]+3
		
	
