cl = 0
wl = 1
bl = 2
cr = 3
wr = 4
br = 5


class Node:
	def __init__(self,state,parent = None ,cost = 0):
		self.actions = []
		
		self.state   = state
		self.parent  = parent
		self.cost    = cost

		legalmove = self.legalmove()

	def legalmove(self):
		if self.state[cl] >= self.state[wl] and self.state[cr] >= self.state[wr]:
			return True
		elif self.state[cl] == 0 or self.state[cr] == 0:
			return True
		else:
			return False

	def issame(self,node):
		if self.state == node.state and self.cost == node.state:
			return True
		else:
			return False	

	def printstate(self):
		leftbank = []
		rightbank = []
		for i in range(3):
			leftbank.append(self.state[i])
		for i in range(3,6):
			rightbank.append(self.state[i])
		print(leftbank)
		print(rightbank)

	def printparentstate(self):
		leftbank = []
		rightbank = []
		for i in range(3):
			leftbank.append(self.parent.state[i])
		for i in range(3,6):
			rightbank.append(self.parent.state[i])
		print(leftbank)
		print(rightbank)

	def debug(self):
		self.printstate()
		print(bool(self.legalmove))
		self.generatechildren()
		for actions in self.actions:
			actions.printstate()

	def generatechildren(self):
		if self.legalmove():
			if self.state[br]:
				if self.state[cr] >= 2:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[cr] = newnode.state[cr] - 2
					newnode.state[cl] = newnode.state[cl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[wr] >= 2:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[wr] = newnode.state[wr] - 2
					newnode.state[wl] = newnode.state[wl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[cr] >= 1 and self.state[wr] >= 1:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[cr] = newnode.state[cr] - 1
					newnode.state[cl] = newnode.state[cl] + 1
					newnode.state[wr] = newnode.state[wr] - 1
					newnode.state[wl] = newnode.state[wl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[cr] >= 1:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[cr] = newnode.state[cr] - 1
					newnode.state[cl] = newnode.state[cl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[wr] >= 1:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[wr] = newnode.state[wr] - 1
					newnode.state[wl] = newnode.state[wl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
			else:		
				if self.state[cl] >= 2:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[cl] = newnode.state[cl] - 2
					newnode.state[cr] = newnode.state[cr] + 2
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[wl] >= 2:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[wl] = newnode.state[wl] - 2
					newnode.state[wr] = newnode.state[wr] + 2
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[cl] >= 1 and self.state[wl] >= 1:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[cl] = newnode.state[cl] - 1
					newnode.state[cr] = newnode.state[cr] + 1
					newnode.state[wl] = newnode.state[wl] - 1
					newnode.state[wr] = newnode.state[wr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[cl] >= 1:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[cl] = newnode.state[cl] - 1
					newnode.state[cr] = newnode.state[cr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[wl] >= 1:
					newnode = Node(self.state[:],self,self.cost + 1)
					newnode.state[wl] = newnode.state[wl] - 1
					newnode.state[wr] = newnode.state[wr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
	#	else:
			#print('Leaf node, not a legal state')
			#self.printparentstate()
			#self.printstate()
			#print(self.cost)
			#print()
