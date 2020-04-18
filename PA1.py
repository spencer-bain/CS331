#import numpy as np
from problem import *
from node import *
from uninformed_search import *
import sys
argument = sys.argv
goal = []
start = []

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
	print('Call bfs algorithm')
elif str(mode)=='dfs':
	print('Call dfs algorithm')
elif str(mode)=='iddfs':
	print('Call iddfs algorithm')
elif str(mode)=='astar':
	print('call astar algorithm')
else:
	print('error')


start = Node(start)
goal = Node(goal)
#start.debug()
#goal.debug()

problem = Problem(start,goal)
#test = bfs(problem)
#test = dfs(problem)

test = bfsdebug(problem)
print(bool(test))

#testnode = Node(list([2,1,0,1,2,1]))
#testnode.debug()
