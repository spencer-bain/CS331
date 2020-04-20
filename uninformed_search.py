from node import *
from problem import *


def bfs(problem):

	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode) #place holder
	
	frontier = [startnode] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	count = 0
	
	while len(frontier) != 0:
		count = count + 1
		newnode = frontier.pop(0)


		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):

			if tuple(actions.state) not in explored.keys() and actions not in frontier:
				if problem.goaltest(actions):
					solutions = [problem.solution(actions)]
					solutions.append(count)
					return solutions
				frontier.append(actions)
	
	
	return False	

def dfs(problem):		
	startnode = Node(problem.start.state,0,None)
	if startnode.state == problem.goal.state:
		return problem.solution(startnode)
	
	frontier = [startnode] #making frontier
	explored = {} #{tuple(startnode.state):startnode.cost}#making explored hash table
	count = 0

	while len(frontier) != 0:
		count = count + 1
		newnode = frontier.pop()
		explored[tuple(newnode.state)] = newnode.cost
		for actions in problem.actions(newnode):
			if tuple(actions.state) not in explored.keys() and actions not in frontier:
				if problem.goaltest(actions):
					solutions = [problem.solution(actions)]
					solutions.append(count)
					return solutions
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
	count = 0
	return recursiveIDDFSdebug(problem.start,problem,limit,explored,count)

def recursiveIDDFSdebug(startnode,problem,limit,explored,count):
	count = count+1
#	print('limit: ',limit)
#	print('Node being considerd')
	#results = [None]

	if startnode.state == problem.goal.state:
		solutions = [problem.solution(startnode)]
		solutions.append(count)
		return solutions
	elif limit == 0:
#		print('hit the depth limit\n')
		LIST = ['cut off']
		return LIST
	elif tuple(startnode.state) in explored.keys():
		LIST = []
		return LIST
	else:
		explored[tuple(startnode.state)] = startnode.cost
		cutoff = False
		for actions in problem.actions(startnode):#going through all the children nodes
			
#			print('child node')
#			actions.printstate()

			results = recursiveIDDFSdebug(actions,problem,limit - 1,explored,count)
			'''
			going to get back a list, [cutoff], [False] or a list of nodes
			'''
			

#			print('what we got from child nodes iddfs:',results)


			if 'cut off' in results:
				cutoff = True
			elif False not in results and results != []:
				return results
#			print('Leaf Node\n********************\n')
		if cutoff == True:
#			print('we got cut off, stop exploring this branch\n')
			LIST = ['cut off']
			return LIST
#		elif results == []:
#			return results

		else:# results[0] != None:
#			print('this is an end node\n')
			LIST = [False]
			return LIST
	print("shouldn't be here:",results)


def iddfs(problem):
	for i in range(5):
		results = idfs(problem,i*160)
		if 'cut off' not in results:
			return results

