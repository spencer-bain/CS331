from informed_search import *
from problem import *
from node import *
from uninformed_search import *
import sys
#importing os to manage files
import os
argument = sys.argv

# Reading in arguments as follows, PA1.py [start.txt] [goal.txt] [search arg]
# Arguments can be the following: bfs, dfs, iddfs, astar

# For now, when you run the program an output file will be created
# If you run the program again with the same search algorithm,
# but with different start and end goal it should overwrite said file.


def showresults(test):
	counter = 0
	print("here is the Path:")
	if bool(test) is True:
		for node in test:
			print(counter)
			counter = counter + 1
			if type(node) is Node:
				node.printstate()
			else:
				print(node)
	else:
		print(test)

def writeresults(test):
	counter = 0
	if bool(test) is True:
		for node in test:
			counter = counter + 1
			if type(node) is Node:
				outputFile.write(node.stringstate())
	outputFile.write(str(counter))

def printresults():
	print('help')

def reading(filehandle):
	LIST = []
	for i in range(2):
		string = filehandle.readline()
		LIST.append(list(map(int,string.split(','))))

	state = []
	for i in range(2):
		statelr = LIST[i]
		for x in range(3):
			state.append(statelr[x])
	return state

s = open(argument[1],'r')
start = reading(s)
s.close()

g = open(argument[2],'r')
goal = reading(g)
g.close()

start = Node(start)
goal = Node(goal)

problem = Problem(start,goal)

mode = argument[3]
if str(mode)=='bfs':
	test = bfs(problem)
	showresults(test[0])
	if(os.path.exists("outputBFS.txt")):
		os.remove("outputBFS.txt")
	outputFile = open("outputBFS.txt", "w")
	writeresults(test)	
elif str(mode)=='dfs':
	test = dfs(problem)
	showresults(test[0])
	if(os.path.exists("outputDFS.txt")):
		os.remove("outputDFS.txt")
  outputFile = open("outputDFS.txt", "w")
	writeresults(test)

elif str(mode)=='iddfs':
	test = iddfs(problem)
	showresults(test[0])

	if(os.path.exists("outputIddfs.txt")):
		os.remove("outputIddfs.txt")
	outputFile = open("outputIDDFS.txt", "w")
	writeresults(test)


elif str(mode)=='astar':
	test = astar(problem)
	showresults(test[0])
	if(os.path.exists("outputAstar.txt")):
		os.remove("outputAstar.txt")

	outputFile = open("outputAstar.txt", "w")
	writeresults(test)


else:
	print('error')

print('this is the end of the path')
print('number of expanded nodes:',test[1])
