#import numpy as np
from problem import *
from node import *
from uninformed_search import *
import sys
#importing os to manage files
import os
argument = sys.argv
goal = []
start = []

# Reading in arguments as follows, PA1.py [start.txt] [goal.txt] [search arg]
# Arguments can be the following: bfs, dfs, iddfs, astar

# For now, when you run the program an output file will be created
# If you run the program again with the same search algorithm,
# but with different start and end goal it should overwrite said file.

def grabaline(filehandel,listtoappend):
	yeah = filehandel.read(1)
	while yeah != '\n':
		if yeah != ',':
			listtoappend.append(yeah)
			yeah=filehandel.read(1)
		else:
			yeah=filehandel.read(1)
	return listtoappend

s = open(argument[1],'r')
grabaline(s,start)
grabaline(s,start)
s.close()

g = open(argument[2],'r')
grabaline(g,goal)
grabaline(g,goal)
g.close()

goal = list(map(int,goal))
start = list(map(int,start))

mode = argument[3]
if str(mode)=='bfs':
	if(os.path.exists("outputBFS.txt")):
		os.remove("outputBFS.txt")
	else:
		outputFile = open("outputBFS.txt", "a")
		outputFile.write("test")
		outputFile.close()
	print('Call bfs algorithm')

elif str(mode)=='dfs':
	if(os.path.exists("outputDFS.txt")):
		os.remove("outputDFS.txt")
	else:
		outputFile = open("outputDFS.txt", "a")	
	print('Call dfs algorithm')

elif str(mode)=='iddfs':
	if(os.path.exists("outputIddfs.txt")):
		os.remove("outputIddfs.txt")
	else:
		outputFile = open("outputIddfs.txt", "a")
	print('Call iddfs algorithm')

elif str(mode)=='astar':
	if(os.path.exists("outputAstar.txt")):
		os.remove("outputAstar.txt")
	else:
		outputFile = open("outputAstar.txt", "a")
	print('call astar algorithm')

else:
	print('error')

start = Node(start)
goal = Node(goal)
problem = Problem(start,goal)
#test = bfs(problem)


