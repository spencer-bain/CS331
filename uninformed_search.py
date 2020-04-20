from node import *
from problem import *


def bfs(problem):

	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode) #place holder
	
	frontier = [startnode] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	
	while len(frontier) != 0:
		newnode = frontier.pop(0)


		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):

			if tuple(actions.state) not in explored.keys() and actions not in frontier:
				if problem.goaltest(actions):
					return problem.solution(actions)
				frontier.append(actions)
	
	
	return False	

def dfs(problem):		
	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode)
	
	frontier = [startnode] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table

	while len(frontier) != 0:
		newnode = frontier.pop()
		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):
			if tuple(actions.state) not in explored.keys() and actions not in frontier:
				if problem.goaltest(actions):
					return problem.solution(actions)
				frontier.append(actions)
	
	
	return False	
		
def dfsdebug(problem):		
	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode)
	
	frontier = [startnode] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table

	counter = 0	
	while len(frontier) != 0:
		counter = counter + 1
		print(counter)

		newnode = frontier.pop()

		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):

			if tuple(actions.state) not in explored.keys() and actions not in frontier:
				if problem.goaltest(actions):
					return problem.solution(actions)
				frontier.append(actions)
	

def idfs(problem,limit):
	explored = {}
	return recursiveIDDFSdebug(problem.start,problem,limit,explored)

def recursiveIDDFSdebug(startnode,problem,limit,explored):
	
	print('limit: ',limit)
#	print('Node being considerd')
	#results = [None]

	if startnode.state == problem.goal.state:
		return problem.solution(startnode)
	elif limit == 0 or tuple(startnode.state) in explored.keys():
#		print('hit the depth limit\n')
		LIST = ['cut off']
		return LIST
	else:
		explored[tuple(startnode.state)] = startnode.cost
		cutoff = False
		for actions in problem.actions(startnode):#going through all the children nodes
			
#			print('child node')
#			actions.printstate()

			results = recursiveIDDFSdebug(actions,problem,limit - 1,explored)
			'''
			going to get back a list, [cutoff], [False] or a list of nodes
			'''
			

#			print('what we got from child nodes iddfs:',results)

			 


			if 'cut off' in results:
				cutoff = True
			elif False not in results:
#				print('getting that there is no solution being returned:\n')
				return results
#			print('Leaf Node\n********************\n')
		if cutoff == True:
#			print('we got cut off, stop exploring this branch\n')
			LIST = ['cut off']
			return LIST
		else:# results[0] != None:
#			print('this is an end node\n')
			LIST = [False]
			return LIST
	print("shouldn't be here:",results)


def iddfs(problem):
	for i in range(1000):
		results = idfs(problem,i)
		if 'cut off' not in results:
			return results

