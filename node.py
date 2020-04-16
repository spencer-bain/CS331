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
		
		self.state   = state
		self.parent  = parent
		self.cost    = cost

		legalmove = self.legalmove()

	def legalmove(self):
		if self.state[cl]>self.state[wl] and self.state[cr]>self.state[wr]:
			return True
		else:
			return False

	def mystate(self):
		x = self.state
		return x

	
	def generatechildren(self):
		if self.legalmove:
			if br:
				print('boat right')
				if self.state[cr] >= 2:
				
				#------------------------------------------------------------
					x = self.mystate()
					print(x)
					newnode = Node(x)
					newnode.state[cr] = newnode.state[cr] - 2
					newnode.state[cl] = newnode.state[cl] + 2
					newnode.state[br] = 0
					newnode.state[bl] = 1
					self.printstate()
					action1 = Node(newnode.mystate(),self,self.cost + 1)
					action1.printstate()
				#------------------------------------------------------------
				if self.state[wr] >= 2:
					newstate = self.state
					newstate[wr] = newstate[wr] - 2
					newstate[wl] = newstate[wl] + 2
					newstate[br] = 0
					newstate[bl] = 1
					action2 = Node(newstate,self,self.cost + 1)
				#	action2.printstate()
				#	print(self.state[wr])
				#	self.printstate()
				if self.state[cr] >= 1 and self.state[wr] >= 1:
					newstate = self.state
					newstate[cr] = newstate[cr] - 1
					newstate[cl] = newstate[cl] + 1
					newstate[wr] = newstate[wr] - 1
					newstate[wl] = newstate[wl] + 1
					newstate[br] = 0
					newstate[bl] = 1
					action3 = Node(newstate,self,self.cost + 1)
				#	action3.printstate()
				if self.state[wr] >= 1:
					newstate = self.state
					newstate[cr] = newstate[cr] - 1
					newstate[cl] = newstate[cl] + 1
					newstate[br] = 0
					newstate[bl] = 1
					action4 = Node(newstate,self,self.cost + 1)
					action4.printstate()
				if self.state[cr] >= 1:
					newstate = self.state
					newstate[wr] = newstate[wr] - 1
					newstate[wl] = newstate[wl] + 1
					newstate[br] = 0
					newstate[bl] = 1
					action5 = Node(newstate,self,self.cost + 1)
					action5.printstate()


			elif bl:
				print('boat left')
				
			else:
				print("what's up with the boat?")
		else:
			print("leaf node")

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
