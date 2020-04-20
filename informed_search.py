from node import *
from problem import *
from queue import PriorityQueue

def astar(problem):
	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode)
	
	frontier = PriorityQueue() #making frontier
	frontier.put((startnode.state[cr],startnode))
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	counter = 0	
	while not frontier.empty():
		tuple_with_newnode = frontier.get()
		newnode = tuple_with_newnode[1]
		
		counter = counter + 1
		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):
			if tuple(actions.state) not in explored.keys(): #and actions not in frontier:
				if problem.goaltest(actions):
					return problem.solution(actions)
				frontier.put((problem.evaluation(actions),actions))
	
	return False	
		
def astardebug(problem):
	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode)
	
	frontier = PriorityQueue() #making frontier
	frontier.put((startnode.state[cr],startnode))
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	counter = 0	
	while not frontier.empty():
		tuple_with_newnode = frontier.get()
		newnode = tuple_with_newnode[1]
		
		counter = counter + 1
		print('nodes expanded',counter)
		print('node:')
		newnode.printstate()
		if type(newnode.parent) is Node:	
			print('parent node:')
			newnode.parent.printstate()
		
		print('children nodes:')


		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):
			
			print('costs:',problem.huristic(actions))
			#actions.printstate()
			if tuple(actions.state) not in explored.keys(): #and actions not in frontier:
				if problem.goaltest(actions):
					return problem.solution(actions)
				frontier.put((problem.evaluation(actions),actions))
			'''
			elif actions in frontier:
				index_of_old_frontier_node = frontier.index(actions)
				old_frontier_node = frontier[index_of_old_frontier_node]
				if actions < old_frontier_node:
					pop(index_of_old_frontier_node)
					frontier.append(actions.state)
			'''
	
		print()
		print('New Frontier:')
		placeholder = PriorityQueue()
		for i in frontier.queue:placeholder.put(i)
		while not placeholder.empty():
			tups = placeholder.get()
			print(tups[0])
			tups[1].printstate()
		
		print('explored list:')
		print(explored)	
		
		print()
#		if counter > 3: break
	
	return False	
		
