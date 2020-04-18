#The following formats as such
#chickens, wolves, boat
#[cl, wl, bl] left side of bank
#[cr, wc, br] right side of bank
cl = 0
wl = 1
bl = 2
cr = 3
wr = 4
br = 5


class Node:
	def __init__(self,state,parent = None ,cost = 0):
		self.action1 = None
		self.action2 = None
		self.action3 = None
		self.action4 = None
		self.action5 = None
		
		#current state
		self.state   = state
		#parent node
		self.parent  = parent
		#current cost = parent.cost + 1
		self.cost    = parent.cost + 1

		legalmove = self.legalmove()

	def legalmove(self):
		if self.state[cl] >= self.state[wl] and self.state[cr] >= self.state[wr]:
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

	def debug(self):
		self.printstate()
		print(bool(self.legalmove))
		self.generatechildren()

	def generatechildren(self):
		if self.legalmove():
			if self.state[br]:
				if self.state[cr] >= 2:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[cr] = newnode.state[cr] - 2
					newnode.state[cl] = newnode.state[cl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.action1 = newnode
				if self.state[wr] >= 2:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[wr] = newnode.state[wr] - 2
					newnode.state[wl] = newnode.state[wl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.action2 = newnode
				if self.state[cr] >= 1 and self.state[wr] >= 1:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[cr] = newnode.state[cr] - 1
					newnode.state[cl] = newnode.state[cl] + 1
					newnode.state[wr] = newnode.state[wr] - 1
					newnode.state[wl] = newnode.state[wl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.action3 = newnode
				if self.state[wr] >= 1:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[cr] = newnode.state[cr] - 1
					newnode.state[cl] = newnode.state[cl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.action4 = newnode
				if self.state[wr] >= 1:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[wr] = newnode.state[wr] - 1
					newnode.state[wl] = newnode.state[wl] + 1
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.action5 = newnode
			else:		
				if self.state[cl] >= 2:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[cl] = newnode.state[cl] - 2
					newnode.state[cr] = newnode.state[cr] + 2
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.action1 = newnode
				if self.state[wl] >= 2:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[wl] = newnode.state[wl] - 2
					newnode.state[wr] = newnode.state[wr] + 2
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.action2 = newnode
				if self.state[cl] >= 1 and self.state[wl] >= 1:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[cl] = newnode.state[cl] - 1
					newnode.state[cr] = newnode.state[cr] + 1
					newnode.state[wl] = newnode.state[wl] - 1
					newnode.state[wr] = newnode.state[wr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.action3 = newnode
				if self.state[wl] >= 1:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[cl] = newnode.state[cl] - 1
					newnode.state[cr] = newnode.state[cr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.action4 = newnode
				if self.state[wl] >= 1:
					newnode = Node(self.state[:],self,self.cost)
					newnode.state[wl] = newnode.state[wl] - 1
					newnode.state[wr] = newnode.state[wr] + 1
					newnode.state[bl] = 0
					newnode.state[br] = 1
					self.action5 = newnode
		else:
			print('stuff is suppose to go here')	

#-----------------------------------------------------------
#Garbage Past this point
#-----------------------------------------------------------
def generatechildren(state):
	#------------------------------------------------------------
	newnode = Node(state[:])
	newnode.state[cr] = newnode.state[cr] - 2
	newnode.state[cl] = newnode.state[cl] + 2
	newnode.state[br] = 0
	newnode.state[bl] = 1
	print('Here!!!')
	newnode.printstate()
	print(state)
	#------------------------------------------------------------

