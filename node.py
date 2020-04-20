# The following formats as such
# chickens, wolves, boat
# [cl, wl, bl] left side of bank
# [cr, wc, br] right side of bank
cl = 0
wl = 1
bl = 2
cr = 3
wr = 4
br = 5


class Node:
	def __init__(self,state,cost=0,parent=None):
		self.actions = []
		
		# current state
		self.state   = state
		# parent node
		self.parent  = parent
		# current cost = parent.cost + 1
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
		
	def stringstate(self):
		state_string = f"[{self.state[0]}, {self.state[1]}, {self.state[2]}] \n[{self.state[3]}, {self.state[4]}, {self.state[5]}] \n"
		return state_string

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
	
	def __eq__(self,other):
		'''
		print('this is self')
		self.printstate()
		print('this is other')
		other.printstate()
		'''
		if type(other) is Node:
			if self.state == other.state:
				return True
			else:
				return False
		else:
			return False
	def __ne__(self,other):
		#print('overloaded != is being called for Node')
		if type(other) is Node:
			if self.state != other.state or self.cost != other.cost:
				return True
			else:
				return False
		else:
			return False

	def __lt__(self,other):
		if self.cost < other.cost:
			return True
		else:
			return False

	def generatechildren(self):
		if self.legalmove():
			newnodecost = self.cost + 1
			if self.state[br]:
				if self.state[cr] >= 2:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[cr] = newnode.state[cr] - 2
					newnode.state[cl] = newnode.state[cl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[wr] >= 2:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[wr] = newnode.state[wr] - 2
					newnode.state[wl] = newnode.state[wl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[cr] >= 1 and self.state[wr] >= 1:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[cr] = newnode.state[cr] - 1
					newnode.state[cl] = newnode.state[cl] + 1
					newnode.state[wr] = newnode.state[wr] - 1
					newnode.state[wl] = newnode.state[wl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[cr] >= 1:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[cr] = newnode.state[cr] - 1
					newnode.state[cl] = newnode.state[cl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
				if self.state[wr] >= 1:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[wr] = newnode.state[wr] - 1
					newnode.state[wl] = newnode.state[wl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.actions.append(newnode)
			else:		
				if self.state[cl] >= 2:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[cl] = newnode.state[cl] - 2
					newnode.state[cr] = newnode.state[cr] + 2
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[wl] >= 2:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[wl] = newnode.state[wl] - 2
					newnode.state[wr] = newnode.state[wr] + 2
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[cl] >= 1 and self.state[wl] >= 1:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[cl] = newnode.state[cl] - 1
					newnode.state[cr] = newnode.state[cr] + 1
					newnode.state[wl] = newnode.state[wl] - 1
					newnode.state[wr] = newnode.state[wr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[cl] >= 1:
					newnode = Node(self.state[:],newnodecost,self)
					newnode.state[cl] = newnode.state[cl] - 1
					newnode.state[cr] = newnode.state[cr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.actions.append(newnode)
				if self.state[wl] >= 1:
					newnode = Node(self.state[:],newnodecost,self)
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
