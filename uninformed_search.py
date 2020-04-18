import queue
from node import *
from problem import *


def bfs(problem):

	startnode = Node(problem.start.state,None,0)
	if startnode.state == problem.goal.state:
		return True #place holder
	
	frontier = [startnode.state] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	
	while len(frontier) != 0:
		newnode = Node(frontier.pop(0))

		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):

			if tuple(actions.state) not in explored.keys() and actions.state not in frontier:
				if problem.goaltest(actions):
					return True #place holder
				frontier.append(actions.state)
	
	
	return False	

def dfs(problem):		
	startnode = Node(problem.start.state,None,0)
	if startnode.state == problem.goal.state:
		return True #place holder
	
	frontier = [startnode.state] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table

	counter = 0	
	while len(frontier) != 0:
		counter = counter + 1
		print(counter)

		newnode = Node(frontier.pop())

		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):

			if tuple(actions.state) not in explored.keys() and actions.state not in frontier:
				if problem.goaltest(actions):
					return True #place holder
				frontier.append(actions.state)
	
	
	return False	
		
#---------------------------------------------------
#examples
#---------------------------------------------------

#	explored = set([tuple(problem.start.state)])
#	explored.add(tuple(problem.goal.state))
#	if tuple(problem.start.state) in explored and tuple(problem.goal.state):
#		print('yep')


def bfsdebug(problem):
	startnode = Node(problem.start.state,None,0)
	if startnode.state == problem.goal.state:
		return True #place holder
	
	frontier = [startnode.state] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	counter = 0	
	while len(frontier) != 0:
		newnode = Node(frontier.pop(0))
		
		
		counter = counter + 1
		print(counter)
		print('parent node:')
		newnode.printstate()
		

	
		print('children nodes:')


		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):
			
			actions.printstate()
			print('costs:',actions.cost)

			if tuple(actions.state) not in explored.keys() and actions.state not in frontier:
				if problem.goaltest(actions):
					return True #place holder
				frontier.append(actions.state)
	
		print()
		print('New Frontier:')	
		for state in frontier:
			#node.printstate()
			print(state)
		
		print('explored list:')
		print(explored)	
		
		print()
#		if counter > 3: break
	
	
	return False	
		
		
#---------------------------------------------------
#examples
#---------------------------------------------------

#	explored = set([tuple(problem.start.state)])
#	explored.add(tuple(problem.goal.state))
#	if tuple(problem.start.state) in explored and tuple(problem.goal.state):
#		print('yep')

